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
from ..._base_client import make_request_options
from ...types.events import volume_list_params
from ...types.events.event_volumes import EventVolumes

__all__ = ["Volume", "AsyncVolume"]


class Volume(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VolumeWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return VolumeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VolumeWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return VolumeWithStreamingResponse(self)

    def list(
        self,
        *,
        timeframe_start: Union[str, datetime],
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        timeframe_end: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVolumes:
        """
        This endpoint returns the event volume for an account in a
        [paginated list format](/api-reference/pagination).

        The event volume is aggregated by the hour and the
        [timestamp](/api-reference/event/ingest-events) field is used to determine which
        hour an event is associated with. Note, this means that late-arriving events
        increment the volume count for the hour window the timestamp is in, not the
        latest hour window.

        Each item in the response contains the count of events aggregated by the hour
        where the start and end time are hour-aligned and in UTC. When a specific
        timestamp is passed in for either start or end time, the response includes the
        hours the timestamp falls in.

        Args:
          timeframe_start: The start of the timeframe, inclusive, in which to return event volume. All
              datetime values are converted to UTC time. If the specified time isn't
              hour-aligned, the response includes the event volume count for the hour the time
              falls in.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          timeframe_end: The end of the timeframe, exclusive, in which to return event volume. If not
              specified, the current time is used. All datetime values are converted to UTC
              time.If the specified time isn't hour-aligned, the response includes the event
              volumecount for the hour the time falls in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/events/volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "timeframe_start": timeframe_start,
                        "cursor": cursor,
                        "limit": limit,
                        "timeframe_end": timeframe_end,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            cast_to=EventVolumes,
        )


class AsyncVolume(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVolumeWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVolumeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVolumeWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncVolumeWithStreamingResponse(self)

    async def list(
        self,
        *,
        timeframe_start: Union[str, datetime],
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        timeframe_end: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventVolumes:
        """
        This endpoint returns the event volume for an account in a
        [paginated list format](/api-reference/pagination).

        The event volume is aggregated by the hour and the
        [timestamp](/api-reference/event/ingest-events) field is used to determine which
        hour an event is associated with. Note, this means that late-arriving events
        increment the volume count for the hour window the timestamp is in, not the
        latest hour window.

        Each item in the response contains the count of events aggregated by the hour
        where the start and end time are hour-aligned and in UTC. When a specific
        timestamp is passed in for either start or end time, the response includes the
        hours the timestamp falls in.

        Args:
          timeframe_start: The start of the timeframe, inclusive, in which to return event volume. All
              datetime values are converted to UTC time. If the specified time isn't
              hour-aligned, the response includes the event volume count for the hour the time
              falls in.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          timeframe_end: The end of the timeframe, exclusive, in which to return event volume. If not
              specified, the current time is used. All datetime values are converted to UTC
              time.If the specified time isn't hour-aligned, the response includes the event
              volumecount for the hour the time falls in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/events/volume",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "timeframe_start": timeframe_start,
                        "cursor": cursor,
                        "limit": limit,
                        "timeframe_end": timeframe_end,
                    },
                    volume_list_params.VolumeListParams,
                ),
            ),
            cast_to=EventVolumes,
        )


class VolumeWithRawResponse:
    def __init__(self, volume: Volume) -> None:
        self._volume = volume

        self.list = _legacy_response.to_raw_response_wrapper(
            volume.list,
        )


class AsyncVolumeWithRawResponse:
    def __init__(self, volume: AsyncVolume) -> None:
        self._volume = volume

        self.list = _legacy_response.async_to_raw_response_wrapper(
            volume.list,
        )


class VolumeWithStreamingResponse:
    def __init__(self, volume: Volume) -> None:
        self._volume = volume

        self.list = to_streamed_response_wrapper(
            volume.list,
        )


class AsyncVolumeWithStreamingResponse:
    def __init__(self, volume: AsyncVolume) -> None:
        self._volume = volume

        self.list = async_to_streamed_response_wrapper(
            volume.list,
        )
