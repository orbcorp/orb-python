# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.account import payment_gateway_connection_list_params
from ...types.account.payment_gateway_connection import PaymentGatewayConnection

__all__ = ["PaymentGatewayConnections", "AsyncPaymentGatewayConnections"]


class PaymentGatewayConnections(SyncAPIResource):
    """
    A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
    payments through.
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

    def list(
        self,
        *,
        billing_entity_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        provider_type: Optional[Literal["stripe", "adyen"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[PaymentGatewayConnection]:
        """
        This endpoint returns the account's payment gateway connections with the billing
        entity each one collects for, ordered in descending order by creation time.

        Args:
          billing_entity_id: Only return connections of this billing entity.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          provider_type: Only return connections of this payment provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account/payment_gateway_connections",
            page=SyncPage[PaymentGatewayConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "billing_entity_id": billing_entity_id,
                        "cursor": cursor,
                        "limit": limit,
                        "provider_type": provider_type,
                    },
                    payment_gateway_connection_list_params.PaymentGatewayConnectionListParams,
                ),
            ),
            model=PaymentGatewayConnection,
        )

    def fetch(
        self,
        payment_gateway_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentGatewayConnection:
        """
        This endpoint returns a payment gateway connection identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return self._get(
            path_template(
                "/account/payment_gateway_connections/{payment_gateway_connection_id}",
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentGatewayConnection,
        )


class AsyncPaymentGatewayConnections(AsyncAPIResource):
    """
    A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
    payments through.
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

    def list(
        self,
        *,
        billing_entity_id: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        provider_type: Optional[Literal["stripe", "adyen"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentGatewayConnection, AsyncPage[PaymentGatewayConnection]]:
        """
        This endpoint returns the account's payment gateway connections with the billing
        entity each one collects for, ordered in descending order by creation time.

        Args:
          billing_entity_id: Only return connections of this billing entity.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          provider_type: Only return connections of this payment provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/account/payment_gateway_connections",
            page=AsyncPage[PaymentGatewayConnection],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "billing_entity_id": billing_entity_id,
                        "cursor": cursor,
                        "limit": limit,
                        "provider_type": provider_type,
                    },
                    payment_gateway_connection_list_params.PaymentGatewayConnectionListParams,
                ),
            ),
            model=PaymentGatewayConnection,
        )

    async def fetch(
        self,
        payment_gateway_connection_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentGatewayConnection:
        """
        This endpoint returns a payment gateway connection identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_gateway_connection_id:
            raise ValueError(
                f"Expected a non-empty value for `payment_gateway_connection_id` but received {payment_gateway_connection_id!r}"
            )
        return await self._get(
            path_template(
                "/account/payment_gateway_connections/{payment_gateway_connection_id}",
                payment_gateway_connection_id=payment_gateway_connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentGatewayConnection,
        )


class PaymentGatewayConnectionsWithRawResponse:
    def __init__(self, payment_gateway_connections: PaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.list = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.list,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            payment_gateway_connections.fetch,
        )


class AsyncPaymentGatewayConnectionsWithRawResponse:
    def __init__(self, payment_gateway_connections: AsyncPaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.list = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.list,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            payment_gateway_connections.fetch,
        )


class PaymentGatewayConnectionsWithStreamingResponse:
    def __init__(self, payment_gateway_connections: PaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.list = to_streamed_response_wrapper(
            payment_gateway_connections.list,
        )
        self.fetch = to_streamed_response_wrapper(
            payment_gateway_connections.fetch,
        )


class AsyncPaymentGatewayConnectionsWithStreamingResponse:
    def __init__(self, payment_gateway_connections: AsyncPaymentGatewayConnections) -> None:
        self._payment_gateway_connections = payment_gateway_connections

        self.list = async_to_streamed_response_wrapper(
            payment_gateway_connections.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            payment_gateway_connections.fetch,
        )
