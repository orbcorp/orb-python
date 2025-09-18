# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ... import _legacy_response
from ...types import (
    dimensional_price_group_list_params,
    dimensional_price_group_create_params,
    dimensional_price_group_update_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dimensional_price_group import DimensionalPriceGroup
from .external_dimensional_price_group_id import (
    ExternalDimensionalPriceGroupID,
    AsyncExternalDimensionalPriceGroupID,
    ExternalDimensionalPriceGroupIDWithRawResponse,
    AsyncExternalDimensionalPriceGroupIDWithRawResponse,
    ExternalDimensionalPriceGroupIDWithStreamingResponse,
    AsyncExternalDimensionalPriceGroupIDWithStreamingResponse,
)

__all__ = ["DimensionalPriceGroups", "AsyncDimensionalPriceGroups"]


class DimensionalPriceGroups(SyncAPIResource):
    @cached_property
    def external_dimensional_price_group_id(self) -> ExternalDimensionalPriceGroupID:
        return ExternalDimensionalPriceGroupID(self._client)

    @cached_property
    def with_raw_response(self) -> DimensionalPriceGroupsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return DimensionalPriceGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DimensionalPriceGroupsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return DimensionalPriceGroupsWithStreamingResponse(self)

    def create(
        self,
        *,
        billable_metric_id: str,
        dimensions: SequenceNotStr[str],
        name: str,
        external_dimensional_price_group_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> DimensionalPriceGroup:
        """
        A dimensional price group is used to partition the result of a billable metric
        by a set of dimensions. Prices in a price group must specify the partition used
        to derive their usage.

        For example, suppose we have a billable metric that measures the number of
        widgets used and we want to charge differently depending on the color of the
        widget. We can create a price group with a dimension "color" and two prices: one
        that charges \\$$10 per red widget and one that charges \\$$20 per blue widget.

        Args:
          dimensions: The set of keys (in order) used to disambiguate prices in the group.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/dimensional_price_groups",
            body=maybe_transform(
                {
                    "billable_metric_id": billable_metric_id,
                    "dimensions": dimensions,
                    "name": name,
                    "external_dimensional_price_group_id": external_dimensional_price_group_id,
                    "metadata": metadata,
                },
                dimensional_price_group_create_params.DimensionalPriceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DimensionalPriceGroup,
        )

    def retrieve(
        self,
        dimensional_price_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DimensionalPriceGroup:
        """
        Fetch dimensional price group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return self._get(
            f"/dimensional_price_groups/{dimensional_price_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionalPriceGroup,
        )

    def update(
        self,
        dimensional_price_group_id: str,
        *,
        external_dimensional_price_group_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> DimensionalPriceGroup:
        """
        This endpoint can be used to update the `external_dimensional_price_group_id`
        and `metadata` of an existing dimensional price group. Other fields on a
        dimensional price group are currently immutable.

        Args:
          external_dimensional_price_group_id: An optional user-defined ID for this dimensional price group resource, used
              throughout the system as an alias for this dimensional price group. Use this
              field to identify a dimensional price group by an existing identifier in your
              system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return self._put(
            f"/dimensional_price_groups/{dimensional_price_group_id}",
            body=maybe_transform(
                {
                    "external_dimensional_price_group_id": external_dimensional_price_group_id,
                    "metadata": metadata,
                },
                dimensional_price_group_update_params.DimensionalPriceGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DimensionalPriceGroup,
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
    ) -> SyncPage[DimensionalPriceGroup]:
        """List dimensional price groups

        Args:
          cursor: Cursor for pagination.

        This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dimensional_price_groups",
            page=SyncPage[DimensionalPriceGroup],
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
                    dimensional_price_group_list_params.DimensionalPriceGroupListParams,
                ),
            ),
            model=DimensionalPriceGroup,
        )


class AsyncDimensionalPriceGroups(AsyncAPIResource):
    @cached_property
    def external_dimensional_price_group_id(self) -> AsyncExternalDimensionalPriceGroupID:
        return AsyncExternalDimensionalPriceGroupID(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDimensionalPriceGroupsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDimensionalPriceGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDimensionalPriceGroupsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncDimensionalPriceGroupsWithStreamingResponse(self)

    async def create(
        self,
        *,
        billable_metric_id: str,
        dimensions: SequenceNotStr[str],
        name: str,
        external_dimensional_price_group_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> DimensionalPriceGroup:
        """
        A dimensional price group is used to partition the result of a billable metric
        by a set of dimensions. Prices in a price group must specify the partition used
        to derive their usage.

        For example, suppose we have a billable metric that measures the number of
        widgets used and we want to charge differently depending on the color of the
        widget. We can create a price group with a dimension "color" and two prices: one
        that charges \\$$10 per red widget and one that charges \\$$20 per blue widget.

        Args:
          dimensions: The set of keys (in order) used to disambiguate prices in the group.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/dimensional_price_groups",
            body=await async_maybe_transform(
                {
                    "billable_metric_id": billable_metric_id,
                    "dimensions": dimensions,
                    "name": name,
                    "external_dimensional_price_group_id": external_dimensional_price_group_id,
                    "metadata": metadata,
                },
                dimensional_price_group_create_params.DimensionalPriceGroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DimensionalPriceGroup,
        )

    async def retrieve(
        self,
        dimensional_price_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DimensionalPriceGroup:
        """
        Fetch dimensional price group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return await self._get(
            f"/dimensional_price_groups/{dimensional_price_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DimensionalPriceGroup,
        )

    async def update(
        self,
        dimensional_price_group_id: str,
        *,
        external_dimensional_price_group_id: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> DimensionalPriceGroup:
        """
        This endpoint can be used to update the `external_dimensional_price_group_id`
        and `metadata` of an existing dimensional price group. Other fields on a
        dimensional price group are currently immutable.

        Args:
          external_dimensional_price_group_id: An optional user-defined ID for this dimensional price group resource, used
              throughout the system as an alias for this dimensional price group. Use this
              field to identify a dimensional price group by an existing identifier in your
              system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return await self._put(
            f"/dimensional_price_groups/{dimensional_price_group_id}",
            body=await async_maybe_transform(
                {
                    "external_dimensional_price_group_id": external_dimensional_price_group_id,
                    "metadata": metadata,
                },
                dimensional_price_group_update_params.DimensionalPriceGroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=DimensionalPriceGroup,
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
    ) -> AsyncPaginator[DimensionalPriceGroup, AsyncPage[DimensionalPriceGroup]]:
        """List dimensional price groups

        Args:
          cursor: Cursor for pagination.

        This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dimensional_price_groups",
            page=AsyncPage[DimensionalPriceGroup],
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
                    dimensional_price_group_list_params.DimensionalPriceGroupListParams,
                ),
            ),
            model=DimensionalPriceGroup,
        )


class DimensionalPriceGroupsWithRawResponse:
    def __init__(self, dimensional_price_groups: DimensionalPriceGroups) -> None:
        self._dimensional_price_groups = dimensional_price_groups

        self.create = _legacy_response.to_raw_response_wrapper(
            dimensional_price_groups.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            dimensional_price_groups.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            dimensional_price_groups.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            dimensional_price_groups.list,
        )

    @cached_property
    def external_dimensional_price_group_id(self) -> ExternalDimensionalPriceGroupIDWithRawResponse:
        return ExternalDimensionalPriceGroupIDWithRawResponse(
            self._dimensional_price_groups.external_dimensional_price_group_id
        )


class AsyncDimensionalPriceGroupsWithRawResponse:
    def __init__(self, dimensional_price_groups: AsyncDimensionalPriceGroups) -> None:
        self._dimensional_price_groups = dimensional_price_groups

        self.create = _legacy_response.async_to_raw_response_wrapper(
            dimensional_price_groups.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            dimensional_price_groups.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            dimensional_price_groups.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            dimensional_price_groups.list,
        )

    @cached_property
    def external_dimensional_price_group_id(self) -> AsyncExternalDimensionalPriceGroupIDWithRawResponse:
        return AsyncExternalDimensionalPriceGroupIDWithRawResponse(
            self._dimensional_price_groups.external_dimensional_price_group_id
        )


class DimensionalPriceGroupsWithStreamingResponse:
    def __init__(self, dimensional_price_groups: DimensionalPriceGroups) -> None:
        self._dimensional_price_groups = dimensional_price_groups

        self.create = to_streamed_response_wrapper(
            dimensional_price_groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            dimensional_price_groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dimensional_price_groups.update,
        )
        self.list = to_streamed_response_wrapper(
            dimensional_price_groups.list,
        )

    @cached_property
    def external_dimensional_price_group_id(self) -> ExternalDimensionalPriceGroupIDWithStreamingResponse:
        return ExternalDimensionalPriceGroupIDWithStreamingResponse(
            self._dimensional_price_groups.external_dimensional_price_group_id
        )


class AsyncDimensionalPriceGroupsWithStreamingResponse:
    def __init__(self, dimensional_price_groups: AsyncDimensionalPriceGroups) -> None:
        self._dimensional_price_groups = dimensional_price_groups

        self.create = async_to_streamed_response_wrapper(
            dimensional_price_groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            dimensional_price_groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dimensional_price_groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dimensional_price_groups.list,
        )

    @cached_property
    def external_dimensional_price_group_id(self) -> AsyncExternalDimensionalPriceGroupIDWithStreamingResponse:
        return AsyncExternalDimensionalPriceGroupIDWithStreamingResponse(
            self._dimensional_price_groups.external_dimensional_price_group_id
        )
