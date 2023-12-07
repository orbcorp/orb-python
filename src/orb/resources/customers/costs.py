# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.customers import (
    CostListResponse,
    CostListByExternalIDResponse,
    cost_list_params,
    cost_list_by_external_id_params,
)

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["Costs", "AsyncCosts"]


class Costs(SyncAPIResource):
    with_raw_response: CostsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = CostsWithRawResponse(self)

    def list(
        self,
        customer_id: Optional[str],
        *,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        timeframe_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        view_mode: Optional[Literal["periodic", "cumulative"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CostListResponse:
        """
        This endpoint is used to fetch a day-by-day snapshot of a customer's costs in
        Orb, calculated by applying pricing information to the underlying usage (see the
        [subscription usage endpoint](fetch-subscription-usage.api.mdx) to fetch usage
        per metric, in usage units rather than a currency).

        This endpoint can be leveraged for internal tooling and to provide a more
        transparent billing experience for your end users:

        1. Understand the cost breakdown per line item historically and in real-time for
           the current billing period.
        2. Provide customer visibility into how different services are contributing to
           the overall invoice with a per-day timeseries (as compared to the
           [upcoming invoice](fetch-upcoming-invoice) resource, which represents a
           snapshot for the current period).
        3. Assess how minimums and discounts affect your customers by teasing apart
           costs directly as a result of usage, as opposed to minimums and discounts at
           the plan and price level.
        4. Gain insight into key customer health metrics, such as the percent
           utilization of the minimum committed spend.

        ## Fetching subscriptions

        By default, this endpoint fetches the currently active subscription for the
        customer, and returns cost information for the subscription's current billing
        period, broken down by each participating price. If there are no currently
        active subscriptions, this will instead default to the most recently active
        subscription or return an empty series if none are found. For example, if your
        plan charges for compute hours, job runs, and data syncs, then this endpoint
        would provide a daily breakdown of your customer's cost for each of those axes.

        If timeframe bounds are specified, Orb fetches all subscriptions that were
        active in that timeframe. If two subscriptions overlap on a single day, costs
        from each price will be summed, and prices for both subscriptions will be
        included in the breakdown.

        ## Prepaid plans

        For plans that include prices which deduct credits rather than accrue in-arrears
        charges in a billable currency, this endpoint will return the total deduction
        amount, in credits, for the specified timeframe.

        ## Cumulative subtotals and totals

        Since the subtotal and total must factor in any billing-period level discounts
        and minimums, it's most meaningful to consider costs relative to the start of
        the subscription's billing period. As a result, by default this endpoint returns
        cumulative totals since the beginning of the billing period. In particular, the
        `timeframe_start` of a returned timeframe window is _always_ the beginning of
        the billing period and `timeframe_end` is incremented one day at a time to build
        the result.

        A customer that uses a few API calls a day but has a minimum commitment might
        exhibit the following pattern for their subtotal and total in the first few days
        of the month. Here, we assume that each API call is $2.50, the customer's plan
        has a monthly minimum of $50 for this price, and that the subscription's billing
        period bounds are aligned to the first of the month:

        | timeframe_start | timeframe_end | Cumulative usage | Subtotal | Total (incl. commitment) |
        | --------------- | ------------- | ---------------- | -------- | ------------------------ |
        | 2023-02-01      | 2023-02-02    | 9                | $22.50   | $50.00                   |
        | 2023-02-01      | 2023-02-03    | 19               | $47.50   | $50.00                   |
        | 2023-02-01      | 2023-02-04    | 20               | $50.00   | $50.00                   |
        | 2023-02-01      | 2023-02-05    | 28               | $70.00   | $70.00                   |
        | 2023-02-01      | 2023-02-06    | 36               | $90.00   | $90.00                   |

        ### Periodic values

        When the query parameter `view_mode=periodic` is specified, Orb will return an
        incremental day-by-day view of costs. In this case, there will always be a
        one-day difference between `timeframe_start` and `timeframe_end` for the
        timeframes returned. This is a transform on top of the cumulative costs,
        calculated by taking the difference of each timeframe with the last. Note that
        in the above example, the `Total` value would be 0 for the second two data
        points, since the minimum commitment has not yet been hit and each day is not
        contributing anything to the total cost.

        ## Timeframe bounds

        If no timeframe bounds are specified, the response will default to the current
        billing period for the customer's subscription. For subscriptions that have
        ended, this will be the billing period when they were last active. If the
        subscription starts or ends within the timeframe, the response will only include
        windows where the subscription is active.

        As noted above, `timeframe_start` for a given cumulative datapoint is always the
        beginning of the billing period, and `timeframe_end` is incremented one day at a
        time to construct the response. When a timeframe is passed in that is not
        aligned to the current subscription's billing period, the response will contain
        cumulative totals from multiple billing periods.

        Suppose the queried customer has a subscription aligned to the 15th of every
        month. If this endpoint is queried with the date range `2023-06-01` -
        `2023-07-01`, the first data point will represent about half a billing period's
        worth of costs, accounting for accruals from the start of the billing period and
        inclusive of the first day of the timeframe
        (`timeframe_start = 2023-05-15 00:00:00`, `timeframe_end = 2023-06-02 00:00:00`)

        | datapoint index | timeframe_start | timeframe_end |
        | --------------- | --------------- | ------------- |
        | 0               | 2023-05-15      | 2023-06-02    |
        | 1               | 2023-05-15      | 2023-06-03    |
        | 2               | ...             | ...           |
        | 3               | 2023-05-15      | 2023-06-14    |
        | 4               | 2023-06-15      | 2023-06-16    |
        | 5               | 2023-06-15      | 2023-06-17    |
        | 6               | ...             | ...           |
        | 7               | 2023-06-15      | 2023-07-01    |

        You can see this sliced timeframe visualized
        [here](https://i.imgur.com/TXhYgme.png).

        ## Grouping by custom attributes

        In order to view costs grouped by a specific _attribute_ that each event is
        tagged with (i.e. `cluster`), you can additionally specify a `group_by` key. The
        `group_by` key denotes the event property on which to group.

        When returning grouped costs, a separate `price_group` object in the
        `per_price_costs` array is returned for each value of the `group_by` key present
        in your events. The `subtotal` value of the `per_price_costs` object is the sum
        of each `price_group`'s total.

        Orb expects events will contain values in the `properties` dictionary that
        correspond to the `group_by` key specified. By default, Orb will return a `null`
        group (i.e. events that match the metric but do not have the key set).
        Currently, it is only possible to view costs grouped by a single attribute at a
        time.

        ### Matrix prices

        When a price uses matrix pricing, it's important to view costs grouped by those
        matrix dimensions. Orb will return `price_groups` with the `grouping_key` and
        `secondary_grouping_key` based on the matrix price definition, for each
        `grouping_value` and `secondary_grouping_value` available.

        Args:
          group_by: Groups per-price costs by the key provided.

          timeframe_end: Costs returned are exclusive of `timeframe_end`.

          timeframe_start: Costs returned are inclusive of `timeframe_start`.

          view_mode: Controls whether Orb returns cumulative costs since the start of the billing
              period, or incremental day-by-day costs. If your customer has minimums or
              discounts, it's strongly recommended that you use the default cumulative
              behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/customers/{customer_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "group_by": group_by,
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                        "view_mode": view_mode,
                    },
                    cost_list_params.CostListParams,
                ),
            ),
            cast_to=CostListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: Optional[str],
        *,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        timeframe_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        view_mode: Optional[Literal["periodic", "cumulative"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CostListByExternalIDResponse:
        """
        This endpoint is used to fetch a day-by-day snapshot of a customer's costs in
        Orb, calculated by applying pricing information to the underlying usage (see the
        [subscription usage endpoint](fetch-subscription-usage.api.mdx) to fetch usage
        per metric, in usage units rather than a currency).

        This endpoint can be leveraged for internal tooling and to provide a more
        transparent billing experience for your end users:

        1. Understand the cost breakdown per line item historically and in real-time for
           the current billing period.
        2. Provide customer visibility into how different services are contributing to
           the overall invoice with a per-day timeseries (as compared to the
           [upcoming invoice](fetch-upcoming-invoice) resource, which represents a
           snapshot for the current period).
        3. Assess how minimums and discounts affect your customers by teasing apart
           costs directly as a result of usage, as opposed to minimums and discounts at
           the plan and price level.
        4. Gain insight into key customer health metrics, such as the percent
           utilization of the minimum committed spend.

        ## Fetching subscriptions

        By default, this endpoint fetches the currently active subscription for the
        customer, and returns cost information for the subscription's current billing
        period, broken down by each participating price. If there are no currently
        active subscriptions, this will instead default to the most recently active
        subscription or return an empty series if none are found. For example, if your
        plan charges for compute hours, job runs, and data syncs, then this endpoint
        would provide a daily breakdown of your customer's cost for each of those axes.

        If timeframe bounds are specified, Orb fetches all subscriptions that were
        active in that timeframe. If two subscriptions overlap on a single day, costs
        from each price will be summed, and prices for both subscriptions will be
        included in the breakdown.

        ## Prepaid plans

        For plans that include prices which deduct credits rather than accrue in-arrears
        charges in a billable currency, this endpoint will return the total deduction
        amount, in credits, for the specified timeframe.

        ## Cumulative subtotals and totals

        Since the subtotal and total must factor in any billing-period level discounts
        and minimums, it's most meaningful to consider costs relative to the start of
        the subscription's billing period. As a result, by default this endpoint returns
        cumulative totals since the beginning of the billing period. In particular, the
        `timeframe_start` of a returned timeframe window is _always_ the beginning of
        the billing period and `timeframe_end` is incremented one day at a time to build
        the result.

        A customer that uses a few API calls a day but has a minimum commitment might
        exhibit the following pattern for their subtotal and total in the first few days
        of the month. Here, we assume that each API call is $2.50, the customer's plan
        has a monthly minimum of $50 for this price, and that the subscription's billing
        period bounds are aligned to the first of the month:

        | timeframe_start | timeframe_end | Cumulative usage | Subtotal | Total (incl. commitment) |
        | --------------- | ------------- | ---------------- | -------- | ------------------------ |
        | 2023-02-01      | 2023-02-02    | 9                | $22.50   | $50.00                   |
        | 2023-02-01      | 2023-02-03    | 19               | $47.50   | $50.00                   |
        | 2023-02-01      | 2023-02-04    | 20               | $50.00   | $50.00                   |
        | 2023-02-01      | 2023-02-05    | 28               | $70.00   | $70.00                   |
        | 2023-02-01      | 2023-02-06    | 36               | $90.00   | $90.00                   |

        ### Periodic values

        When the query parameter `view_mode=periodic` is specified, Orb will return an
        incremental day-by-day view of costs. In this case, there will always be a
        one-day difference between `timeframe_start` and `timeframe_end` for the
        timeframes returned. This is a transform on top of the cumulative costs,
        calculated by taking the difference of each timeframe with the last. Note that
        in the above example, the `Total` value would be 0 for the second two data
        points, since the minimum commitment has not yet been hit and each day is not
        contributing anything to the total cost.

        ## Timeframe bounds

        If no timeframe bounds are specified, the response will default to the current
        billing period for the customer's subscription. For subscriptions that have
        ended, this will be the billing period when they were last active. If the
        subscription starts or ends within the timeframe, the response will only include
        windows where the subscription is active.

        As noted above, `timeframe_start` for a given cumulative datapoint is always the
        beginning of the billing period, and `timeframe_end` is incremented one day at a
        time to construct the response. When a timeframe is passed in that is not
        aligned to the current subscription's billing period, the response will contain
        cumulative totals from multiple billing periods.

        Suppose the queried customer has a subscription aligned to the 15th of every
        month. If this endpoint is queried with the date range `2023-06-01` -
        `2023-07-01`, the first data point will represent about half a billing period's
        worth of costs, accounting for accruals from the start of the billing period and
        inclusive of the first day of the timeframe
        (`timeframe_start = 2023-05-15 00:00:00`, `timeframe_end = 2023-06-02 00:00:00`)

        | datapoint index | timeframe_start | timeframe_end |
        | --------------- | --------------- | ------------- |
        | 0               | 2023-05-15      | 2023-06-02    |
        | 1               | 2023-05-15      | 2023-06-03    |
        | 2               | ...             | ...           |
        | 3               | 2023-05-15      | 2023-06-14    |
        | 4               | 2023-06-15      | 2023-06-16    |
        | 5               | 2023-06-15      | 2023-06-17    |
        | 6               | ...             | ...           |
        | 7               | 2023-06-15      | 2023-07-01    |

        You can see this sliced timeframe visualized
        [here](https://i.imgur.com/TXhYgme.png).

        ## Grouping by custom attributes

        In order to view costs grouped by a specific _attribute_ that each event is
        tagged with (i.e. `cluster`), you can additionally specify a `group_by` key. The
        `group_by` key denotes the event property on which to group.

        When returning grouped costs, a separate `price_group` object in the
        `per_price_costs` array is returned for each value of the `group_by` key present
        in your events. The `subtotal` value of the `per_price_costs` object is the sum
        of each `price_group`'s total.

        Orb expects events will contain values in the `properties` dictionary that
        correspond to the `group_by` key specified. By default, Orb will return a `null`
        group (i.e. events that match the metric but do not have the key set).
        Currently, it is only possible to view costs grouped by a single attribute at a
        time.

        ### Matrix prices

        When a price uses matrix pricing, it's important to view costs grouped by those
        matrix dimensions. Orb will return `price_groups` with the `grouping_key` and
        `secondary_grouping_key` based on the matrix price definition, for each
        `grouping_value` and `secondary_grouping_value` available.

        Args:
          group_by: Groups per-price costs by the key provided.

          timeframe_end: Costs returned are exclusive of `timeframe_end`.

          timeframe_start: Costs returned are inclusive of `timeframe_start`.

          view_mode: Controls whether Orb returns cumulative costs since the start of the billing
              period, or incremental day-by-day costs. If your customer has minimums or
              discounts, it's strongly recommended that you use the default cumulative
              behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/customers/external_customer_id/{external_customer_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "group_by": group_by,
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                        "view_mode": view_mode,
                    },
                    cost_list_by_external_id_params.CostListByExternalIDParams,
                ),
            ),
            cast_to=CostListByExternalIDResponse,
        )


class AsyncCosts(AsyncAPIResource):
    with_raw_response: AsyncCostsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCostsWithRawResponse(self)

    async def list(
        self,
        customer_id: Optional[str],
        *,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        timeframe_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        view_mode: Optional[Literal["periodic", "cumulative"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CostListResponse:
        """
        This endpoint is used to fetch a day-by-day snapshot of a customer's costs in
        Orb, calculated by applying pricing information to the underlying usage (see the
        [subscription usage endpoint](fetch-subscription-usage.api.mdx) to fetch usage
        per metric, in usage units rather than a currency).

        This endpoint can be leveraged for internal tooling and to provide a more
        transparent billing experience for your end users:

        1. Understand the cost breakdown per line item historically and in real-time for
           the current billing period.
        2. Provide customer visibility into how different services are contributing to
           the overall invoice with a per-day timeseries (as compared to the
           [upcoming invoice](fetch-upcoming-invoice) resource, which represents a
           snapshot for the current period).
        3. Assess how minimums and discounts affect your customers by teasing apart
           costs directly as a result of usage, as opposed to minimums and discounts at
           the plan and price level.
        4. Gain insight into key customer health metrics, such as the percent
           utilization of the minimum committed spend.

        ## Fetching subscriptions

        By default, this endpoint fetches the currently active subscription for the
        customer, and returns cost information for the subscription's current billing
        period, broken down by each participating price. If there are no currently
        active subscriptions, this will instead default to the most recently active
        subscription or return an empty series if none are found. For example, if your
        plan charges for compute hours, job runs, and data syncs, then this endpoint
        would provide a daily breakdown of your customer's cost for each of those axes.

        If timeframe bounds are specified, Orb fetches all subscriptions that were
        active in that timeframe. If two subscriptions overlap on a single day, costs
        from each price will be summed, and prices for both subscriptions will be
        included in the breakdown.

        ## Prepaid plans

        For plans that include prices which deduct credits rather than accrue in-arrears
        charges in a billable currency, this endpoint will return the total deduction
        amount, in credits, for the specified timeframe.

        ## Cumulative subtotals and totals

        Since the subtotal and total must factor in any billing-period level discounts
        and minimums, it's most meaningful to consider costs relative to the start of
        the subscription's billing period. As a result, by default this endpoint returns
        cumulative totals since the beginning of the billing period. In particular, the
        `timeframe_start` of a returned timeframe window is _always_ the beginning of
        the billing period and `timeframe_end` is incremented one day at a time to build
        the result.

        A customer that uses a few API calls a day but has a minimum commitment might
        exhibit the following pattern for their subtotal and total in the first few days
        of the month. Here, we assume that each API call is $2.50, the customer's plan
        has a monthly minimum of $50 for this price, and that the subscription's billing
        period bounds are aligned to the first of the month:

        | timeframe_start | timeframe_end | Cumulative usage | Subtotal | Total (incl. commitment) |
        | --------------- | ------------- | ---------------- | -------- | ------------------------ |
        | 2023-02-01      | 2023-02-02    | 9                | $22.50   | $50.00                   |
        | 2023-02-01      | 2023-02-03    | 19               | $47.50   | $50.00                   |
        | 2023-02-01      | 2023-02-04    | 20               | $50.00   | $50.00                   |
        | 2023-02-01      | 2023-02-05    | 28               | $70.00   | $70.00                   |
        | 2023-02-01      | 2023-02-06    | 36               | $90.00   | $90.00                   |

        ### Periodic values

        When the query parameter `view_mode=periodic` is specified, Orb will return an
        incremental day-by-day view of costs. In this case, there will always be a
        one-day difference between `timeframe_start` and `timeframe_end` for the
        timeframes returned. This is a transform on top of the cumulative costs,
        calculated by taking the difference of each timeframe with the last. Note that
        in the above example, the `Total` value would be 0 for the second two data
        points, since the minimum commitment has not yet been hit and each day is not
        contributing anything to the total cost.

        ## Timeframe bounds

        If no timeframe bounds are specified, the response will default to the current
        billing period for the customer's subscription. For subscriptions that have
        ended, this will be the billing period when they were last active. If the
        subscription starts or ends within the timeframe, the response will only include
        windows where the subscription is active.

        As noted above, `timeframe_start` for a given cumulative datapoint is always the
        beginning of the billing period, and `timeframe_end` is incremented one day at a
        time to construct the response. When a timeframe is passed in that is not
        aligned to the current subscription's billing period, the response will contain
        cumulative totals from multiple billing periods.

        Suppose the queried customer has a subscription aligned to the 15th of every
        month. If this endpoint is queried with the date range `2023-06-01` -
        `2023-07-01`, the first data point will represent about half a billing period's
        worth of costs, accounting for accruals from the start of the billing period and
        inclusive of the first day of the timeframe
        (`timeframe_start = 2023-05-15 00:00:00`, `timeframe_end = 2023-06-02 00:00:00`)

        | datapoint index | timeframe_start | timeframe_end |
        | --------------- | --------------- | ------------- |
        | 0               | 2023-05-15      | 2023-06-02    |
        | 1               | 2023-05-15      | 2023-06-03    |
        | 2               | ...             | ...           |
        | 3               | 2023-05-15      | 2023-06-14    |
        | 4               | 2023-06-15      | 2023-06-16    |
        | 5               | 2023-06-15      | 2023-06-17    |
        | 6               | ...             | ...           |
        | 7               | 2023-06-15      | 2023-07-01    |

        You can see this sliced timeframe visualized
        [here](https://i.imgur.com/TXhYgme.png).

        ## Grouping by custom attributes

        In order to view costs grouped by a specific _attribute_ that each event is
        tagged with (i.e. `cluster`), you can additionally specify a `group_by` key. The
        `group_by` key denotes the event property on which to group.

        When returning grouped costs, a separate `price_group` object in the
        `per_price_costs` array is returned for each value of the `group_by` key present
        in your events. The `subtotal` value of the `per_price_costs` object is the sum
        of each `price_group`'s total.

        Orb expects events will contain values in the `properties` dictionary that
        correspond to the `group_by` key specified. By default, Orb will return a `null`
        group (i.e. events that match the metric but do not have the key set).
        Currently, it is only possible to view costs grouped by a single attribute at a
        time.

        ### Matrix prices

        When a price uses matrix pricing, it's important to view costs grouped by those
        matrix dimensions. Orb will return `price_groups` with the `grouping_key` and
        `secondary_grouping_key` based on the matrix price definition, for each
        `grouping_value` and `secondary_grouping_value` available.

        Args:
          group_by: Groups per-price costs by the key provided.

          timeframe_end: Costs returned are exclusive of `timeframe_end`.

          timeframe_start: Costs returned are inclusive of `timeframe_start`.

          view_mode: Controls whether Orb returns cumulative costs since the start of the billing
              period, or incremental day-by-day costs. If your customer has minimums or
              discounts, it's strongly recommended that you use the default cumulative
              behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/customers/{customer_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "group_by": group_by,
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                        "view_mode": view_mode,
                    },
                    cost_list_params.CostListParams,
                ),
            ),
            cast_to=CostListResponse,
        )

    async def list_by_external_id(
        self,
        external_customer_id: Optional[str],
        *,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        timeframe_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        view_mode: Optional[Literal["periodic", "cumulative"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CostListByExternalIDResponse:
        """
        This endpoint is used to fetch a day-by-day snapshot of a customer's costs in
        Orb, calculated by applying pricing information to the underlying usage (see the
        [subscription usage endpoint](fetch-subscription-usage.api.mdx) to fetch usage
        per metric, in usage units rather than a currency).

        This endpoint can be leveraged for internal tooling and to provide a more
        transparent billing experience for your end users:

        1. Understand the cost breakdown per line item historically and in real-time for
           the current billing period.
        2. Provide customer visibility into how different services are contributing to
           the overall invoice with a per-day timeseries (as compared to the
           [upcoming invoice](fetch-upcoming-invoice) resource, which represents a
           snapshot for the current period).
        3. Assess how minimums and discounts affect your customers by teasing apart
           costs directly as a result of usage, as opposed to minimums and discounts at
           the plan and price level.
        4. Gain insight into key customer health metrics, such as the percent
           utilization of the minimum committed spend.

        ## Fetching subscriptions

        By default, this endpoint fetches the currently active subscription for the
        customer, and returns cost information for the subscription's current billing
        period, broken down by each participating price. If there are no currently
        active subscriptions, this will instead default to the most recently active
        subscription or return an empty series if none are found. For example, if your
        plan charges for compute hours, job runs, and data syncs, then this endpoint
        would provide a daily breakdown of your customer's cost for each of those axes.

        If timeframe bounds are specified, Orb fetches all subscriptions that were
        active in that timeframe. If two subscriptions overlap on a single day, costs
        from each price will be summed, and prices for both subscriptions will be
        included in the breakdown.

        ## Prepaid plans

        For plans that include prices which deduct credits rather than accrue in-arrears
        charges in a billable currency, this endpoint will return the total deduction
        amount, in credits, for the specified timeframe.

        ## Cumulative subtotals and totals

        Since the subtotal and total must factor in any billing-period level discounts
        and minimums, it's most meaningful to consider costs relative to the start of
        the subscription's billing period. As a result, by default this endpoint returns
        cumulative totals since the beginning of the billing period. In particular, the
        `timeframe_start` of a returned timeframe window is _always_ the beginning of
        the billing period and `timeframe_end` is incremented one day at a time to build
        the result.

        A customer that uses a few API calls a day but has a minimum commitment might
        exhibit the following pattern for their subtotal and total in the first few days
        of the month. Here, we assume that each API call is $2.50, the customer's plan
        has a monthly minimum of $50 for this price, and that the subscription's billing
        period bounds are aligned to the first of the month:

        | timeframe_start | timeframe_end | Cumulative usage | Subtotal | Total (incl. commitment) |
        | --------------- | ------------- | ---------------- | -------- | ------------------------ |
        | 2023-02-01      | 2023-02-02    | 9                | $22.50   | $50.00                   |
        | 2023-02-01      | 2023-02-03    | 19               | $47.50   | $50.00                   |
        | 2023-02-01      | 2023-02-04    | 20               | $50.00   | $50.00                   |
        | 2023-02-01      | 2023-02-05    | 28               | $70.00   | $70.00                   |
        | 2023-02-01      | 2023-02-06    | 36               | $90.00   | $90.00                   |

        ### Periodic values

        When the query parameter `view_mode=periodic` is specified, Orb will return an
        incremental day-by-day view of costs. In this case, there will always be a
        one-day difference between `timeframe_start` and `timeframe_end` for the
        timeframes returned. This is a transform on top of the cumulative costs,
        calculated by taking the difference of each timeframe with the last. Note that
        in the above example, the `Total` value would be 0 for the second two data
        points, since the minimum commitment has not yet been hit and each day is not
        contributing anything to the total cost.

        ## Timeframe bounds

        If no timeframe bounds are specified, the response will default to the current
        billing period for the customer's subscription. For subscriptions that have
        ended, this will be the billing period when they were last active. If the
        subscription starts or ends within the timeframe, the response will only include
        windows where the subscription is active.

        As noted above, `timeframe_start` for a given cumulative datapoint is always the
        beginning of the billing period, and `timeframe_end` is incremented one day at a
        time to construct the response. When a timeframe is passed in that is not
        aligned to the current subscription's billing period, the response will contain
        cumulative totals from multiple billing periods.

        Suppose the queried customer has a subscription aligned to the 15th of every
        month. If this endpoint is queried with the date range `2023-06-01` -
        `2023-07-01`, the first data point will represent about half a billing period's
        worth of costs, accounting for accruals from the start of the billing period and
        inclusive of the first day of the timeframe
        (`timeframe_start = 2023-05-15 00:00:00`, `timeframe_end = 2023-06-02 00:00:00`)

        | datapoint index | timeframe_start | timeframe_end |
        | --------------- | --------------- | ------------- |
        | 0               | 2023-05-15      | 2023-06-02    |
        | 1               | 2023-05-15      | 2023-06-03    |
        | 2               | ...             | ...           |
        | 3               | 2023-05-15      | 2023-06-14    |
        | 4               | 2023-06-15      | 2023-06-16    |
        | 5               | 2023-06-15      | 2023-06-17    |
        | 6               | ...             | ...           |
        | 7               | 2023-06-15      | 2023-07-01    |

        You can see this sliced timeframe visualized
        [here](https://i.imgur.com/TXhYgme.png).

        ## Grouping by custom attributes

        In order to view costs grouped by a specific _attribute_ that each event is
        tagged with (i.e. `cluster`), you can additionally specify a `group_by` key. The
        `group_by` key denotes the event property on which to group.

        When returning grouped costs, a separate `price_group` object in the
        `per_price_costs` array is returned for each value of the `group_by` key present
        in your events. The `subtotal` value of the `per_price_costs` object is the sum
        of each `price_group`'s total.

        Orb expects events will contain values in the `properties` dictionary that
        correspond to the `group_by` key specified. By default, Orb will return a `null`
        group (i.e. events that match the metric but do not have the key set).
        Currently, it is only possible to view costs grouped by a single attribute at a
        time.

        ### Matrix prices

        When a price uses matrix pricing, it's important to view costs grouped by those
        matrix dimensions. Orb will return `price_groups` with the `grouping_key` and
        `secondary_grouping_key` based on the matrix price definition, for each
        `grouping_value` and `secondary_grouping_value` available.

        Args:
          group_by: Groups per-price costs by the key provided.

          timeframe_end: Costs returned are exclusive of `timeframe_end`.

          timeframe_start: Costs returned are inclusive of `timeframe_start`.

          view_mode: Controls whether Orb returns cumulative costs since the start of the billing
              period, or incremental day-by-day costs. If your customer has minimums or
              discounts, it's strongly recommended that you use the default cumulative
              behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/customers/external_customer_id/{external_customer_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "group_by": group_by,
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                        "view_mode": view_mode,
                    },
                    cost_list_by_external_id_params.CostListByExternalIDParams,
                ),
            ),
            cast_to=CostListByExternalIDResponse,
        )


class CostsWithRawResponse:
    def __init__(self, costs: Costs) -> None:
        self.list = to_raw_response_wrapper(
            costs.list,
        )
        self.list_by_external_id = to_raw_response_wrapper(
            costs.list_by_external_id,
        )


class AsyncCostsWithRawResponse:
    def __init__(self, costs: AsyncCosts) -> None:
        self.list = async_to_raw_response_wrapper(
            costs.list,
        )
        self.list_by_external_id = async_to_raw_response_wrapper(
            costs.list_by_external_id,
        )
