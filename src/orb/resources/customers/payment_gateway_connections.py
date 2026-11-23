# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.customers import (
    payment_gateway_connection_list_params,
    payment_gateway_connection_create_params,
    payment_gateway_connection_update_params,
    payment_gateway_connection_list_by_external_id_params,
    payment_gateway_connection_create_by_external_id_params,
    payment_gateway_connection_update_by_external_id_params,
)
from ...types.customers.customer_payment_gateway_connection import CustomerPaymentGatewayConnection
from ...types.customers.payment_gateway_connection_list_response import PaymentGatewayConnectionListResponse
from ...types.customers.payment_gateway_connection_list_by_external_id_response import (
    PaymentGatewayConnectionListByExternalIDResponse,
)

__all__ = ["PaymentGatewayConnections", "AsyncPaymentGatewayConnections"]


class PaymentGatewayConnections(SyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> PaymentGatewayConnectionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return PaymentGatewayConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentGatewayConnectionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return PaymentGatewayConnectionsWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        payment_gateway_connection_id: str,
        is_default: bool | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """This endpoint maps the customer to a payment gateway connection.

        Orb charges the
        customer for a billing entity's invoices through the customer's first mapping
        for that billing entity; `is_default` moves that to this mapping when the
        customer already has one.

        Args:
          payment_gateway_connection_id: The ID of the payment gateway connection to map the customer to.

          is_default: Whether Orb charges the customer for the billing entity's invoices through this
              mapping. The customer's first mapping for a billing entity is the default
              regardless.

          provider_customer_id: The ID of the customer in the external payment provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            path_template("/customers/{customer_id}/payment_gateway_connections", customer_id=customer_id),
            body=maybe_transform(
                {
                    "payment_gateway_connection_id": payment_gateway_connection_id,
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_create_params.PaymentGatewayConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    def update(
        self,
        payment_gateway_connection_id: str,
        *,
        customer_id: str,
        is_default: Optional[Literal[True]] | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint updates the customer's mapping to a payment gateway connection:
        the customer's ID in that account, and whether Orb charges the customer for the
        billing entity's invoices through it. Omitted fields keep their value.

        Args:
          is_default: Only `true` is accepted: it makes this the customer's default mapping for the
              connection's billing entity. Omit it to keep the current default. To move the
              default, set it on another mapping.

          provider_customer_id: The ID of the customer in the external payment provider. Omit it to keep the
              current one; `null` clears it, and Orb creates a Stripe customer at the next
              payment through this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return self._put(
            path_template(
                "/customers/{customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                customer_id=customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            body=maybe_transform(
                {
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_update_params.PaymentGatewayConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    def list(
        self,
        customer_id: str,
        *,
        billing_entity_id: Optional[str] | Omit = omit,
        payment_gateway_connection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentGatewayConnectionListResponse:
        """
        This endpoint returns the customer's mappings to payment gateway connections,
        for example the customer's Stripe ID in each connected Stripe account. A
        customer has at most one mapping per connection, so the list is not paginated.

        Args:
          billing_entity_id: Only return mappings to this billing entity's connections.

          payment_gateway_connection_id: Only return the mapping to this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get(
            path_template("/customers/{customer_id}/payment_gateway_connections", customer_id=customer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "billing_entity_id": billing_entity_id,
                        "payment_gateway_connection_id": payment_gateway_connection_id,
                    },
                    payment_gateway_connection_list_params.PaymentGatewayConnectionListParams,
                ),
            ),
            cast_to=PaymentGatewayConnectionListResponse,
        )

    def delete(
        self,
        payment_gateway_connection_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint removes the customer's mapping to a payment gateway connection and
        returns it. Active subscriptions and unpaid invoices do not block it. If the
        mapping was the customer's default for the billing entity, the customer's oldest
        remaining mapping on that entity becomes the default. With no mapping left, the
        next charge goes through the billing entity's default connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return self._delete(
            path_template(
                "/customers/{customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                customer_id=customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    def create_by_external_id(
        self,
        external_customer_id: str,
        *,
        payment_gateway_connection_id: str,
        is_default: bool | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """This endpoint maps the customer to a payment gateway connection.

        Orb charges the
        customer for a billing entity's invoices through the customer's first mapping
        for that billing entity; `is_default` moves that to this mapping when the
        customer already has one.

        Args:
          payment_gateway_connection_id: The ID of the payment gateway connection to map the customer to.

          is_default: Whether Orb charges the customer for the billing entity's invoices through this
              mapping. The customer's first mapping for a billing entity is the default
              regardless.

          provider_customer_id: The ID of the customer in the external payment provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._post(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections",
                external_customer_id=external_customer_id,
            ),
            body=maybe_transform(
                {
                    "payment_gateway_connection_id": payment_gateway_connection_id,
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_create_by_external_id_params.PaymentGatewayConnectionCreateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    def delete_by_external_id(
        self,
        payment_gateway_connection_id: str,
        *,
        external_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint removes the customer's mapping to a payment gateway connection and
        returns it. Active subscriptions and unpaid invoices do not block it. If the
        mapping was the customer's default for the billing entity, the customer's oldest
        remaining mapping on that entity becomes the default. With no mapping left, the
        next charge goes through the billing entity's default connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return self._delete(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                external_customer_id=external_customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        billing_entity_id: Optional[str] | Omit = omit,
        payment_gateway_connection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentGatewayConnectionListByExternalIDResponse:
        """
        This endpoint returns the customer's mappings to payment gateway connections,
        for example the customer's Stripe ID in each connected Stripe account. A
        customer has at most one mapping per connection, so the list is not paginated.

        Args:
          billing_entity_id: Only return mappings to this billing entity's connections.

          payment_gateway_connection_id: Only return the mapping to this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._get(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections",
                external_customer_id=external_customer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "billing_entity_id": billing_entity_id,
                        "payment_gateway_connection_id": payment_gateway_connection_id,
                    },
                    payment_gateway_connection_list_by_external_id_params.PaymentGatewayConnectionListByExternalIDParams,
                ),
            ),
            cast_to=PaymentGatewayConnectionListByExternalIDResponse,
        )

    def update_by_external_id(
        self,
        payment_gateway_connection_id: str,
        *,
        external_customer_id: str,
        is_default: Optional[Literal[True]] | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint updates the customer's mapping to a payment gateway connection:
        the customer's ID in that account, and whether Orb charges the customer for the
        billing entity's invoices through it. Omitted fields keep their value.

        Args:
          is_default: Only `true` is accepted: it makes this the customer's default mapping for the
              connection's billing entity. Omit it to keep the current default. To move the
              default, set it on another mapping.

          provider_customer_id: The ID of the customer in the external payment provider. Omit it to keep the
              current one; `null` clears it, and Orb creates a Stripe customer at the next
              payment through this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return self._put(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                external_customer_id=external_customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            body=maybe_transform(
                {
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_update_by_external_id_params.PaymentGatewayConnectionUpdateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )


class AsyncPaymentGatewayConnections(AsyncAPIResource):
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

    @cached_property
    def with_raw_response(self) -> AsyncPaymentGatewayConnectionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentGatewayConnectionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentGatewayConnectionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncPaymentGatewayConnectionsWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        payment_gateway_connection_id: str,
        is_default: bool | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """This endpoint maps the customer to a payment gateway connection.

        Orb charges the
        customer for a billing entity's invoices through the customer's first mapping
        for that billing entity; `is_default` moves that to this mapping when the
        customer already has one.

        Args:
          payment_gateway_connection_id: The ID of the payment gateway connection to map the customer to.

          is_default: Whether Orb charges the customer for the billing entity's invoices through this
              mapping. The customer's first mapping for a billing entity is the default
              regardless.

          provider_customer_id: The ID of the customer in the external payment provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            path_template("/customers/{customer_id}/payment_gateway_connections", customer_id=customer_id),
            body=await async_maybe_transform(
                {
                    "payment_gateway_connection_id": payment_gateway_connection_id,
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_create_params.PaymentGatewayConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    async def update(
        self,
        payment_gateway_connection_id: str,
        *,
        customer_id: str,
        is_default: Optional[Literal[True]] | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint updates the customer's mapping to a payment gateway connection:
        the customer's ID in that account, and whether Orb charges the customer for the
        billing entity's invoices through it. Omitted fields keep their value.

        Args:
          is_default: Only `true` is accepted: it makes this the customer's default mapping for the
              connection's billing entity. Omit it to keep the current default. To move the
              default, set it on another mapping.

          provider_customer_id: The ID of the customer in the external payment provider. Omit it to keep the
              current one; `null` clears it, and Orb creates a Stripe customer at the next
              payment through this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return await self._put(
            path_template(
                "/customers/{customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                customer_id=customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            body=await async_maybe_transform(
                {
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_update_params.PaymentGatewayConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    async def list(
        self,
        customer_id: str,
        *,
        billing_entity_id: Optional[str] | Omit = omit,
        payment_gateway_connection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentGatewayConnectionListResponse:
        """
        This endpoint returns the customer's mappings to payment gateway connections,
        for example the customer's Stripe ID in each connected Stripe account. A
        customer has at most one mapping per connection, so the list is not paginated.

        Args:
          billing_entity_id: Only return mappings to this billing entity's connections.

          payment_gateway_connection_id: Only return the mapping to this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._get(
            path_template("/customers/{customer_id}/payment_gateway_connections", customer_id=customer_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "billing_entity_id": billing_entity_id,
                        "payment_gateway_connection_id": payment_gateway_connection_id,
                    },
                    payment_gateway_connection_list_params.PaymentGatewayConnectionListParams,
                ),
            ),
            cast_to=PaymentGatewayConnectionListResponse,
        )

    async def delete(
        self,
        payment_gateway_connection_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint removes the customer's mapping to a payment gateway connection and
        returns it. Active subscriptions and unpaid invoices do not block it. If the
        mapping was the customer's default for the billing entity, the customer's oldest
        remaining mapping on that entity becomes the default. With no mapping left, the
        next charge goes through the billing entity's default connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return await self._delete(
            path_template(
                "/customers/{customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                customer_id=customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    async def create_by_external_id(
        self,
        external_customer_id: str,
        *,
        payment_gateway_connection_id: str,
        is_default: bool | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """This endpoint maps the customer to a payment gateway connection.

        Orb charges the
        customer for a billing entity's invoices through the customer's first mapping
        for that billing entity; `is_default` moves that to this mapping when the
        customer already has one.

        Args:
          payment_gateway_connection_id: The ID of the payment gateway connection to map the customer to.

          is_default: Whether Orb charges the customer for the billing entity's invoices through this
              mapping. The customer's first mapping for a billing entity is the default
              regardless.

          provider_customer_id: The ID of the customer in the external payment provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return await self._post(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections",
                external_customer_id=external_customer_id,
            ),
            body=await async_maybe_transform(
                {
                    "payment_gateway_connection_id": payment_gateway_connection_id,
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_create_by_external_id_params.PaymentGatewayConnectionCreateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    async def delete_by_external_id(
        self,
        payment_gateway_connection_id: str,
        *,
        external_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint removes the customer's mapping to a payment gateway connection and
        returns it. Active subscriptions and unpaid invoices do not block it. If the
        mapping was the customer's default for the billing entity, the customer's oldest
        remaining mapping on that entity becomes the default. With no mapping left, the
        next charge goes through the billing entity's default connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return await self._delete(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                external_customer_id=external_customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )

    async def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        billing_entity_id: Optional[str] | Omit = omit,
        payment_gateway_connection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentGatewayConnectionListByExternalIDResponse:
        """
        This endpoint returns the customer's mappings to payment gateway connections,
        for example the customer's Stripe ID in each connected Stripe account. A
        customer has at most one mapping per connection, so the list is not paginated.

        Args:
          billing_entity_id: Only return mappings to this billing entity's connections.

          payment_gateway_connection_id: Only return the mapping to this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return await self._get(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections",
                external_customer_id=external_customer_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "billing_entity_id": billing_entity_id,
                        "payment_gateway_connection_id": payment_gateway_connection_id,
                    },
                    payment_gateway_connection_list_by_external_id_params.PaymentGatewayConnectionListByExternalIDParams,
                ),
            ),
            cast_to=PaymentGatewayConnectionListByExternalIDResponse,
        )

    async def update_by_external_id(
        self,
        payment_gateway_connection_id: str,
        *,
        external_customer_id: str,
        is_default: Optional[Literal[True]] | Omit = omit,
        provider_customer_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CustomerPaymentGatewayConnection:
        """
        This endpoint updates the customer's mapping to a payment gateway connection:
        the customer's ID in that account, and whether Orb charges the customer for the
        billing entity's invoices through it. Omitted fields keep their value.

        Args:
          is_default: Only `true` is accepted: it makes this the customer's default mapping for the
              connection's billing entity. Omit it to keep the current default. To move the
              default, set it on another mapping.

          provider_customer_id: The ID of the customer in the external payment provider. Omit it to keep the
              current one; `null` clears it, and Orb creates a Stripe customer at the next
              payment through this connection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return await self._put(
            path_template(
                "/customers/external_customer_id/{external_customer_id}/payment_gateway_connections/{payment_gateway_connection_id}",
                external_customer_id=external_customer_id,
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            body=await async_maybe_transform(
                {
                    "is_default": is_default,
                    "provider_customer_id": provider_customer_id,
                },
                payment_gateway_connection_update_by_external_id_params.PaymentGatewayConnectionUpdateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CustomerPaymentGatewayConnection,
        )


class PaymentGatewayConnectionsWithRawResponse:
    def __init__(self, payment_gateway_connections: PaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.create = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.delete,
        )
        self.create_by_external_id = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.create_by_external_id,
        )
        self.delete_by_external_id = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.delete_by_external_id,
        )
        self.list_by_external_id = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.list_by_external_id,
        )
        self.update_by_external_id = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.update_by_external_id,
        )


class AsyncPaymentGatewayConnectionsWithRawResponse:
    def __init__(self, payment_gateway_connections: AsyncPaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.create = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.delete,
        )
        self.create_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.create_by_external_id,
        )
        self.delete_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.delete_by_external_id,
        )
        self.list_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.list_by_external_id,
        )
        self.update_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.update_by_external_id,
        )


class PaymentGatewayConnectionsWithStreamingResponse:
    def __init__(self, payment_gateway_connections: PaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.create = to_streamed_response_wrapper(
            payment_gateway_connections.create,
        )
        self.update = to_streamed_response_wrapper(
            payment_gateway_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            payment_gateway_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            payment_gateway_connections.delete,
        )
        self.create_by_external_id = to_streamed_response_wrapper(
            payment_gateway_connections.create_by_external_id,
        )
        self.delete_by_external_id = to_streamed_response_wrapper(
            payment_gateway_connections.delete_by_external_id,
        )
        self.list_by_external_id = to_streamed_response_wrapper(
            payment_gateway_connections.list_by_external_id,
        )
        self.update_by_external_id = to_streamed_response_wrapper(
            payment_gateway_connections.update_by_external_id,
        )


class AsyncPaymentGatewayConnectionsWithStreamingResponse:
    def __init__(self, payment_gateway_connections: AsyncPaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.create = async_to_streamed_response_wrapper(
            payment_gateway_connections.create,
        )
        self.update = async_to_streamed_response_wrapper(
            payment_gateway_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            payment_gateway_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            payment_gateway_connections.delete,
        )
        self.create_by_external_id = async_to_streamed_response_wrapper(
            payment_gateway_connections.create_by_external_id,
        )
        self.delete_by_external_id = async_to_streamed_response_wrapper(
            payment_gateway_connections.delete_by_external_id,
        )
        self.list_by_external_id = async_to_streamed_response_wrapper(
            payment_gateway_connections.list_by_external_id,
        )
        self.update_by_external_id = async_to_streamed_response_wrapper(
            payment_gateway_connections.update_by_external_id,
        )
