"""Ergonomic SDK facade for neurosynth_compose_sdk."""

from __future__ import annotations

import importlib
import pkgutil
import re
from typing import Any, Dict, List, Optional, Tuple, Type

from neurosynth_compose_sdk.api_client import ApiClient
from neurosynth_compose_sdk.auth import Auth0RefreshTokenAuth
from neurosynth_compose_sdk.configuration import Configuration


ApiClass = Type[Any]
_API_DISCOVERY_CACHE: Optional[Tuple[Dict[str, ApiClass], List[str]]] = None


def _normalize_alias(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def _to_snake_case(name: str) -> str:
    first_pass = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first_pass).lower()


def _discover_api_classes() -> Tuple[Dict[str, ApiClass], List[str]]:
    global _API_DISCOVERY_CACHE
    if _API_DISCOVERY_CACHE is not None:
        return _API_DISCOVERY_CACHE

    alias_to_class: Dict[str, ApiClass] = {}
    canonical_names: List[str] = []
    api_package = importlib.import_module("neurosynth_compose_sdk.api")

    for module_info in pkgutil.iter_modules(api_package.__path__):
        module_name = module_info.name
        if not module_name.endswith("_api"):
            continue

        module = importlib.import_module(f"neurosynth_compose_sdk.api.{module_name}")
        api_class: Optional[ApiClass] = None

        for attr_name in dir(module):
            attr_value = getattr(module, attr_name)
            if isinstance(attr_value, type) and attr_name.endswith("Api"):
                api_class = attr_value
                break

        if api_class is None:
            continue

        canonical_name = module_name[: -len("_api")]
        canonical_names.append(canonical_name)

        alias_candidates = {
            canonical_name,
            module_name,
            api_class.__name__,
            _to_snake_case(api_class.__name__),
            _to_snake_case(api_class.__name__.removesuffix("Api")),
        }

        for alias in alias_candidates:
            alias_to_class[_normalize_alias(alias)] = api_class

    canonical_names.sort()
    _API_DISCOVERY_CACHE = (alias_to_class, canonical_names)
    return _API_DISCOVERY_CACHE


class SDK:
    """One-stop facade for API groups with optional Auth0 token refresh."""

    def __init__(
        self,
        host: Optional[str] = None,
        access_token: Optional[str] = None,
        configuration: Optional[Configuration] = None,
        auth: Optional[Auth0RefreshTokenAuth] = None,
    ) -> None:
        if configuration is None:
            configuration = Configuration(host=host) if host else Configuration()
        elif host is not None:
            configuration.host = host

        if access_token:
            configuration.access_token = access_token

        if auth is not None:
            auth.install(configuration)

        self.configuration = configuration
        self.auth = auth
        self.api_client = ApiClient(self.configuration)
        self._instances: Dict[ApiClass, Any] = {}
        self._aliases, self._canonical_names = _discover_api_classes()

    @classmethod
    def from_auth0_refresh_token(
        cls,
        domain: str,
        client_id: str,
        refresh_token: str,
        host: Optional[str] = None,
        configuration: Optional[Configuration] = None,
        audience: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[str] = None,
    ) -> "SDK":
        auth = Auth0RefreshTokenAuth(
            domain=domain,
            client_id=client_id,
            refresh_token=refresh_token,
            audience=audience,
            client_secret=client_secret,
            scope=scope,
        )
        return cls(host=host, configuration=configuration, auth=auth)

    @classmethod
    def from_auth0_env(
        cls,
        host: Optional[str] = None,
        configuration: Optional[Configuration] = None,
        prefix: str = "AUTH0",
    ) -> "SDK":
        auth = Auth0RefreshTokenAuth.from_env(prefix=prefix)
        return cls(host=host, configuration=configuration, auth=auth)

    def available_apis(self) -> List[str]:
        return list(self._canonical_names)

    def api(self, name: str) -> Any:
        normalized = _normalize_alias(name)
        api_class = self._aliases.get(normalized)
        if api_class is None:
            available = ", ".join(self._canonical_names)
            raise KeyError(f"Unknown API group `{name}`. Available APIs: {available}")

        instance = self._instances.get(api_class)
        if instance is None:
            instance = api_class(self.api_client)
            self._instances[api_class] = instance
        return instance

    def __getattr__(self, name: str) -> Any:
        try:
            return self.api(name)
        except KeyError as exc:
            raise AttributeError(str(exc)) from exc

    def __enter__(self) -> "SDK":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        api_client_exit = getattr(self.api_client, "__exit__", None)
        if callable(api_client_exit):
            return bool(api_client_exit(exc_type, exc_value, traceback))
        return False


__all__ = ["SDK"]
