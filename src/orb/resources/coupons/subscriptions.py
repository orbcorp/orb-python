# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.coupons import subscription_list_params
from ...types.subscription import Subscription

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self)

    def list(
        self,
        coupon_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Subscription]:
        """
        This endpoint returns a list of all subscriptions that have redeemed a given
        coupon as a [paginated](../reference/pagination) list, ordered starting from the
        most recently created subscription. For a full discussion of the subscription
        resource, see [Subscription](../guides/concepts#subscription).

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return self._get_api_list(
            f"/coupons/{coupon_id}/subscriptions",
            page=SyncPage[Subscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=Subscription,
        )


class AsyncSubscriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        return AsyncSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsWithStreamingResponse:
        return AsyncSubscriptionsWithStreamingResponse(self)

    def list(
        self,
        coupon_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subscription, AsyncPage[Subscription]]:
        """
        This endpoint returns a list of all subscriptions that have redeemed a given
        coupon as a [paginated](../reference/pagination) list, ordered starting from the
        most recently created subscription. For a full discussion of the subscription
        resource, see [Subscription](../guides/concepts#subscription).

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not coupon_id:
            raise ValueError(f"Expected a non-empty value for `coupon_id` but received {coupon_id!r}")
        return self._get_api_list(
            f"/coupons/{coupon_id}/subscriptions",
            page=AsyncPage[Subscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=Subscription,
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.list = _legacy_response.to_raw_response_wrapper(
            subscriptions.list,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.list = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.list,
        )


class SubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )


class AsyncSubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
