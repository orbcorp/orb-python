# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import OrbError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        beta,
        items,
        plans,
        alerts,
        events,
        prices,
        coupons,
        metrics,
        invoices,
        webhooks,
        licenses,
        customers,
        top_level,
        credit_notes,
        credit_blocks,
        license_types,
        subscriptions,
        invoice_line_items,
        subscription_changes,
        dimensional_price_groups,
    )
    from .resources.items import Items, AsyncItems
    from .resources.alerts import Alerts, AsyncAlerts
    from .resources.metrics import Metrics, AsyncMetrics
    from .resources.invoices import Invoices, AsyncInvoices
    from .resources.beta.beta import Beta, AsyncBeta
    from .resources.top_level import TopLevel, AsyncTopLevel
    from .resources.plans.plans import Plans, AsyncPlans
    from .resources.credit_notes import CreditNotes, AsyncCreditNotes
    from .resources.credit_blocks import CreditBlocks, AsyncCreditBlocks
    from .resources.events.events import Events, AsyncEvents
    from .resources.license_types import LicenseTypes, AsyncLicenseTypes
    from .resources.prices.prices import Prices, AsyncPrices
    from .resources.subscriptions import Subscriptions, AsyncSubscriptions
    from .resources.coupons.coupons import Coupons, AsyncCoupons
    from .resources.licenses.licenses import Licenses, AsyncLicenses
    from .resources.invoice_line_items import InvoiceLineItems, AsyncInvoiceLineItems
    from .resources.customers.customers import Customers, AsyncCustomers
    from .resources.subscription_changes import SubscriptionChanges, AsyncSubscriptionChanges
    from .resources.dimensional_price_groups.dimensional_price_groups import (
        DimensionalPriceGroups,
        AsyncDimensionalPriceGroups,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Orb", "AsyncOrb", "Client", "AsyncClient"]


class Orb(SyncAPIClient):
    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Orb client instance.

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

        custom_headers_env = os.environ.get("ORB_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

    @cached_property
    def top_level(self) -> TopLevel:
        from .resources.top_level import TopLevel

        return TopLevel(self)

    @cached_property
    def beta(self) -> Beta:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.beta import Beta

        return Beta(self)

    @cached_property
    def coupons(self) -> Coupons:
        """
        A coupon represents a reusable discount configuration that can be applied either as a fixed or percentage amount to an invoice or subscription. Coupons are activated using a redemption code, which applies the discount to a subscription or invoice. The duration of a coupon determines how long it remains available for use by end users.
        """
        from .resources.coupons import Coupons

        return Coupons(self)

    @cached_property
    def credit_notes(self) -> CreditNotes:
        """
        The [Credit Note](/invoicing/credit-notes) resource represents a credit that has been applied to a
        particular invoice.
        """
        from .resources.credit_notes import CreditNotes

        return CreditNotes(self)

    @cached_property
    def customers(self) -> Customers:
        """
        A customer is a buyer of your products, and the other party to the billing relationship.

        In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these
        match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an
        `external_customer_id` with your own identifier. See
        [Customer ID Aliases](/events-and-metrics/customer-aliases) for further information about how these
        aliases work in Orb.

        In addition to having an identifier in your system, a customer may exist in a payment provider solution like
        Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.

        A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which
        defaults to your account's timezone. See [Timezone localization](/essentials/timezones) for
        information on what this timezone parameter influences within Orb.
        """
        from .resources.customers import Customers

        return Customers(self)

    @cached_property
    def events(self) -> Events:
        """
        The [Event](/core-concepts#event) resource represents a usage event that has been created for a
        customer. Events are the core of Orb's usage-based billing model, and are used to calculate the usage charges for
        a given billing period.
        """
        from .resources.events import Events

        return Events(self)

    @cached_property
    def invoice_line_items(self) -> InvoiceLineItems:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoice_line_items import InvoiceLineItems

        return InvoiceLineItems(self)

    @cached_property
    def invoices(self) -> Invoices:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoices import Invoices

        return Invoices(self)

    @cached_property
    def items(self) -> Items:
        """The Item resource represents a sellable product or good.

        Items are associated with all line items, billable metrics,
        and prices and are used for defining external sync behavior for invoices and tax calculation purposes.
        """
        from .resources.items import Items

        return Items(self)

    @cached_property
    def metrics(self) -> Metrics:
        """
        The Metric resource represents a calculation of a quantity based on events.
        Metrics are defined by the query that transforms raw usage events into meaningful values for your customers.
        """
        from .resources.metrics import Metrics

        return Metrics(self)

    @cached_property
    def plans(self) -> Plans:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.plans import Plans

        return Plans(self)

    @cached_property
    def prices(self) -> Prices:
        """
        The Price resource represents a price that can be billed on a subscription, resulting in a charge on an invoice in
        the form of an invoice line item. Prices take a quantity and determine an amount to bill.

        Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a
        given Price object. The model_type field determines the key for the configuration object that is present.

        For more on the types of prices, see [the core concepts documentation](/core-concepts#plan-and-price)
        """
        from .resources.prices import Prices

        return Prices(self)

    @cached_property
    def subscriptions(self) -> Subscriptions:
        from .resources.subscriptions import Subscriptions

        return Subscriptions(self)

    @cached_property
    def alerts(self) -> Alerts:
        """
        [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
        usage, or credit balance and trigger webhooks when a threshold is exceeded.

        Alerts created through the API can be scoped to either customers or subscriptions.
        """
        from .resources.alerts import Alerts

        return Alerts(self)

    @cached_property
    def dimensional_price_groups(self) -> DimensionalPriceGroups:
        from .resources.dimensional_price_groups import DimensionalPriceGroups

        return DimensionalPriceGroups(self)

    @cached_property
    def subscription_changes(self) -> SubscriptionChanges:
        from .resources.subscription_changes import SubscriptionChanges

        return SubscriptionChanges(self)

    @cached_property
    def webhooks(self) -> webhooks.Webhooks:
        from .resources.webhooks import Webhooks

        return Webhooks(self)

    @cached_property
    def credit_blocks(self) -> CreditBlocks:
        """
        The [Credit Ledger Entry resource](/product-catalog/prepurchase) models prepaid credits within Orb.
        """
        from .resources.credit_blocks import CreditBlocks

        return CreditBlocks(self)

    @cached_property
    def license_types(self) -> LicenseTypes:
        """
        The LicenseType resource represents a type of license that can be assigned to users.
        License types are used during billing by grouping metrics on the configured grouping key.
        """
        from .resources.license_types import LicenseTypes

        return LicenseTypes(self)

    @cached_property
    def licenses(self) -> Licenses:
        from .resources.licenses import Licenses

        return Licenses(self)

    @cached_property
    def with_raw_response(self) -> OrbWithRawResponse:
        return OrbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrbWithStreamedResponse:
        return OrbWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    api_key: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncOrb client instance.

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

        custom_headers_env = os.environ.get("ORB_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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

    @cached_property
    def top_level(self) -> AsyncTopLevel:
        from .resources.top_level import AsyncTopLevel

        return AsyncTopLevel(self)

    @cached_property
    def beta(self) -> AsyncBeta:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.beta import AsyncBeta

        return AsyncBeta(self)

    @cached_property
    def coupons(self) -> AsyncCoupons:
        """
        A coupon represents a reusable discount configuration that can be applied either as a fixed or percentage amount to an invoice or subscription. Coupons are activated using a redemption code, which applies the discount to a subscription or invoice. The duration of a coupon determines how long it remains available for use by end users.
        """
        from .resources.coupons import AsyncCoupons

        return AsyncCoupons(self)

    @cached_property
    def credit_notes(self) -> AsyncCreditNotes:
        """
        The [Credit Note](/invoicing/credit-notes) resource represents a credit that has been applied to a
        particular invoice.
        """
        from .resources.credit_notes import AsyncCreditNotes

        return AsyncCreditNotes(self)

    @cached_property
    def customers(self) -> AsyncCustomers:
        """
        A customer is a buyer of your products, and the other party to the billing relationship.

        In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these
        match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an
        `external_customer_id` with your own identifier. See
        [Customer ID Aliases](/events-and-metrics/customer-aliases) for further information about how these
        aliases work in Orb.

        In addition to having an identifier in your system, a customer may exist in a payment provider solution like
        Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.

        A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which
        defaults to your account's timezone. See [Timezone localization](/essentials/timezones) for
        information on what this timezone parameter influences within Orb.
        """
        from .resources.customers import AsyncCustomers

        return AsyncCustomers(self)

    @cached_property
    def events(self) -> AsyncEvents:
        """
        The [Event](/core-concepts#event) resource represents a usage event that has been created for a
        customer. Events are the core of Orb's usage-based billing model, and are used to calculate the usage charges for
        a given billing period.
        """
        from .resources.events import AsyncEvents

        return AsyncEvents(self)

    @cached_property
    def invoice_line_items(self) -> AsyncInvoiceLineItems:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoice_line_items import AsyncInvoiceLineItems

        return AsyncInvoiceLineItems(self)

    @cached_property
    def invoices(self) -> AsyncInvoices:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoices import AsyncInvoices

        return AsyncInvoices(self)

    @cached_property
    def items(self) -> AsyncItems:
        """The Item resource represents a sellable product or good.

        Items are associated with all line items, billable metrics,
        and prices and are used for defining external sync behavior for invoices and tax calculation purposes.
        """
        from .resources.items import AsyncItems

        return AsyncItems(self)

    @cached_property
    def metrics(self) -> AsyncMetrics:
        """
        The Metric resource represents a calculation of a quantity based on events.
        Metrics are defined by the query that transforms raw usage events into meaningful values for your customers.
        """
        from .resources.metrics import AsyncMetrics

        return AsyncMetrics(self)

    @cached_property
    def plans(self) -> AsyncPlans:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.plans import AsyncPlans

        return AsyncPlans(self)

    @cached_property
    def prices(self) -> AsyncPrices:
        """
        The Price resource represents a price that can be billed on a subscription, resulting in a charge on an invoice in
        the form of an invoice line item. Prices take a quantity and determine an amount to bill.

        Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a
        given Price object. The model_type field determines the key for the configuration object that is present.

        For more on the types of prices, see [the core concepts documentation](/core-concepts#plan-and-price)
        """
        from .resources.prices import AsyncPrices

        return AsyncPrices(self)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        from .resources.subscriptions import AsyncSubscriptions

        return AsyncSubscriptions(self)

    @cached_property
    def alerts(self) -> AsyncAlerts:
        """
        [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
        usage, or credit balance and trigger webhooks when a threshold is exceeded.

        Alerts created through the API can be scoped to either customers or subscriptions.
        """
        from .resources.alerts import AsyncAlerts

        return AsyncAlerts(self)

    @cached_property
    def dimensional_price_groups(self) -> AsyncDimensionalPriceGroups:
        from .resources.dimensional_price_groups import AsyncDimensionalPriceGroups

        return AsyncDimensionalPriceGroups(self)

    @cached_property
    def subscription_changes(self) -> AsyncSubscriptionChanges:
        from .resources.subscription_changes import AsyncSubscriptionChanges

        return AsyncSubscriptionChanges(self)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooks:
        from .resources.webhooks import AsyncWebhooks

        return AsyncWebhooks(self)

    @cached_property
    def credit_blocks(self) -> AsyncCreditBlocks:
        """
        The [Credit Ledger Entry resource](/product-catalog/prepurchase) models prepaid credits within Orb.
        """
        from .resources.credit_blocks import AsyncCreditBlocks

        return AsyncCreditBlocks(self)

    @cached_property
    def license_types(self) -> AsyncLicenseTypes:
        """
        The LicenseType resource represents a type of license that can be assigned to users.
        License types are used during billing by grouping metrics on the configured grouping key.
        """
        from .resources.license_types import AsyncLicenseTypes

        return AsyncLicenseTypes(self)

    @cached_property
    def licenses(self) -> AsyncLicenses:
        from .resources.licenses import AsyncLicenses

        return AsyncLicenses(self)

    @cached_property
    def with_raw_response(self) -> AsyncOrbWithRawResponse:
        return AsyncOrbWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrbWithStreamedResponse:
        return AsyncOrbWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Orb

    def __init__(self, client: Orb) -> None:
        self._client = client

    @cached_property
    def top_level(self) -> top_level.TopLevelWithRawResponse:
        from .resources.top_level import TopLevelWithRawResponse

        return TopLevelWithRawResponse(self._client.top_level)

    @cached_property
    def beta(self) -> beta.BetaWithRawResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.beta import BetaWithRawResponse

        return BetaWithRawResponse(self._client.beta)

    @cached_property
    def coupons(self) -> coupons.CouponsWithRawResponse:
        """
        A coupon represents a reusable discount configuration that can be applied either as a fixed or percentage amount to an invoice or subscription. Coupons are activated using a redemption code, which applies the discount to a subscription or invoice. The duration of a coupon determines how long it remains available for use by end users.
        """
        from .resources.coupons import CouponsWithRawResponse

        return CouponsWithRawResponse(self._client.coupons)

    @cached_property
    def credit_notes(self) -> credit_notes.CreditNotesWithRawResponse:
        """
        The [Credit Note](/invoicing/credit-notes) resource represents a credit that has been applied to a
        particular invoice.
        """
        from .resources.credit_notes import CreditNotesWithRawResponse

        return CreditNotesWithRawResponse(self._client.credit_notes)

    @cached_property
    def customers(self) -> customers.CustomersWithRawResponse:
        """
        A customer is a buyer of your products, and the other party to the billing relationship.

        In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these
        match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an
        `external_customer_id` with your own identifier. See
        [Customer ID Aliases](/events-and-metrics/customer-aliases) for further information about how these
        aliases work in Orb.

        In addition to having an identifier in your system, a customer may exist in a payment provider solution like
        Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.

        A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which
        defaults to your account's timezone. See [Timezone localization](/essentials/timezones) for
        information on what this timezone parameter influences within Orb.
        """
        from .resources.customers import CustomersWithRawResponse

        return CustomersWithRawResponse(self._client.customers)

    @cached_property
    def events(self) -> events.EventsWithRawResponse:
        """
        The [Event](/core-concepts#event) resource represents a usage event that has been created for a
        customer. Events are the core of Orb's usage-based billing model, and are used to calculate the usage charges for
        a given billing period.
        """
        from .resources.events import EventsWithRawResponse

        return EventsWithRawResponse(self._client.events)

    @cached_property
    def invoice_line_items(self) -> invoice_line_items.InvoiceLineItemsWithRawResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoice_line_items import InvoiceLineItemsWithRawResponse

        return InvoiceLineItemsWithRawResponse(self._client.invoice_line_items)

    @cached_property
    def invoices(self) -> invoices.InvoicesWithRawResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoices import InvoicesWithRawResponse

        return InvoicesWithRawResponse(self._client.invoices)

    @cached_property
    def items(self) -> items.ItemsWithRawResponse:
        """The Item resource represents a sellable product or good.

        Items are associated with all line items, billable metrics,
        and prices and are used for defining external sync behavior for invoices and tax calculation purposes.
        """
        from .resources.items import ItemsWithRawResponse

        return ItemsWithRawResponse(self._client.items)

    @cached_property
    def metrics(self) -> metrics.MetricsWithRawResponse:
        """
        The Metric resource represents a calculation of a quantity based on events.
        Metrics are defined by the query that transforms raw usage events into meaningful values for your customers.
        """
        from .resources.metrics import MetricsWithRawResponse

        return MetricsWithRawResponse(self._client.metrics)

    @cached_property
    def plans(self) -> plans.PlansWithRawResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.plans import PlansWithRawResponse

        return PlansWithRawResponse(self._client.plans)

    @cached_property
    def prices(self) -> prices.PricesWithRawResponse:
        """
        The Price resource represents a price that can be billed on a subscription, resulting in a charge on an invoice in
        the form of an invoice line item. Prices take a quantity and determine an amount to bill.

        Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a
        given Price object. The model_type field determines the key for the configuration object that is present.

        For more on the types of prices, see [the core concepts documentation](/core-concepts#plan-and-price)
        """
        from .resources.prices import PricesWithRawResponse

        return PricesWithRawResponse(self._client.prices)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsWithRawResponse:
        from .resources.subscriptions import SubscriptionsWithRawResponse

        return SubscriptionsWithRawResponse(self._client.subscriptions)

    @cached_property
    def alerts(self) -> alerts.AlertsWithRawResponse:
        """
        [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
        usage, or credit balance and trigger webhooks when a threshold is exceeded.

        Alerts created through the API can be scoped to either customers or subscriptions.
        """
        from .resources.alerts import AlertsWithRawResponse

        return AlertsWithRawResponse(self._client.alerts)

    @cached_property
    def dimensional_price_groups(self) -> dimensional_price_groups.DimensionalPriceGroupsWithRawResponse:
        from .resources.dimensional_price_groups import DimensionalPriceGroupsWithRawResponse

        return DimensionalPriceGroupsWithRawResponse(self._client.dimensional_price_groups)

    @cached_property
    def subscription_changes(self) -> subscription_changes.SubscriptionChangesWithRawResponse:
        from .resources.subscription_changes import SubscriptionChangesWithRawResponse

        return SubscriptionChangesWithRawResponse(self._client.subscription_changes)

    @cached_property
    def credit_blocks(self) -> credit_blocks.CreditBlocksWithRawResponse:
        """
        The [Credit Ledger Entry resource](/product-catalog/prepurchase) models prepaid credits within Orb.
        """
        from .resources.credit_blocks import CreditBlocksWithRawResponse

        return CreditBlocksWithRawResponse(self._client.credit_blocks)

    @cached_property
    def license_types(self) -> license_types.LicenseTypesWithRawResponse:
        """
        The LicenseType resource represents a type of license that can be assigned to users.
        License types are used during billing by grouping metrics on the configured grouping key.
        """
        from .resources.license_types import LicenseTypesWithRawResponse

        return LicenseTypesWithRawResponse(self._client.license_types)

    @cached_property
    def licenses(self) -> licenses.LicensesWithRawResponse:
        from .resources.licenses import LicensesWithRawResponse

        return LicensesWithRawResponse(self._client.licenses)


class AsyncOrbWithRawResponse:
    _client: AsyncOrb

    def __init__(self, client: AsyncOrb) -> None:
        self._client = client

    @cached_property
    def top_level(self) -> top_level.AsyncTopLevelWithRawResponse:
        from .resources.top_level import AsyncTopLevelWithRawResponse

        return AsyncTopLevelWithRawResponse(self._client.top_level)

    @cached_property
    def beta(self) -> beta.AsyncBetaWithRawResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.beta import AsyncBetaWithRawResponse

        return AsyncBetaWithRawResponse(self._client.beta)

    @cached_property
    def coupons(self) -> coupons.AsyncCouponsWithRawResponse:
        """
        A coupon represents a reusable discount configuration that can be applied either as a fixed or percentage amount to an invoice or subscription. Coupons are activated using a redemption code, which applies the discount to a subscription or invoice. The duration of a coupon determines how long it remains available for use by end users.
        """
        from .resources.coupons import AsyncCouponsWithRawResponse

        return AsyncCouponsWithRawResponse(self._client.coupons)

    @cached_property
    def credit_notes(self) -> credit_notes.AsyncCreditNotesWithRawResponse:
        """
        The [Credit Note](/invoicing/credit-notes) resource represents a credit that has been applied to a
        particular invoice.
        """
        from .resources.credit_notes import AsyncCreditNotesWithRawResponse

        return AsyncCreditNotesWithRawResponse(self._client.credit_notes)

    @cached_property
    def customers(self) -> customers.AsyncCustomersWithRawResponse:
        """
        A customer is a buyer of your products, and the other party to the billing relationship.

        In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these
        match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an
        `external_customer_id` with your own identifier. See
        [Customer ID Aliases](/events-and-metrics/customer-aliases) for further information about how these
        aliases work in Orb.

        In addition to having an identifier in your system, a customer may exist in a payment provider solution like
        Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.

        A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which
        defaults to your account's timezone. See [Timezone localization](/essentials/timezones) for
        information on what this timezone parameter influences within Orb.
        """
        from .resources.customers import AsyncCustomersWithRawResponse

        return AsyncCustomersWithRawResponse(self._client.customers)

    @cached_property
    def events(self) -> events.AsyncEventsWithRawResponse:
        """
        The [Event](/core-concepts#event) resource represents a usage event that has been created for a
        customer. Events are the core of Orb's usage-based billing model, and are used to calculate the usage charges for
        a given billing period.
        """
        from .resources.events import AsyncEventsWithRawResponse

        return AsyncEventsWithRawResponse(self._client.events)

    @cached_property
    def invoice_line_items(self) -> invoice_line_items.AsyncInvoiceLineItemsWithRawResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoice_line_items import AsyncInvoiceLineItemsWithRawResponse

        return AsyncInvoiceLineItemsWithRawResponse(self._client.invoice_line_items)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesWithRawResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoices import AsyncInvoicesWithRawResponse

        return AsyncInvoicesWithRawResponse(self._client.invoices)

    @cached_property
    def items(self) -> items.AsyncItemsWithRawResponse:
        """The Item resource represents a sellable product or good.

        Items are associated with all line items, billable metrics,
        and prices and are used for defining external sync behavior for invoices and tax calculation purposes.
        """
        from .resources.items import AsyncItemsWithRawResponse

        return AsyncItemsWithRawResponse(self._client.items)

    @cached_property
    def metrics(self) -> metrics.AsyncMetricsWithRawResponse:
        """
        The Metric resource represents a calculation of a quantity based on events.
        Metrics are defined by the query that transforms raw usage events into meaningful values for your customers.
        """
        from .resources.metrics import AsyncMetricsWithRawResponse

        return AsyncMetricsWithRawResponse(self._client.metrics)

    @cached_property
    def plans(self) -> plans.AsyncPlansWithRawResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.plans import AsyncPlansWithRawResponse

        return AsyncPlansWithRawResponse(self._client.plans)

    @cached_property
    def prices(self) -> prices.AsyncPricesWithRawResponse:
        """
        The Price resource represents a price that can be billed on a subscription, resulting in a charge on an invoice in
        the form of an invoice line item. Prices take a quantity and determine an amount to bill.

        Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a
        given Price object. The model_type field determines the key for the configuration object that is present.

        For more on the types of prices, see [the core concepts documentation](/core-concepts#plan-and-price)
        """
        from .resources.prices import AsyncPricesWithRawResponse

        return AsyncPricesWithRawResponse(self._client.prices)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsWithRawResponse:
        from .resources.subscriptions import AsyncSubscriptionsWithRawResponse

        return AsyncSubscriptionsWithRawResponse(self._client.subscriptions)

    @cached_property
    def alerts(self) -> alerts.AsyncAlertsWithRawResponse:
        """
        [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
        usage, or credit balance and trigger webhooks when a threshold is exceeded.

        Alerts created through the API can be scoped to either customers or subscriptions.
        """
        from .resources.alerts import AsyncAlertsWithRawResponse

        return AsyncAlertsWithRawResponse(self._client.alerts)

    @cached_property
    def dimensional_price_groups(self) -> dimensional_price_groups.AsyncDimensionalPriceGroupsWithRawResponse:
        from .resources.dimensional_price_groups import AsyncDimensionalPriceGroupsWithRawResponse

        return AsyncDimensionalPriceGroupsWithRawResponse(self._client.dimensional_price_groups)

    @cached_property
    def subscription_changes(self) -> subscription_changes.AsyncSubscriptionChangesWithRawResponse:
        from .resources.subscription_changes import AsyncSubscriptionChangesWithRawResponse

        return AsyncSubscriptionChangesWithRawResponse(self._client.subscription_changes)

    @cached_property
    def credit_blocks(self) -> credit_blocks.AsyncCreditBlocksWithRawResponse:
        """
        The [Credit Ledger Entry resource](/product-catalog/prepurchase) models prepaid credits within Orb.
        """
        from .resources.credit_blocks import AsyncCreditBlocksWithRawResponse

        return AsyncCreditBlocksWithRawResponse(self._client.credit_blocks)

    @cached_property
    def license_types(self) -> license_types.AsyncLicenseTypesWithRawResponse:
        """
        The LicenseType resource represents a type of license that can be assigned to users.
        License types are used during billing by grouping metrics on the configured grouping key.
        """
        from .resources.license_types import AsyncLicenseTypesWithRawResponse

        return AsyncLicenseTypesWithRawResponse(self._client.license_types)

    @cached_property
    def licenses(self) -> licenses.AsyncLicensesWithRawResponse:
        from .resources.licenses import AsyncLicensesWithRawResponse

        return AsyncLicensesWithRawResponse(self._client.licenses)


class OrbWithStreamedResponse:
    _client: Orb

    def __init__(self, client: Orb) -> None:
        self._client = client

    @cached_property
    def top_level(self) -> top_level.TopLevelWithStreamingResponse:
        from .resources.top_level import TopLevelWithStreamingResponse

        return TopLevelWithStreamingResponse(self._client.top_level)

    @cached_property
    def beta(self) -> beta.BetaWithStreamingResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.beta import BetaWithStreamingResponse

        return BetaWithStreamingResponse(self._client.beta)

    @cached_property
    def coupons(self) -> coupons.CouponsWithStreamingResponse:
        """
        A coupon represents a reusable discount configuration that can be applied either as a fixed or percentage amount to an invoice or subscription. Coupons are activated using a redemption code, which applies the discount to a subscription or invoice. The duration of a coupon determines how long it remains available for use by end users.
        """
        from .resources.coupons import CouponsWithStreamingResponse

        return CouponsWithStreamingResponse(self._client.coupons)

    @cached_property
    def credit_notes(self) -> credit_notes.CreditNotesWithStreamingResponse:
        """
        The [Credit Note](/invoicing/credit-notes) resource represents a credit that has been applied to a
        particular invoice.
        """
        from .resources.credit_notes import CreditNotesWithStreamingResponse

        return CreditNotesWithStreamingResponse(self._client.credit_notes)

    @cached_property
    def customers(self) -> customers.CustomersWithStreamingResponse:
        """
        A customer is a buyer of your products, and the other party to the billing relationship.

        In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these
        match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an
        `external_customer_id` with your own identifier. See
        [Customer ID Aliases](/events-and-metrics/customer-aliases) for further information about how these
        aliases work in Orb.

        In addition to having an identifier in your system, a customer may exist in a payment provider solution like
        Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.

        A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which
        defaults to your account's timezone. See [Timezone localization](/essentials/timezones) for
        information on what this timezone parameter influences within Orb.
        """
        from .resources.customers import CustomersWithStreamingResponse

        return CustomersWithStreamingResponse(self._client.customers)

    @cached_property
    def events(self) -> events.EventsWithStreamingResponse:
        """
        The [Event](/core-concepts#event) resource represents a usage event that has been created for a
        customer. Events are the core of Orb's usage-based billing model, and are used to calculate the usage charges for
        a given billing period.
        """
        from .resources.events import EventsWithStreamingResponse

        return EventsWithStreamingResponse(self._client.events)

    @cached_property
    def invoice_line_items(self) -> invoice_line_items.InvoiceLineItemsWithStreamingResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoice_line_items import InvoiceLineItemsWithStreamingResponse

        return InvoiceLineItemsWithStreamingResponse(self._client.invoice_line_items)

    @cached_property
    def invoices(self) -> invoices.InvoicesWithStreamingResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoices import InvoicesWithStreamingResponse

        return InvoicesWithStreamingResponse(self._client.invoices)

    @cached_property
    def items(self) -> items.ItemsWithStreamingResponse:
        """The Item resource represents a sellable product or good.

        Items are associated with all line items, billable metrics,
        and prices and are used for defining external sync behavior for invoices and tax calculation purposes.
        """
        from .resources.items import ItemsWithStreamingResponse

        return ItemsWithStreamingResponse(self._client.items)

    @cached_property
    def metrics(self) -> metrics.MetricsWithStreamingResponse:
        """
        The Metric resource represents a calculation of a quantity based on events.
        Metrics are defined by the query that transforms raw usage events into meaningful values for your customers.
        """
        from .resources.metrics import MetricsWithStreamingResponse

        return MetricsWithStreamingResponse(self._client.metrics)

    @cached_property
    def plans(self) -> plans.PlansWithStreamingResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.plans import PlansWithStreamingResponse

        return PlansWithStreamingResponse(self._client.plans)

    @cached_property
    def prices(self) -> prices.PricesWithStreamingResponse:
        """
        The Price resource represents a price that can be billed on a subscription, resulting in a charge on an invoice in
        the form of an invoice line item. Prices take a quantity and determine an amount to bill.

        Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a
        given Price object. The model_type field determines the key for the configuration object that is present.

        For more on the types of prices, see [the core concepts documentation](/core-concepts#plan-and-price)
        """
        from .resources.prices import PricesWithStreamingResponse

        return PricesWithStreamingResponse(self._client.prices)

    @cached_property
    def subscriptions(self) -> subscriptions.SubscriptionsWithStreamingResponse:
        from .resources.subscriptions import SubscriptionsWithStreamingResponse

        return SubscriptionsWithStreamingResponse(self._client.subscriptions)

    @cached_property
    def alerts(self) -> alerts.AlertsWithStreamingResponse:
        """
        [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
        usage, or credit balance and trigger webhooks when a threshold is exceeded.

        Alerts created through the API can be scoped to either customers or subscriptions.
        """
        from .resources.alerts import AlertsWithStreamingResponse

        return AlertsWithStreamingResponse(self._client.alerts)

    @cached_property
    def dimensional_price_groups(self) -> dimensional_price_groups.DimensionalPriceGroupsWithStreamingResponse:
        from .resources.dimensional_price_groups import DimensionalPriceGroupsWithStreamingResponse

        return DimensionalPriceGroupsWithStreamingResponse(self._client.dimensional_price_groups)

    @cached_property
    def subscription_changes(self) -> subscription_changes.SubscriptionChangesWithStreamingResponse:
        from .resources.subscription_changes import SubscriptionChangesWithStreamingResponse

        return SubscriptionChangesWithStreamingResponse(self._client.subscription_changes)

    @cached_property
    def credit_blocks(self) -> credit_blocks.CreditBlocksWithStreamingResponse:
        """
        The [Credit Ledger Entry resource](/product-catalog/prepurchase) models prepaid credits within Orb.
        """
        from .resources.credit_blocks import CreditBlocksWithStreamingResponse

        return CreditBlocksWithStreamingResponse(self._client.credit_blocks)

    @cached_property
    def license_types(self) -> license_types.LicenseTypesWithStreamingResponse:
        """
        The LicenseType resource represents a type of license that can be assigned to users.
        License types are used during billing by grouping metrics on the configured grouping key.
        """
        from .resources.license_types import LicenseTypesWithStreamingResponse

        return LicenseTypesWithStreamingResponse(self._client.license_types)

    @cached_property
    def licenses(self) -> licenses.LicensesWithStreamingResponse:
        from .resources.licenses import LicensesWithStreamingResponse

        return LicensesWithStreamingResponse(self._client.licenses)


class AsyncOrbWithStreamedResponse:
    _client: AsyncOrb

    def __init__(self, client: AsyncOrb) -> None:
        self._client = client

    @cached_property
    def top_level(self) -> top_level.AsyncTopLevelWithStreamingResponse:
        from .resources.top_level import AsyncTopLevelWithStreamingResponse

        return AsyncTopLevelWithStreamingResponse(self._client.top_level)

    @cached_property
    def beta(self) -> beta.AsyncBetaWithStreamingResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.beta import AsyncBetaWithStreamingResponse

        return AsyncBetaWithStreamingResponse(self._client.beta)

    @cached_property
    def coupons(self) -> coupons.AsyncCouponsWithStreamingResponse:
        """
        A coupon represents a reusable discount configuration that can be applied either as a fixed or percentage amount to an invoice or subscription. Coupons are activated using a redemption code, which applies the discount to a subscription or invoice. The duration of a coupon determines how long it remains available for use by end users.
        """
        from .resources.coupons import AsyncCouponsWithStreamingResponse

        return AsyncCouponsWithStreamingResponse(self._client.coupons)

    @cached_property
    def credit_notes(self) -> credit_notes.AsyncCreditNotesWithStreamingResponse:
        """
        The [Credit Note](/invoicing/credit-notes) resource represents a credit that has been applied to a
        particular invoice.
        """
        from .resources.credit_notes import AsyncCreditNotesWithStreamingResponse

        return AsyncCreditNotesWithStreamingResponse(self._client.credit_notes)

    @cached_property
    def customers(self) -> customers.AsyncCustomersWithStreamingResponse:
        """
        A customer is a buyer of your products, and the other party to the billing relationship.

        In Orb, customers are assigned system generated identifiers automatically, but it's often desirable to have these
        match existing identifiers in your system. To avoid having to denormalize Orb ID information, you can pass in an
        `external_customer_id` with your own identifier. See
        [Customer ID Aliases](/events-and-metrics/customer-aliases) for further information about how these
        aliases work in Orb.

        In addition to having an identifier in your system, a customer may exist in a payment provider solution like
        Stripe. Use the `payment_provider_id` and the `payment_provider` enum field to express this mapping.

        A customer also has a timezone (from the standard [IANA timezone database](https://www.iana.org/time-zones)), which
        defaults to your account's timezone. See [Timezone localization](/essentials/timezones) for
        information on what this timezone parameter influences within Orb.
        """
        from .resources.customers import AsyncCustomersWithStreamingResponse

        return AsyncCustomersWithStreamingResponse(self._client.customers)

    @cached_property
    def events(self) -> events.AsyncEventsWithStreamingResponse:
        """
        The [Event](/core-concepts#event) resource represents a usage event that has been created for a
        customer. Events are the core of Orb's usage-based billing model, and are used to calculate the usage charges for
        a given billing period.
        """
        from .resources.events import AsyncEventsWithStreamingResponse

        return AsyncEventsWithStreamingResponse(self._client.events)

    @cached_property
    def invoice_line_items(self) -> invoice_line_items.AsyncInvoiceLineItemsWithStreamingResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoice_line_items import AsyncInvoiceLineItemsWithStreamingResponse

        return AsyncInvoiceLineItemsWithStreamingResponse(self._client.invoice_line_items)

    @cached_property
    def invoices(self) -> invoices.AsyncInvoicesWithStreamingResponse:
        """
        An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity, representing the request for payment for
        a single subscription. This includes a set of line items, which correspond to prices in the subscription's plan and
        can represent fixed recurring fees or usage-based fees. They are generated at the end of a billing period, or as
        the result of an action, such as a cancellation.
        """
        from .resources.invoices import AsyncInvoicesWithStreamingResponse

        return AsyncInvoicesWithStreamingResponse(self._client.invoices)

    @cached_property
    def items(self) -> items.AsyncItemsWithStreamingResponse:
        """The Item resource represents a sellable product or good.

        Items are associated with all line items, billable metrics,
        and prices and are used for defining external sync behavior for invoices and tax calculation purposes.
        """
        from .resources.items import AsyncItemsWithStreamingResponse

        return AsyncItemsWithStreamingResponse(self._client.items)

    @cached_property
    def metrics(self) -> metrics.AsyncMetricsWithStreamingResponse:
        """
        The Metric resource represents a calculation of a quantity based on events.
        Metrics are defined by the query that transforms raw usage events into meaningful values for your customers.
        """
        from .resources.metrics import AsyncMetricsWithStreamingResponse

        return AsyncMetricsWithStreamingResponse(self._client.metrics)

    @cached_property
    def plans(self) -> plans.AsyncPlansWithStreamingResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        from .resources.plans import AsyncPlansWithStreamingResponse

        return AsyncPlansWithStreamingResponse(self._client.plans)

    @cached_property
    def prices(self) -> prices.AsyncPricesWithStreamingResponse:
        """
        The Price resource represents a price that can be billed on a subscription, resulting in a charge on an invoice in
        the form of an invoice line item. Prices take a quantity and determine an amount to bill.

        Orb supports a few different pricing models out of the box. Each of these models is serialized differently in a
        given Price object. The model_type field determines the key for the configuration object that is present.

        For more on the types of prices, see [the core concepts documentation](/core-concepts#plan-and-price)
        """
        from .resources.prices import AsyncPricesWithStreamingResponse

        return AsyncPricesWithStreamingResponse(self._client.prices)

    @cached_property
    def subscriptions(self) -> subscriptions.AsyncSubscriptionsWithStreamingResponse:
        from .resources.subscriptions import AsyncSubscriptionsWithStreamingResponse

        return AsyncSubscriptionsWithStreamingResponse(self._client.subscriptions)

    @cached_property
    def alerts(self) -> alerts.AsyncAlertsWithStreamingResponse:
        """
        [Alerts within Orb](/product-catalog/configuring-alerts) monitor spending,
        usage, or credit balance and trigger webhooks when a threshold is exceeded.

        Alerts created through the API can be scoped to either customers or subscriptions.
        """
        from .resources.alerts import AsyncAlertsWithStreamingResponse

        return AsyncAlertsWithStreamingResponse(self._client.alerts)

    @cached_property
    def dimensional_price_groups(self) -> dimensional_price_groups.AsyncDimensionalPriceGroupsWithStreamingResponse:
        from .resources.dimensional_price_groups import AsyncDimensionalPriceGroupsWithStreamingResponse

        return AsyncDimensionalPriceGroupsWithStreamingResponse(self._client.dimensional_price_groups)

    @cached_property
    def subscription_changes(self) -> subscription_changes.AsyncSubscriptionChangesWithStreamingResponse:
        from .resources.subscription_changes import AsyncSubscriptionChangesWithStreamingResponse

        return AsyncSubscriptionChangesWithStreamingResponse(self._client.subscription_changes)

    @cached_property
    def credit_blocks(self) -> credit_blocks.AsyncCreditBlocksWithStreamingResponse:
        """
        The [Credit Ledger Entry resource](/product-catalog/prepurchase) models prepaid credits within Orb.
        """
        from .resources.credit_blocks import AsyncCreditBlocksWithStreamingResponse

        return AsyncCreditBlocksWithStreamingResponse(self._client.credit_blocks)

    @cached_property
    def license_types(self) -> license_types.AsyncLicenseTypesWithStreamingResponse:
        """
        The LicenseType resource represents a type of license that can be assigned to users.
        License types are used during billing by grouping metrics on the configured grouping key.
        """
        from .resources.license_types import AsyncLicenseTypesWithStreamingResponse

        return AsyncLicenseTypesWithStreamingResponse(self._client.license_types)

    @cached_property
    def licenses(self) -> licenses.AsyncLicensesWithStreamingResponse:
        from .resources.licenses import AsyncLicensesWithStreamingResponse

        return AsyncLicensesWithStreamingResponse(self._client.licenses)


Client = Orb

AsyncClient = AsyncOrb
