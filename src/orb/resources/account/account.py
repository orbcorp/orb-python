# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .billing_entities import (
    BillingEntities,
    AsyncBillingEntities,
    BillingEntitiesWithRawResponse,
    AsyncBillingEntitiesWithRawResponse,
    BillingEntitiesWithStreamingResponse,
    AsyncBillingEntitiesWithStreamingResponse,
)
from .payment_gateway_connections import (
    PaymentGatewayConnections,
    AsyncPaymentGatewayConnections,
    PaymentGatewayConnectionsWithRawResponse,
    AsyncPaymentGatewayConnectionsWithRawResponse,
    PaymentGatewayConnectionsWithStreamingResponse,
    AsyncPaymentGatewayConnectionsWithStreamingResponse,
)

__all__ = ["Account", "AsyncAccount"]


class Account(SyncAPIResource):
    @cached_property
    def billing_entities(self) -> BillingEntities:
        """
        A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
        registrations.
        """
        return BillingEntities(self._client)

    @cached_property
    def payment_gateway_connections(self) -> PaymentGatewayConnections:
        """
        A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
        payments through.
        """
        return PaymentGatewayConnections(self._client)

    @cached_property
    def with_raw_response(self) -> AccountWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AccountWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AccountWithStreamingResponse(self)


class AsyncAccount(AsyncAPIResource):
    @cached_property
    def billing_entities(self) -> AsyncBillingEntities:
        """
        A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
        registrations.
        """
        return AsyncBillingEntities(self._client)

    @cached_property
    def payment_gateway_connections(self) -> AsyncPaymentGatewayConnections:
        """
        A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
        payments through.
        """
        return AsyncPaymentGatewayConnections(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncAccountWithStreamingResponse(self)


class AccountWithRawResponse:
    def __init__(self, account: Account) -> None:
        self._account = account

    @cached_property
    def billing_entities(self) -> BillingEntitiesWithRawResponse:
        """
        A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
        registrations.
        """
        return BillingEntitiesWithRawResponse(self._account.billing_entities)

    @cached_property
    def payment_gateway_connections(self) -> PaymentGatewayConnectionsWithRawResponse:
        """
        A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
        payments through.
        """
        return PaymentGatewayConnectionsWithRawResponse(self._account.payment_gateway_connections)


class AsyncAccountWithRawResponse:
    def __init__(self, account: AsyncAccount) -> None:
        self._account = account

    @cached_property
    def billing_entities(self) -> AsyncBillingEntitiesWithRawResponse:
        """
        A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
        registrations.
        """
        return AsyncBillingEntitiesWithRawResponse(self._account.billing_entities)

    @cached_property
    def payment_gateway_connections(self) -> AsyncPaymentGatewayConnectionsWithRawResponse:
        """
        A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
        payments through.
        """
        return AsyncPaymentGatewayConnectionsWithRawResponse(self._account.payment_gateway_connections)


class AccountWithStreamingResponse:
    def __init__(self, account: Account) -> None:
        self._account = account

    @cached_property
    def billing_entities(self) -> BillingEntitiesWithStreamingResponse:
        """
        A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
        registrations.
        """
        return BillingEntitiesWithStreamingResponse(self._account.billing_entities)

    @cached_property
    def payment_gateway_connections(self) -> PaymentGatewayConnectionsWithStreamingResponse:
        """
        A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
        payments through.
        """
        return PaymentGatewayConnectionsWithStreamingResponse(self._account.payment_gateway_connections)


class AsyncAccountWithStreamingResponse:
    def __init__(self, account: AsyncAccount) -> None:
        self._account = account

    @cached_property
    def billing_entities(self) -> AsyncBillingEntitiesWithStreamingResponse:
        """
        A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
        registrations.
        """
        return AsyncBillingEntitiesWithStreamingResponse(self._account.billing_entities)

    @cached_property
    def payment_gateway_connections(self) -> AsyncPaymentGatewayConnectionsWithStreamingResponse:
        """
        A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
        payments through.
        """
        return AsyncPaymentGatewayConnectionsWithStreamingResponse(self._account.payment_gateway_connections)
