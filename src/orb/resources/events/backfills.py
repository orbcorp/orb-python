# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.events import backfill_list_params, backfill_create_params
from ...types.events.backfill_list_response import BackfillListResponse
from ...types.events.backfill_close_response import BackfillCloseResponse
from ...types.events.backfill_fetch_response import BackfillFetchResponse
from ...types.events.backfill_create_response import BackfillCreateResponse
from ...types.events.backfill_revert_response import BackfillRevertResponse

__all__ = ["Backfills", "AsyncBackfills"]


class Backfills(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BackfillsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return BackfillsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BackfillsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return BackfillsWithStreamingResponse(self)

    def create(
        self,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        close_time: Union[str, datetime, None] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        deprecation_filter: Optional[str] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        replace_existing_events: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BackfillCreateResponse:
        """
        Creating the backfill enables adding or replacing past events, even those that
        are older than the ingestion grace period. Performing a backfill in Orb involves
        3 steps:

        1. Create the backfill, specifying its parameters.
        2. [Ingest](ingest) usage events, referencing the backfill (query parameter
           `backfill_id`).
        3. [Close](close-backfill) the backfill, propagating the update in past usage
           throughout Orb.

        Changes from a backfill are not reflected until the backfill is closed, so you
        won’t need to worry about your customers seeing partially updated usage data.
        Backfills are also reversible, so you’ll be able to revert a backfill if you’ve
        made a mistake.

        This endpoint will return a backfill object, which contains an `id`. That `id`
        can then be used as the `backfill_id` query parameter to the event ingestion
        endpoint to associate ingested events with this backfill. The effects (e.g.
        updated usage graphs) of this backfill will not take place until the backfill is
        closed.

        If the `replace_existing_events` is `true`, existing events in the backfill's
        timeframe will be replaced with the newly ingested events associated with the
        backfill. If `false`, newly ingested events will be added to the existing
        events.

        If a `customer_id` or `external_customer_id` is specified, the backfill will
        only affect events for that customer. If neither is specified, the backfill will
        affect all customers.

        When `replace_existing_events` is `true`, this indicates that existing events in
        the timeframe should no longer be counted towards invoiced usage. In this
        scenario, the parameter `deprecation_filter` can be optionally added which
        enables filtering using
        [computed properties](/extensibility/advanced-metrics#computed-properties). The
        expressiveness of computed properties allows you to deprecate existing events
        based on both a period of time and specific property values.

        You may not have multiple backfills in a pending or pending_revert state with
        overlapping timeframes.

        Args:
          timeframe_end: The (exclusive) end of the usage timeframe affected by this backfill. By
              default, Orb allows backfills up to 31 days in duration at a time. Reach out to
              discuss extending this limit and your use case.

          timeframe_start: The (inclusive) start of the usage timeframe affected by this backfill. By
              default, Orb allows backfills up to 31 days in duration at a time. Reach out to
              discuss extending this limit and your use case.

          close_time: The time at which no more events will be accepted for this backfill. The
              backfill will automatically begin reflecting throughout Orb at the close time.
              If not specified, it will default to 1 day after the creation of the backfill.

          customer_id: The Orb-generated ID of the customer to which this backfill is scoped. Omitting
              this field will scope the backfill to all customers.

          deprecation_filter: A boolean
              [computed property](/extensibility/advanced-metrics#computed-properties) used to
              filter the set of events to deprecate

          external_customer_id: The external customer ID of the customer to which this backfill is scoped.
              Omitting this field will scope the backfill to all customers.

          replace_existing_events: If true, replaces all existing events in the timeframe with the newly ingested
              events. If false, adds the newly ingested events to the existing events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/events/backfills",
            body=maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "close_time": close_time,
                    "customer_id": customer_id,
                    "deprecation_filter": deprecation_filter,
                    "external_customer_id": external_customer_id,
                    "replace_existing_events": replace_existing_events,
                },
                backfill_create_params.BackfillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BackfillCreateResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[BackfillListResponse]:
        """
        This endpoint returns a list of all backfills in a list format.

        The list of backfills is ordered starting from the most recently created
        backfill. The response also includes
        [`pagination_metadata`](/api-reference/pagination), which lets the caller
        retrieve the next page of results if they exist. More information about
        pagination can be found in the [Pagination-metadata schema](pagination).

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
            "/events/backfills",
            page=SyncPage[BackfillListResponse],
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
                    backfill_list_params.BackfillListParams,
                ),
            ),
            model=BackfillListResponse,
        )

    def close(
        self,
        backfill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BackfillCloseResponse:
        """Closing a backfill makes the updated usage visible in Orb.

        Upon closing a
        backfill, Orb will asynchronously reflect the updated usage in invoice amounts
        and usage graphs. Once all of the updates are complete, the backfill's status
        will transition to `reflected`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        return self._post(
            f"/events/backfills/{backfill_id}/close",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BackfillCloseResponse,
        )

    def fetch(
        self,
        backfill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackfillFetchResponse:
        """
        This endpoint is used to fetch a backfill given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        return self._get(
            f"/events/backfills/{backfill_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackfillFetchResponse,
        )

    def revert(
        self,
        backfill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BackfillRevertResponse:
        """Reverting a backfill undoes all the effects of closing the backfill.

        If the
        backfill is reflected, the status will transition to `pending_revert` while the
        effects of the backfill are undone. Once all effects are undone, the backfill
        will transition to `reverted`.

        If a backfill is reverted before its closed, no usage will be updated as a
        result of the backfill and it will immediately transition to `reverted`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        return self._post(
            f"/events/backfills/{backfill_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BackfillRevertResponse,
        )


class AsyncBackfills(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBackfillsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBackfillsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBackfillsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncBackfillsWithStreamingResponse(self)

    async def create(
        self,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        close_time: Union[str, datetime, None] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        deprecation_filter: Optional[str] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        replace_existing_events: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BackfillCreateResponse:
        """
        Creating the backfill enables adding or replacing past events, even those that
        are older than the ingestion grace period. Performing a backfill in Orb involves
        3 steps:

        1. Create the backfill, specifying its parameters.
        2. [Ingest](ingest) usage events, referencing the backfill (query parameter
           `backfill_id`).
        3. [Close](close-backfill) the backfill, propagating the update in past usage
           throughout Orb.

        Changes from a backfill are not reflected until the backfill is closed, so you
        won’t need to worry about your customers seeing partially updated usage data.
        Backfills are also reversible, so you’ll be able to revert a backfill if you’ve
        made a mistake.

        This endpoint will return a backfill object, which contains an `id`. That `id`
        can then be used as the `backfill_id` query parameter to the event ingestion
        endpoint to associate ingested events with this backfill. The effects (e.g.
        updated usage graphs) of this backfill will not take place until the backfill is
        closed.

        If the `replace_existing_events` is `true`, existing events in the backfill's
        timeframe will be replaced with the newly ingested events associated with the
        backfill. If `false`, newly ingested events will be added to the existing
        events.

        If a `customer_id` or `external_customer_id` is specified, the backfill will
        only affect events for that customer. If neither is specified, the backfill will
        affect all customers.

        When `replace_existing_events` is `true`, this indicates that existing events in
        the timeframe should no longer be counted towards invoiced usage. In this
        scenario, the parameter `deprecation_filter` can be optionally added which
        enables filtering using
        [computed properties](/extensibility/advanced-metrics#computed-properties). The
        expressiveness of computed properties allows you to deprecate existing events
        based on both a period of time and specific property values.

        You may not have multiple backfills in a pending or pending_revert state with
        overlapping timeframes.

        Args:
          timeframe_end: The (exclusive) end of the usage timeframe affected by this backfill. By
              default, Orb allows backfills up to 31 days in duration at a time. Reach out to
              discuss extending this limit and your use case.

          timeframe_start: The (inclusive) start of the usage timeframe affected by this backfill. By
              default, Orb allows backfills up to 31 days in duration at a time. Reach out to
              discuss extending this limit and your use case.

          close_time: The time at which no more events will be accepted for this backfill. The
              backfill will automatically begin reflecting throughout Orb at the close time.
              If not specified, it will default to 1 day after the creation of the backfill.

          customer_id: The Orb-generated ID of the customer to which this backfill is scoped. Omitting
              this field will scope the backfill to all customers.

          deprecation_filter: A boolean
              [computed property](/extensibility/advanced-metrics#computed-properties) used to
              filter the set of events to deprecate

          external_customer_id: The external customer ID of the customer to which this backfill is scoped.
              Omitting this field will scope the backfill to all customers.

          replace_existing_events: If true, replaces all existing events in the timeframe with the newly ingested
              events. If false, adds the newly ingested events to the existing events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/events/backfills",
            body=await async_maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "close_time": close_time,
                    "customer_id": customer_id,
                    "deprecation_filter": deprecation_filter,
                    "external_customer_id": external_customer_id,
                    "replace_existing_events": replace_existing_events,
                },
                backfill_create_params.BackfillCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BackfillCreateResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BackfillListResponse, AsyncPage[BackfillListResponse]]:
        """
        This endpoint returns a list of all backfills in a list format.

        The list of backfills is ordered starting from the most recently created
        backfill. The response also includes
        [`pagination_metadata`](/api-reference/pagination), which lets the caller
        retrieve the next page of results if they exist. More information about
        pagination can be found in the [Pagination-metadata schema](pagination).

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
            "/events/backfills",
            page=AsyncPage[BackfillListResponse],
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
                    backfill_list_params.BackfillListParams,
                ),
            ),
            model=BackfillListResponse,
        )

    async def close(
        self,
        backfill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BackfillCloseResponse:
        """Closing a backfill makes the updated usage visible in Orb.

        Upon closing a
        backfill, Orb will asynchronously reflect the updated usage in invoice amounts
        and usage graphs. Once all of the updates are complete, the backfill's status
        will transition to `reflected`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        return await self._post(
            f"/events/backfills/{backfill_id}/close",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BackfillCloseResponse,
        )

    async def fetch(
        self,
        backfill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BackfillFetchResponse:
        """
        This endpoint is used to fetch a backfill given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        return await self._get(
            f"/events/backfills/{backfill_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BackfillFetchResponse,
        )

    async def revert(
        self,
        backfill_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BackfillRevertResponse:
        """Reverting a backfill undoes all the effects of closing the backfill.

        If the
        backfill is reflected, the status will transition to `pending_revert` while the
        effects of the backfill are undone. Once all effects are undone, the backfill
        will transition to `reverted`.

        If a backfill is reverted before its closed, no usage will be updated as a
        result of the backfill and it will immediately transition to `reverted`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not backfill_id:
            raise ValueError(f"Expected a non-empty value for `backfill_id` but received {backfill_id!r}")
        return await self._post(
            f"/events/backfills/{backfill_id}/revert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BackfillRevertResponse,
        )


class BackfillsWithRawResponse:
    def __init__(self, backfills: Backfills) -> None:
        self._backfills = backfills

        self.create = _legacy_response.to_raw_response_wrapper(
            backfills.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            backfills.list,
        )
        self.close = _legacy_response.to_raw_response_wrapper(
            backfills.close,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            backfills.fetch,
        )
        self.revert = _legacy_response.to_raw_response_wrapper(
            backfills.revert,
        )


class AsyncBackfillsWithRawResponse:
    def __init__(self, backfills: AsyncBackfills) -> None:
        self._backfills = backfills

        self.create = _legacy_response.async_to_raw_response_wrapper(
            backfills.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            backfills.list,
        )
        self.close = _legacy_response.async_to_raw_response_wrapper(
            backfills.close,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            backfills.fetch,
        )
        self.revert = _legacy_response.async_to_raw_response_wrapper(
            backfills.revert,
        )


class BackfillsWithStreamingResponse:
    def __init__(self, backfills: Backfills) -> None:
        self._backfills = backfills

        self.create = to_streamed_response_wrapper(
            backfills.create,
        )
        self.list = to_streamed_response_wrapper(
            backfills.list,
        )
        self.close = to_streamed_response_wrapper(
            backfills.close,
        )
        self.fetch = to_streamed_response_wrapper(
            backfills.fetch,
        )
        self.revert = to_streamed_response_wrapper(
            backfills.revert,
        )


class AsyncBackfillsWithStreamingResponse:
    def __init__(self, backfills: AsyncBackfills) -> None:
        self._backfills = backfills

        self.create = async_to_streamed_response_wrapper(
            backfills.create,
        )
        self.list = async_to_streamed_response_wrapper(
            backfills.list,
        )
        self.close = async_to_streamed_response_wrapper(
            backfills.close,
        )
        self.fetch = async_to_streamed_response_wrapper(
            backfills.fetch,
        )
        self.revert = async_to_streamed_response_wrapper(
            backfills.revert,
        )
