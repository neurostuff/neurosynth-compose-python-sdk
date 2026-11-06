# flake8: noqa

__all__ = [
    "ComposeApi",
    "DefaultApi",
]

import typing as _typing

if _typing.TYPE_CHECKING:
    # import apis into api package
    from neurosynth_compose_sdk.api.compose_api import ComposeApi
    from neurosynth_compose_sdk.api.default_api import DefaultApi
    
else:
    from importlib import import_module

    _exports = {
        "ComposeApi": ".compose_api",
        "DefaultApi": ".default_api",
    }

    def __getattr__(name: str) -> object:
        if (module_name := _exports.get(name)) is None:
            raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
        value = getattr(import_module(module_name, __name__), name)
        globals()[name] = value
        return value

    def __dir__() -> list[str]:
        return sorted(globals().keys() | _exports.keys())
