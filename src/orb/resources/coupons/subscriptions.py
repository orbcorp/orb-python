# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from ...types import Subscription
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.coupons import subscription_list_params

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    with_raw_response: SubscriptionsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = SubscriptionsWithRawResponse(self)

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
    with_raw_response: AsyncSubscriptionsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncSubscriptionsWithRawResponse(self)

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
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
