# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import metric_list_params, metric_create_params, metric_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.billable_metric import BillableMetric

__all__ = ["Metrics", "AsyncMetrics"]


class Metrics(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return MetricsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return MetricsWithStreamingResponse(self)

    def create(
        self,
        *,
        description: Optional[str],
        item_id: str,
        name: str,
        sql: str,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillableMetric:
        """
        This endpoint is used to create a [metric](/core-concepts###metric) using a SQL
        string. See [SQL support](/extensibility/advanced-metrics#sql-support) for a
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
            cast_to=BillableMetric,
        )

    def update(
        self,
        metric_id: str,
        *,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillableMetric:
        """This endpoint allows you to update the `metadata` property on a metric.

        If you
        pass `null` for the metadata value, it will clear any existing metadata for that
        invoice.

        Args:
          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return self._put(
            f"/metrics/{metric_id}",
            body=maybe_transform({"metadata": metadata}, metric_update_params.MetricUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillableMetric,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[BillableMetric]:
        """
        This endpoint is used to fetch [metric](/core-concepts##metric) details given a
        metric identifier. It returns information about the metrics including its name,
        description, and item.

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
            page=SyncPage[BillableMetric],
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
            model=BillableMetric,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetric:
        """This endpoint is used to list [metrics](/core-concepts#metric).

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
            cast_to=BillableMetric,
        )


class AsyncMetrics(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncMetricsWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: Optional[str],
        item_id: str,
        name: str,
        sql: str,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillableMetric:
        """
        This endpoint is used to create a [metric](/core-concepts###metric) using a SQL
        string. See [SQL support](/extensibility/advanced-metrics#sql-support) for a
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
            body=await async_maybe_transform(
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
            cast_to=BillableMetric,
        )

    async def update(
        self,
        metric_id: str,
        *,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillableMetric:
        """This endpoint allows you to update the `metadata` property on a metric.

        If you
        pass `null` for the metadata value, it will clear any existing metadata for that
        invoice.

        Args:
          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not metric_id:
            raise ValueError(f"Expected a non-empty value for `metric_id` but received {metric_id!r}")
        return await self._put(
            f"/metrics/{metric_id}",
            body=await async_maybe_transform({"metadata": metadata}, metric_update_params.MetricUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillableMetric,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BillableMetric, AsyncPage[BillableMetric]]:
        """
        This endpoint is used to fetch [metric](/core-concepts##metric) details given a
        metric identifier. It returns information about the metrics including its name,
        description, and item.

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
            page=AsyncPage[BillableMetric],
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
            model=BillableMetric,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetric:
        """This endpoint is used to list [metrics](/core-concepts#metric).

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
            cast_to=BillableMetric,
        )


class MetricsWithRawResponse:
    def __init__(self, metrics: Metrics) -> None:
        self._metrics = metrics

        self.create = _legacy_response.to_raw_response_wrapper(
            metrics.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            metrics.update,
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
        self.update = _legacy_response.async_to_raw_response_wrapper(
            metrics.update,
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
        self.update = to_streamed_response_wrapper(
            metrics.update,
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
        self.update = async_to_streamed_response_wrapper(
            metrics.update,
        )
        self.list = async_to_streamed_response_wrapper(
            metrics.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            metrics.fetch,
        )
