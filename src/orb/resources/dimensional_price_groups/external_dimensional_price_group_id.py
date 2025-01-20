# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.dimensional_price_group import DimensionalPriceGroup

__all__ = ["ExternalDimensionalPriceGroupID", "AsyncExternalDimensionalPriceGroupID"]


class ExternalDimensionalPriceGroupID(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalDimensionalPriceGroupIDWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return ExternalDimensionalPriceGroupIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalDimensionalPriceGroupIDWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return ExternalDimensionalPriceGroupIDWithStreamingResponse(self)

    def retrieve(
        self,
        external_dimensional_price_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DimensionalPriceGroup:
        """
        Fetch dimensional price group by external ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `external_dimensional_price_group_id` but received {external_dimensional_price_group_id!r}"
            )
        return self._get(
            f"/dimensional_price_groups/external_dimensional_price_group_id/{external_dimensional_price_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionalPriceGroup,
        )


class AsyncExternalDimensionalPriceGroupID(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalDimensionalPriceGroupIDWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalDimensionalPriceGroupIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalDimensionalPriceGroupIDWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncExternalDimensionalPriceGroupIDWithStreamingResponse(self)

    async def retrieve(
        self,
        external_dimensional_price_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DimensionalPriceGroup:
        """
        Fetch dimensional price group by external ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `external_dimensional_price_group_id` but received {external_dimensional_price_group_id!r}"
            )
        return await self._get(
            f"/dimensional_price_groups/external_dimensional_price_group_id/{external_dimensional_price_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionalPriceGroup,
        )


class ExternalDimensionalPriceGroupIDWithRawResponse:
    def __init__(self, external_dimensional_price_group_id: ExternalDimensionalPriceGroupID) -> None:
        self._external_dimensional_price_group_id = external_dimensional_price_group_id

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            external_dimensional_price_group_id.retrieve,
        )


class AsyncExternalDimensionalPriceGroupIDWithRawResponse:
    def __init__(self, external_dimensional_price_group_id: AsyncExternalDimensionalPriceGroupID) -> None:
        self._external_dimensional_price_group_id = external_dimensional_price_group_id

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            external_dimensional_price_group_id.retrieve,
        )


class ExternalDimensionalPriceGroupIDWithStreamingResponse:
    def __init__(self, external_dimensional_price_group_id: ExternalDimensionalPriceGroupID) -> None:
        self._external_dimensional_price_group_id = external_dimensional_price_group_id

        self.retrieve = to_streamed_response_wrapper(
            external_dimensional_price_group_id.retrieve,
        )


class AsyncExternalDimensionalPriceGroupIDWithStreamingResponse:
    def __init__(self, external_dimensional_price_group_id: AsyncExternalDimensionalPriceGroupID) -> None:
        self._external_dimensional_price_group_id = external_dimensional_price_group_id

        self.retrieve = async_to_streamed_response_wrapper(
            external_dimensional_price_group_id.retrieve,
        )
