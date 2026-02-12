# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.licenses import usage_get_usage_params, usage_get_all_usage_params
from ...types.licenses.usage_get_usage_response import UsageGetUsageResponse
from ...types.licenses.usage_get_all_usage_response import UsageGetAllUsageResponse

__all__ = ["Usage", "AsyncUsage"]


class Usage(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return UsageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return UsageWithStreamingResponse(self)

    def get_all_usage(
        self,
        *,
        license_type_id: str,
        subscription_id: str,
        cursor: Optional[str] | Omit = omit,
        end_date: Union[str, date, None] | Omit = omit,
        group_by: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAllUsageResponse:
        """
        Returns usage and remaining credits for all licenses of a given type on a
        subscription.

        Date range defaults to the current billing period if not specified.

        Args:
          license_type_id: The license type ID to filter licenses by.

          subscription_id: The subscription ID to get license usage for.

          cursor: Pagination cursor from a previous request.

          end_date: End date for the usage period (YYYY-MM-DD). Defaults to end of current billing
              period.

          group_by: How to group the results. Valid values: 'license', 'day'. Can be combined (e.g.,
              'license,day').

          limit: Maximum number of rows in the response data (default 20, max 100).

          start_date: Start date for the usage period (YYYY-MM-DD). Defaults to start of current
              billing period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/licenses/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "license_type_id": license_type_id,
                        "subscription_id": subscription_id,
                        "cursor": cursor,
                        "end_date": end_date,
                        "group_by": group_by,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    usage_get_all_usage_params.UsageGetAllUsageParams,
                ),
            ),
            cast_to=UsageGetAllUsageResponse,
        )

    def get_usage(
        self,
        license_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        end_date: Union[str, date, None] | Omit = omit,
        group_by: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetUsageResponse:
        """
        Returns usage and remaining credits for a specific license over a date range.

        Date range defaults to the current billing period if not specified.

        Args:
          cursor: Pagination cursor from a previous request.

          end_date: End date for the usage period (YYYY-MM-DD). Defaults to end of current billing
              period.

          group_by: How to group the results. Valid values: 'license', 'day'. Can be combined (e.g.,
              'license,day').

          limit: Maximum number of rows in the response data (default 20, max 100).

          start_date: Start date for the usage period (YYYY-MM-DD). Defaults to start of current
              billing period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license_id:
            raise ValueError(f"Expected a non-empty value for `license_id` but received {license_id!r}")
        return self._get(
            f"/licenses/{license_id}/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "end_date": end_date,
                        "group_by": group_by,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    usage_get_usage_params.UsageGetUsageParams,
                ),
            ),
            cast_to=UsageGetUsageResponse,
        )


class AsyncUsage(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncUsageWithStreamingResponse(self)

    async def get_all_usage(
        self,
        *,
        license_type_id: str,
        subscription_id: str,
        cursor: Optional[str] | Omit = omit,
        end_date: Union[str, date, None] | Omit = omit,
        group_by: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAllUsageResponse:
        """
        Returns usage and remaining credits for all licenses of a given type on a
        subscription.

        Date range defaults to the current billing period if not specified.

        Args:
          license_type_id: The license type ID to filter licenses by.

          subscription_id: The subscription ID to get license usage for.

          cursor: Pagination cursor from a previous request.

          end_date: End date for the usage period (YYYY-MM-DD). Defaults to end of current billing
              period.

          group_by: How to group the results. Valid values: 'license', 'day'. Can be combined (e.g.,
              'license,day').

          limit: Maximum number of rows in the response data (default 20, max 100).

          start_date: Start date for the usage period (YYYY-MM-DD). Defaults to start of current
              billing period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/licenses/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "license_type_id": license_type_id,
                        "subscription_id": subscription_id,
                        "cursor": cursor,
                        "end_date": end_date,
                        "group_by": group_by,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    usage_get_all_usage_params.UsageGetAllUsageParams,
                ),
            ),
            cast_to=UsageGetAllUsageResponse,
        )

    async def get_usage(
        self,
        license_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        end_date: Union[str, date, None] | Omit = omit,
        group_by: Optional[SequenceNotStr[str]] | Omit = omit,
        limit: int | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetUsageResponse:
        """
        Returns usage and remaining credits for a specific license over a date range.

        Date range defaults to the current billing period if not specified.

        Args:
          cursor: Pagination cursor from a previous request.

          end_date: End date for the usage period (YYYY-MM-DD). Defaults to end of current billing
              period.

          group_by: How to group the results. Valid values: 'license', 'day'. Can be combined (e.g.,
              'license,day').

          limit: Maximum number of rows in the response data (default 20, max 100).

          start_date: Start date for the usage period (YYYY-MM-DD). Defaults to start of current
              billing period.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license_id:
            raise ValueError(f"Expected a non-empty value for `license_id` but received {license_id!r}")
        return await self._get(
            f"/licenses/{license_id}/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "end_date": end_date,
                        "group_by": group_by,
                        "limit": limit,
                        "start_date": start_date,
                    },
                    usage_get_usage_params.UsageGetUsageParams,
                ),
            ),
            cast_to=UsageGetUsageResponse,
        )


class UsageWithRawResponse:
    def __init__(self, usage: Usage) -> None:
        self._usage = usage

        self.get_all_usage = _legacy_response.to_raw_response_wrapper(
            usage.get_all_usage,
        )
        self.get_usage = _legacy_response.to_raw_response_wrapper(
            usage.get_usage,
        )


class AsyncUsageWithRawResponse:
    def __init__(self, usage: AsyncUsage) -> None:
        self._usage = usage

        self.get_all_usage = _legacy_response.async_to_raw_response_wrapper(
            usage.get_all_usage,
        )
        self.get_usage = _legacy_response.async_to_raw_response_wrapper(
            usage.get_usage,
        )


class UsageWithStreamingResponse:
    def __init__(self, usage: Usage) -> None:
        self._usage = usage

        self.get_all_usage = to_streamed_response_wrapper(
            usage.get_all_usage,
        )
        self.get_usage = to_streamed_response_wrapper(
            usage.get_usage,
        )


class AsyncUsageWithStreamingResponse:
    def __init__(self, usage: AsyncUsage) -> None:
        self._usage = usage

        self.get_all_usage = async_to_streamed_response_wrapper(
            usage.get_all_usage,
        )
        self.get_usage = async_to_streamed_response_wrapper(
            usage.get_usage,
        )
