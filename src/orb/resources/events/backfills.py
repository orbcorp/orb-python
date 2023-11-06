# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.events import (
    BackfillListResponse,
    BackfillCloseResponse,
    BackfillFetchResponse,
    BackfillCreateResponse,
    BackfillRevertResponse,
    backfill_list_params,
    backfill_create_params,
)

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["Backfills", "AsyncBackfills"]


class Backfills(SyncAPIResource):
    with_raw_response: BackfillsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = BackfillsWithRawResponse(self)

    def create(
        self,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        close_time: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        replace_existing_events: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        Args:
          timeframe_end: The (exclusive) end of the usage timeframe affected by this backfill.

          timeframe_start: The (inclusive) start of the usage timeframe affected by this backfill.

          close_time: The time at which no more events will be accepted for this backfill. The
              backfill will automatically begin reflecting throughout Orb at the close time.
              If not specified, it will default to 1 day after the creation of the backfill.

          customer_id: The ID of the customer to which this backfill is scoped.

          external_customer_id: The external customer ID of the customer to which this backfill is scoped.

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
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BackfillListResponse]:
        """
        This endpoint returns a list of all backfills in a list format.

        The list of backfills is ordered starting from the most recently created
        backfill. The response also includes
        [`pagination_metadata`](../reference/pagination), which lets the caller retrieve
        the next page of results if they exist. More information about pagination can be
        found in the [Pagination-metadata schema](pagination).

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BackfillFetchResponse:
        """
        This endpoint is used to fetch a backfill given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
    with_raw_response: AsyncBackfillsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncBackfillsWithRawResponse(self)

    async def create(
        self,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        close_time: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        replace_existing_events: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

        Args:
          timeframe_end: The (exclusive) end of the usage timeframe affected by this backfill.

          timeframe_start: The (inclusive) start of the usage timeframe affected by this backfill.

          close_time: The time at which no more events will be accepted for this backfill. The
              backfill will automatically begin reflecting throughout Orb at the close time.
              If not specified, it will default to 1 day after the creation of the backfill.

          customer_id: The ID of the customer to which this backfill is scoped.

          external_customer_id: The external customer ID of the customer to which this backfill is scoped.

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
            body=maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "close_time": close_time,
                    "customer_id": customer_id,
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
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BackfillListResponse, AsyncPage[BackfillListResponse]]:
        """
        This endpoint returns a list of all backfills in a list format.

        The list of backfills is ordered starting from the most recently created
        backfill. The response also includes
        [`pagination_metadata`](../reference/pagination), which lets the caller retrieve
        the next page of results if they exist. More information about pagination can be
        found in the [Pagination-metadata schema](pagination).

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BackfillFetchResponse:
        """
        This endpoint is used to fetch a backfill given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        self.create = to_raw_response_wrapper(
            backfills.create,
        )
        self.list = to_raw_response_wrapper(
            backfills.list,
        )
        self.close = to_raw_response_wrapper(
            backfills.close,
        )
        self.fetch = to_raw_response_wrapper(
            backfills.fetch,
        )
        self.revert = to_raw_response_wrapper(
            backfills.revert,
        )


class AsyncBackfillsWithRawResponse:
    def __init__(self, backfills: AsyncBackfills) -> None:
        self.create = async_to_raw_response_wrapper(
            backfills.create,
        )
        self.list = async_to_raw_response_wrapper(
            backfills.list,
        )
        self.close = async_to_raw_response_wrapper(
            backfills.close,
        )
        self.fetch = async_to_raw_response_wrapper(
            backfills.fetch,
        )
        self.revert = async_to_raw_response_wrapper(
            backfills.revert,
        )
