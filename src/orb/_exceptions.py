# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ._utils import is_mapping
from ._models import construct_type

__all__ = [
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
    "FeatureNotAvailable",
    "RequestValidationError",
    "OrbAuthenticationError",
    "ResourceNotFound",
    "URLNotFound",
    "ResourceConflict",
    "RequestTooLarge",
    "ResourceTooLarge",
    "TooManyRequests",
    "OrbInternalServerError",
]


class OrbError(Exception):
    pass


class APIError(OrbError):
    message: str
    request: httpx.Request

    body: object | None
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:  # noqa: ARG002
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body


class APIResponseValidationError(APIError):
    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, body: object | None, *, message: str | None = None) -> None:
        super().__init__(message or "Data returned by API invalid for expected schema.", response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """Raised when an API response has a status code of 4xx or 5xx."""

    response: httpx.Response
    status_code: int

    def __init__(self, message: str, *, response: httpx.Response, body: object | None) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code


class APIConnectionError(APIError):
    def __init__(self, *, message: str = "Connection error.", request: httpx.Request) -> None:
        super().__init__(message, request, body=None)


class APITimeoutError(APIConnectionError):
    def __init__(self, request: httpx.Request) -> None:
        super().__init__(message="Request timed out.", request=request)


class BadRequestError(APIStatusError):
    status_code: Literal[400] = 400  # pyright: ignore[reportIncompatibleVariableOverride]


class AuthenticationError(APIStatusError):
    status_code: Literal[401] = 401  # pyright: ignore[reportIncompatibleVariableOverride]


class PermissionDeniedError(APIStatusError):
    status_code: Literal[403] = 403  # pyright: ignore[reportIncompatibleVariableOverride]


class NotFoundError(APIStatusError):
    status_code: Literal[404] = 404  # pyright: ignore[reportIncompatibleVariableOverride]


class ConflictError(APIStatusError):
    status_code: Literal[409] = 409  # pyright: ignore[reportIncompatibleVariableOverride]


class UnprocessableEntityError(APIStatusError):
    status_code: Literal[422] = 422  # pyright: ignore[reportIncompatibleVariableOverride]


class RateLimitError(APIStatusError):
    status_code: Literal[429] = 429  # pyright: ignore[reportIncompatibleVariableOverride]


class InternalServerError(APIStatusError):
    pass


class ConstraintViolation(BadRequestError):
    status: Literal[400]

    type: Literal["https://docs.withorb.com/reference/error-responses#400-constraint-violation"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[400], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#400-constraint-violation"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class DuplicateResourceCreation(BadRequestError):
    status: Literal[400]

    type: Literal["https://docs.withorb.com/reference/error-responses#400-duplicate-resource-creation"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[400], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#400-duplicate-resource-creation"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class FeatureNotAvailable(BadRequestError):
    status: Literal[400]

    type: Literal["https://docs.withorb.com/reference/error-responses#404-feature-not-available"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[400], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#404-feature-not-available"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class RequestValidationError(BadRequestError):
    status: Literal[400]

    type: Literal["https://docs.withorb.com/reference/error-responses#400-request-validation-errors"]

    validation_errors: List[object]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[400], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#400-request-validation-errors"],
                value=data.get("type"),
            ),
        )
        self.validation_errors = cast(Any, construct_type(type_=List[object], value=data.get("validation_errors")))
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class OrbAuthenticationError(AuthenticationError):
    status: Literal[401]

    type: Literal["https://docs.withorb.com/reference/error-responses#401-authentication-error"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[401], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#401-authentication-error"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class ResourceNotFound(NotFoundError):
    status: Literal[404]

    title: str

    type: Literal["https://docs.withorb.com/reference/error-responses#404-resource-not-found"]

    detail: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[404], value=data.get("status")))
        self.title = cast(Any, construct_type(type_=str, value=data.get("title")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#404-resource-not-found"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))


class URLNotFound(NotFoundError):
    status: Literal[404]

    type: Literal["https://docs.withorb.com/reference/error-responses#404-url-not-found"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[404], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#404-url-not-found"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class ResourceConflict(ConflictError):
    status: Literal[409]

    type: Literal["https://docs.withorb.com/reference/error-responses#409-resource-conflict"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[409], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#409-resource-conflict"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class RequestTooLarge(APIStatusError):
    status: Literal[413]

    type: Literal["https://docs.withorb.com/reference/error-responses#413-request-too-large"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[413], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#413-request-too-large"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class ResourceTooLarge(APIStatusError):
    status: Literal[413]

    type: Literal["https://docs.withorb.com/reference/error-responses#413-resource-too-large"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[413], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#413-resource-too-large"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class TooManyRequests(RateLimitError):
    status: Literal[429]

    type: Literal["https://docs.withorb.com/reference/error-responses#429-too-many-requests"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[429], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#429-too-many-requests"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))


class OrbInternalServerError(InternalServerError):
    status: Literal[500]

    type: Literal["https://docs.withorb.com/reference/error-responses#500-internal-server-error"]

    detail: Optional[str] = None

    title: Optional[str] = None

    def __init__(self, message: str, *, body: object, response: httpx.Response) -> None:
        data = cast(Mapping[str, object], body if is_mapping(body) else {})
        super().__init__(message, response=response, body=body)

        self.status = cast(Any, construct_type(type_=Literal[500], value=data.get("status")))
        self.type = cast(
            Any,
            construct_type(
                type_=Literal["https://docs.withorb.com/reference/error-responses#500-internal-server-error"],
                value=data.get("type"),
            ),
        )
        self.detail = cast(Any, construct_type(type_=Optional[str], value=data.get("detail")))
        self.title = cast(Any, construct_type(type_=Optional[str], value=data.get("title")))
