# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.add_subscription_price_params import AddSubscriptionPriceParams
from .shared_params.remove_subscription_price_params import RemoveSubscriptionPriceParams
from .shared_params.replace_subscription_price_params import ReplaceSubscriptionPriceParams
from .shared_params.add_subscription_adjustment_params import AddSubscriptionAdjustmentParams
from .shared_params.remove_subscription_adjustment_params import RemoveSubscriptionAdjustmentParams
from .shared_params.replace_subscription_adjustment_params import ReplaceSubscriptionAdjustmentParams

__all__ = ["SubscriptionSchedulePlanChangeParams", "BillingCycleAnchorConfiguration"]


class SubscriptionSchedulePlanChangeParams(TypedDict, total=False):
    change_option: Required[Literal["requested_date", "end_of_subscription_term", "immediate"]]

    add_adjustments: Optional[Iterable[AddSubscriptionAdjustmentParams]]
    """Additional adjustments to be added to the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    add_prices: Optional[Iterable[AddSubscriptionPriceParams]]
    """Additional prices to be added to the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    align_billing_with_plan_change_date: Optional[bool]
    """[DEPRECATED] Use billing_cycle_alignment instead.

    Reset billing periods to be aligned with the plan change's effective date.
    """

    auto_collection: Optional[bool]
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. If not specified, this
    defaults to the behavior configured for this customer.
    """

    billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]]
    """
    Reset billing periods to be aligned with the plan change's effective date or
    start of the month. Defaults to `unchanged` which keeps subscription's existing
    billing cycle alignment.
    """

    billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration]

    change_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date that the plan change should take effect.

    This parameter can only be passed if the `change_option` is `requested_date`. If
    a date with no time is passed, the plan change will happen at midnight in the
    customer's timezone.
    """

    coupon_redemption_code: Optional[str]
    """Redemption code to be used for this subscription.

    If the coupon cannot be found by its redemption code, or cannot be redeemed, an
    error response will be returned and the subscription creation or plan change
    will not be scheduled.
    """

    credits_overage_rate: Optional[float]

    default_invoice_memo: Optional[str]
    """Determines the default memo on this subscription's invoices.

    Note that if this is not provided, it is determined by the plan configuration.
    """

    external_plan_id: Optional[str]
    """
    The external_plan_id of the plan that the given subscription should be switched
    to. Note that either this property or `plan_id` must be specified.
    """

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](/extensibility/advanced-metrics#computed-properties). If
    null, usage queries will not include any additional filter.
    """

    initial_phase_order: Optional[int]
    """The phase of the plan to start with"""

    invoicing_threshold: Optional[str]
    """
    When this subscription's accrued usage reaches this threshold, an invoice will
    be issued for the subscription. If not specified, invoices will only be issued
    at the end of the billing period.
    """

    net_terms: Optional[int]
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0. If not provided, this defaults to the value specified in the plan.
    """

    per_credit_overage_amount: Optional[float]

    plan_id: Optional[str]
    """The plan that the given subscription should be switched to.

    Note that either this property or `external_plan_id` must be specified.
    """

    plan_version_number: Optional[int]
    """Specifies which version of the plan to change to.

    If null, the default version will be used.
    """

    price_overrides: Optional[Iterable[object]]
    """Optionally provide a list of overrides for prices on the plan"""

    remove_adjustments: Optional[Iterable[RemoveSubscriptionAdjustmentParams]]
    """Plan adjustments to be removed from the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    remove_prices: Optional[Iterable[RemoveSubscriptionPriceParams]]
    """Plan prices to be removed from the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    replace_adjustments: Optional[Iterable[ReplaceSubscriptionAdjustmentParams]]
    """Plan adjustments to be replaced with additional adjustments on the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    replace_prices: Optional[Iterable[ReplaceSubscriptionPriceParams]]
    """Plan prices to be replaced with additional prices on the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    trial_duration_days: Optional[int]
    """The duration of the trial period in days.

    If not provided, this defaults to the value specified in the plan. If `0` is
    provided, the trial on the plan will be skipped.
    """

    usage_customer_ids: Optional[List[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


class BillingCycleAnchorConfiguration(TypedDict, total=False):
    day: Required[int]
    """The day of the month on which the billing cycle is anchored.

    If the maximum number of days in a month is greater than this value, the last
    day of the month is the billing cycle day (e.g. billing_cycle_day=31 for April
    means the billing period begins on the 30th.
    """

    month: Optional[int]
    """The month on which the billing cycle is anchored (e.g.

    a quarterly price anchored in February would have cycles starting February, May,
    August, and November).
    """

    year: Optional[int]
    """The year on which the billing cycle is anchored (e.g.

    a 2 year billing cycle anchored on 2021 would have cycles starting on 2021,
    2023, 2025, etc.).
    """
