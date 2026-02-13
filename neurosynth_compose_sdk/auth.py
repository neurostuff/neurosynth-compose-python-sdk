"""Auth helpers for neurosynth_compose_sdk."""

from __future__ import annotations

import json
import os
import threading
import time
import types
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from neurosynth_compose_sdk.configuration import Configuration


class Auth0TokenExchangeError(RuntimeError):
    """Raised when the refresh-token exchange with Auth0 fails."""


@dataclass
class Auth0RefreshTokenAuth:
    """Refreshes Auth0 access tokens and injects them into SDK Configuration."""

    domain: str
    client_id: str
    refresh_token: str
    audience: Optional[str] = None
    client_secret: Optional[str] = None
    scope: Optional[str] = None
    timeout_seconds: float = 15.0
    refresh_skew_seconds: int = 60
    _access_token: Optional[str] = field(default=None, init=False, repr=False)
    _expires_at: float = field(default=0.0, init=False, repr=False)
    _lock: threading.Lock = field(default_factory=threading.Lock, init=False, repr=False)

    @classmethod
    def from_env(cls, prefix: str = "AUTH0") -> "Auth0RefreshTokenAuth":
        required = {
            f"{prefix}_DOMAIN": os.getenv(f"{prefix}_DOMAIN"),
            f"{prefix}_CLIENT_ID": os.getenv(f"{prefix}_CLIENT_ID"),
            f"{prefix}_REFRESH_TOKEN": os.getenv(f"{prefix}_REFRESH_TOKEN"),
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            missing_vars = ", ".join(sorted(missing))
            raise ValueError(f"Missing required Auth0 environment variables: {missing_vars}")

        return cls(
            domain=required[f"{prefix}_DOMAIN"],
            client_id=required[f"{prefix}_CLIENT_ID"],
            refresh_token=required[f"{prefix}_REFRESH_TOKEN"],
            audience=os.getenv(f"{prefix}_AUDIENCE") or None,
            client_secret=os.getenv(f"{prefix}_CLIENT_SECRET") or None,
            scope=os.getenv(f"{prefix}_SCOPE") or None,
        )

    def token_endpoint(self) -> str:
        normalized = self.domain.strip().rstrip("/")
        if normalized.startswith("http://") or normalized.startswith("https://"):
            base = normalized
        else:
            base = f"https://{normalized}"

        if base.endswith("/oauth/token"):
            return base
        return f"{base}/oauth/token"

    def install(self, configuration: Configuration) -> None:
        """Inject automatic refresh logic into this configuration instance."""

        original_auth_settings = configuration.__class__.auth_settings

        def _auth_settings(config_self: Configuration) -> Dict[str, Any]:
            config_self.access_token = self.get_access_token()
            return original_auth_settings(config_self)

        configuration.auth_settings = types.MethodType(_auth_settings, configuration)
        configuration.access_token = self.get_access_token()

    def needs_refresh(self) -> bool:
        if not self._access_token:
            return True
        return time.time() >= (self._expires_at - self.refresh_skew_seconds)

    def get_access_token(self, force_refresh: bool = False) -> str:
        with self._lock:
            if force_refresh or self.needs_refresh():
                self._exchange_refresh_token()

            if not self._access_token:
                raise Auth0TokenExchangeError("Auth0 token exchange returned no access token.")
            return self._access_token

    def _exchange_refresh_token(self) -> None:
        payload: Dict[str, Any] = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "refresh_token": self.refresh_token,
        }
        if self.client_secret:
            payload["client_secret"] = self.client_secret
        if self.audience:
            payload["audience"] = self.audience
        if self.scope:
            payload["scope"] = self.scope

        request = urllib.request.Request(
            self.token_endpoint(),
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                raw_body = response.read().decode("utf-8")
                body = json.loads(raw_body)
        except urllib.error.HTTPError as exc:
            raw_error = exc.read().decode("utf-8", "replace")
            raise Auth0TokenExchangeError(
                f"Auth0 token exchange failed with HTTP {exc.code}: {raw_error}"
            ) from exc
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            raise Auth0TokenExchangeError(f"Auth0 token exchange failed: {exc}") from exc

        access_token = body.get("access_token")
        if not access_token:
            raise Auth0TokenExchangeError(
                "Auth0 token exchange response does not contain `access_token`."
            )

        rotated_refresh_token = body.get("refresh_token")
        if rotated_refresh_token:
            self.refresh_token = rotated_refresh_token

        expires_in_raw = body.get("expires_in", 3600)
        try:
            expires_in = int(expires_in_raw)
        except (TypeError, ValueError):
            expires_in = 3600

        self._access_token = access_token
        self._expires_at = time.time() + max(expires_in, 0)


__all__ = ["Auth0RefreshTokenAuth", "Auth0TokenExchangeError"]
