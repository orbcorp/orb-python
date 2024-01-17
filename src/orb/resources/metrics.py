# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import (
    MetricListResponse,
    MetricFetchResponse,
    MetricCreateResponse,
    metric_list_params,
    metric_create_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Metrics", "AsyncMetrics"]


class Metrics(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsWithRawResponse:
        return MetricsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsWithStreamingResponse:
        return MetricsWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        item_id: str,
        name: str,
        sql: str,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> MetricCreateResponse:
        """
        This endpoint is used to create a [metric](../guides/concepts##metric) using a
        SQL string. See
        [SQL support](../guides/extensibility/advanced-metrics#sql-support) for a
        description of constructing SQL queries with examples.

        Args:
          description: A description of the metric.

          item_id: The id of the item

          name: The name of the metric.

          sql: A sql string defining the metric.

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
            "/metrics",
            body=maybe_transform(
                {
                    "description": description,
                    "item_id": item_id,
                    "name": name,
                    "sql": sql,
                    "metadata": metadata,
                },
                metric_create_params.MetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MetricCreateResponse,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[MetricListResponse]:
        """
        This endpoint is used to fetch [metric](../guides/concepts#metric) details given
        a metric identifier. It returns information about the metrics including its
        name, description, and item.

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
            "/metrics",
            page=SyncPage[MetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            model=MetricListResponse,
        )

    def fetch(
        self,
        metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricFetchResponse:
        """This endpoint is used to list [metrics](../guides/concepts##metric).

        It returns
        information about the metrics including its name, description, and item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return self._get(
            f"/metrics/{metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricFetchResponse,
        )


class AsyncMetrics(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsWithRawResponse:
        return AsyncMetricsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsWithStreamingResponse:
        return AsyncMetricsWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        item_id: str,
        name: str,
        sql: str,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> MetricCreateResponse:
        """
        This endpoint is used to create a [metric](../guides/concepts##metric) using a
        SQL string. See
        [SQL support](../guides/extensibility/advanced-metrics#sql-support) for a
        description of constructing SQL queries with examples.

        Args:
          description: A description of the metric.

          item_id: The id of the item

          name: The name of the metric.

          sql: A sql string defining the metric.

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
            "/metrics",
            body=maybe_transform(
                {
                    "description": description,
                    "item_id": item_id,
                    "name": name,
                    "sql": sql,
                    "metadata": metadata,
                },
                metric_create_params.MetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MetricCreateResponse,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MetricListResponse, AsyncPage[MetricListResponse]]:
        """
        This endpoint is used to fetch [metric](../guides/concepts#metric) details given
        a metric identifier. It returns information about the metrics including its
        name, description, and item.

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
            "/metrics",
            page=AsyncPage[MetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    metric_list_params.MetricListParams,
                ),
            ),
            model=MetricListResponse,
        )

    async def fetch(
        self,
        metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MetricFetchResponse:
        """This endpoint is used to list [metrics](../guides/concepts##metric).

        It returns
        information about the metrics including its name, description, and item.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return await self._get(
            f"/metrics/{metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MetricFetchResponse,
        )


class MetricsWithRawResponse:
    def __init__(self, metrics: Metrics) -> None:
        self._metrics = metrics

        self.create = _legacy_response.to_raw_response_wrapper(
            metrics.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            metrics.list,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            metrics.fetch,
        )


class AsyncMetricsWithRawResponse:
    def __init__(self, metrics: AsyncMetrics) -> None:
        self._metrics = metrics

        self.create = _legacy_response.async_to_raw_response_wrapper(
            metrics.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            metrics.list,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            metrics.fetch,
        )


class MetricsWithStreamingResponse:
    def __init__(self, metrics: Metrics) -> None:
        self._metrics = metrics

        self.create = to_streamed_response_wrapper(
            metrics.create,
        )
        self.list = to_streamed_response_wrapper(
            metrics.list,
        )
        self.fetch = to_streamed_response_wrapper(
            metrics.fetch,
        )


class AsyncMetricsWithStreamingResponse:
    def __init__(self, metrics: AsyncMetrics) -> None:
        self._metrics = metrics

        self.create = async_to_streamed_response_wrapper(
            metrics.create,
        )
        self.list = async_to_streamed_response_wrapper(
            metrics.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            metrics.fetch,
        )
