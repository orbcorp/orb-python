# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    subscription_list_params,
    subscription_cancel_params,
    subscription_create_params,
    subscription_update_params,
    subscription_fetch_costs_params,
    subscription_fetch_usage_params,
    subscription_update_trial_params,
    subscription_redeem_coupon_params,
    subscription_trigger_phase_params,
    subscription_fetch_schedule_params,
    subscription_price_intervals_params,
    subscription_schedule_plan_change_params,
    subscription_update_fixed_fee_quantity_params,
    subscription_unschedule_fixed_fee_quantity_updates_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.subscription import Subscription
from ..types.subscription_usage import SubscriptionUsage
from ..types.mutated_subscription import MutatedSubscription
from ..types.subscription_fetch_costs_response import SubscriptionFetchCostsResponse
from ..types.subscription_fetch_schedule_response import SubscriptionFetchScheduleResponse
from ..types.shared_params.billing_cycle_anchor_configuration import BillingCycleAnchorConfiguration

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return SubscriptionsWithStreamingResponse(self)

    def create(
        self,
        *,
        add_adjustments: Optional[Iterable[subscription_create_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[subscription_create_params.AddPrice]] | Omit = omit,
        align_billing_with_subscription_start_date: bool | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        aws_region: Optional[str] | Omit = omit,
        billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration] | Omit = omit,
        coupon_redemption_code: Optional[str] | Omit = omit,
        credits_overage_rate: Optional[float] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        default_invoice_memo: Optional[str] | Omit = omit,
        end_date: Union[str, datetime, None] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        external_marketplace: Optional[Literal["google", "aws", "azure"]] | Omit = omit,
        external_marketplace_reporting_id: Optional[str] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        initial_phase_order: Optional[int] | Omit = omit,
        invoicing_threshold: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        net_terms: Optional[int] | Omit = omit,
        per_credit_overage_amount: Optional[float] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        plan_version_number: Optional[int] | Omit = omit,
        price_overrides: Optional[Iterable[object]] | Omit = omit,
        remove_adjustments: Optional[Iterable[subscription_create_params.RemoveAdjustment]] | Omit = omit,
        remove_prices: Optional[Iterable[subscription_create_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[subscription_create_params.ReplaceAdjustment]] | Omit = omit,
        replace_prices: Optional[Iterable[subscription_create_params.ReplacePrice]] | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        trial_duration_days: Optional[int] | Omit = omit,
        usage_customer_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """A subscription represents the purchase of a plan by a customer.

        The customer is
        identified by either the `customer_id` or the `external_customer_id`, and
        exactly one of these fields must be provided.

        By default, subscriptions begin on the day that they're created and renew
        automatically for each billing cycle at the cadence that's configured in the
        plan definition.

        The default configuration for subscriptions in Orb is **In-advance billing** and
        **Beginning of month alignment** (see
        [Subscription](/core-concepts##subscription) for more details).

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

        ## Customize your customer's subscriptions

        Prices and adjustments in a plan can be added, removed, or replaced for the
        subscription being created. This is useful when a customer has prices that
        differ from the default prices for a specific plan.

        <Note>
        This feature is only available for accounts that have migrated to Subscription Overrides Version 2. You can find your
        Subscription Overrides Version at the bottom of your [Plans page](https://app.withorb.com/plans)
        </Note>

        ### Adding Prices

        To add prices, provide a list of objects with the key `add_prices`. An object in
        the list must specify an existing add-on price with a `price_id` or
        `external_price_id` field, or create a new add-on price by including an object
        with the key `price`, identical to what would be used in the request body for
        the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the price should be added to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. This is equivalent to creating a price interval with the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).
        If unspecified, the start or end date of the phase or subscription will be used.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference this price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Removing Prices

        To remove prices, provide a list of objects with the key `remove_prices`. An
        object in the list must specify a plan price with either a `price_id` or
        `external_price_id` field.

        ### Replacing Prices

        To replace prices, provide a list of objects with the key `replace_prices`. An
        object in the list must specify a plan price to replace with the
        `replaces_price_id` key, and it must specify a price to replace it with by
        either referencing an existing add-on price with a `price_id` or
        `external_price_id` field, or by creating a new add-on price by including an
        object with the key `price`, identical to what would be used in the request body
        for the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        For fixed fees, an object in the list can supply a `fixed_price_quantity`
        instead of a `price`, `price_id`, or `external_price_id` field. This will update
        only the quantity for the price, similar to the
        [Update price quantity](/api-reference/subscription/update-price-quantity)
        endpoint.

        The replacement price will have the same phase, if applicable, and the same
        start and end dates as the price it replaces.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference the replacement price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Adding adjustments

        To add adjustments, provide a list of objects with the key `add_adjustments`. An
        object in the list must include an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the adjustment should be added
        to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. If unspecified, the start or end date of the phase or subscription
        will be used.

        ### Removing adjustments

        To remove adjustments, provide a list of objects with the key
        `remove_adjustments`. An object in the list must include a key, `adjustment_id`,
        with the ID of the adjustment to be removed.

        ### Replacing adjustments

        To replace adjustments, provide a list of objects with the key
        `replace_adjustments`. An object in the list must specify a plan adjustment to
        replace with the `replaces_adjustment_id` key, and it must specify an adjustment
        to replace it with by including an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        The replacement adjustment will have the same phase, if applicable, and the same
        start and end dates as the adjustment it replaces.

        ## Price overrides (DEPRECATED)

        <Note>
        Price overrides are being phased out in favor adding/removing/replacing prices. (See
        [Customize your customer's subscriptions](/api-reference/subscription/create-subscription))
        </Note>

        Price overrides are used to update some or all prices in a plan for the specific
        subscription being created. This is useful when a new customer has negotiated a
        rate that is unique to the customer.

        To override prices, provide a list of objects with the key `price_overrides`.
        The price object in the list of overrides is expected to contain the existing
        price id, the `model_type` and configuration. (See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations.) The numerical values can be updated, but
        the billable metric, cadence, type, and name of a price can not be overridden.

        ### Maximums and Minimums

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

        ### Discounts

        Discounts, like price overrides, can be useful when a new customer has
        negotiated a new or different discount than the default for a price. If a
        discount exists for a price and a null discount is provided on creation, then
        there will be no discount on the new subscription.

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
        \\$$10.00 for a subscription that invoices in USD.

        Args:
          add_adjustments: Additional adjustments to be added to the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          add_prices: Additional prices to be added to the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          auto_collection: Determines whether issued invoices for this subscription will automatically be
              charged with the saved payment method on the due date. If not specified, this
              defaults to the behavior configured for this customer.

          coupon_redemption_code: Redemption code to be used for this subscription. If the coupon cannot be found
              by its redemption code, or cannot be redeemed, an error response will be
              returned and the subscription creation or plan change will not be scheduled.

          currency: The currency to use for the subscription. If not specified, the invoicing
              currency for the plan will be used.

          default_invoice_memo: Determines the default memo on this subscription's invoices. Note that if this
              is not provided, it is determined by the plan configuration.

          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          filter: An additional filter to apply to usage queries. This filter must be expressed as
              a boolean
              [computed property](/extensibility/advanced-metrics#computed-properties). If
              null, usage queries will not include any additional filter.

          initial_phase_order: The phase of the plan to start with

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          name: The name to use for the subscription. If not specified, the plan name will be
              used.

          net_terms: The net terms determines the difference between the invoice date and the issue
              date for the invoice. If you intend the invoice to be due on issue, set this
              to 0. If not provided, this defaults to the value specified in the plan.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          plan_version_number: Specifies which version of the plan to subscribe to. If null, the default
              version will be used.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          remove_adjustments: Plan adjustments to be removed from the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          remove_prices: Plan prices to be removed from the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          replace_adjustments: Plan adjustments to be replaced with additional adjustments on the subscription.
              (Only available for accounts that have migrated off of legacy subscription
              overrides)

          replace_prices: Plan prices to be replaced with additional prices on the subscription. (Only
              available for accounts that have migrated off of legacy subscription overrides)

          trial_duration_days: The duration of the trial period in days. If not provided, this defaults to the
              value specified in the plan. If `0` is provided, the trial on the plan will be
              skipped.

          usage_customer_ids: A list of customer IDs whose usage events will be aggregated and billed under
              this subscription. By default, a subscription only considers usage events
              associated with its attached customer's customer_id. When usage_customer_ids is
              provided, the subscription includes usage events from the specified customers
              only. Provided usage_customer_ids must be either the customer for this
              subscription itself, or any of that customer's children.

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
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "align_billing_with_subscription_start_date": align_billing_with_subscription_start_date,
                    "auto_collection": auto_collection,
                    "aws_region": aws_region,
                    "billing_cycle_anchor_configuration": billing_cycle_anchor_configuration,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "currency": currency,
                    "customer_id": customer_id,
                    "default_invoice_memo": default_invoice_memo,
                    "end_date": end_date,
                    "external_customer_id": external_customer_id,
                    "external_marketplace": external_marketplace,
                    "external_marketplace_reporting_id": external_marketplace_reporting_id,
                    "external_plan_id": external_plan_id,
                    "filter": filter,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "metadata": metadata,
                    "name": name,
                    "net_terms": net_terms,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "plan_version_number": plan_version_number,
                    "price_overrides": price_overrides,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                    "start_date": start_date,
                    "trial_duration_days": trial_duration_days,
                    "usage_customer_ids": usage_customer_ids,
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
            cast_to=MutatedSubscription,
        )

    def update(
        self,
        subscription_id: str,
        *,
        auto_collection: Optional[bool] | Omit = omit,
        default_invoice_memo: Optional[str] | Omit = omit,
        invoicing_threshold: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        net_terms: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to update the `metadata`, `net terms`,
        `auto_collection`, `invoicing_threshold`, and `default_invoice_memo` properties
        on a subscription.

        Args:
          auto_collection: Determines whether issued invoices for this subscription will automatically be
              charged with the saved payment method on the due date. This property defaults to
              the plan's behavior.

          default_invoice_memo: Determines the default memo on this subscription's invoices. Note that if this
              is not provided, it is determined by the plan configuration.

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          net_terms: Determines the difference between the invoice issue date for subscription
              invoices as the date that they are due. A value of `0` here represents that the
              invoice is due on issue, whereas a value of `30` represents that the customer
              has a month to pay the invoice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._put(
            f"/subscriptions/{subscription_id}",
            body=maybe_transform(
                {
                    "auto_collection": auto_collection,
                    "default_invoice_memo": default_invoice_memo,
                    "invoicing_threshold": invoicing_threshold,
                    "metadata": metadata,
                    "net_terms": net_terms,
                },
                subscription_update_params.SubscriptionUpdateParams,
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
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        customer_id: Optional[SequenceNotStr[str]] | Omit = omit,
        external_customer_id: Optional[SequenceNotStr[str]] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "ended", "upcoming"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Subscription]:
        """
        This endpoint returns a list of all subscriptions for an account as a
        [paginated](/api-reference/pagination) list, ordered starting from the most
        recently created subscription. For a full discussion of the subscription
        resource, see [Subscription](/core-concepts##subscription).

        Subscriptions can be filtered for a specific customer by using either the
        customer_id or external_customer_id query parameters. To filter subscriptions
        for multiple customers, use the customer_id[] or external_customer_id[] query
        parameters.

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
                        "external_plan_id": external_plan_id,
                        "limit": limit,
                        "plan_id": plan_id,
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
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        cancellation_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
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
        [cancellation behaviors](/product-catalog/creating-subscriptions#cancellation-behaviors).

        Args:
          cancel_option: Determines the timing of subscription cancellation

          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          cancellation_date: The date that the cancellation should take effect. This parameter can only be
              passed if the `cancel_option` is `requested_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/cancel",
            body=maybe_transform(
                {
                    "cancel_option": cancel_option,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
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
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        This endpoint is used to fetch a [Subscription](/core-concepts##subscription)
        given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
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
        currency: Optional[str] | Omit = omit,
        timeframe_end: Union[str, datetime, None] | Omit = omit,
        timeframe_start: Union[str, datetime, None] | Omit = omit,
        view_mode: Optional[Literal["periodic", "cumulative"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
          currency: The currency or custom pricing unit to use.

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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._get(
            f"/subscriptions/{subscription_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
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
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        start_date_gt: Union[str, datetime, None] | Omit = omit,
        start_date_gte: Union[str, datetime, None] | Omit = omit,
        start_date_lt: Union[str, datetime, None] | Omit = omit,
        start_date_lte: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[SubscriptionFetchScheduleResponse]:
        """
        This endpoint returns a [paginated](/api-reference/pagination) list of all plans
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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
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
        billable_metric_id: Optional[str] | Omit = omit,
        first_dimension_key: Optional[str] | Omit = omit,
        first_dimension_value: Optional[str] | Omit = omit,
        granularity: Optional[Literal["day"]] | Omit = omit,
        group_by: Optional[str] | Omit = omit,
        second_dimension_key: Optional[str] | Omit = omit,
        second_dimension_value: Optional[str] | Omit = omit,
        timeframe_end: Union[str, datetime, None] | Omit = omit,
        timeframe_start: Union[str, datetime, None] | Omit = omit,
        view_mode: Optional[Literal["periodic", "cumulative"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          granularity: This determines the windowing of usage reporting.

          group_by: Groups per-price usage by the key provided.

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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
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
                            "first_dimension_key": first_dimension_key,
                            "first_dimension_value": first_dimension_value,
                            "granularity": granularity,
                            "group_by": group_by,
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
        add: Iterable[subscription_price_intervals_params.Add] | Omit = omit,
        add_adjustments: Iterable[subscription_price_intervals_params.AddAdjustment] | Omit = omit,
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        can_defer_billing: Optional[bool] | Omit = omit,
        edit: Iterable[subscription_price_intervals_params.Edit] | Omit = omit,
        edit_adjustments: Iterable[subscription_price_intervals_params.EditAdjustment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        This endpoint is used to add and edit subscription
        [price intervals](/api-reference/price-interval/add-or-edit-price-intervals). By
        making modifications to a subscription’s price intervals, you can
        [flexibly and atomically control the billing behavior of a subscription](/product-catalog/modifying-subscriptions).

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

        ## Adjustment intervals

        An adjustment interval represents the time period that a particular adjustment
        (a discount, minimum, or maximum) applies to the prices on a subscription.
        Adjustment intervals can be added to a subscription by specifying them in the
        `add_adjustments` array, or modified via the `edit_adjustments` array. When
        creating an adjustment interval, you'll need to provide the definition of the
        new adjustment (the type of adjustment, and which prices it applies to), as well
        as the start and end dates for the adjustment interval. The start and end dates
        of an existing adjustment interval can be edited via the `edit_adjustments`
        field (just like price intervals). (To "change" the amount of a discount,
        minimum, or maximum, then, you'll need to end the existing interval, and create
        a new adjustment interval with the new amount and a start date that matches the
        end date of the previous interval.)

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

          add_adjustments: A list of adjustments to add to the subscription.

          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          can_defer_billing: If true, ending an in-arrears price interval mid-cycle will defer billing the
              final line itemuntil the next scheduled invoice. If false, it will be billed on
              its end date. If not provided, behaviorwill follow account default.

          edit: A list of price intervals to edit on the subscription.

          edit_adjustments: A list of adjustments to edit on the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/price_intervals",
            body=maybe_transform(
                {
                    "add": add,
                    "add_adjustments": add_adjustments,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "can_defer_billing": can_defer_billing,
                    "edit": edit,
                    "edit_adjustments": edit_adjustments,
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
            cast_to=MutatedSubscription,
        )

    def redeem_coupon(
        self,
        subscription_id: str,
        *,
        change_option: Literal["requested_date", "end_of_subscription_term", "immediate"],
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        change_date: Union[str, datetime, None] | Omit = omit,
        coupon_id: Optional[str] | Omit = omit,
        coupon_redemption_code: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        Redeem a coupon effective at a given time.

        Args:
          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          change_date: The date that the coupon discount should take effect. This parameter can only be
              passed if the `change_option` is `requested_date`.

          coupon_id: Coupon ID to be redeemed for this subscription.

          coupon_redemption_code: Redemption code of the coupon to be redeemed for this subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/redeem_coupon",
            body=maybe_transform(
                {
                    "change_option": change_option,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "change_date": change_date,
                    "coupon_id": coupon_id,
                    "coupon_redemption_code": coupon_redemption_code,
                },
                subscription_redeem_coupon_params.SubscriptionRedeemCouponParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
        )

    def schedule_plan_change(
        self,
        subscription_id: str,
        *,
        change_option: Literal["requested_date", "end_of_subscription_term", "immediate"],
        add_adjustments: Optional[Iterable[subscription_schedule_plan_change_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[subscription_schedule_plan_change_params.AddPrice]] | Omit = omit,
        align_billing_with_plan_change_date: Optional[bool] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]] | Omit = omit,
        billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration] | Omit = omit,
        change_date: Union[str, datetime, None] | Omit = omit,
        coupon_redemption_code: Optional[str] | Omit = omit,
        credits_overage_rate: Optional[float] | Omit = omit,
        default_invoice_memo: Optional[str] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        initial_phase_order: Optional[int] | Omit = omit,
        invoicing_threshold: Optional[str] | Omit = omit,
        net_terms: Optional[int] | Omit = omit,
        per_credit_overage_amount: Optional[float] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        plan_version_number: Optional[int] | Omit = omit,
        price_overrides: Optional[Iterable[object]] | Omit = omit,
        remove_adjustments: Optional[Iterable[subscription_schedule_plan_change_params.RemoveAdjustment]] | Omit = omit,
        remove_prices: Optional[Iterable[subscription_schedule_plan_change_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[subscription_schedule_plan_change_params.ReplaceAdjustment]]
        | Omit = omit,
        replace_prices: Optional[Iterable[subscription_schedule_plan_change_params.ReplacePrice]] | Omit = omit,
        trial_duration_days: Optional[int] | Omit = omit,
        usage_customer_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """This endpoint can be used to change an existing subscription's plan.

        It returns
        the serialized updated subscription object.

        The body parameter `change_option` determines when the plan change occurs. Orb
        supports three options:

        - `end_of_subscription_term`: changes the plan at the end of the existing plan's
          term.
          - Issuing this plan change request for a monthly subscription will keep the
            existing plan active until the start of the subsequent month. Issuing this
            plan change request for a yearly subscription will keep the existing plan
            active for the full year. Charges incurred in the remaining period will be
            invoiced as normal.
          - Example: The plan is billed monthly on the 1st of the month, the request is
            made on January 15th, so the plan will be changed on February 1st, and
            invoice will be issued on February 1st for the last month of the original
            plan.
        - `immediate`: changes the plan immediately.
          - Subscriptions that have their plan changed with this option will move to the
            new plan immediately, and be invoiced immediately.
          - This invoice will include any usage fees incurred in the billing period up
            to the change, along with any prorated recurring fees for the billing
            period, if applicable.
          - Example: The plan is billed monthly on the 1st of the month, the request is
            made on January 15th, so the plan will be changed on January 15th, and an
            invoice will be issued for the partial month, from January 1 to January 15,
            on the original plan.
        - `requested_date`: changes the plan on the requested date (`change_date`).
          - If no timezone is provided, the customer's timezone is used. The
            `change_date` body parameter is required if this option is chosen.
          - Example: The plan is billed monthly on the 1st of the month, the request is
            made on January 15th, with a requested `change_date` of February 15th, so
            the plan will be changed on February 15th, and invoices will be issued on
            February 1st and February 15th.

        Note that one of `plan_id` or `external_plan_id` is required in the request body
        for this operation.

        ## Customize your customer's subscriptions

        Prices and adjustments in a plan can be added, removed, or replaced on the
        subscription when you schedule the plan change. This is useful when a customer
        has prices that differ from the default prices for a specific plan.

        <Note>
        This feature is only available for accounts that have migrated to Subscription Overrides Version 2. You can find your
        Subscription Overrides Version at the bottom of your [Plans page](https://app.withorb.com/plans)
        </Note>

        ### Adding Prices

        To add prices, provide a list of objects with the key `add_prices`. An object in
        the list must specify an existing add-on price with a `price_id` or
        `external_price_id` field, or create a new add-on price by including an object
        with the key `price`, identical to what would be used in the request body for
        the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the price should be added to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. If `start_date` is unspecified, the start of the phase / plan change
        time will be used. If `end_date` is unspecified, it will finish at the end of
        the phase / have no end time.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference this price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Removing Prices

        To remove prices, provide a list of objects with the key `remove_prices`. An
        object in the list must specify a plan price with either a `price_id` or
        `external_price_id` field.

        ### Replacing Prices

        To replace prices, provide a list of objects with the key `replace_prices`. An
        object in the list must specify a plan price to replace with the
        `replaces_price_id` key, and it must specify a price to replace it with by
        either referencing an existing add-on price with a `price_id` or
        `external_price_id` field, or by creating a new add-on price by including an
        object with the key `price`, identical to what would be used in the request body
        for the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        For fixed fees, an object in the list can supply a `fixed_price_quantity`
        instead of a `price`, `price_id`, or `external_price_id` field. This will update
        only the quantity for the price, similar to the
        [Update price quantity](/api-reference/subscription/update-price-quantity)
        endpoint.

        The replacement price will have the same phase, if applicable, and the same
        start and end dates as the price it replaces.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference the replacement price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Adding adjustments

        To add adjustments, provide a list of objects with the key `add_adjustments`. An
        object in the list must include an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the adjustment should be added
        to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. If `start_date` is unspecified, the start of the phase / plan change
        time will be used. If `end_date` is unspecified, it will finish at the end of
        the phase / have no end time.

        ### Removing adjustments

        To remove adjustments, provide a list of objects with the key
        `remove_adjustments`. An object in the list must include a key, `adjustment_id`,
        with the ID of the adjustment to be removed.

        ### Replacing adjustments

        To replace adjustments, provide a list of objects with the key
        `replace_adjustments`. An object in the list must specify a plan adjustment to
        replace with the `replaces_adjustment_id` key, and it must specify an adjustment
        to replace it with by including an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        The replacement adjustment will have the same phase, if applicable, and the same
        start and end dates as the adjustment it replaces.

        ## Price overrides (DEPRECATED)

        <Note>
        Price overrides are being phased out in favor adding/removing/replacing prices. (See
        [Customize your customer's subscriptions](/api-reference/subscription/schedule-plan-change))
        </Note>

        Price overrides are used to update some or all prices in a plan for the specific
        subscription being created. This is useful when a new customer has negotiated a
        rate that is unique to the customer.

        To override prices, provide a list of objects with the key `price_overrides`.
        The price object in the list of overrides is expected to contain the existing
        price id, the `model_type` and configuration. (See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations.) The numerical values can be updated, but
        the billable metric, cadence, type, and name of a price can not be overridden.

        ### Maximums, and minimums

        Price overrides are used to update some or all prices in the target plan.
        Minimums and maximums, much like price overrides, can be useful when a new
        customer has negotiated a new or different minimum or maximum spend cap than the
        default for the plan. The request format for maximums and minimums is the same
        as those in [subscription creation](create-subscription).

        ## Scheduling multiple plan changes

        When scheduling multiple plan changes with the same date, the latest plan change
        on that day takes effect.

        ## Prorations for in-advance fees

        By default, Orb calculates the prorated difference in any fixed fees when making
        a plan change, adjusting the customer balance as needed. For details on this
        behavior, see
        [Modifying subscriptions](/product-catalog/modifying-subscriptions#prorations-for-in-advance-fees).

        Args:
          add_adjustments: Additional adjustments to be added to the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          add_prices: Additional prices to be added to the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          align_billing_with_plan_change_date: [DEPRECATED] Use billing_cycle_alignment instead. Reset billing periods to be
              aligned with the plan change's effective date.

          auto_collection: Determines whether issued invoices for this subscription will automatically be
              charged with the saved payment method on the due date. If not specified, this
              defaults to the behavior configured for this customer.

          billing_cycle_alignment: Reset billing periods to be aligned with the plan change's effective date or
              start of the month. Defaults to `unchanged` which keeps subscription's existing
              billing cycle alignment.

          change_date: The date that the plan change should take effect. This parameter can only be
              passed if the `change_option` is `requested_date`. If a date with no time is
              passed, the plan change will happen at midnight in the customer's timezone.

          coupon_redemption_code: Redemption code to be used for this subscription. If the coupon cannot be found
              by its redemption code, or cannot be redeemed, an error response will be
              returned and the subscription creation or plan change will not be scheduled.

          default_invoice_memo: Determines the default memo on this subscription's invoices. Note that if this
              is not provided, it is determined by the plan configuration.

          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          filter: An additional filter to apply to usage queries. This filter must be expressed as
              a boolean
              [computed property](/extensibility/advanced-metrics#computed-properties). If
              null, usage queries will not include any additional filter.

          initial_phase_order: The phase of the plan to start with

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          net_terms: The net terms determines the difference between the invoice date and the issue
              date for the invoice. If you intend the invoice to be due on issue, set this
              to 0. If not provided, this defaults to the value specified in the plan.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          plan_version_number: Specifies which version of the plan to change to. If null, the default version
              will be used.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          remove_adjustments: Plan adjustments to be removed from the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          remove_prices: Plan prices to be removed from the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          replace_adjustments: Plan adjustments to be replaced with additional adjustments on the subscription.
              (Only available for accounts that have migrated off of legacy subscription
              overrides)

          replace_prices: Plan prices to be replaced with additional prices on the subscription. (Only
              available for accounts that have migrated off of legacy subscription overrides)

          trial_duration_days: The duration of the trial period in days. If not provided, this defaults to the
              value specified in the plan. If `0` is provided, the trial on the plan will be
              skipped.

          usage_customer_ids: A list of customer IDs whose usage events will be aggregated and billed under
              this subscription. By default, a subscription only considers usage events
              associated with its attached customer's customer_id. When usage_customer_ids is
              provided, the subscription includes usage events from the specified customers
              only. Provided usage_customer_ids must be either the customer for this
              subscription itself, or any of that customer's children.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/schedule_plan_change",
            body=maybe_transform(
                {
                    "change_option": change_option,
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "align_billing_with_plan_change_date": align_billing_with_plan_change_date,
                    "auto_collection": auto_collection,
                    "billing_cycle_alignment": billing_cycle_alignment,
                    "billing_cycle_anchor_configuration": billing_cycle_anchor_configuration,
                    "change_date": change_date,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "default_invoice_memo": default_invoice_memo,
                    "external_plan_id": external_plan_id,
                    "filter": filter,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "net_terms": net_terms,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "plan_version_number": plan_version_number,
                    "price_overrides": price_overrides,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                    "trial_duration_days": trial_duration_days,
                    "usage_customer_ids": usage_customer_ids,
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
            cast_to=MutatedSubscription,
        )

    def trigger_phase(
        self,
        subscription_id: str,
        *,
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        effective_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        Manually trigger a phase, effective the given date (or the current time, if not
        specified).

        Args:
          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          effective_date: The date on which the phase change should take effect. If not provided, defaults
              to today in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/trigger_phase",
            body=maybe_transform(
                {
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "effective_date": effective_date,
                },
                subscription_trigger_phase_params.SubscriptionTriggerPhaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/unschedule_cancellation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        This endpoint can be used to clear scheduled updates to the quantity for a fixed
        fee.

        If there are no updates scheduled, a request validation error will be returned
        with a 400 status code.

        Args:
          price_id: Price for which the updates should be cleared. Must be a fixed fee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
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
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        This endpoint can be used to unschedule any pending plan changes on an existing
        subscription. When called, all upcoming plan changes will be unscheduled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/unschedule_pending_plan_changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
        )

    def update_fixed_fee_quantity(
        self,
        subscription_id: str,
        *,
        price_id: str,
        quantity: float,
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        change_option: Literal["immediate", "upcoming_invoice", "effective_date"] | Omit = omit,
        effective_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
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

          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          change_option: Determines when the change takes effect. Note that if `effective_date` is
              specified, this defaults to `effective_date`. Otherwise, this defaults to
              `immediate` unless it's explicitly set to `upcoming_invoice`.

          effective_date: The date that the quantity change should take effect, localized to the
              customer's timezone. If this parameter is not passed in, the quantity change is
              effective according to `change_option`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/update_fixed_fee_quantity",
            body=maybe_transform(
                {
                    "price_id": price_id,
                    "quantity": quantity,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
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
            cast_to=MutatedSubscription,
        )

    def update_trial(
        self,
        subscription_id: str,
        *,
        trial_end_date: Union[Union[str, datetime], Literal["immediate"]],
        shift: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """This endpoint is used to update the trial end date for a subscription.

        The new
        trial end date must be within the time range of the current plan (i.e. the new
        trial end date must be on or after the subscription's start date on the current
        plan, and on or before the subscription end date).

        In order to retroactively remove a trial completely, the end date can be set to
        the transition date of the subscription to this plan (or, if this is the first
        plan for this subscription, the subscription's start date). In order to end a
        trial immediately, the keyword `immediate` can be provided as the trial end
        date.

        By default, Orb will shift only the trial end date (and price intervals that
        start or end on the previous trial end date), and leave all other future price
        intervals untouched. If the `shift` parameter is set to `true`, Orb will shift
        all subsequent price and adjustment intervals by the same amount as the trial
        end date shift (so, e.g., if a plan change is scheduled or an add-on price was
        added, that change will be pushed back by the same amount of time the trial is
        extended).

        Args:
          trial_end_date: The new date that the trial should end, or the literal string `immediate` to end
              the trial immediately.

          shift: If true, shifts subsequent price and adjustment intervals (preserving their
              durations, but adjusting their absolute dates).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/subscriptions/{subscription_id}/update_trial",
            body=maybe_transform(
                {
                    "trial_end_date": trial_end_date,
                    "shift": shift,
                },
                subscription_update_trial_params.SubscriptionUpdateTrialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
        )


class AsyncSubscriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncSubscriptionsWithStreamingResponse(self)

    async def create(
        self,
        *,
        add_adjustments: Optional[Iterable[subscription_create_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[subscription_create_params.AddPrice]] | Omit = omit,
        align_billing_with_subscription_start_date: bool | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        aws_region: Optional[str] | Omit = omit,
        billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration] | Omit = omit,
        coupon_redemption_code: Optional[str] | Omit = omit,
        credits_overage_rate: Optional[float] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        default_invoice_memo: Optional[str] | Omit = omit,
        end_date: Union[str, datetime, None] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        external_marketplace: Optional[Literal["google", "aws", "azure"]] | Omit = omit,
        external_marketplace_reporting_id: Optional[str] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        initial_phase_order: Optional[int] | Omit = omit,
        invoicing_threshold: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        net_terms: Optional[int] | Omit = omit,
        per_credit_overage_amount: Optional[float] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        plan_version_number: Optional[int] | Omit = omit,
        price_overrides: Optional[Iterable[object]] | Omit = omit,
        remove_adjustments: Optional[Iterable[subscription_create_params.RemoveAdjustment]] | Omit = omit,
        remove_prices: Optional[Iterable[subscription_create_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[subscription_create_params.ReplaceAdjustment]] | Omit = omit,
        replace_prices: Optional[Iterable[subscription_create_params.ReplacePrice]] | Omit = omit,
        start_date: Union[str, datetime, None] | Omit = omit,
        trial_duration_days: Optional[int] | Omit = omit,
        usage_customer_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """A subscription represents the purchase of a plan by a customer.

        The customer is
        identified by either the `customer_id` or the `external_customer_id`, and
        exactly one of these fields must be provided.

        By default, subscriptions begin on the day that they're created and renew
        automatically for each billing cycle at the cadence that's configured in the
        plan definition.

        The default configuration for subscriptions in Orb is **In-advance billing** and
        **Beginning of month alignment** (see
        [Subscription](/core-concepts##subscription) for more details).

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

        ## Customize your customer's subscriptions

        Prices and adjustments in a plan can be added, removed, or replaced for the
        subscription being created. This is useful when a customer has prices that
        differ from the default prices for a specific plan.

        <Note>
        This feature is only available for accounts that have migrated to Subscription Overrides Version 2. You can find your
        Subscription Overrides Version at the bottom of your [Plans page](https://app.withorb.com/plans)
        </Note>

        ### Adding Prices

        To add prices, provide a list of objects with the key `add_prices`. An object in
        the list must specify an existing add-on price with a `price_id` or
        `external_price_id` field, or create a new add-on price by including an object
        with the key `price`, identical to what would be used in the request body for
        the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the price should be added to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. This is equivalent to creating a price interval with the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).
        If unspecified, the start or end date of the phase or subscription will be used.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference this price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Removing Prices

        To remove prices, provide a list of objects with the key `remove_prices`. An
        object in the list must specify a plan price with either a `price_id` or
        `external_price_id` field.

        ### Replacing Prices

        To replace prices, provide a list of objects with the key `replace_prices`. An
        object in the list must specify a plan price to replace with the
        `replaces_price_id` key, and it must specify a price to replace it with by
        either referencing an existing add-on price with a `price_id` or
        `external_price_id` field, or by creating a new add-on price by including an
        object with the key `price`, identical to what would be used in the request body
        for the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        For fixed fees, an object in the list can supply a `fixed_price_quantity`
        instead of a `price`, `price_id`, or `external_price_id` field. This will update
        only the quantity for the price, similar to the
        [Update price quantity](/api-reference/subscription/update-price-quantity)
        endpoint.

        The replacement price will have the same phase, if applicable, and the same
        start and end dates as the price it replaces.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference the replacement price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Adding adjustments

        To add adjustments, provide a list of objects with the key `add_adjustments`. An
        object in the list must include an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the adjustment should be added
        to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. If unspecified, the start or end date of the phase or subscription
        will be used.

        ### Removing adjustments

        To remove adjustments, provide a list of objects with the key
        `remove_adjustments`. An object in the list must include a key, `adjustment_id`,
        with the ID of the adjustment to be removed.

        ### Replacing adjustments

        To replace adjustments, provide a list of objects with the key
        `replace_adjustments`. An object in the list must specify a plan adjustment to
        replace with the `replaces_adjustment_id` key, and it must specify an adjustment
        to replace it with by including an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        The replacement adjustment will have the same phase, if applicable, and the same
        start and end dates as the adjustment it replaces.

        ## Price overrides (DEPRECATED)

        <Note>
        Price overrides are being phased out in favor adding/removing/replacing prices. (See
        [Customize your customer's subscriptions](/api-reference/subscription/create-subscription))
        </Note>

        Price overrides are used to update some or all prices in a plan for the specific
        subscription being created. This is useful when a new customer has negotiated a
        rate that is unique to the customer.

        To override prices, provide a list of objects with the key `price_overrides`.
        The price object in the list of overrides is expected to contain the existing
        price id, the `model_type` and configuration. (See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations.) The numerical values can be updated, but
        the billable metric, cadence, type, and name of a price can not be overridden.

        ### Maximums and Minimums

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

        ### Discounts

        Discounts, like price overrides, can be useful when a new customer has
        negotiated a new or different discount than the default for a price. If a
        discount exists for a price and a null discount is provided on creation, then
        there will be no discount on the new subscription.

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
        \\$$10.00 for a subscription that invoices in USD.

        Args:
          add_adjustments: Additional adjustments to be added to the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          add_prices: Additional prices to be added to the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          auto_collection: Determines whether issued invoices for this subscription will automatically be
              charged with the saved payment method on the due date. If not specified, this
              defaults to the behavior configured for this customer.

          coupon_redemption_code: Redemption code to be used for this subscription. If the coupon cannot be found
              by its redemption code, or cannot be redeemed, an error response will be
              returned and the subscription creation or plan change will not be scheduled.

          currency: The currency to use for the subscription. If not specified, the invoicing
              currency for the plan will be used.

          default_invoice_memo: Determines the default memo on this subscription's invoices. Note that if this
              is not provided, it is determined by the plan configuration.

          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          filter: An additional filter to apply to usage queries. This filter must be expressed as
              a boolean
              [computed property](/extensibility/advanced-metrics#computed-properties). If
              null, usage queries will not include any additional filter.

          initial_phase_order: The phase of the plan to start with

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          name: The name to use for the subscription. If not specified, the plan name will be
              used.

          net_terms: The net terms determines the difference between the invoice date and the issue
              date for the invoice. If you intend the invoice to be due on issue, set this
              to 0. If not provided, this defaults to the value specified in the plan.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          plan_version_number: Specifies which version of the plan to subscribe to. If null, the default
              version will be used.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          remove_adjustments: Plan adjustments to be removed from the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          remove_prices: Plan prices to be removed from the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          replace_adjustments: Plan adjustments to be replaced with additional adjustments on the subscription.
              (Only available for accounts that have migrated off of legacy subscription
              overrides)

          replace_prices: Plan prices to be replaced with additional prices on the subscription. (Only
              available for accounts that have migrated off of legacy subscription overrides)

          trial_duration_days: The duration of the trial period in days. If not provided, this defaults to the
              value specified in the plan. If `0` is provided, the trial on the plan will be
              skipped.

          usage_customer_ids: A list of customer IDs whose usage events will be aggregated and billed under
              this subscription. By default, a subscription only considers usage events
              associated with its attached customer's customer_id. When usage_customer_ids is
              provided, the subscription includes usage events from the specified customers
              only. Provided usage_customer_ids must be either the customer for this
              subscription itself, or any of that customer's children.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/subscriptions",
            body=await async_maybe_transform(
                {
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "align_billing_with_subscription_start_date": align_billing_with_subscription_start_date,
                    "auto_collection": auto_collection,
                    "aws_region": aws_region,
                    "billing_cycle_anchor_configuration": billing_cycle_anchor_configuration,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "currency": currency,
                    "customer_id": customer_id,
                    "default_invoice_memo": default_invoice_memo,
                    "end_date": end_date,
                    "external_customer_id": external_customer_id,
                    "external_marketplace": external_marketplace,
                    "external_marketplace_reporting_id": external_marketplace_reporting_id,
                    "external_plan_id": external_plan_id,
                    "filter": filter,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "metadata": metadata,
                    "name": name,
                    "net_terms": net_terms,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "plan_version_number": plan_version_number,
                    "price_overrides": price_overrides,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                    "start_date": start_date,
                    "trial_duration_days": trial_duration_days,
                    "usage_customer_ids": usage_customer_ids,
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
            cast_to=MutatedSubscription,
        )

    async def update(
        self,
        subscription_id: str,
        *,
        auto_collection: Optional[bool] | Omit = omit,
        default_invoice_memo: Optional[str] | Omit = omit,
        invoicing_threshold: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        net_terms: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Subscription:
        """
        This endpoint can be used to update the `metadata`, `net terms`,
        `auto_collection`, `invoicing_threshold`, and `default_invoice_memo` properties
        on a subscription.

        Args:
          auto_collection: Determines whether issued invoices for this subscription will automatically be
              charged with the saved payment method on the due date. This property defaults to
              the plan's behavior.

          default_invoice_memo: Determines the default memo on this subscription's invoices. Note that if this
              is not provided, it is determined by the plan configuration.

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          net_terms: Determines the difference between the invoice issue date for subscription
              invoices as the date that they are due. A value of `0` here represents that the
              invoice is due on issue, whereas a value of `30` represents that the customer
              has a month to pay the invoice.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._put(
            f"/subscriptions/{subscription_id}",
            body=await async_maybe_transform(
                {
                    "auto_collection": auto_collection,
                    "default_invoice_memo": default_invoice_memo,
                    "invoicing_threshold": invoicing_threshold,
                    "metadata": metadata,
                    "net_terms": net_terms,
                },
                subscription_update_params.SubscriptionUpdateParams,
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
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        customer_id: Optional[SequenceNotStr[str]] | Omit = omit,
        external_customer_id: Optional[SequenceNotStr[str]] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        status: Optional[Literal["active", "ended", "upcoming"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Subscription, AsyncPage[Subscription]]:
        """
        This endpoint returns a list of all subscriptions for an account as a
        [paginated](/api-reference/pagination) list, ordered starting from the most
        recently created subscription. For a full discussion of the subscription
        resource, see [Subscription](/core-concepts##subscription).

        Subscriptions can be filtered for a specific customer by using either the
        customer_id or external_customer_id query parameters. To filter subscriptions
        for multiple customers, use the customer_id[] or external_customer_id[] query
        parameters.

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
                        "external_plan_id": external_plan_id,
                        "limit": limit,
                        "plan_id": plan_id,
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
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        cancellation_date: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
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
        [cancellation behaviors](/product-catalog/creating-subscriptions#cancellation-behaviors).

        Args:
          cancel_option: Determines the timing of subscription cancellation

          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          cancellation_date: The date that the cancellation should take effect. This parameter can only be
              passed if the `cancel_option` is `requested_date`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/cancel",
            body=await async_maybe_transform(
                {
                    "cancel_option": cancel_option,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
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
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Subscription:
        """
        This endpoint is used to fetch a [Subscription](/core-concepts##subscription)
        given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
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
        currency: Optional[str] | Omit = omit,
        timeframe_end: Union[str, datetime, None] | Omit = omit,
        timeframe_start: Union[str, datetime, None] | Omit = omit,
        view_mode: Optional[Literal["periodic", "cumulative"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
          currency: The currency or custom pricing unit to use.

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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._get(
            f"/subscriptions/{subscription_id}/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency": currency,
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
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        start_date_gt: Union[str, datetime, None] | Omit = omit,
        start_date_gte: Union[str, datetime, None] | Omit = omit,
        start_date_lt: Union[str, datetime, None] | Omit = omit,
        start_date_lte: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SubscriptionFetchScheduleResponse, AsyncPage[SubscriptionFetchScheduleResponse]]:
        """
        This endpoint returns a [paginated](/api-reference/pagination) list of all plans
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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
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
        billable_metric_id: Optional[str] | Omit = omit,
        first_dimension_key: Optional[str] | Omit = omit,
        first_dimension_value: Optional[str] | Omit = omit,
        granularity: Optional[Literal["day"]] | Omit = omit,
        group_by: Optional[str] | Omit = omit,
        second_dimension_key: Optional[str] | Omit = omit,
        second_dimension_value: Optional[str] | Omit = omit,
        timeframe_end: Union[str, datetime, None] | Omit = omit,
        timeframe_start: Union[str, datetime, None] | Omit = omit,
        view_mode: Optional[Literal["periodic", "cumulative"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          granularity: This determines the windowing of usage reporting.

          group_by: Groups per-price usage by the key provided.

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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return cast(
            SubscriptionUsage,
            await self._get(
                f"/subscriptions/{subscription_id}/usage",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "billable_metric_id": billable_metric_id,
                            "first_dimension_key": first_dimension_key,
                            "first_dimension_value": first_dimension_value,
                            "granularity": granularity,
                            "group_by": group_by,
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
        add: Iterable[subscription_price_intervals_params.Add] | Omit = omit,
        add_adjustments: Iterable[subscription_price_intervals_params.AddAdjustment] | Omit = omit,
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        can_defer_billing: Optional[bool] | Omit = omit,
        edit: Iterable[subscription_price_intervals_params.Edit] | Omit = omit,
        edit_adjustments: Iterable[subscription_price_intervals_params.EditAdjustment] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        This endpoint is used to add and edit subscription
        [price intervals](/api-reference/price-interval/add-or-edit-price-intervals). By
        making modifications to a subscription’s price intervals, you can
        [flexibly and atomically control the billing behavior of a subscription](/product-catalog/modifying-subscriptions).

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

        ## Adjustment intervals

        An adjustment interval represents the time period that a particular adjustment
        (a discount, minimum, or maximum) applies to the prices on a subscription.
        Adjustment intervals can be added to a subscription by specifying them in the
        `add_adjustments` array, or modified via the `edit_adjustments` array. When
        creating an adjustment interval, you'll need to provide the definition of the
        new adjustment (the type of adjustment, and which prices it applies to), as well
        as the start and end dates for the adjustment interval. The start and end dates
        of an existing adjustment interval can be edited via the `edit_adjustments`
        field (just like price intervals). (To "change" the amount of a discount,
        minimum, or maximum, then, you'll need to end the existing interval, and create
        a new adjustment interval with the new amount and a start date that matches the
        end date of the previous interval.)

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

          add_adjustments: A list of adjustments to add to the subscription.

          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          can_defer_billing: If true, ending an in-arrears price interval mid-cycle will defer billing the
              final line itemuntil the next scheduled invoice. If false, it will be billed on
              its end date. If not provided, behaviorwill follow account default.

          edit: A list of price intervals to edit on the subscription.

          edit_adjustments: A list of adjustments to edit on the subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/price_intervals",
            body=await async_maybe_transform(
                {
                    "add": add,
                    "add_adjustments": add_adjustments,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "can_defer_billing": can_defer_billing,
                    "edit": edit,
                    "edit_adjustments": edit_adjustments,
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
            cast_to=MutatedSubscription,
        )

    async def redeem_coupon(
        self,
        subscription_id: str,
        *,
        change_option: Literal["requested_date", "end_of_subscription_term", "immediate"],
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        change_date: Union[str, datetime, None] | Omit = omit,
        coupon_id: Optional[str] | Omit = omit,
        coupon_redemption_code: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        Redeem a coupon effective at a given time.

        Args:
          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          change_date: The date that the coupon discount should take effect. This parameter can only be
              passed if the `change_option` is `requested_date`.

          coupon_id: Coupon ID to be redeemed for this subscription.

          coupon_redemption_code: Redemption code of the coupon to be redeemed for this subscription.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/redeem_coupon",
            body=await async_maybe_transform(
                {
                    "change_option": change_option,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "change_date": change_date,
                    "coupon_id": coupon_id,
                    "coupon_redemption_code": coupon_redemption_code,
                },
                subscription_redeem_coupon_params.SubscriptionRedeemCouponParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
        )

    async def schedule_plan_change(
        self,
        subscription_id: str,
        *,
        change_option: Literal["requested_date", "end_of_subscription_term", "immediate"],
        add_adjustments: Optional[Iterable[subscription_schedule_plan_change_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[subscription_schedule_plan_change_params.AddPrice]] | Omit = omit,
        align_billing_with_plan_change_date: Optional[bool] | Omit = omit,
        auto_collection: Optional[bool] | Omit = omit,
        billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]] | Omit = omit,
        billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration] | Omit = omit,
        change_date: Union[str, datetime, None] | Omit = omit,
        coupon_redemption_code: Optional[str] | Omit = omit,
        credits_overage_rate: Optional[float] | Omit = omit,
        default_invoice_memo: Optional[str] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        initial_phase_order: Optional[int] | Omit = omit,
        invoicing_threshold: Optional[str] | Omit = omit,
        net_terms: Optional[int] | Omit = omit,
        per_credit_overage_amount: Optional[float] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        plan_version_number: Optional[int] | Omit = omit,
        price_overrides: Optional[Iterable[object]] | Omit = omit,
        remove_adjustments: Optional[Iterable[subscription_schedule_plan_change_params.RemoveAdjustment]] | Omit = omit,
        remove_prices: Optional[Iterable[subscription_schedule_plan_change_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[subscription_schedule_plan_change_params.ReplaceAdjustment]]
        | Omit = omit,
        replace_prices: Optional[Iterable[subscription_schedule_plan_change_params.ReplacePrice]] | Omit = omit,
        trial_duration_days: Optional[int] | Omit = omit,
        usage_customer_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """This endpoint can be used to change an existing subscription's plan.

        It returns
        the serialized updated subscription object.

        The body parameter `change_option` determines when the plan change occurs. Orb
        supports three options:

        - `end_of_subscription_term`: changes the plan at the end of the existing plan's
          term.
          - Issuing this plan change request for a monthly subscription will keep the
            existing plan active until the start of the subsequent month. Issuing this
            plan change request for a yearly subscription will keep the existing plan
            active for the full year. Charges incurred in the remaining period will be
            invoiced as normal.
          - Example: The plan is billed monthly on the 1st of the month, the request is
            made on January 15th, so the plan will be changed on February 1st, and
            invoice will be issued on February 1st for the last month of the original
            plan.
        - `immediate`: changes the plan immediately.
          - Subscriptions that have their plan changed with this option will move to the
            new plan immediately, and be invoiced immediately.
          - This invoice will include any usage fees incurred in the billing period up
            to the change, along with any prorated recurring fees for the billing
            period, if applicable.
          - Example: The plan is billed monthly on the 1st of the month, the request is
            made on January 15th, so the plan will be changed on January 15th, and an
            invoice will be issued for the partial month, from January 1 to January 15,
            on the original plan.
        - `requested_date`: changes the plan on the requested date (`change_date`).
          - If no timezone is provided, the customer's timezone is used. The
            `change_date` body parameter is required if this option is chosen.
          - Example: The plan is billed monthly on the 1st of the month, the request is
            made on January 15th, with a requested `change_date` of February 15th, so
            the plan will be changed on February 15th, and invoices will be issued on
            February 1st and February 15th.

        Note that one of `plan_id` or `external_plan_id` is required in the request body
        for this operation.

        ## Customize your customer's subscriptions

        Prices and adjustments in a plan can be added, removed, or replaced on the
        subscription when you schedule the plan change. This is useful when a customer
        has prices that differ from the default prices for a specific plan.

        <Note>
        This feature is only available for accounts that have migrated to Subscription Overrides Version 2. You can find your
        Subscription Overrides Version at the bottom of your [Plans page](https://app.withorb.com/plans)
        </Note>

        ### Adding Prices

        To add prices, provide a list of objects with the key `add_prices`. An object in
        the list must specify an existing add-on price with a `price_id` or
        `external_price_id` field, or create a new add-on price by including an object
        with the key `price`, identical to what would be used in the request body for
        the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the price should be added to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. If `start_date` is unspecified, the start of the phase / plan change
        time will be used. If `end_date` is unspecified, it will finish at the end of
        the phase / have no end time.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference this price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Removing Prices

        To remove prices, provide a list of objects with the key `remove_prices`. An
        object in the list must specify a plan price with either a `price_id` or
        `external_price_id` field.

        ### Replacing Prices

        To replace prices, provide a list of objects with the key `replace_prices`. An
        object in the list must specify a plan price to replace with the
        `replaces_price_id` key, and it must specify a price to replace it with by
        either referencing an existing add-on price with a `price_id` or
        `external_price_id` field, or by creating a new add-on price by including an
        object with the key `price`, identical to what would be used in the request body
        for the [create price endpoint](/api-reference/price/create-price). See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations possible in this object.

        For fixed fees, an object in the list can supply a `fixed_price_quantity`
        instead of a `price`, `price_id`, or `external_price_id` field. This will update
        only the quantity for the price, similar to the
        [Update price quantity](/api-reference/subscription/update-price-quantity)
        endpoint.

        The replacement price will have the same phase, if applicable, and the same
        start and end dates as the price it replaces.

        An object in the list can specify an optional `minimum_amount`,
        `maximum_amount`, or `discounts`. This will create adjustments which apply only
        to this price.

        Additionally, an object in the list can specify an optional `reference_id`. This
        ID can be used to reference the replacement price when
        [adding an adjustment](#adding-adjustments) in the same API call. However the ID
        is _transient_ and cannot be used to refer to the price in future API calls.

        ### Adding adjustments

        To add adjustments, provide a list of objects with the key `add_adjustments`. An
        object in the list must include an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        If the plan has phases, each object in the list must include a number with
        `plan_phase_order` key to indicate which phase the adjustment should be added
        to.

        An object in the list can specify an optional `start_date` and optional
        `end_date`. If `start_date` is unspecified, the start of the phase / plan change
        time will be used. If `end_date` is unspecified, it will finish at the end of
        the phase / have no end time.

        ### Removing adjustments

        To remove adjustments, provide a list of objects with the key
        `remove_adjustments`. An object in the list must include a key, `adjustment_id`,
        with the ID of the adjustment to be removed.

        ### Replacing adjustments

        To replace adjustments, provide a list of objects with the key
        `replace_adjustments`. An object in the list must specify a plan adjustment to
        replace with the `replaces_adjustment_id` key, and it must specify an adjustment
        to replace it with by including an object with the key `adjustment`, identical
        to the adjustment object in the
        [add/edit price intervals endpoint](/api-reference/price-interval/add-or-edit-price-intervals).

        The replacement adjustment will have the same phase, if applicable, and the same
        start and end dates as the adjustment it replaces.

        ## Price overrides (DEPRECATED)

        <Note>
        Price overrides are being phased out in favor adding/removing/replacing prices. (See
        [Customize your customer's subscriptions](/api-reference/subscription/schedule-plan-change))
        </Note>

        Price overrides are used to update some or all prices in a plan for the specific
        subscription being created. This is useful when a new customer has negotiated a
        rate that is unique to the customer.

        To override prices, provide a list of objects with the key `price_overrides`.
        The price object in the list of overrides is expected to contain the existing
        price id, the `model_type` and configuration. (See the
        [Price resource](/product-catalog/price-configuration) for the specification of
        different price model configurations.) The numerical values can be updated, but
        the billable metric, cadence, type, and name of a price can not be overridden.

        ### Maximums, and minimums

        Price overrides are used to update some or all prices in the target plan.
        Minimums and maximums, much like price overrides, can be useful when a new
        customer has negotiated a new or different minimum or maximum spend cap than the
        default for the plan. The request format for maximums and minimums is the same
        as those in [subscription creation](create-subscription).

        ## Scheduling multiple plan changes

        When scheduling multiple plan changes with the same date, the latest plan change
        on that day takes effect.

        ## Prorations for in-advance fees

        By default, Orb calculates the prorated difference in any fixed fees when making
        a plan change, adjusting the customer balance as needed. For details on this
        behavior, see
        [Modifying subscriptions](/product-catalog/modifying-subscriptions#prorations-for-in-advance-fees).

        Args:
          add_adjustments: Additional adjustments to be added to the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          add_prices: Additional prices to be added to the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          align_billing_with_plan_change_date: [DEPRECATED] Use billing_cycle_alignment instead. Reset billing periods to be
              aligned with the plan change's effective date.

          auto_collection: Determines whether issued invoices for this subscription will automatically be
              charged with the saved payment method on the due date. If not specified, this
              defaults to the behavior configured for this customer.

          billing_cycle_alignment: Reset billing periods to be aligned with the plan change's effective date or
              start of the month. Defaults to `unchanged` which keeps subscription's existing
              billing cycle alignment.

          change_date: The date that the plan change should take effect. This parameter can only be
              passed if the `change_option` is `requested_date`. If a date with no time is
              passed, the plan change will happen at midnight in the customer's timezone.

          coupon_redemption_code: Redemption code to be used for this subscription. If the coupon cannot be found
              by its redemption code, or cannot be redeemed, an error response will be
              returned and the subscription creation or plan change will not be scheduled.

          default_invoice_memo: Determines the default memo on this subscription's invoices. Note that if this
              is not provided, it is determined by the plan configuration.

          external_plan_id: The external_plan_id of the plan that the given subscription should be switched
              to. Note that either this property or `plan_id` must be specified.

          filter: An additional filter to apply to usage queries. This filter must be expressed as
              a boolean
              [computed property](/extensibility/advanced-metrics#computed-properties). If
              null, usage queries will not include any additional filter.

          initial_phase_order: The phase of the plan to start with

          invoicing_threshold: When this subscription's accrued usage reaches this threshold, an invoice will
              be issued for the subscription. If not specified, invoices will only be issued
              at the end of the billing period.

          net_terms: The net terms determines the difference between the invoice date and the issue
              date for the invoice. If you intend the invoice to be due on issue, set this
              to 0. If not provided, this defaults to the value specified in the plan.

          plan_id: The plan that the given subscription should be switched to. Note that either
              this property or `external_plan_id` must be specified.

          plan_version_number: Specifies which version of the plan to change to. If null, the default version
              will be used.

          price_overrides: Optionally provide a list of overrides for prices on the plan

          remove_adjustments: Plan adjustments to be removed from the subscription. (Only available for
              accounts that have migrated off of legacy subscription overrides)

          remove_prices: Plan prices to be removed from the subscription. (Only available for accounts
              that have migrated off of legacy subscription overrides)

          replace_adjustments: Plan adjustments to be replaced with additional adjustments on the subscription.
              (Only available for accounts that have migrated off of legacy subscription
              overrides)

          replace_prices: Plan prices to be replaced with additional prices on the subscription. (Only
              available for accounts that have migrated off of legacy subscription overrides)

          trial_duration_days: The duration of the trial period in days. If not provided, this defaults to the
              value specified in the plan. If `0` is provided, the trial on the plan will be
              skipped.

          usage_customer_ids: A list of customer IDs whose usage events will be aggregated and billed under
              this subscription. By default, a subscription only considers usage events
              associated with its attached customer's customer_id. When usage_customer_ids is
              provided, the subscription includes usage events from the specified customers
              only. Provided usage_customer_ids must be either the customer for this
              subscription itself, or any of that customer's children.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/schedule_plan_change",
            body=await async_maybe_transform(
                {
                    "change_option": change_option,
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "align_billing_with_plan_change_date": align_billing_with_plan_change_date,
                    "auto_collection": auto_collection,
                    "billing_cycle_alignment": billing_cycle_alignment,
                    "billing_cycle_anchor_configuration": billing_cycle_anchor_configuration,
                    "change_date": change_date,
                    "coupon_redemption_code": coupon_redemption_code,
                    "credits_overage_rate": credits_overage_rate,
                    "default_invoice_memo": default_invoice_memo,
                    "external_plan_id": external_plan_id,
                    "filter": filter,
                    "initial_phase_order": initial_phase_order,
                    "invoicing_threshold": invoicing_threshold,
                    "net_terms": net_terms,
                    "per_credit_overage_amount": per_credit_overage_amount,
                    "plan_id": plan_id,
                    "plan_version_number": plan_version_number,
                    "price_overrides": price_overrides,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                    "trial_duration_days": trial_duration_days,
                    "usage_customer_ids": usage_customer_ids,
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
            cast_to=MutatedSubscription,
        )

    async def trigger_phase(
        self,
        subscription_id: str,
        *,
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        effective_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        Manually trigger a phase, effective the given date (or the current time, if not
        specified).

        Args:
          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          effective_date: The date on which the phase change should take effect. If not provided, defaults
              to today in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/trigger_phase",
            body=await async_maybe_transform(
                {
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "effective_date": effective_date,
                },
                subscription_trigger_phase_params.SubscriptionTriggerPhaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
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
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/unschedule_cancellation",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        This endpoint can be used to clear scheduled updates to the quantity for a fixed
        fee.

        If there are no updates scheduled, a request validation error will be returned
        with a 400 status code.

        Args:
          price_id: Price for which the updates should be cleared. Must be a fixed fee.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/unschedule_fixed_fee_quantity_updates",
            body=await async_maybe_transform(
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
            cast_to=MutatedSubscription,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """
        This endpoint can be used to unschedule any pending plan changes on an existing
        subscription. When called, all upcoming plan changes will be unscheduled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/unschedule_pending_plan_changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
        )

    async def update_fixed_fee_quantity(
        self,
        subscription_id: str,
        *,
        price_id: str,
        quantity: float,
        allow_invoice_credit_or_void: Optional[bool] | Omit = omit,
        change_option: Literal["immediate", "upcoming_invoice", "effective_date"] | Omit = omit,
        effective_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
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

          allow_invoice_credit_or_void: If false, this request will fail if it would void an issued invoice or create a
              credit note. Consider using this as a safety mechanism if you do not expect
              existing invoices to be changed.

          change_option: Determines when the change takes effect. Note that if `effective_date` is
              specified, this defaults to `effective_date`. Otherwise, this defaults to
              `immediate` unless it's explicitly set to `upcoming_invoice`.

          effective_date: The date that the quantity change should take effect, localized to the
              customer's timezone. If this parameter is not passed in, the quantity change is
              effective according to `change_option`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/update_fixed_fee_quantity",
            body=await async_maybe_transform(
                {
                    "price_id": price_id,
                    "quantity": quantity,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
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
            cast_to=MutatedSubscription,
        )

    async def update_trial(
        self,
        subscription_id: str,
        *,
        trial_end_date: Union[Union[str, datetime], Literal["immediate"]],
        shift: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MutatedSubscription:
        """This endpoint is used to update the trial end date for a subscription.

        The new
        trial end date must be within the time range of the current plan (i.e. the new
        trial end date must be on or after the subscription's start date on the current
        plan, and on or before the subscription end date).

        In order to retroactively remove a trial completely, the end date can be set to
        the transition date of the subscription to this plan (or, if this is the first
        plan for this subscription, the subscription's start date). In order to end a
        trial immediately, the keyword `immediate` can be provided as the trial end
        date.

        By default, Orb will shift only the trial end date (and price intervals that
        start or end on the previous trial end date), and leave all other future price
        intervals untouched. If the `shift` parameter is set to `true`, Orb will shift
        all subsequent price and adjustment intervals by the same amount as the trial
        end date shift (so, e.g., if a plan change is scheduled or an add-on price was
        added, that change will be pushed back by the same amount of time the trial is
        extended).

        Args:
          trial_end_date: The new date that the trial should end, or the literal string `immediate` to end
              the trial immediately.

          shift: If true, shifts subsequent price and adjustment intervals (preserving their
              durations, but adjusting their absolute dates).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/subscriptions/{subscription_id}/update_trial",
            body=await async_maybe_transform(
                {
                    "trial_end_date": trial_end_date,
                    "shift": shift,
                },
                subscription_update_trial_params.SubscriptionUpdateTrialParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MutatedSubscription,
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = _legacy_response.to_raw_response_wrapper(
            subscriptions.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            subscriptions.list,
        )
        self.cancel = _legacy_response.to_raw_response_wrapper(
            subscriptions.cancel,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            subscriptions.fetch,
        )
        self.fetch_costs = _legacy_response.to_raw_response_wrapper(
            subscriptions.fetch_costs,
        )
        self.fetch_schedule = _legacy_response.to_raw_response_wrapper(
            subscriptions.fetch_schedule,
        )
        self.fetch_usage = _legacy_response.to_raw_response_wrapper(
            subscriptions.fetch_usage,
        )
        self.price_intervals = _legacy_response.to_raw_response_wrapper(
            subscriptions.price_intervals,
        )
        self.redeem_coupon = _legacy_response.to_raw_response_wrapper(
            subscriptions.redeem_coupon,
        )
        self.schedule_plan_change = _legacy_response.to_raw_response_wrapper(
            subscriptions.schedule_plan_change,
        )
        self.trigger_phase = _legacy_response.to_raw_response_wrapper(
            subscriptions.trigger_phase,
        )
        self.unschedule_cancellation = _legacy_response.to_raw_response_wrapper(
            subscriptions.unschedule_cancellation,
        )
        self.unschedule_fixed_fee_quantity_updates = _legacy_response.to_raw_response_wrapper(
            subscriptions.unschedule_fixed_fee_quantity_updates,
        )
        self.unschedule_pending_plan_changes = _legacy_response.to_raw_response_wrapper(
            subscriptions.unschedule_pending_plan_changes,
        )
        self.update_fixed_fee_quantity = _legacy_response.to_raw_response_wrapper(
            subscriptions.update_fixed_fee_quantity,
        )
        self.update_trial = _legacy_response.to_raw_response_wrapper(
            subscriptions.update_trial,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.cancel = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.cancel,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.fetch,
        )
        self.fetch_costs = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.fetch_costs,
        )
        self.fetch_schedule = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.fetch_schedule,
        )
        self.fetch_usage = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.fetch_usage,
        )
        self.price_intervals = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.price_intervals,
        )
        self.redeem_coupon = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.redeem_coupon,
        )
        self.schedule_plan_change = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.schedule_plan_change,
        )
        self.trigger_phase = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.trigger_phase,
        )
        self.unschedule_cancellation = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.unschedule_cancellation,
        )
        self.unschedule_fixed_fee_quantity_updates = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.unschedule_fixed_fee_quantity_updates,
        )
        self.unschedule_pending_plan_changes = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.unschedule_pending_plan_changes,
        )
        self.update_fixed_fee_quantity = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.update_fixed_fee_quantity,
        )
        self.update_trial = _legacy_response.async_to_raw_response_wrapper(
            subscriptions.update_trial,
        )


class SubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.update = to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.cancel = to_streamed_response_wrapper(
            subscriptions.cancel,
        )
        self.fetch = to_streamed_response_wrapper(
            subscriptions.fetch,
        )
        self.fetch_costs = to_streamed_response_wrapper(
            subscriptions.fetch_costs,
        )
        self.fetch_schedule = to_streamed_response_wrapper(
            subscriptions.fetch_schedule,
        )
        self.fetch_usage = to_streamed_response_wrapper(
            subscriptions.fetch_usage,
        )
        self.price_intervals = to_streamed_response_wrapper(
            subscriptions.price_intervals,
        )
        self.redeem_coupon = to_streamed_response_wrapper(
            subscriptions.redeem_coupon,
        )
        self.schedule_plan_change = to_streamed_response_wrapper(
            subscriptions.schedule_plan_change,
        )
        self.trigger_phase = to_streamed_response_wrapper(
            subscriptions.trigger_phase,
        )
        self.unschedule_cancellation = to_streamed_response_wrapper(
            subscriptions.unschedule_cancellation,
        )
        self.unschedule_fixed_fee_quantity_updates = to_streamed_response_wrapper(
            subscriptions.unschedule_fixed_fee_quantity_updates,
        )
        self.unschedule_pending_plan_changes = to_streamed_response_wrapper(
            subscriptions.unschedule_pending_plan_changes,
        )
        self.update_fixed_fee_quantity = to_streamed_response_wrapper(
            subscriptions.update_fixed_fee_quantity,
        )
        self.update_trial = to_streamed_response_wrapper(
            subscriptions.update_trial,
        )


class AsyncSubscriptionsWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            subscriptions.cancel,
        )
        self.fetch = async_to_streamed_response_wrapper(
            subscriptions.fetch,
        )
        self.fetch_costs = async_to_streamed_response_wrapper(
            subscriptions.fetch_costs,
        )
        self.fetch_schedule = async_to_streamed_response_wrapper(
            subscriptions.fetch_schedule,
        )
        self.fetch_usage = async_to_streamed_response_wrapper(
            subscriptions.fetch_usage,
        )
        self.price_intervals = async_to_streamed_response_wrapper(
            subscriptions.price_intervals,
        )
        self.redeem_coupon = async_to_streamed_response_wrapper(
            subscriptions.redeem_coupon,
        )
        self.schedule_plan_change = async_to_streamed_response_wrapper(
            subscriptions.schedule_plan_change,
        )
        self.trigger_phase = async_to_streamed_response_wrapper(
            subscriptions.trigger_phase,
        )
        self.unschedule_cancellation = async_to_streamed_response_wrapper(
            subscriptions.unschedule_cancellation,
        )
        self.unschedule_fixed_fee_quantity_updates = async_to_streamed_response_wrapper(
            subscriptions.unschedule_fixed_fee_quantity_updates,
        )
        self.unschedule_pending_plan_changes = async_to_streamed_response_wrapper(
            subscriptions.unschedule_pending_plan_changes,
        )
        self.update_fixed_fee_quantity = async_to_streamed_response_wrapper(
            subscriptions.update_fixed_fee_quantity,
        )
        self.update_trial = async_to_streamed_response_wrapper(
            subscriptions.update_trial,
        )
