# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.migrations import subscription_list_params
from ...types.migration_subscription import MigrationSubscription

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    @cached_property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return SubscriptionsWithStreamingResponse(self)

    def list(
        self,
        migration_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[List[Literal["scheduling", "scheduled", "completed", "skipped", "failed"]]] | Omit = omit,
        subscription_id: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[MigrationSubscription]:
        """
        This endpoint returns the subscriptions a migration applies to, with the status
        of each one. A subscription that could not be migrated has the status `failed`
        and a `failure_reason`.

        The list is empty until the migration has finished selecting its subscriptions.
        Once a migration is canceled, only the subscriptions it processed before the
        cancellation are returned.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: Only return subscriptions with one of these statuses.

          subscription_id: Only return these subscriptions. Up to 100 IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return self._get_api_list(
            path_template("/migrations/{migration_id}/subscriptions", migration_id=migration_id),
            page=SyncPage[MigrationSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=MigrationSubscription,
        )


class AsyncSubscriptions(AsyncAPIResource):
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncSubscriptionsWithStreamingResponse(self)

    def list(
        self,
        migration_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[List[Literal["scheduling", "scheduled", "completed", "skipped", "failed"]]] | Omit = omit,
        subscription_id: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MigrationSubscription, AsyncPage[MigrationSubscription]]:
        """
        This endpoint returns the subscriptions a migration applies to, with the status
        of each one. A subscription that could not be migrated has the status `failed`
        and a `failure_reason`.

        The list is empty until the migration has finished selecting its subscriptions.
        Once a migration is canceled, only the subscriptions it processed before the
        cancellation are returned.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: Only return subscriptions with one of these statuses.

          subscription_id: Only return these subscriptions. Up to 100 IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return self._get_api_list(
            path_template("/migrations/{migration_id}/subscriptions", migration_id=migration_id),
            page=AsyncPage[MigrationSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=MigrationSubscription,
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
