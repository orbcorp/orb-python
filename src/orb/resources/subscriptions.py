# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Union, Optional, cast
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import (
    Subscription,
    SubscriptionUsage,
    SubscriptionFetchCostsResponse,
    SubscriptionFetchScheduleResponse,
    subscription_list_params,
    subscription_cancel_params,
    subscription_create_params,
    subscription_fetch_costs_params,
    subscription_fetch_usage_params,
    subscription_trigger_phase_params,
    subscription_fetch_schedule_params,
    subscription_price_intervals_params,
    subscription_schedule_plan_change_params,
    subscription_update_fixed_fee_quantity_params,
    subscription_unschedule_fixed_fee_quantity_updates_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from .._client import Orb, AsyncOrb

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    with_raw_response: SubscriptionsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = SubscriptionsWithRawResponse(self)

    def create(
        self,
        *,
        align_billing_with_subscription_start_date: bool | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        aws_region: Optional[str] | NotGiven = NOT_GIVEN,
        coupon_redemption_code: Optional[str] | NotGiven = NOT_GIVEN,
        credits_overage_rate: Optional[float] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        default_invoice_memo: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_marketplace: Optional[Literal["google", "aws", "azure"]] | NotGiven = NOT_GIVEN,
        external_marketplace_reporting_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        initial_phase_order: Optional[int] | NotGiven = NOT_GIVEN,
        invoicing_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        net_terms: Optional[int] | NotGiven = NOT_GIVEN,
        per_credit_overage_amount: Optional[str] | NotGiven = NOT_GIVEN,
        plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        price_overrides: Optional[List[subscription_create_params.PriceOverride]] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """A subscription represents the purchase of a plan by a customer.

        The customer is
        identified by either the `customer_id` or the `external_customer_id`, and
        exactly one of these fields must be provided.

        By default, subscriptions begin on the day that they're created and renew
        automatically for each billing cycle at the cadence that's configured in the
        plan definition.

        The default configuration for subscriptions in Orb is **In-advance billing** and
        **Beginning of month alignment** (see
        [Subscription](../guides/concepts#subscription) for more details).

        In order to change the alignment behavior, Orb also supports billing
        subscriptions on the day of the month they are created. If
        `align_billing_with_subscription_start_date = true` is specified, subscriptions
        have billing cycles that are aligned with their `start_date`. For example, a
        subscription that begins on January 15th will have a billing cycle from January
        15th to February 15th. Every subsequent billing cycle will continue to start and
        invoice on the 15th.

        If the "day" value is greater than the number of days in the month, the next
        billing cycle will start at the end of the month. For example, if the start_date
        is January 31st, the next billing cycle will start on February 28th.

        If a customer was created with a currency, Orb only allows subscribing the
        customer to a plan with a matching `invoicing_currency`. If the customer does
        not have a currency set, on subscription creation, we set the customer's
        currency to be the `invoicing_currency` of the plan.

        ## Price overrides

        Price overrides are used to update some or all prices in a plan for the specific
        subscription being created. This is useful when a new customer has negotiated
        one or more different prices for a specific plan than the plan's default prices.
        Any type of price can be overridden, if the correct data is provided. The
        billable metric, cadence, type, and name of a price can not be overridden.

        To override prices, provide a list of objects with the key `price_overrides`.
        The price object in the list of overrides is expected to contain the existing
        price id, the `model_type` and config value in the format below. The specific
        numerical values can be updated, but the config value and `model_type` must
        match the existing price that is being overridden

        ### Request format for price overrides

        Orb supports a few different pricing models out of the box. The `model_type`
        field determines the key for the configuration object that is present.

        ### Unit pricing

        With unit pricing, each unit costs a fixed amount.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          }
          ...
        }
        ```

        ### Tiered pricing

        In tiered pricing, the cost of a given unit depends on the tier range that it
        falls into, where each tier range is defined by an upper and lower bound. For
        example, the first ten units may cost $0.50 each and all units thereafter may
        cost $0.10 each. Tiered prices can be overridden with a new number of tiers or
        new values for `first_unit`, `last_unit`, or `unit_amount`.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "tiered",
          "tiered_config": {
            "tiers": [
              {
                "first_unit":"1",
                "last_unit": "10",
                "unit_amount": "0.50"
              },
              {
                "first_unit": "10",
                "last_unit": null,
                "unit_amount": "0.10"
              }
            ]
          }
          ...
        }
        ```

        ### Bulk pricing

        Bulk pricing applies when the number of units determine the cost of _all_ units.
        For example, if you've bought less than 10 units, they may each be $0.50 for a
        total of $5.00. Once you've bought more than 10 units, all units may now be
        priced at $0.40 (i.e. 101 units total would be $40.40). Bulk prices can be
        overridden with a new number of tiers or new values for `maximum_units`, or
        `unit_amount`.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "bulk",
          "bulk_config": {
            "tiers": [
              {
                "maximum_units": "10",
                "unit_amount": "0.50"
              },
              {
                "maximum_units": "1000",
                "unit_amount": "0.40"
              }
            ]
          }
          ...
        }
        ```

        ### Package pricing

        Package pricing defines the size or granularity of a unit for billing purposes.
        For example, if the package size is set to 5, then 4 units will be billed as 5
        and 6 units will be billed at 10.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "package",
          "package_config": {
            "package_amount": "0.80",
            "package_size": 10
          }
          ...
        }
        ```

        ### BPS pricing

        BPS pricing specifies a per-event (e.g. per-payment) rate in one hundredth of a
        percent (the number of basis points to charge), as well as a cap per event to
        assess. For example, this would allow you to assess a fee of 0.25% on every
        payment you process, with a maximum charge of $25 per payment.

        ```json
        {
          ...
          "id": "price_id"
          "model_type": "bps",
          "bps_config": {
            "bps": 125,
            "per_event_cap": "11.00"
          }
          ...
        }
        ```

        ### Bulk BPS pricing

        Bulk BPS pricing specifies BPS parameters in a tiered manner, dependent on the
        total quantity across all events. Similar to bulk pricing, the BPS parameters of
        a given event depends on the tier range that the billing period falls into. Each
        tier range is defined by an upper and lower bound. For example, after $1.5M of
        payment volume is reached, each individual payment may have a lower cap or a
        smaller take-rate.

        ```json
        {
          ...
          "id": "price_id"
          "model_type": "bulk_bps",
          "bulk_bps_config": {
            "tiers": [
              {
                "minimum_amount": "0.00",
                "maximum_amount": "1000000.00",
                "bps": 125,
                "per_event_cap": "19.00"
              },
              {
                "minimum_amount":"1000000.00",
                "maximum_amount": null,
                "bps": 115,
                "per_event_cap": "4.00"
              }
            ]
          }
        ...
        }
        ```

        ### Tiered BPS pricing

        Tiered BPS pricing specifies BPS parameters in a graduated manner, where an
        event's applicable parameter is a function of its marginal addition to the
        period total. Similar to tiered pricing, the BPS parameters of a given event
        depends on the tier range that it falls into, where each tier range is defined
        by an upper and lower bound. For example, the first few payments may have a 0.8
        BPS take-rate and all payments after a specific volume may incur a take-rate of
        0.5 BPS each.

        ```json
        {
          ...
          "id": "price_id"
          "model_type": "tiered_bps",
          "tiered_bps_config": {
            "tiers": [
              {
                "minimum_amount": "0.00",
                "maximum_amount": "1000000.00",
                "bps": 125,
                "per_event_cap": "19.00"
              },
              {
                "minimum_amount":"1000000",
                "maximum_amount": null,
                "bps": 115,
                "per_event_cap": "4.00"
              }
            ]
          }
          ...
        }
        ```

        ### Matrix pricing

        Matrix pricing defines a set of unit prices in a one or two-dimensional matrix.
        `dimensions` defines the two event property values evaluated in this pricing
        model. In a one-dimensional matrix, the second value is `null`. Every
        configuration has a list of `matrix_values` which give the unit prices for
        specified property values. In a one-dimensional matrix, the matrix values will
        have `dimension_values` where the second value of the pair is null. If an event
        does not match any of the dimension values in the matrix, it will resort to the
        `default_unit_amount`.

        ```json
        {
          ...
          "model_type": "matrix",
          "matrix_config": {
            "default_unit_amount": "3.00",
            "dimensions": [
              "cluster_name",
              "region"
            ],
            "matrix_values": [
              {
                "dimension_values": [
                  "alpha",
                  "west"
                ],
                "unit_amount": "2.00"
              },
              ...
            ]
          }
        }
        ```

        ### Fixed fees

        Fixed fees follow unit pricing, and also have an additional parameter
        `fixed_price_quantity` that indicates how many of a fixed fee that should be
        applied for a subscription. This parameter defaults to 1.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "2.00"
          },
          "fixed_price_quantity": 3.0
          ...
        }
        ```

        ## Maximums and Minimums

        Minimums and maximums, much like price overrides, can be useful when a new
        customer has negotiated a new or different minimum or maximum spend cap than the
        default for a given price. If one exists for a price and null is provided for
        the minimum/maximum override on creation, then there will be no minimum/maximum
        on the new subscription. If no value is provided, then the default price maximum
        or minimum is used.

        To add a minimum for a specific price, add `minimum_amount` to the specific
        price in the `price_overrides` object.

        To add a maximum for a specific price, add `maximum_amount` to the specific
        price in the `price_overrides` object.

        ### Minimum override example

        Price minimum override example:

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          },
          "minimum_amount": "100.00"
          ...
        }
        ```

        Removing an existing minimum example

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          },
          "minimum_amount": null
          ...
        }
        ```

        ## Discounts

        Discounts, like price overrides, can be useful when a new customer has
        negotiated a new or different discount than the default for a price. A single
        price price can have at most one discount. If a discount exists for a price and
        a null discount is provided on creation, then there will be no discount on the
        new subscription.

        To add a discount for a specific price, add `discount` to the price in the
        `price_overrides` object. Discount should be a dictionary of the format:

        ```ts
        {
          "discount_type": "amount" | "percentage" | "usage",
          "amount_discount": string,
          "percentage_discount": string,
          "usage_discount": string
        }
        ```

        where either `amount_discount`, `percentage_discount`, or `usage_discount` is
        provided.

        Price discount example

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          },
          "discount": {"discount_type": "amount", "amount_discount": "175"},
        }
        ```

        Removing an existing discount example

        ```json
        {
          "customer_id": "customer_id",
          "plan_id": "plan_id",
          "discount": null,
          "price_overrides": [ ... ]
          ...
        }
        ```

        ## Threshold Billing

        Orb supports invoicing for a subscription when a preconfigured usage threshold
        is hit. To enable threshold billing, pass in an `invoicing_threshold`, which is
        specified in the subscription's invoicing currency, when creating a
        subscription. E.g. pass in `10.00` to issue an invoice when usage amounts hit
        $10.00 for a subscription that invoices in USD.

        Args:
          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/subscriptions",
            body=maybe_transform(
                {
                    "align_billing_with_subscription_start_date": align_billing_with_subscription_start_date,
                    "auto_collection": auto_collection,
                    "aws_region": aws_region,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "customer_id": customer_id,
                    "default_invoice_memo": default_invoice_memo,
                    "end_date": end_date,
                    "external_customer_id": external_customer_id,
                    "external_marketplace": external_marketplace,
                    "external_marketplace_reporting_id": external_marketplace_reporting_id,
                    "external_plan_id": external_plan_id,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "metadata": metadata,
                    "net_terms": net_terms,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "price_overrides": price_overrides,
                    "start_date": start_date,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Optional[Literal["active", "ended", "upcoming"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Subscription]:
        """
        This endpoint returns a list of all subscriptions for an account as a
        [paginated](../reference/pagination) list, ordered starting from the most
        recently created subscription. For a full discussion of the subscription
        resource, see [Subscription](../guides/concepts#subscription).

        Subscriptions can be filtered to a single customer by passing in the
        `customer_id` query parameter or the `external_customer_id` query parameter.

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
            "/subscriptions",
            page=SyncPage[Subscription],
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
                        "customer_id": customer_id,
                        "external_customer_id": external_customer_id,
                        "limit": limit,
                        "status": status,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=Subscription,
        )

    def cancel(
        self,
        subscription_id: str,
        *,
        cancel_option: Literal["end_of_subscription_term", "immediate", "requested_date"],
        cancellation_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """This endpoint can be used to cancel an existing subscription.

        It returns the
        serialized subscription object with an `end_date` parameter that signifies when
        the subscription will transition to an ended state.

        The body parameter `cancel_option` determines the cancellation behavior. Orb
        supports three cancellation options:

        - `end_of_subscription_term`: stops the subscription from auto-renewing.
          Subscriptions that have been cancelled with this option can still incur
          charges for the remainder of their term:

          - Issuing this cancellation request for a monthly subscription will keep the
            subscription active until the start of the subsequent month, and potentially
            issue an invoice for any usage charges incurred in the intervening period.
          - Issuing this cancellation request for a quarterly subscription will keep the
            subscription active until the end of the quarter and potentially issue an
            invoice for any usage charges incurred in the intervening period.
          - Issuing this cancellation request for a yearly subscription will keep the
            subscription active for the full year. For example, a yearly subscription
            starting on 2021-11-01 and cancelled on 2021-12-08 will remain active until
            2022-11-01 and potentially issue charges in the intervening months for any
            recurring monthly usage charges in its plan.
          - **Note**: If a subscription's plan contains prices with difference cadences,
            the end of term date will be determined by the largest cadence value. For
            example, cancelling end of term for a subscription with a quarterly fixed
            fee with a monthly usage fee will result in the subscription ending at the
            end of the quarter.

        - `immediate`: ends the subscription immediately, setting the `end_date` to the
          current time:

          - Subscriptions that have been cancelled with this option will be invoiced
            immediately. This invoice will include any usage fees incurred in the
            billing period up to the cancellation, along with any prorated recurring
            fees for the billing period, if applicable.
          - **Note**: If the subscription has a recurring fee that was paid in-advance,
            the prorated amount for the remaining time period will be added to the
            [customer's balance](list-balance-transactions) upon immediate cancellation.
            However, if the customer is ineligible to use the customer balance, the
            subscription cannot be cancelled immediately.

        - `requested_date`: ends the subscription on a specified date, which requires a
          `cancellation_date` to be passed in. If no timezone is provided, the
          customer's timezone is used. For example, a subscription starting on January
          1st with a monthly price can be set to be cancelled on the first of any month
          after January 1st (e.g. March 1st, April 1st, May 1st). A subscription with
          multiple prices with different cadences defines the "term" to be the highest
          cadence of the prices.

        Upcoming subscriptions are only eligible for immediate cancellation, which will
        set the `end_date` equal to the `start_date` upon cancellation.

        ## Backdated cancellations

        Orb allows you to cancel a subscription in the past as long as there are no paid
        invoices between the `requested_date` and the current time. If the cancellation
        is after the latest issued invoice, Orb will generate a balance refund for the
        current period. If the cancellation is before the most recently issued invoice,
        Orb will void the intervening invoice and generate a new one based on the new
        dates for the subscription. See the section on
        [cancellation behaviors](../guides/product-catalog/creating-subscriptions.md#cancellation-behaviors).

        Args:
          cancel_option: Determines the timing of subscription cancellation

          cancellation_date: The date that the cancellation should take effect. This parameter can only be
              passed if the `cancel_option` is `requested_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/cancel",
            body=maybe_transform(
                {
                    "cancel_option": cancel_option,
                    "cancellation_date": cancellation_date,
                },
                subscription_cancel_params.SubscriptionCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def fetch(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        This endpoint is used to fetch a [Subscription](../guides/concepts#subscription)
        given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    def fetch_costs(
        self,
        subscription_id: str,
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
    ) -> SubscriptionFetchCostsResponse:
        """
        This endpoint is used to fetch a day-by-day snapshot of a subscription's costs
        in Orb, calculated by applying pricing information to the underlying usage (see
        the [subscription usage endpoint](fetch-subscription-usage) to fetch usage per
        metric, in usage units rather than a currency).

        The semantics of this endpoint exactly mirror those of
        [fetching a customer's costs](fetch-customer-costs). Use this endpoint to limit
        your analysis of costs to a specific subscription for the customer (e.g. to
        de-aggregate costs when a customer's subscription has started and stopped on the
        same day).

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
            f"/subscriptions/{subscription_id}/costs",
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
                    subscription_fetch_costs_params.SubscriptionFetchCostsParams,
                ),
            ),
            cast_to=SubscriptionFetchCostsResponse,
        )

    def fetch_schedule(
        self,
        subscription_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        start_date_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[SubscriptionFetchScheduleResponse]:
        """
        This endpoint returns a [paginated](../reference/pagination) list of all plans
        associated with a subscription along with their start and end dates. This list
        contains the subscription's initial plan along with past and future plan
        changes.

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
            f"/subscriptions/{subscription_id}/schedule",
            page=SyncPage[SubscriptionFetchScheduleResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "start_date_gt": start_date_gt,
                        "start_date_gte": start_date_gte,
                        "start_date_lt": start_date_lt,
                        "start_date_lte": start_date_lte,
                    },
                    subscription_fetch_schedule_params.SubscriptionFetchScheduleParams,
                ),
            ),
            model=SubscriptionFetchScheduleResponse,
        )

    def fetch_usage(
        self,
        subscription_id: str,
        *,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        first_dimension_key: Optional[str] | NotGiven = NOT_GIVEN,
        first_dimension_value: Optional[str] | NotGiven = NOT_GIVEN,
        granularity: Optional[Literal["day"]] | NotGiven = NOT_GIVEN,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        second_dimension_key: Optional[str] | NotGiven = NOT_GIVEN,
        second_dimension_value: Optional[str] | NotGiven = NOT_GIVEN,
        timeframe_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        view_mode: Optional[Literal["periodic", "cumulative"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionUsage:
        """This endpoint is used to fetch a subscription's usage in Orb.

        Especially when
        combined with optional query parameters, this endpoint is a powerful way to
        build visualizations on top of Orb's event data and metrics.

        With no query parameters specified, this endpoint returns usage for the
        subscription's _current billing period_ across each billable metric that
        participates in the subscription. Usage quantities returned are the result of
        evaluating the metric definition for the entirety of the customer's billing
        period.

        ### Default response shape

        Orb returns a `data` array with an object corresponding to each billable metric.
        Nested within this object is a `usage` array which has a `quantity` value and a
        corresponding `timeframe_start` and `timeframe_end`. The `quantity` value
        represents the calculated usage value for the billable metric over the specified
        timeframe (inclusive of the `timeframe_start` timestamp and exclusive of the
        `timeframe_end` timestamp).

        Orb will include _every_ window in the response starting from the beginning of
        the billing period, even when there were no events (and therefore no usage) in
        the window. This increases the size of the response but prevents the caller from
        filling in gaps and handling cumbersome time-based logic.

        The query parameters in this endpoint serve to override this behavior and
        provide some key functionality, as listed below. Note that this functionality
        can also be used _in conjunction_ with each other, e.g. to display grouped usage
        on a custom timeframe.

        ## Custom timeframe

        In order to view usage for a custom timeframe rather than the current billing
        period, specify a `timeframe_start` and `timeframe_end`. This will calculate
        quantities for usage incurred between timeframe_start (inclusive) and
        timeframe_end (exclusive), i.e. `[timeframe_start, timeframe_end)`.

        Note:

        - These timestamps must be specified in ISO 8601 format and UTC timezone, e.g.
          `2022-02-01T05:00:00Z`.
        - Both parameters must be specified if either is specified.

        ## Grouping by custom attributes

        In order to view a single metric grouped by a specific _attribute_ that each
        event is tagged with (e.g. `cluster`), you must additionally specify a
        `billable_metric_id` and a `group_by` key. The `group_by` key denotes the event
        property on which to group.

        When returning grouped usage, only usage for `billable_metric_id` is returned,
        and a separate object in the `data` array is returned for each value of the
        `group_by` key present in your events. The `quantity` value is the result of
        evaluating the billable metric for events filtered to a single value of the
        `group_by` key.

        Orb expects that events that match the billable metric will contain values in
        the `properties` dictionary that correspond to the `group_by` key specified. By
        default, Orb will not return a `null` group (i.e. events that match the metric
        but do not have the key set). Currently, it is only possible to view usage
        grouped by a single attribute at a time.

        When viewing grouped usage, Orb uses pagination to limit the response size to
        1000 groups by default. If there are more groups for a given subscription,
        pagination metadata in the response can be used to fetch all of the data.

        The following example shows usage for an "API Requests" billable metric grouped
        by `region`. Note the extra `metric_group` dictionary in the response, which
        provides metadata about the group:

        ```json
        {
            "data": [
                {
                    "usage": [
                        {
                            "quantity": 0.19291,
                            "timeframe_start": "2021-10-01T07:00:00Z",
                            "timeframe_end": "2021-10-02T07:00:00Z",
                        },
                        ...
                    ],
                    "metric_group": {
                        "property_key": "region",
                        "property_value": "asia/pacific"
                    },
                    "billable_metric": {
                        "id": "Fe9pbpMk86xpwdGB",
                        "name": "API Requests"
                    },
                    "view_mode": "periodic"
                },
                ...
            ]
        }
        ```

        ## Windowed usage

        The `granularity` parameter can be used to _window_ the usage `quantity` value
        into periods. When not specified, usage is returned for the entirety of the time
        range.

        When `granularity = day` is specified with a timeframe longer than a day, Orb
        will return a `quantity` value for each full day between `timeframe_start` and
        `timeframe_end`. Note that the days are demarcated by the _customer's local
        midnight_.

        For example, with `timeframe_start = 2022-02-01T05:00:00Z`,
        `timeframe_end = 2022-02-04T01:00:00Z` and `granularity=day`, the following
        windows will be returned for a customer in the `America/Los_Angeles` timezone
        since local midnight is `08:00` UTC:

        - `[2022-02-01T05:00:00Z, 2022-02-01T08:00:00Z)`
        - `[2022-02-01T08:00:00, 2022-02-02T08:00:00Z)`
        - `[2022-02-02T08:00:00, 2022-02-03T08:00:00Z)`
        - `[2022-02-03T08:00:00, 2022-02-04T01:00:00Z)`

        ```json
        {
            "data": [
                {
                    "billable_metric": {
                        "id": "Q8w89wjTtBdejXKsm",
                        "name": "API Requests"
                    },
                    "usage": [
                        {
                            "quantity": 0,
                            "timeframe_end": "2022-02-01T08:00:00+00:00",
                            "timeframe_start": "2022-02-01T05:00:00+00:00"
                        },
                        {

                            "quantity": 0,
                            "timeframe_end": "2022-02-02T08:00:00+00:00",
                            "timeframe_start": "2022-02-01T08:00:00+00:00"
                        },
                        {
                            "quantity": 0,
                            "timeframe_end": "2022-02-03T08:00:00+00:00",
                            "timeframe_start": "2022-02-02T08:00:00+00:00"
                        },
                        {
                            "quantity": 0,
                            "timeframe_end": "2022-02-04T01:00:00+00:00",
                            "timeframe_start": "2022-02-03T08:00:00+00:00"
                        }
                    ],
                    "view_mode": "periodic"
                },
                ...
            ]
        }
        ```

        ## Decomposable vs. non-decomposable metrics

        Billable metrics fall into one of two categories: decomposable and
        non-decomposable. A decomposable billable metric, such as a sum or a count, can
        be displayed and aggregated across arbitrary timescales. On the other hand, a
        non-decomposable metric is not meaningful when only a slice of the billing
        window is considered.

        As an example, if we have a billable metric that's defined to count unique
        users, displaying a graph of unique users for each day is not representative of
        the billable metric value over the month (days could have an overlapping set of
        'unique' users). Instead, what's useful for any given day is the number of
        unique users in the billing period so far, which are the _cumulative_ unique
        users.

        Accordingly, this endpoint returns treats these two types of metrics differently
        when `group_by` is specified:

        - Decomposable metrics can be grouped by any event property.
        - Non-decomposable metrics can only be grouped by the corresponding price's
          invoice grouping key. If no invoice grouping key is present, the metric does
          not support `group_by`.

        ## Matrix prices

        When a billable metric is attached to a price that uses matrix pricing, it's
        important to view usage grouped by those matrix dimensions. In this case, use
        the query parameters `first_dimension_key`, `first_dimension_value` and
        `second_dimension_key`, `second_dimension_value` while filtering to a specific
        `billable_metric_id`.

        For example, if your compute metric has a separate unit price (i.e. a matrix
        pricing model) per `region` and `provider`, your request might provide the
        following parameters:

        - `first_dimension_key`: `region`
        - `first_dimension_value`: `us-east-1`
        - `second_dimension_key`: `provider`
        - `second_dimension_value`: `aws`

        Args:
          billable_metric_id: When specified in conjunction with `group_by`, this parameter filters usage to a
              single billable metric. Note that both `group_by` and `billable_metric_id` must
              be specified together.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          granularity: This determines the windowing of usage reporting.

          group_by: Groups per-price usage by the key provided.

          limit: If including a `group_by`, the number of groups to fetch data for. Defaults
              to 1000.

          timeframe_end: Usage returned is exclusive of `timeframe_end`.

          timeframe_start: Usage returned is inclusive of `timeframe_start`.

          view_mode: Controls whether Orb returns cumulative usage since the start of the billing
              period, or incremental day-by-day usage. If your customer has minimums or
              discounts, it's strongly recommended that you use the default cumulative
              behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            SubscriptionUsage,
            self._get(
                f"/subscriptions/{subscription_id}/usage",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "billable_metric_id": billable_metric_id,
                            "cursor": cursor,
                            "first_dimension_key": first_dimension_key,
                            "first_dimension_value": first_dimension_value,
                            "granularity": granularity,
                            "group_by": group_by,
                            "limit": limit,
                            "second_dimension_key": second_dimension_key,
                            "second_dimension_value": second_dimension_value,
                            "timeframe_end": timeframe_end,
                            "timeframe_start": timeframe_start,
                            "view_mode": view_mode,
                        },
                        subscription_fetch_usage_params.SubscriptionFetchUsageParams,
                    ),
                ),
                cast_to=cast(Any, SubscriptionUsage),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def price_intervals(
        self,
        subscription_id: str,
        *,
        add: List[subscription_price_intervals_params.Add] | NotGiven = NOT_GIVEN,
        edit: List[subscription_price_intervals_params.Edit] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint is used to add and edit subscription
        [price intervals](../reference/price-interval). By making modifications to a
        subscription’s price intervals, you can
        [flexibly and atomically control the billing behavior of a subscription](../guides/product-catalog/modifying-subscriptions).

        ## Adding price intervals

        Prices can be added as price intervals to a subscription by specifying them in
        the `add` array. A `price_id` or `external_price_id` from an add-on price or
        previously removed plan price can be specified to reuse an existing price
        definition (however, please note that prices from other plans cannot be added to
        the subscription). Additionally, a new price can be specified using the `price`
        field — this price will be created automatically.

        A `start_date` must be specified for the price interval. This is the date when
        the price will start billing on the subscription, so this will notably result in
        an immediate charge at this time for any billed in advance fixed fees. The
        `end_date` will default to null, resulting in a price interval that will bill on
        a continually recurring basis. Both of these dates can be set in the past or the
        future and Orb will generate or modify invoices to ensure the subscription’s
        invoicing behavior is correct.

        Additionally, a discount, minimum, or maximum can be specified on the price
        interval. This will only apply to this price interval, not any other price
        intervals on the subscription.

        ## Editing price intervals

        Price intervals can be adjusted by specifying edits to make in the `edit` array.
        A `price_interval_id` to edit must be specified — this can be retrieved from the
        `price_intervals` field on the subscription.

        A new `start_date` or `end_date` can be specified to change the range of the
        price interval, which will modify past or future invoices to ensure correctness.
        If either of these dates are unspecified, they will default to the existing date
        on the price interval. To remove a price interval entirely from a subscription,
        set the `end_date` to be equivalent to the `start_date`.

        ## Fixed fee quantity transitions

        The fixed fee quantity transitions for a fixed fee price interval can also be
        specified when adding or editing by passing an array for
        `fixed_fee_quantity_transitions`. A fixed fee quantity transition must have a
        `quantity` and an `effective_date`, which is the date after which the new
        quantity will be used for billing. If a fixed fee quantity transition is
        scheduled at a billing period boundary, the full quantity will be billed on an
        invoice with the other prices on the subscription. If the fixed fee quantity
        transition is scheduled mid-billing period, the difference between the existing
        quantity and quantity specified in the transition will be prorated for the rest
        of the billing period and billed immediately, which will generate a new invoice.

        Notably, the list of fixed fee quantity transitions passed will overwrite the
        existing fixed fee quantity transitions on the price interval, so the entire
        list of transitions must be specified to add additional transitions. The
        existing list of transitions can be retrieved using the
        `fixed_fee_quantity_transitions` property on a subscription’s serialized price
        intervals.

        Args:
          add: A list of price intervals to add to the subscription.

          edit: A list of price intervals to edit on the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/price_intervals",
            body=maybe_transform(
                {
                    "add": add,
                    "edit": edit,
                },
                subscription_price_intervals_params.SubscriptionPriceIntervalsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def schedule_plan_change(
        self,
        subscription_id: str,
        *,
        change_option: Literal["requested_date", "end_of_subscription_term", "immediate"],
        align_billing_with_plan_change_date: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]]
        | NotGiven = NOT_GIVEN,
        change_date: Optional[str] | NotGiven = NOT_GIVEN,
        coupon_redemption_code: Optional[str] | NotGiven = NOT_GIVEN,
        credits_overage_rate: Optional[float] | NotGiven = NOT_GIVEN,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        initial_phase_order: Optional[int] | NotGiven = NOT_GIVEN,
        invoicing_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        per_credit_overage_amount: Optional[str] | NotGiven = NOT_GIVEN,
        plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        price_overrides: Optional[List[subscription_schedule_plan_change_params.PriceOverride]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """This endpoint can be used to change the plan on an existing subscription.

        It
        returns the serialized updated subscription object.

        The body parameter `change_option` determines the timing of the plan change. Orb
        supports three options:

        - `end_of_subscription_term`: changes the plan at the end of the existing plan's
          term.
          - Issuing this plan change request for a monthly subscription will keep the
            existing plan active until the start of the subsequent month, and
            potentially issue an invoice for any usage charges incurred in the
            intervening period.
          - Issuing this plan change request for a yearly subscription will keep the
            existing plan active for the full year.
        - `immediate`: changes the plan immediately. Subscriptions that have their plan
          changed with this option will be invoiced immediately. This invoice will
          include any usage fees incurred in the billing period up to the change, along
          with any prorated recurring fees for the billing period, if applicable.
        - `requested_date`: changes the plan on the requested date (`change_date`). If
          no timezone is provided, the customer's timezone is used. The `change_date`
          body parameter is required if this option is chosen.

        Note that one of `plan_id` or `external_plan_id` is required in the request body
        for this operation.

        ## Price overrides, maximums, and minimums

        Price overrides are used to update some or all prices in the target plan.
        Minimums and maximums, much like price overrides, can be useful when a new
        customer has negotiated a new or different minimum or maximum spend cap than the
        default for the plan. The request format for price overrides, maximums, and
        minimums are the same as those in [subscription creation](create-subscription).

        ## Prorations for in-advance fees

        By default, Orb calculates the prorated difference in any fixed fees when making
        a plan change, adjusting the customer balance as needed. For details on this
        behavior, see
        [Modifying subscriptions](../guides/product-catalog/modifying-subscriptions.md#prorations-for-in-advance-fees).

        Args:
          align_billing_with_plan_change_date: [DEPRECATED] Use billing_cycle_alignment instead. Reset billing periods to be
              aligned with the plan change’s effective date.

          billing_cycle_alignment: Reset billing periods to be aligned with the plan change’s effective date or
              start of the month. Defaults to `unchanged` which keeps subscription's existing
              billing cycle alignment.

          change_date: The date that the plan change should take effect. This parameter can only be
              passed if the `change_option` is `requested_date`.

          coupon_redemption_code: Redemption code to be used for this subscription. If the coupon cannot be found
              by its redemption code, or cannot be redeemed, an error response will be
              returned and the plan change will not be scheduled.

          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          initial_phase_order: The phase of the plan to start with

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/schedule_plan_change",
            body=maybe_transform(
                {
                    "change_option": change_option,
                    "align_billing_with_plan_change_date": align_billing_with_plan_change_date,
                    "billing_cycle_alignment": billing_cycle_alignment,
                    "change_date": change_date,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "external_plan_id": external_plan_id,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "price_overrides": price_overrides,
                },
                subscription_schedule_plan_change_params.SubscriptionSchedulePlanChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def trigger_phase(
        self,
        subscription_id: str,
        *,
        effective_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        Manually trigger a phase, effective the given date (or the current time, if not
        specified).

        Args:
          effective_date: The date on which the phase change should take effect. If not provided, defaults
              to today in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/trigger_phase",
            body=maybe_transform(
                {"effective_date": effective_date}, subscription_trigger_phase_params.SubscriptionTriggerPhaseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def unschedule_cancellation(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to unschedule any pending cancellations for a
        subscription.

        To be eligible, the subscription must currently be active and have a future
        cancellation. This operation will turn on auto-renew, ensuring that the
        subscription does not end at the currently scheduled cancellation time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/unschedule_cancellation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def unschedule_fixed_fee_quantity_updates(
        self,
        subscription_id: str,
        *,
        price_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to clear scheduled updates to the quantity for a fixed
        fee.

        If there are no updates scheduled, this endpoint is a no-op.

        Args:
          price_id: Price for which the updates should be cleared. Must be a fixed fee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/unschedule_fixed_fee_quantity_updates",
            body=maybe_transform(
                {"price_id": price_id},
                subscription_unschedule_fixed_fee_quantity_updates_params.SubscriptionUnscheduleFixedFeeQuantityUpdatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def unschedule_pending_plan_changes(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to unschedule any pending plan changes on an existing
        subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/unschedule_pending_plan_changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def update_fixed_fee_quantity(
        self,
        subscription_id: str,
        *,
        price_id: str,
        quantity: float,
        change_option: Literal["immediate", "upcoming_invoice", "effective_date"] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to update the quantity for a fixed fee.

        To be eligible, the subscription must currently be active and the price
        specified must be a fixed fee (not usage-based). This operation will immediately
        update the quantity for the fee, or if a `effective_date` is passed in, will
        update the quantity on the requested date at midnight in the customer's
        timezone.

        In order to change the fixed fee quantity as of the next draft invoice for this
        subscription, pass `change_option=upcoming_invoice` without an `effective_date`
        specified.

        If the fee is an in-advance fixed fee, it will also issue an immediate invoice
        for the difference for the remainder of the billing period.

        Args:
          price_id: Price for which the quantity should be updated. Must be a fixed fee.

          change_option: Determines when the change takes effect. Note that if `effective_date` is
              specified, this defaults to `effective_date`. Otherwise, this defaults to
              `immediate` unless it's explicitly set to `upcoming_invoice.

          effective_date: The date that the quantity change should take effect, localized to the
              customer's timezone. Ifthis parameter is not passed in, the quantity change is
              effective according to `change_option`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/subscriptions/{subscription_id}/update_fixed_fee_quantity",
            body=maybe_transform(
                {
                    "price_id": price_id,
                    "quantity": quantity,
                    "change_option": change_option,
                    "effective_date": effective_date,
                },
                subscription_update_fixed_fee_quantity_params.SubscriptionUpdateFixedFeeQuantityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )


class AsyncSubscriptions(AsyncAPIResource):
    with_raw_response: AsyncSubscriptionsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncSubscriptionsWithRawResponse(self)

    async def create(
        self,
        *,
        align_billing_with_subscription_start_date: bool | NotGiven = NOT_GIVEN,
        auto_collection: Optional[bool] | NotGiven = NOT_GIVEN,
        aws_region: Optional[str] | NotGiven = NOT_GIVEN,
        coupon_redemption_code: Optional[str] | NotGiven = NOT_GIVEN,
        credits_overage_rate: Optional[float] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        default_invoice_memo: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_marketplace: Optional[Literal["google", "aws", "azure"]] | NotGiven = NOT_GIVEN,
        external_marketplace_reporting_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        initial_phase_order: Optional[int] | NotGiven = NOT_GIVEN,
        invoicing_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        net_terms: Optional[int] | NotGiven = NOT_GIVEN,
        per_credit_overage_amount: Optional[str] | NotGiven = NOT_GIVEN,
        plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        price_overrides: Optional[List[subscription_create_params.PriceOverride]] | NotGiven = NOT_GIVEN,
        start_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """A subscription represents the purchase of a plan by a customer.

        The customer is
        identified by either the `customer_id` or the `external_customer_id`, and
        exactly one of these fields must be provided.

        By default, subscriptions begin on the day that they're created and renew
        automatically for each billing cycle at the cadence that's configured in the
        plan definition.

        The default configuration for subscriptions in Orb is **In-advance billing** and
        **Beginning of month alignment** (see
        [Subscription](../guides/concepts#subscription) for more details).

        In order to change the alignment behavior, Orb also supports billing
        subscriptions on the day of the month they are created. If
        `align_billing_with_subscription_start_date = true` is specified, subscriptions
        have billing cycles that are aligned with their `start_date`. For example, a
        subscription that begins on January 15th will have a billing cycle from January
        15th to February 15th. Every subsequent billing cycle will continue to start and
        invoice on the 15th.

        If the "day" value is greater than the number of days in the month, the next
        billing cycle will start at the end of the month. For example, if the start_date
        is January 31st, the next billing cycle will start on February 28th.

        If a customer was created with a currency, Orb only allows subscribing the
        customer to a plan with a matching `invoicing_currency`. If the customer does
        not have a currency set, on subscription creation, we set the customer's
        currency to be the `invoicing_currency` of the plan.

        ## Price overrides

        Price overrides are used to update some or all prices in a plan for the specific
        subscription being created. This is useful when a new customer has negotiated
        one or more different prices for a specific plan than the plan's default prices.
        Any type of price can be overridden, if the correct data is provided. The
        billable metric, cadence, type, and name of a price can not be overridden.

        To override prices, provide a list of objects with the key `price_overrides`.
        The price object in the list of overrides is expected to contain the existing
        price id, the `model_type` and config value in the format below. The specific
        numerical values can be updated, but the config value and `model_type` must
        match the existing price that is being overridden

        ### Request format for price overrides

        Orb supports a few different pricing models out of the box. The `model_type`
        field determines the key for the configuration object that is present.

        ### Unit pricing

        With unit pricing, each unit costs a fixed amount.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          }
          ...
        }
        ```

        ### Tiered pricing

        In tiered pricing, the cost of a given unit depends on the tier range that it
        falls into, where each tier range is defined by an upper and lower bound. For
        example, the first ten units may cost $0.50 each and all units thereafter may
        cost $0.10 each. Tiered prices can be overridden with a new number of tiers or
        new values for `first_unit`, `last_unit`, or `unit_amount`.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "tiered",
          "tiered_config": {
            "tiers": [
              {
                "first_unit":"1",
                "last_unit": "10",
                "unit_amount": "0.50"
              },
              {
                "first_unit": "10",
                "last_unit": null,
                "unit_amount": "0.10"
              }
            ]
          }
          ...
        }
        ```

        ### Bulk pricing

        Bulk pricing applies when the number of units determine the cost of _all_ units.
        For example, if you've bought less than 10 units, they may each be $0.50 for a
        total of $5.00. Once you've bought more than 10 units, all units may now be
        priced at $0.40 (i.e. 101 units total would be $40.40). Bulk prices can be
        overridden with a new number of tiers or new values for `maximum_units`, or
        `unit_amount`.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "bulk",
          "bulk_config": {
            "tiers": [
              {
                "maximum_units": "10",
                "unit_amount": "0.50"
              },
              {
                "maximum_units": "1000",
                "unit_amount": "0.40"
              }
            ]
          }
          ...
        }
        ```

        ### Package pricing

        Package pricing defines the size or granularity of a unit for billing purposes.
        For example, if the package size is set to 5, then 4 units will be billed as 5
        and 6 units will be billed at 10.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "package",
          "package_config": {
            "package_amount": "0.80",
            "package_size": 10
          }
          ...
        }
        ```

        ### BPS pricing

        BPS pricing specifies a per-event (e.g. per-payment) rate in one hundredth of a
        percent (the number of basis points to charge), as well as a cap per event to
        assess. For example, this would allow you to assess a fee of 0.25% on every
        payment you process, with a maximum charge of $25 per payment.

        ```json
        {
          ...
          "id": "price_id"
          "model_type": "bps",
          "bps_config": {
            "bps": 125,
            "per_event_cap": "11.00"
          }
          ...
        }
        ```

        ### Bulk BPS pricing

        Bulk BPS pricing specifies BPS parameters in a tiered manner, dependent on the
        total quantity across all events. Similar to bulk pricing, the BPS parameters of
        a given event depends on the tier range that the billing period falls into. Each
        tier range is defined by an upper and lower bound. For example, after $1.5M of
        payment volume is reached, each individual payment may have a lower cap or a
        smaller take-rate.

        ```json
        {
          ...
          "id": "price_id"
          "model_type": "bulk_bps",
          "bulk_bps_config": {
            "tiers": [
              {
                "minimum_amount": "0.00",
                "maximum_amount": "1000000.00",
                "bps": 125,
                "per_event_cap": "19.00"
              },
              {
                "minimum_amount":"1000000.00",
                "maximum_amount": null,
                "bps": 115,
                "per_event_cap": "4.00"
              }
            ]
          }
        ...
        }
        ```

        ### Tiered BPS pricing

        Tiered BPS pricing specifies BPS parameters in a graduated manner, where an
        event's applicable parameter is a function of its marginal addition to the
        period total. Similar to tiered pricing, the BPS parameters of a given event
        depends on the tier range that it falls into, where each tier range is defined
        by an upper and lower bound. For example, the first few payments may have a 0.8
        BPS take-rate and all payments after a specific volume may incur a take-rate of
        0.5 BPS each.

        ```json
        {
          ...
          "id": "price_id"
          "model_type": "tiered_bps",
          "tiered_bps_config": {
            "tiers": [
              {
                "minimum_amount": "0.00",
                "maximum_amount": "1000000.00",
                "bps": 125,
                "per_event_cap": "19.00"
              },
              {
                "minimum_amount":"1000000",
                "maximum_amount": null,
                "bps": 115,
                "per_event_cap": "4.00"
              }
            ]
          }
          ...
        }
        ```

        ### Matrix pricing

        Matrix pricing defines a set of unit prices in a one or two-dimensional matrix.
        `dimensions` defines the two event property values evaluated in this pricing
        model. In a one-dimensional matrix, the second value is `null`. Every
        configuration has a list of `matrix_values` which give the unit prices for
        specified property values. In a one-dimensional matrix, the matrix values will
        have `dimension_values` where the second value of the pair is null. If an event
        does not match any of the dimension values in the matrix, it will resort to the
        `default_unit_amount`.

        ```json
        {
          ...
          "model_type": "matrix",
          "matrix_config": {
            "default_unit_amount": "3.00",
            "dimensions": [
              "cluster_name",
              "region"
            ],
            "matrix_values": [
              {
                "dimension_values": [
                  "alpha",
                  "west"
                ],
                "unit_amount": "2.00"
              },
              ...
            ]
          }
        }
        ```

        ### Fixed fees

        Fixed fees follow unit pricing, and also have an additional parameter
        `fixed_price_quantity` that indicates how many of a fixed fee that should be
        applied for a subscription. This parameter defaults to 1.

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "2.00"
          },
          "fixed_price_quantity": 3.0
          ...
        }
        ```

        ## Maximums and Minimums

        Minimums and maximums, much like price overrides, can be useful when a new
        customer has negotiated a new or different minimum or maximum spend cap than the
        default for a given price. If one exists for a price and null is provided for
        the minimum/maximum override on creation, then there will be no minimum/maximum
        on the new subscription. If no value is provided, then the default price maximum
        or minimum is used.

        To add a minimum for a specific price, add `minimum_amount` to the specific
        price in the `price_overrides` object.

        To add a maximum for a specific price, add `maximum_amount` to the specific
        price in the `price_overrides` object.

        ### Minimum override example

        Price minimum override example:

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          },
          "minimum_amount": "100.00"
          ...
        }
        ```

        Removing an existing minimum example

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          },
          "minimum_amount": null
          ...
        }
        ```

        ## Discounts

        Discounts, like price overrides, can be useful when a new customer has
        negotiated a new or different discount than the default for a price. A single
        price price can have at most one discount. If a discount exists for a price and
        a null discount is provided on creation, then there will be no discount on the
        new subscription.

        To add a discount for a specific price, add `discount` to the price in the
        `price_overrides` object. Discount should be a dictionary of the format:

        ```ts
        {
          "discount_type": "amount" | "percentage" | "usage",
          "amount_discount": string,
          "percentage_discount": string,
          "usage_discount": string
        }
        ```

        where either `amount_discount`, `percentage_discount`, or `usage_discount` is
        provided.

        Price discount example

        ```json
        {
          ...
          "id": "price_id",
          "model_type": "unit",
          "unit_config": {
            "unit_amount": "0.50"
          },
          "discount": {"discount_type": "amount", "amount_discount": "175"},
        }
        ```

        Removing an existing discount example

        ```json
        {
          "customer_id": "customer_id",
          "plan_id": "plan_id",
          "discount": null,
          "price_overrides": [ ... ]
          ...
        }
        ```

        ## Threshold Billing

        Orb supports invoicing for a subscription when a preconfigured usage threshold
        is hit. To enable threshold billing, pass in an `invoicing_threshold`, which is
        specified in the subscription's invoicing currency, when creating a
        subscription. E.g. pass in `10.00` to issue an invoice when usage amounts hit
        $10.00 for a subscription that invoices in USD.

        Args:
          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/subscriptions",
            body=maybe_transform(
                {
                    "align_billing_with_subscription_start_date": align_billing_with_subscription_start_date,
                    "auto_collection": auto_collection,
                    "aws_region": aws_region,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "customer_id": customer_id,
                    "default_invoice_memo": default_invoice_memo,
                    "end_date": end_date,
                    "external_customer_id": external_customer_id,
                    "external_marketplace": external_marketplace,
                    "external_marketplace_reporting_id": external_marketplace_reporting_id,
                    "external_plan_id": external_plan_id,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "metadata": metadata,
                    "net_terms": net_terms,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "price_overrides": price_overrides,
                    "start_date": start_date,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Optional[Literal["active", "ended", "upcoming"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Subscription, AsyncPage[Subscription]]:
        """
        This endpoint returns a list of all subscriptions for an account as a
        [paginated](../reference/pagination) list, ordered starting from the most
        recently created subscription. For a full discussion of the subscription
        resource, see [Subscription](../guides/concepts#subscription).

        Subscriptions can be filtered to a single customer by passing in the
        `customer_id` query parameter or the `external_customer_id` query parameter.

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
            "/subscriptions",
            page=AsyncPage[Subscription],
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
                        "customer_id": customer_id,
                        "external_customer_id": external_customer_id,
                        "limit": limit,
                        "status": status,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=Subscription,
        )

    async def cancel(
        self,
        subscription_id: str,
        *,
        cancel_option: Literal["end_of_subscription_term", "immediate", "requested_date"],
        cancellation_date: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """This endpoint can be used to cancel an existing subscription.

        It returns the
        serialized subscription object with an `end_date` parameter that signifies when
        the subscription will transition to an ended state.

        The body parameter `cancel_option` determines the cancellation behavior. Orb
        supports three cancellation options:

        - `end_of_subscription_term`: stops the subscription from auto-renewing.
          Subscriptions that have been cancelled with this option can still incur
          charges for the remainder of their term:

          - Issuing this cancellation request for a monthly subscription will keep the
            subscription active until the start of the subsequent month, and potentially
            issue an invoice for any usage charges incurred in the intervening period.
          - Issuing this cancellation request for a quarterly subscription will keep the
            subscription active until the end of the quarter and potentially issue an
            invoice for any usage charges incurred in the intervening period.
          - Issuing this cancellation request for a yearly subscription will keep the
            subscription active for the full year. For example, a yearly subscription
            starting on 2021-11-01 and cancelled on 2021-12-08 will remain active until
            2022-11-01 and potentially issue charges in the intervening months for any
            recurring monthly usage charges in its plan.
          - **Note**: If a subscription's plan contains prices with difference cadences,
            the end of term date will be determined by the largest cadence value. For
            example, cancelling end of term for a subscription with a quarterly fixed
            fee with a monthly usage fee will result in the subscription ending at the
            end of the quarter.

        - `immediate`: ends the subscription immediately, setting the `end_date` to the
          current time:

          - Subscriptions that have been cancelled with this option will be invoiced
            immediately. This invoice will include any usage fees incurred in the
            billing period up to the cancellation, along with any prorated recurring
            fees for the billing period, if applicable.
          - **Note**: If the subscription has a recurring fee that was paid in-advance,
            the prorated amount for the remaining time period will be added to the
            [customer's balance](list-balance-transactions) upon immediate cancellation.
            However, if the customer is ineligible to use the customer balance, the
            subscription cannot be cancelled immediately.

        - `requested_date`: ends the subscription on a specified date, which requires a
          `cancellation_date` to be passed in. If no timezone is provided, the
          customer's timezone is used. For example, a subscription starting on January
          1st with a monthly price can be set to be cancelled on the first of any month
          after January 1st (e.g. March 1st, April 1st, May 1st). A subscription with
          multiple prices with different cadences defines the "term" to be the highest
          cadence of the prices.

        Upcoming subscriptions are only eligible for immediate cancellation, which will
        set the `end_date` equal to the `start_date` upon cancellation.

        ## Backdated cancellations

        Orb allows you to cancel a subscription in the past as long as there are no paid
        invoices between the `requested_date` and the current time. If the cancellation
        is after the latest issued invoice, Orb will generate a balance refund for the
        current period. If the cancellation is before the most recently issued invoice,
        Orb will void the intervening invoice and generate a new one based on the new
        dates for the subscription. See the section on
        [cancellation behaviors](../guides/product-catalog/creating-subscriptions.md#cancellation-behaviors).

        Args:
          cancel_option: Determines the timing of subscription cancellation

          cancellation_date: The date that the cancellation should take effect. This parameter can only be
              passed if the `cancel_option` is `requested_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/cancel",
            body=maybe_transform(
                {
                    "cancel_option": cancel_option,
                    "cancellation_date": cancellation_date,
                },
                subscription_cancel_params.SubscriptionCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def fetch(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Subscription:
        """
        This endpoint is used to fetch a [Subscription](../guides/concepts#subscription)
        given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Subscription,
        )

    async def fetch_costs(
        self,
        subscription_id: str,
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
    ) -> SubscriptionFetchCostsResponse:
        """
        This endpoint is used to fetch a day-by-day snapshot of a subscription's costs
        in Orb, calculated by applying pricing information to the underlying usage (see
        the [subscription usage endpoint](fetch-subscription-usage) to fetch usage per
        metric, in usage units rather than a currency).

        The semantics of this endpoint exactly mirror those of
        [fetching a customer's costs](fetch-customer-costs). Use this endpoint to limit
        your analysis of costs to a specific subscription for the customer (e.g. to
        de-aggregate costs when a customer's subscription has started and stopped on the
        same day).

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
            f"/subscriptions/{subscription_id}/costs",
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
                    subscription_fetch_costs_params.SubscriptionFetchCostsParams,
                ),
            ),
            cast_to=SubscriptionFetchCostsResponse,
        )

    def fetch_schedule(
        self,
        subscription_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        start_date_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        start_date_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SubscriptionFetchScheduleResponse, AsyncPage[SubscriptionFetchScheduleResponse]]:
        """
        This endpoint returns a [paginated](../reference/pagination) list of all plans
        associated with a subscription along with their start and end dates. This list
        contains the subscription's initial plan along with past and future plan
        changes.

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
            f"/subscriptions/{subscription_id}/schedule",
            page=AsyncPage[SubscriptionFetchScheduleResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "start_date_gt": start_date_gt,
                        "start_date_gte": start_date_gte,
                        "start_date_lt": start_date_lt,
                        "start_date_lte": start_date_lte,
                    },
                    subscription_fetch_schedule_params.SubscriptionFetchScheduleParams,
                ),
            ),
            model=SubscriptionFetchScheduleResponse,
        )

    async def fetch_usage(
        self,
        subscription_id: str,
        *,
        billable_metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        first_dimension_key: Optional[str] | NotGiven = NOT_GIVEN,
        first_dimension_value: Optional[str] | NotGiven = NOT_GIVEN,
        granularity: Optional[Literal["day"]] | NotGiven = NOT_GIVEN,
        group_by: Optional[str] | NotGiven = NOT_GIVEN,
        limit: Optional[int] | NotGiven = NOT_GIVEN,
        second_dimension_key: Optional[str] | NotGiven = NOT_GIVEN,
        second_dimension_value: Optional[str] | NotGiven = NOT_GIVEN,
        timeframe_end: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        view_mode: Optional[Literal["periodic", "cumulative"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionUsage:
        """This endpoint is used to fetch a subscription's usage in Orb.

        Especially when
        combined with optional query parameters, this endpoint is a powerful way to
        build visualizations on top of Orb's event data and metrics.

        With no query parameters specified, this endpoint returns usage for the
        subscription's _current billing period_ across each billable metric that
        participates in the subscription. Usage quantities returned are the result of
        evaluating the metric definition for the entirety of the customer's billing
        period.

        ### Default response shape

        Orb returns a `data` array with an object corresponding to each billable metric.
        Nested within this object is a `usage` array which has a `quantity` value and a
        corresponding `timeframe_start` and `timeframe_end`. The `quantity` value
        represents the calculated usage value for the billable metric over the specified
        timeframe (inclusive of the `timeframe_start` timestamp and exclusive of the
        `timeframe_end` timestamp).

        Orb will include _every_ window in the response starting from the beginning of
        the billing period, even when there were no events (and therefore no usage) in
        the window. This increases the size of the response but prevents the caller from
        filling in gaps and handling cumbersome time-based logic.

        The query parameters in this endpoint serve to override this behavior and
        provide some key functionality, as listed below. Note that this functionality
        can also be used _in conjunction_ with each other, e.g. to display grouped usage
        on a custom timeframe.

        ## Custom timeframe

        In order to view usage for a custom timeframe rather than the current billing
        period, specify a `timeframe_start` and `timeframe_end`. This will calculate
        quantities for usage incurred between timeframe_start (inclusive) and
        timeframe_end (exclusive), i.e. `[timeframe_start, timeframe_end)`.

        Note:

        - These timestamps must be specified in ISO 8601 format and UTC timezone, e.g.
          `2022-02-01T05:00:00Z`.
        - Both parameters must be specified if either is specified.

        ## Grouping by custom attributes

        In order to view a single metric grouped by a specific _attribute_ that each
        event is tagged with (e.g. `cluster`), you must additionally specify a
        `billable_metric_id` and a `group_by` key. The `group_by` key denotes the event
        property on which to group.

        When returning grouped usage, only usage for `billable_metric_id` is returned,
        and a separate object in the `data` array is returned for each value of the
        `group_by` key present in your events. The `quantity` value is the result of
        evaluating the billable metric for events filtered to a single value of the
        `group_by` key.

        Orb expects that events that match the billable metric will contain values in
        the `properties` dictionary that correspond to the `group_by` key specified. By
        default, Orb will not return a `null` group (i.e. events that match the metric
        but do not have the key set). Currently, it is only possible to view usage
        grouped by a single attribute at a time.

        When viewing grouped usage, Orb uses pagination to limit the response size to
        1000 groups by default. If there are more groups for a given subscription,
        pagination metadata in the response can be used to fetch all of the data.

        The following example shows usage for an "API Requests" billable metric grouped
        by `region`. Note the extra `metric_group` dictionary in the response, which
        provides metadata about the group:

        ```json
        {
            "data": [
                {
                    "usage": [
                        {
                            "quantity": 0.19291,
                            "timeframe_start": "2021-10-01T07:00:00Z",
                            "timeframe_end": "2021-10-02T07:00:00Z",
                        },
                        ...
                    ],
                    "metric_group": {
                        "property_key": "region",
                        "property_value": "asia/pacific"
                    },
                    "billable_metric": {
                        "id": "Fe9pbpMk86xpwdGB",
                        "name": "API Requests"
                    },
                    "view_mode": "periodic"
                },
                ...
            ]
        }
        ```

        ## Windowed usage

        The `granularity` parameter can be used to _window_ the usage `quantity` value
        into periods. When not specified, usage is returned for the entirety of the time
        range.

        When `granularity = day` is specified with a timeframe longer than a day, Orb
        will return a `quantity` value for each full day between `timeframe_start` and
        `timeframe_end`. Note that the days are demarcated by the _customer's local
        midnight_.

        For example, with `timeframe_start = 2022-02-01T05:00:00Z`,
        `timeframe_end = 2022-02-04T01:00:00Z` and `granularity=day`, the following
        windows will be returned for a customer in the `America/Los_Angeles` timezone
        since local midnight is `08:00` UTC:

        - `[2022-02-01T05:00:00Z, 2022-02-01T08:00:00Z)`
        - `[2022-02-01T08:00:00, 2022-02-02T08:00:00Z)`
        - `[2022-02-02T08:00:00, 2022-02-03T08:00:00Z)`
        - `[2022-02-03T08:00:00, 2022-02-04T01:00:00Z)`

        ```json
        {
            "data": [
                {
                    "billable_metric": {
                        "id": "Q8w89wjTtBdejXKsm",
                        "name": "API Requests"
                    },
                    "usage": [
                        {
                            "quantity": 0,
                            "timeframe_end": "2022-02-01T08:00:00+00:00",
                            "timeframe_start": "2022-02-01T05:00:00+00:00"
                        },
                        {

                            "quantity": 0,
                            "timeframe_end": "2022-02-02T08:00:00+00:00",
                            "timeframe_start": "2022-02-01T08:00:00+00:00"
                        },
                        {
                            "quantity": 0,
                            "timeframe_end": "2022-02-03T08:00:00+00:00",
                            "timeframe_start": "2022-02-02T08:00:00+00:00"
                        },
                        {
                            "quantity": 0,
                            "timeframe_end": "2022-02-04T01:00:00+00:00",
                            "timeframe_start": "2022-02-03T08:00:00+00:00"
                        }
                    ],
                    "view_mode": "periodic"
                },
                ...
            ]
        }
        ```

        ## Decomposable vs. non-decomposable metrics

        Billable metrics fall into one of two categories: decomposable and
        non-decomposable. A decomposable billable metric, such as a sum or a count, can
        be displayed and aggregated across arbitrary timescales. On the other hand, a
        non-decomposable metric is not meaningful when only a slice of the billing
        window is considered.

        As an example, if we have a billable metric that's defined to count unique
        users, displaying a graph of unique users for each day is not representative of
        the billable metric value over the month (days could have an overlapping set of
        'unique' users). Instead, what's useful for any given day is the number of
        unique users in the billing period so far, which are the _cumulative_ unique
        users.

        Accordingly, this endpoint returns treats these two types of metrics differently
        when `group_by` is specified:

        - Decomposable metrics can be grouped by any event property.
        - Non-decomposable metrics can only be grouped by the corresponding price's
          invoice grouping key. If no invoice grouping key is present, the metric does
          not support `group_by`.

        ## Matrix prices

        When a billable metric is attached to a price that uses matrix pricing, it's
        important to view usage grouped by those matrix dimensions. In this case, use
        the query parameters `first_dimension_key`, `first_dimension_value` and
        `second_dimension_key`, `second_dimension_value` while filtering to a specific
        `billable_metric_id`.

        For example, if your compute metric has a separate unit price (i.e. a matrix
        pricing model) per `region` and `provider`, your request might provide the
        following parameters:

        - `first_dimension_key`: `region`
        - `first_dimension_value`: `us-east-1`
        - `second_dimension_key`: `provider`
        - `second_dimension_value`: `aws`

        Args:
          billable_metric_id: When specified in conjunction with `group_by`, this parameter filters usage to a
              single billable metric. Note that both `group_by` and `billable_metric_id` must
              be specified together.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          granularity: This determines the windowing of usage reporting.

          group_by: Groups per-price usage by the key provided.

          limit: If including a `group_by`, the number of groups to fetch data for. Defaults
              to 1000.

          timeframe_end: Usage returned is exclusive of `timeframe_end`.

          timeframe_start: Usage returned is inclusive of `timeframe_start`.

          view_mode: Controls whether Orb returns cumulative usage since the start of the billing
              period, or incremental day-by-day usage. If your customer has minimums or
              discounts, it's strongly recommended that you use the default cumulative
              behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            SubscriptionUsage,
            await self._get(
                f"/subscriptions/{subscription_id}/usage",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "billable_metric_id": billable_metric_id,
                            "cursor": cursor,
                            "first_dimension_key": first_dimension_key,
                            "first_dimension_value": first_dimension_value,
                            "granularity": granularity,
                            "group_by": group_by,
                            "limit": limit,
                            "second_dimension_key": second_dimension_key,
                            "second_dimension_value": second_dimension_value,
                            "timeframe_end": timeframe_end,
                            "timeframe_start": timeframe_start,
                            "view_mode": view_mode,
                        },
                        subscription_fetch_usage_params.SubscriptionFetchUsageParams,
                    ),
                ),
                cast_to=cast(Any, SubscriptionUsage),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def price_intervals(
        self,
        subscription_id: str,
        *,
        add: List[subscription_price_intervals_params.Add] | NotGiven = NOT_GIVEN,
        edit: List[subscription_price_intervals_params.Edit] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint is used to add and edit subscription
        [price intervals](../reference/price-interval). By making modifications to a
        subscription’s price intervals, you can
        [flexibly and atomically control the billing behavior of a subscription](../guides/product-catalog/modifying-subscriptions).

        ## Adding price intervals

        Prices can be added as price intervals to a subscription by specifying them in
        the `add` array. A `price_id` or `external_price_id` from an add-on price or
        previously removed plan price can be specified to reuse an existing price
        definition (however, please note that prices from other plans cannot be added to
        the subscription). Additionally, a new price can be specified using the `price`
        field — this price will be created automatically.

        A `start_date` must be specified for the price interval. This is the date when
        the price will start billing on the subscription, so this will notably result in
        an immediate charge at this time for any billed in advance fixed fees. The
        `end_date` will default to null, resulting in a price interval that will bill on
        a continually recurring basis. Both of these dates can be set in the past or the
        future and Orb will generate or modify invoices to ensure the subscription’s
        invoicing behavior is correct.

        Additionally, a discount, minimum, or maximum can be specified on the price
        interval. This will only apply to this price interval, not any other price
        intervals on the subscription.

        ## Editing price intervals

        Price intervals can be adjusted by specifying edits to make in the `edit` array.
        A `price_interval_id` to edit must be specified — this can be retrieved from the
        `price_intervals` field on the subscription.

        A new `start_date` or `end_date` can be specified to change the range of the
        price interval, which will modify past or future invoices to ensure correctness.
        If either of these dates are unspecified, they will default to the existing date
        on the price interval. To remove a price interval entirely from a subscription,
        set the `end_date` to be equivalent to the `start_date`.

        ## Fixed fee quantity transitions

        The fixed fee quantity transitions for a fixed fee price interval can also be
        specified when adding or editing by passing an array for
        `fixed_fee_quantity_transitions`. A fixed fee quantity transition must have a
        `quantity` and an `effective_date`, which is the date after which the new
        quantity will be used for billing. If a fixed fee quantity transition is
        scheduled at a billing period boundary, the full quantity will be billed on an
        invoice with the other prices on the subscription. If the fixed fee quantity
        transition is scheduled mid-billing period, the difference between the existing
        quantity and quantity specified in the transition will be prorated for the rest
        of the billing period and billed immediately, which will generate a new invoice.

        Notably, the list of fixed fee quantity transitions passed will overwrite the
        existing fixed fee quantity transitions on the price interval, so the entire
        list of transitions must be specified to add additional transitions. The
        existing list of transitions can be retrieved using the
        `fixed_fee_quantity_transitions` property on a subscription’s serialized price
        intervals.

        Args:
          add: A list of price intervals to add to the subscription.

          edit: A list of price intervals to edit on the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/price_intervals",
            body=maybe_transform(
                {
                    "add": add,
                    "edit": edit,
                },
                subscription_price_intervals_params.SubscriptionPriceIntervalsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def schedule_plan_change(
        self,
        subscription_id: str,
        *,
        change_option: Literal["requested_date", "end_of_subscription_term", "immediate"],
        align_billing_with_plan_change_date: Optional[bool] | NotGiven = NOT_GIVEN,
        billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]]
        | NotGiven = NOT_GIVEN,
        change_date: Optional[str] | NotGiven = NOT_GIVEN,
        coupon_redemption_code: Optional[str] | NotGiven = NOT_GIVEN,
        credits_overage_rate: Optional[float] | NotGiven = NOT_GIVEN,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        initial_phase_order: Optional[int] | NotGiven = NOT_GIVEN,
        invoicing_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        per_credit_overage_amount: Optional[str] | NotGiven = NOT_GIVEN,
        plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        price_overrides: Optional[List[subscription_schedule_plan_change_params.PriceOverride]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """This endpoint can be used to change the plan on an existing subscription.

        It
        returns the serialized updated subscription object.

        The body parameter `change_option` determines the timing of the plan change. Orb
        supports three options:

        - `end_of_subscription_term`: changes the plan at the end of the existing plan's
          term.
          - Issuing this plan change request for a monthly subscription will keep the
            existing plan active until the start of the subsequent month, and
            potentially issue an invoice for any usage charges incurred in the
            intervening period.
          - Issuing this plan change request for a yearly subscription will keep the
            existing plan active for the full year.
        - `immediate`: changes the plan immediately. Subscriptions that have their plan
          changed with this option will be invoiced immediately. This invoice will
          include any usage fees incurred in the billing period up to the change, along
          with any prorated recurring fees for the billing period, if applicable.
        - `requested_date`: changes the plan on the requested date (`change_date`). If
          no timezone is provided, the customer's timezone is used. The `change_date`
          body parameter is required if this option is chosen.

        Note that one of `plan_id` or `external_plan_id` is required in the request body
        for this operation.

        ## Price overrides, maximums, and minimums

        Price overrides are used to update some or all prices in the target plan.
        Minimums and maximums, much like price overrides, can be useful when a new
        customer has negotiated a new or different minimum or maximum spend cap than the
        default for the plan. The request format for price overrides, maximums, and
        minimums are the same as those in [subscription creation](create-subscription).

        ## Prorations for in-advance fees

        By default, Orb calculates the prorated difference in any fixed fees when making
        a plan change, adjusting the customer balance as needed. For details on this
        behavior, see
        [Modifying subscriptions](../guides/product-catalog/modifying-subscriptions.md#prorations-for-in-advance-fees).

        Args:
          align_billing_with_plan_change_date: [DEPRECATED] Use billing_cycle_alignment instead. Reset billing periods to be
              aligned with the plan change’s effective date.

          billing_cycle_alignment: Reset billing periods to be aligned with the plan change’s effective date or
              start of the month. Defaults to `unchanged` which keeps subscription's existing
              billing cycle alignment.

          change_date: The date that the plan change should take effect. This parameter can only be
              passed if the `change_option` is `requested_date`.

          coupon_redemption_code: Redemption code to be used for this subscription. If the coupon cannot be found
              by its redemption code, or cannot be redeemed, an error response will be
              returned and the plan change will not be scheduled.

          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          initial_phase_order: The phase of the plan to start with

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/schedule_plan_change",
            body=maybe_transform(
                {
                    "change_option": change_option,
                    "align_billing_with_plan_change_date": align_billing_with_plan_change_date,
                    "billing_cycle_alignment": billing_cycle_alignment,
                    "change_date": change_date,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "external_plan_id": external_plan_id,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "price_overrides": price_overrides,
                },
                subscription_schedule_plan_change_params.SubscriptionSchedulePlanChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def trigger_phase(
        self,
        subscription_id: str,
        *,
        effective_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        Manually trigger a phase, effective the given date (or the current time, if not
        specified).

        Args:
          effective_date: The date on which the phase change should take effect. If not provided, defaults
              to today in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/trigger_phase",
            body=maybe_transform(
                {"effective_date": effective_date}, subscription_trigger_phase_params.SubscriptionTriggerPhaseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def unschedule_cancellation(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to unschedule any pending cancellations for a
        subscription.

        To be eligible, the subscription must currently be active and have a future
        cancellation. This operation will turn on auto-renew, ensuring that the
        subscription does not end at the currently scheduled cancellation time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/unschedule_cancellation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def unschedule_fixed_fee_quantity_updates(
        self,
        subscription_id: str,
        *,
        price_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to clear scheduled updates to the quantity for a fixed
        fee.

        If there are no updates scheduled, this endpoint is a no-op.

        Args:
          price_id: Price for which the updates should be cleared. Must be a fixed fee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/unschedule_fixed_fee_quantity_updates",
            body=maybe_transform(
                {"price_id": price_id},
                subscription_unschedule_fixed_fee_quantity_updates_params.SubscriptionUnscheduleFixedFeeQuantityUpdatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def unschedule_pending_plan_changes(
        self,
        subscription_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to unschedule any pending plan changes on an existing
        subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/unschedule_pending_plan_changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )

    async def update_fixed_fee_quantity(
        self,
        subscription_id: str,
        *,
        price_id: str,
        quantity: float,
        change_option: Literal["immediate", "upcoming_invoice", "effective_date"] | NotGiven = NOT_GIVEN,
        effective_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to update the quantity for a fixed fee.

        To be eligible, the subscription must currently be active and the price
        specified must be a fixed fee (not usage-based). This operation will immediately
        update the quantity for the fee, or if a `effective_date` is passed in, will
        update the quantity on the requested date at midnight in the customer's
        timezone.

        In order to change the fixed fee quantity as of the next draft invoice for this
        subscription, pass `change_option=upcoming_invoice` without an `effective_date`
        specified.

        If the fee is an in-advance fixed fee, it will also issue an immediate invoice
        for the difference for the remainder of the billing period.

        Args:
          price_id: Price for which the quantity should be updated. Must be a fixed fee.

          change_option: Determines when the change takes effect. Note that if `effective_date` is
              specified, this defaults to `effective_date`. Otherwise, this defaults to
              `immediate` unless it's explicitly set to `upcoming_invoice.

          effective_date: The date that the quantity change should take effect, localized to the
              customer's timezone. Ifthis parameter is not passed in, the quantity change is
              effective according to `change_option`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/subscriptions/{subscription_id}/update_fixed_fee_quantity",
            body=maybe_transform(
                {
                    "price_id": price_id,
                    "quantity": quantity,
                    "change_option": change_option,
                    "effective_date": effective_date,
                },
                subscription_update_fixed_fee_quantity_params.SubscriptionUpdateFixedFeeQuantityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Subscription,
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.cancel = to_raw_response_wrapper(
            subscriptions.cancel,
        )
        self.fetch = to_raw_response_wrapper(
            subscriptions.fetch,
        )
        self.fetch_costs = to_raw_response_wrapper(
            subscriptions.fetch_costs,
        )
        self.fetch_schedule = to_raw_response_wrapper(
            subscriptions.fetch_schedule,
        )
        self.fetch_usage = to_raw_response_wrapper(
            subscriptions.fetch_usage,
        )
        self.price_intervals = to_raw_response_wrapper(
            subscriptions.price_intervals,
        )
        self.schedule_plan_change = to_raw_response_wrapper(
            subscriptions.schedule_plan_change,
        )
        self.trigger_phase = to_raw_response_wrapper(
            subscriptions.trigger_phase,
        )
        self.unschedule_cancellation = to_raw_response_wrapper(
            subscriptions.unschedule_cancellation,
        )
        self.unschedule_fixed_fee_quantity_updates = to_raw_response_wrapper(
            subscriptions.unschedule_fixed_fee_quantity_updates,
        )
        self.unschedule_pending_plan_changes = to_raw_response_wrapper(
            subscriptions.unschedule_pending_plan_changes,
        )
        self.update_fixed_fee_quantity = to_raw_response_wrapper(
            subscriptions.update_fixed_fee_quantity,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            subscriptions.cancel,
        )
        self.fetch = async_to_raw_response_wrapper(
            subscriptions.fetch,
        )
        self.fetch_costs = async_to_raw_response_wrapper(
            subscriptions.fetch_costs,
        )
        self.fetch_schedule = async_to_raw_response_wrapper(
            subscriptions.fetch_schedule,
        )
        self.fetch_usage = async_to_raw_response_wrapper(
            subscriptions.fetch_usage,
        )
        self.price_intervals = async_to_raw_response_wrapper(
            subscriptions.price_intervals,
        )
        self.schedule_plan_change = async_to_raw_response_wrapper(
            subscriptions.schedule_plan_change,
        )
        self.trigger_phase = async_to_raw_response_wrapper(
            subscriptions.trigger_phase,
        )
        self.unschedule_cancellation = async_to_raw_response_wrapper(
            subscriptions.unschedule_cancellation,
        )
        self.unschedule_fixed_fee_quantity_updates = async_to_raw_response_wrapper(
            subscriptions.unschedule_fixed_fee_quantity_updates,
        )
        self.unschedule_pending_plan_changes = async_to_raw_response_wrapper(
            subscriptions.unschedule_pending_plan_changes,
        )
        self.update_fixed_fee_quantity = async_to_raw_response_wrapper(
            subscriptions.update_fixed_fee_quantity,
        )
