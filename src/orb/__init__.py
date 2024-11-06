# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from . import types
from ._version import __version__, __title__
from ._client import Timeout, Transport, RequestOptions, Client, AsyncClient, Stream, AsyncStream, Orb, AsyncOrb
from ._exceptions import (
    OrbError,
    APIError,
    APIStatusError,
    APITimeoutError,
    APIConnectionError,
    APIResponseValidationError,
    BadRequestError,
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    ConflictError,
    UnprocessableEntityError,
    RateLimitError,
    InternalServerError,
    ConstraintViolation,
    DuplicateResourceCreation,
    RequestValidationError,
    OrbAuthenticationError,
    FeatureNotAvailable,
    ResourceNotFound,
    URLNotFound,
    ResourceConflict,
    RequestTooLarge,
    ResourceTooLarge,
    TooManyRequests,
    OrbInternalServerError,
)
from ._types import NoneType, Transport, ProxiesTypes, NotGiven, NOT_GIVEN
from ._utils import file_from_path
from ._models import BaseModel
from ._constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS
from ._base_client import DefaultHttpxClient, DefaultAsyncHttpxClient
from ._utils._logs import setup_logging as _setup_logging
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
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
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
    "DefaultHttpxClient",
    "DefaultAsyncHttpxClient",
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
