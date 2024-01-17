# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.beta import PriceEvaluateResponse, price_evaluate_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Price", "AsyncPrice"]


class Price(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriceWithRawResponse:
        return PriceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriceWithStreamingResponse:
        return PriceWithStreamingResponse(self)

    def evaluate(
        self,
        price_id: str,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        grouping_keys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PriceEvaluateResponse:
        """
        This endpoint is used to evaluate the output of a price for a given customer and
        time range. It enables filtering and grouping the output using
        [computed properties](../guides/extensibility/advanced-metrics#computed-properties),
        supporting the following workflows:

        1. Showing detailed usage and costs to the end customer.
        2. Auditing subtotals on invoice line items.

        For these workflows, the expressiveness of computed properties in both the
        filters and grouping is critical. For example, if you'd like to show your
        customer their usage grouped by hour and another property, you can do so with
        the following `grouping_keys`:
        `["hour_floor_timestamp_millis(timestamp_millis)", "my_property"]`. If you'd
        like to examine a customer's usage for a specific property value, you can do so
        with the following `filter`:
        `my_property = 'foo' AND my_other_property = 'bar'`.

        By default, the start of the time range must be no more than 100 days ago and
        the length of the results must be no greater than 1000. Note that this is a POST
        endpoint rather than a GET endpoint because it employs a JSON body rather than
        query parameters.

        Args:
          timeframe_end: The exclusive upper bound for event timestamps

          timeframe_start: The inclusive lower bound for event timestamps

          customer_id: The ID of the customer to which this evaluation is scoped.

          external_customer_id: The external customer ID of the customer to which this evaluation is scoped.

          filter: A boolean
              [computed property](../guides/extensibility/advanced-metrics#computed-properties)
              used to filter the underlying billable metric

          grouping_keys: Properties (or
              [computed properties](../guides/extensibility/advanced-metrics#computed-properties))
              used to group the underlying billable metric

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return self._post(
            f"/prices/{price_id}/evaluate",
            body=maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "customer_id": customer_id,
                    "external_customer_id": external_customer_id,
                    "filter": filter,
                    "grouping_keys": grouping_keys,
                },
                price_evaluate_params.PriceEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceEvaluateResponse,
        )


class AsyncPrice(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriceWithRawResponse:
        return AsyncPriceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriceWithStreamingResponse:
        return AsyncPriceWithStreamingResponse(self)

    async def evaluate(
        self,
        price_id: str,
        *,
        timeframe_end: Union[str, datetime],
        timeframe_start: Union[str, datetime],
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        filter: Optional[str] | NotGiven = NOT_GIVEN,
        grouping_keys: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> PriceEvaluateResponse:
        """
        This endpoint is used to evaluate the output of a price for a given customer and
        time range. It enables filtering and grouping the output using
        [computed properties](../guides/extensibility/advanced-metrics#computed-properties),
        supporting the following workflows:

        1. Showing detailed usage and costs to the end customer.
        2. Auditing subtotals on invoice line items.

        For these workflows, the expressiveness of computed properties in both the
        filters and grouping is critical. For example, if you'd like to show your
        customer their usage grouped by hour and another property, you can do so with
        the following `grouping_keys`:
        `["hour_floor_timestamp_millis(timestamp_millis)", "my_property"]`. If you'd
        like to examine a customer's usage for a specific property value, you can do so
        with the following `filter`:
        `my_property = 'foo' AND my_other_property = 'bar'`.

        By default, the start of the time range must be no more than 100 days ago and
        the length of the results must be no greater than 1000. Note that this is a POST
        endpoint rather than a GET endpoint because it employs a JSON body rather than
        query parameters.

        Args:
          timeframe_end: The exclusive upper bound for event timestamps

          timeframe_start: The inclusive lower bound for event timestamps

          customer_id: The ID of the customer to which this evaluation is scoped.

          external_customer_id: The external customer ID of the customer to which this evaluation is scoped.

          filter: A boolean
              [computed property](../guides/extensibility/advanced-metrics#computed-properties)
              used to filter the underlying billable metric

          grouping_keys: Properties (or
              [computed properties](../guides/extensibility/advanced-metrics#computed-properties))
              used to group the underlying billable metric

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not price_id:
            raise ValueError(f"Expected a non-empty value for `price_id` but received {price_id!r}")
        return await self._post(
            f"/prices/{price_id}/evaluate",
            body=maybe_transform(
                {
                    "timeframe_end": timeframe_end,
                    "timeframe_start": timeframe_start,
                    "customer_id": customer_id,
                    "external_customer_id": external_customer_id,
                    "filter": filter,
                    "grouping_keys": grouping_keys,
                },
                price_evaluate_params.PriceEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceEvaluateResponse,
        )


class PriceWithRawResponse:
    def __init__(self, price: Price) -> None:
        self._price = price

        self.evaluate = _legacy_response.to_raw_response_wrapper(
            price.evaluate,
        )


class AsyncPriceWithRawResponse:
    def __init__(self, price: AsyncPrice) -> None:
        self._price = price

        self.evaluate = _legacy_response.async_to_raw_response_wrapper(
            price.evaluate,
        )


class PriceWithStreamingResponse:
    def __init__(self, price: Price) -> None:
        self._price = price

        self.evaluate = to_streamed_response_wrapper(
            price.evaluate,
        )


class AsyncPriceWithStreamingResponse:
    def __init__(self, price: AsyncPrice) -> None:
        self._price = price

        self.evaluate = async_to_streamed_response_wrapper(
            price.evaluate,
        )
