# File generated from our OpenAPI spec by Stainless.

from . import types
from ._types import NoneType, Transport, ProxiesTypes
from ._utils import file_from_path
from ._client import (
    Orb,
    Client,
    Stream,
    Timeout,
    AsyncOrb,
    Transport,
    AsyncClient,
    AsyncStream,
    RequestOptions,
)
from ._version import __title__, __version__
from ._exceptions import (
    APIError,
    OrbError,
    URLNotFound,
    ConflictError,
    NotFoundError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    RequestTooLarge,
    TooManyRequests,
    ResourceConflict,
    ResourceNotFound,
    ResourceTooLarge,
    APIConnectionError,
    AuthenticationError,
    ConstraintViolation,
    FeatureNotAvailable,
    InternalServerError,
    PermissionDeniedError,
    OrbAuthenticationError,
    OrbInternalServerError,
    RequestValidationError,
    UnprocessableEntityError,
    DuplicateResourceCreation,
    APIResponseValidationError,
)
from ._utils._logs import setup_logging as _setup_logging

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "OrbError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "ConstraintViolation",
    "DuplicateResourceCreation",
    "RequestValidationError",
    "OrbAuthenticationError",
    "FeatureNotAvailable",
    "ResourceNotFound",
    "URLNotFound",
    "ResourceConflict",
    "RequestTooLarge",
    "ResourceTooLarge",
    "TooManyRequests",
    "OrbInternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Orb",
    "AsyncOrb",
    "file_from_path",
]

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# orb._exceptions.NotFoundError -> orb.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            setattr(__locals[__name], "__module__", "orb")
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
