# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import asyncio
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, is_mapping, get_async_library
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._exceptions import OrbError, APIStatusError
from ._base_client import DEFAULT_MAX_RETRIES, SyncAPIClient, AsyncAPIClient

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Orb",
    "AsyncOrb",
    "Client",
    "AsyncClient",
]


class Orb(SyncAPIClient):
    top_level: resources.TopLevel
    coupons: resources.Coupons
    credit_notes: resources.CreditNotes
    customers: resources.Customers
    events: resources.Events
    invoice_line_items: resources.InvoiceLineItems
    invoices: resources.Invoices
    items: resources.Items
    metrics: resources.Metrics
    plans: resources.Plans
    prices: resources.Prices
    subscriptions: resources.Subscriptions
    with_raw_response: OrbWithRawResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous orb client instance.

        This automatically infers the `api_key` argument from the `ORB_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ORB_API_KEY")
        if api_key is None:
            raise OrbError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ORB_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ORB_BASE_URL")
        if base_url is None:
            base_url = f"https://api.withorb.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.top_level = resources.TopLevel(self)
        self.coupons = resources.Coupons(self)
        self.credit_notes = resources.CreditNotes(self)
        self.customers = resources.Customers(self)
        self.events = resources.Events(self)
        self.invoice_line_items = resources.InvoiceLineItems(self)
        self.invoices = resources.Invoices(self)
        self.items = resources.Items(self)
        self.metrics = resources.Metrics(self)
        self.plans = resources.Plans(self)
        self.prices = resources.Prices(self)
        self.subscriptions = resources.Subscriptions(self)
        self.with_raw_response = OrbWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or str(self.base_url),
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        if not hasattr(self, "_has_custom_http_client") or not hasattr(self, "close"):
            # this can happen if the '__init__' method raised an error
            return

        if self._has_custom_http_client:
            return

        self.close()

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        type_ = body.get("type") if is_mapping(body) else None
        if type_ == "https://docs.withorb.com/reference/error-responses#400-constraint-violation":
            return _exceptions.ConstraintViolation(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#400-duplicate-resource-creation":
            return _exceptions.DuplicateResourceCreation(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#404-feature-not-available":
            return _exceptions.FeatureNotAvailable(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#400-request-validation-errors":
            return _exceptions.RequestValidationError(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#401-authentication-error":
            return _exceptions.OrbAuthenticationError(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#404-resource-not-found":
            return _exceptions.ResourceNotFound(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#404-url-not-found":
            return _exceptions.URLNotFound(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#409-resource-conflict":
            return _exceptions.ResourceConflict(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#413-request-too-large":
            return _exceptions.RequestTooLarge(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#413-resource-too-large":
            return _exceptions.ResourceTooLarge(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#429-too-many-requests":
            return _exceptions.TooManyRequests(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#500-internal-server-error":
            return _exceptions.OrbInternalServerError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.OrbInternalServerError(
                err_msg,
                response=response,
                body={
                    "status": 500,
                    "type": "https://docs.withorb.com/reference/error-responses#500-internal-server-error",
                    "detail": None,
                    "title": None,
                },
            )

        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOrb(AsyncAPIClient):
    top_level: resources.AsyncTopLevel
    coupons: resources.AsyncCoupons
    credit_notes: resources.AsyncCreditNotes
    customers: resources.AsyncCustomers
    events: resources.AsyncEvents
    invoice_line_items: resources.AsyncInvoiceLineItems
    invoices: resources.AsyncInvoices
    items: resources.AsyncItems
    metrics: resources.AsyncMetrics
    plans: resources.AsyncPlans
    prices: resources.AsyncPrices
    subscriptions: resources.AsyncSubscriptions
    with_raw_response: AsyncOrbWithRawResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async orb client instance.

        This automatically infers the `api_key` argument from the `ORB_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ORB_API_KEY")
        if api_key is None:
            raise OrbError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ORB_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ORB_BASE_URL")
        if base_url is None:
            base_url = f"https://api.withorb.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._idempotency_header = "Idempotency-Key"

        self.top_level = resources.AsyncTopLevel(self)
        self.coupons = resources.AsyncCoupons(self)
        self.credit_notes = resources.AsyncCreditNotes(self)
        self.customers = resources.AsyncCustomers(self)
        self.events = resources.AsyncEvents(self)
        self.invoice_line_items = resources.AsyncInvoiceLineItems(self)
        self.invoices = resources.AsyncInvoices(self)
        self.items = resources.AsyncItems(self)
        self.metrics = resources.AsyncMetrics(self)
        self.plans = resources.AsyncPlans(self)
        self.prices = resources.AsyncPrices(self)
        self.subscriptions = resources.AsyncSubscriptions(self)
        self.with_raw_response = AsyncOrbWithRawResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or str(self.base_url),
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        if not hasattr(self, "_has_custom_http_client") or not hasattr(self, "close"):
            # this can happen if the '__init__' method raised an error
            return

        if self._has_custom_http_client:
            return

        try:
            asyncio.get_running_loop().create_task(self.close())
        except Exception:
            pass

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        type_ = body.get("type") if is_mapping(body) else None
        if type_ == "https://docs.withorb.com/reference/error-responses#400-constraint-violation":
            return _exceptions.ConstraintViolation(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#400-duplicate-resource-creation":
            return _exceptions.DuplicateResourceCreation(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#404-feature-not-available":
            return _exceptions.FeatureNotAvailable(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#400-request-validation-errors":
            return _exceptions.RequestValidationError(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#401-authentication-error":
            return _exceptions.OrbAuthenticationError(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#404-resource-not-found":
            return _exceptions.ResourceNotFound(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#404-url-not-found":
            return _exceptions.URLNotFound(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#409-resource-conflict":
            return _exceptions.ResourceConflict(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#413-request-too-large":
            return _exceptions.RequestTooLarge(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#413-resource-too-large":
            return _exceptions.ResourceTooLarge(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#429-too-many-requests":
            return _exceptions.TooManyRequests(err_msg, response=response, body=body)

        if type_ == "https://docs.withorb.com/reference/error-responses#500-internal-server-error":
            return _exceptions.OrbInternalServerError(err_msg, response=response, body=body)
        if response.status_code >= 500:
            return _exceptions.OrbInternalServerError(
                err_msg,
                response=response,
                body={
                    "status": 500,
                    "type": "https://docs.withorb.com/reference/error-responses#500-internal-server-error",
                    "detail": None,
                    "title": None,
                },
            )

        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OrbWithRawResponse:
    def __init__(self, client: Orb) -> None:
        self.top_level = resources.TopLevelWithRawResponse(client.top_level)
        self.coupons = resources.CouponsWithRawResponse(client.coupons)
        self.credit_notes = resources.CreditNotesWithRawResponse(client.credit_notes)
        self.customers = resources.CustomersWithRawResponse(client.customers)
        self.events = resources.EventsWithRawResponse(client.events)
        self.invoice_line_items = resources.InvoiceLineItemsWithRawResponse(client.invoice_line_items)
        self.invoices = resources.InvoicesWithRawResponse(client.invoices)
        self.items = resources.ItemsWithRawResponse(client.items)
        self.metrics = resources.MetricsWithRawResponse(client.metrics)
        self.plans = resources.PlansWithRawResponse(client.plans)
        self.prices = resources.PricesWithRawResponse(client.prices)
        self.subscriptions = resources.SubscriptionsWithRawResponse(client.subscriptions)


class AsyncOrbWithRawResponse:
    def __init__(self, client: AsyncOrb) -> None:
        self.top_level = resources.AsyncTopLevelWithRawResponse(client.top_level)
        self.coupons = resources.AsyncCouponsWithRawResponse(client.coupons)
        self.credit_notes = resources.AsyncCreditNotesWithRawResponse(client.credit_notes)
        self.customers = resources.AsyncCustomersWithRawResponse(client.customers)
        self.events = resources.AsyncEventsWithRawResponse(client.events)
        self.invoice_line_items = resources.AsyncInvoiceLineItemsWithRawResponse(client.invoice_line_items)
        self.invoices = resources.AsyncInvoicesWithRawResponse(client.invoices)
        self.items = resources.AsyncItemsWithRawResponse(client.items)
        self.metrics = resources.AsyncMetricsWithRawResponse(client.metrics)
        self.plans = resources.AsyncPlansWithRawResponse(client.plans)
        self.prices = resources.AsyncPricesWithRawResponse(client.prices)
        self.subscriptions = resources.AsyncSubscriptionsWithRawResponse(client.subscriptions)


Client = Orb

AsyncClient = AsyncOrb
