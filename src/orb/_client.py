# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
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
from ._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._version import __version__
from .resources import (
    items,
    alerts,
    metrics,
    invoices,
    webhooks,
    top_level,
    credit_notes,
    subscriptions,
    invoice_line_items,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import OrbError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.plans import plans
from .resources.events import events
from .resources.prices import prices
from .resources.coupons import coupons
from .resources.customers import customers

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Orb", "AsyncOrb", "Client", "AsyncClient"]


class Orb(SyncAPIClient):
    top_level: top_level.TopLevel
    coupons: coupons.Coupons
    credit_notes: credit_notes.CreditNotes
    customers: customers.Customers
    events: events.Events
    invoice_line_items: invoice_line_items.InvoiceLineItems
    invoices: invoices.Invoices
    items: items.Items
    metrics: metrics.Metrics
    plans: plans.Plans
    prices: prices.Prices
    subscriptions: subscriptions.Subscriptions
    webhooks: webhooks.Webhooks
    alerts: alerts.Alerts
    with_raw_response: OrbWithRawResponse
    with_streaming_response: OrbWithStreamedResponse

    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `ORB_API_KEY`
        - `webhook_secret` from `ORB_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("ORB_API_KEY")
        if api_key is None:
            raise OrbError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ORB_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("ORB_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

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

        self.top_level = top_level.TopLevel(self)
        self.coupons = coupons.Coupons(self)
        self.credit_notes = credit_notes.CreditNotes(self)
        self.customers = customers.Customers(self)
        self.events = events.Events(self)
        self.invoice_line_items = invoice_line_items.InvoiceLineItems(self)
        self.invoices = invoices.Invoices(self)
        self.items = items.Items(self)
        self.metrics = metrics.Metrics(self)
        self.plans = plans.Plans(self)
        self.prices = prices.Prices(self)
        self.subscriptions = subscriptions.Subscriptions(self)
        self.webhooks = webhooks.Webhooks(self)
        self.alerts = alerts.Alerts(self)
        self.with_raw_response = OrbWithRawResponse(self)
        self.with_streaming_response = OrbWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

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
        webhook_secret: str | None = None,
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
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
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
    top_level: top_level.AsyncTopLevel
    coupons: coupons.AsyncCoupons
    credit_notes: credit_notes.AsyncCreditNotes
    customers: customers.AsyncCustomers
    events: events.AsyncEvents
    invoice_line_items: invoice_line_items.AsyncInvoiceLineItems
    invoices: invoices.AsyncInvoices
    items: items.AsyncItems
    metrics: metrics.AsyncMetrics
    plans: plans.AsyncPlans
    prices: prices.AsyncPrices
    subscriptions: subscriptions.AsyncSubscriptions
    webhooks: webhooks.AsyncWebhooks
    alerts: alerts.AsyncAlerts
    with_raw_response: AsyncOrbWithRawResponse
    with_streaming_response: AsyncOrbWithStreamedResponse

    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
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

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `ORB_API_KEY`
        - `webhook_secret` from `ORB_WEBHOOK_SECRET`
        """
        if api_key is None:
            api_key = os.environ.get("ORB_API_KEY")
        if api_key is None:
            raise OrbError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ORB_API_KEY environment variable"
            )
        self.api_key = api_key

        if webhook_secret is None:
            webhook_secret = os.environ.get("ORB_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

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

        self.top_level = top_level.AsyncTopLevel(self)
        self.coupons = coupons.AsyncCoupons(self)
        self.credit_notes = credit_notes.AsyncCreditNotes(self)
        self.customers = customers.AsyncCustomers(self)
        self.events = events.AsyncEvents(self)
        self.invoice_line_items = invoice_line_items.AsyncInvoiceLineItems(self)
        self.invoices = invoices.AsyncInvoices(self)
        self.items = items.AsyncItems(self)
        self.metrics = metrics.AsyncMetrics(self)
        self.plans = plans.AsyncPlans(self)
        self.prices = prices.AsyncPrices(self)
        self.subscriptions = subscriptions.AsyncSubscriptions(self)
        self.webhooks = webhooks.AsyncWebhooks(self)
        self.alerts = alerts.AsyncAlerts(self)
        self.with_raw_response = AsyncOrbWithRawResponse(self)
        self.with_streaming_response = AsyncOrbWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

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
        webhook_secret: str | None = None,
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
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
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
        self.top_level = top_level.TopLevelWithRawResponse(client.top_level)
        self.coupons = coupons.CouponsWithRawResponse(client.coupons)
        self.credit_notes = credit_notes.CreditNotesWithRawResponse(client.credit_notes)
        self.customers = customers.CustomersWithRawResponse(client.customers)
        self.events = events.EventsWithRawResponse(client.events)
        self.invoice_line_items = invoice_line_items.InvoiceLineItemsWithRawResponse(client.invoice_line_items)
        self.invoices = invoices.InvoicesWithRawResponse(client.invoices)
        self.items = items.ItemsWithRawResponse(client.items)
        self.metrics = metrics.MetricsWithRawResponse(client.metrics)
        self.plans = plans.PlansWithRawResponse(client.plans)
        self.prices = prices.PricesWithRawResponse(client.prices)
        self.subscriptions = subscriptions.SubscriptionsWithRawResponse(client.subscriptions)
        self.alerts = alerts.AlertsWithRawResponse(client.alerts)


class AsyncOrbWithRawResponse:
    def __init__(self, client: AsyncOrb) -> None:
        self.top_level = top_level.AsyncTopLevelWithRawResponse(client.top_level)
        self.coupons = coupons.AsyncCouponsWithRawResponse(client.coupons)
        self.credit_notes = credit_notes.AsyncCreditNotesWithRawResponse(client.credit_notes)
        self.customers = customers.AsyncCustomersWithRawResponse(client.customers)
        self.events = events.AsyncEventsWithRawResponse(client.events)
        self.invoice_line_items = invoice_line_items.AsyncInvoiceLineItemsWithRawResponse(client.invoice_line_items)
        self.invoices = invoices.AsyncInvoicesWithRawResponse(client.invoices)
        self.items = items.AsyncItemsWithRawResponse(client.items)
        self.metrics = metrics.AsyncMetricsWithRawResponse(client.metrics)
        self.plans = plans.AsyncPlansWithRawResponse(client.plans)
        self.prices = prices.AsyncPricesWithRawResponse(client.prices)
        self.subscriptions = subscriptions.AsyncSubscriptionsWithRawResponse(client.subscriptions)
        self.alerts = alerts.AsyncAlertsWithRawResponse(client.alerts)


class OrbWithStreamedResponse:
    def __init__(self, client: Orb) -> None:
        self.top_level = top_level.TopLevelWithStreamingResponse(client.top_level)
        self.coupons = coupons.CouponsWithStreamingResponse(client.coupons)
        self.credit_notes = credit_notes.CreditNotesWithStreamingResponse(client.credit_notes)
        self.customers = customers.CustomersWithStreamingResponse(client.customers)
        self.events = events.EventsWithStreamingResponse(client.events)
        self.invoice_line_items = invoice_line_items.InvoiceLineItemsWithStreamingResponse(client.invoice_line_items)
        self.invoices = invoices.InvoicesWithStreamingResponse(client.invoices)
        self.items = items.ItemsWithStreamingResponse(client.items)
        self.metrics = metrics.MetricsWithStreamingResponse(client.metrics)
        self.plans = plans.PlansWithStreamingResponse(client.plans)
        self.prices = prices.PricesWithStreamingResponse(client.prices)
        self.subscriptions = subscriptions.SubscriptionsWithStreamingResponse(client.subscriptions)
        self.alerts = alerts.AlertsWithStreamingResponse(client.alerts)


class AsyncOrbWithStreamedResponse:
    def __init__(self, client: AsyncOrb) -> None:
        self.top_level = top_level.AsyncTopLevelWithStreamingResponse(client.top_level)
        self.coupons = coupons.AsyncCouponsWithStreamingResponse(client.coupons)
        self.credit_notes = credit_notes.AsyncCreditNotesWithStreamingResponse(client.credit_notes)
        self.customers = customers.AsyncCustomersWithStreamingResponse(client.customers)
        self.events = events.AsyncEventsWithStreamingResponse(client.events)
        self.invoice_line_items = invoice_line_items.AsyncInvoiceLineItemsWithStreamingResponse(
            client.invoice_line_items
        )
        self.invoices = invoices.AsyncInvoicesWithStreamingResponse(client.invoices)
        self.items = items.AsyncItemsWithStreamingResponse(client.items)
        self.metrics = metrics.AsyncMetricsWithStreamingResponse(client.metrics)
        self.plans = plans.AsyncPlansWithStreamingResponse(client.plans)
        self.prices = prices.AsyncPricesWithStreamingResponse(client.prices)
        self.subscriptions = subscriptions.AsyncSubscriptionsWithStreamingResponse(client.subscriptions)
        self.alerts = alerts.AsyncAlertsWithStreamingResponse(client.alerts)


Client = Orb

AsyncClient = AsyncOrb
