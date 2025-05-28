# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .plan import Plan
from .price import Price
from .._utils import PropertyInfo
from .invoice import Invoice
from .._models import BaseModel
from .customer import Customer
from .credit_note import CreditNote

__all__ = [
    "SubscriptionSchedulePlanChangeResponse",
    "AdjustmentInterval",
    "AdjustmentIntervalAdjustment",
    "AdjustmentIntervalAdjustmentPlanPhaseUsageDiscountAdjustment",
    "AdjustmentIntervalAdjustmentPlanPhaseUsageDiscountAdjustmentFilter",
    "AdjustmentIntervalAdjustmentPlanPhaseAmountDiscountAdjustment",
    "AdjustmentIntervalAdjustmentPlanPhaseAmountDiscountAdjustmentFilter",
    "AdjustmentIntervalAdjustmentPlanPhasePercentageDiscountAdjustment",
    "AdjustmentIntervalAdjustmentPlanPhasePercentageDiscountAdjustmentFilter",
    "AdjustmentIntervalAdjustmentPlanPhaseMinimumAdjustment",
    "AdjustmentIntervalAdjustmentPlanPhaseMinimumAdjustmentFilter",
    "AdjustmentIntervalAdjustmentPlanPhaseMaximumAdjustment",
    "AdjustmentIntervalAdjustmentPlanPhaseMaximumAdjustmentFilter",
    "BillingCycleAnchorConfiguration",
    "DiscountInterval",
    "DiscountIntervalAmountDiscountInterval",
    "DiscountIntervalAmountDiscountIntervalFilter",
    "DiscountIntervalPercentageDiscountInterval",
    "DiscountIntervalPercentageDiscountIntervalFilter",
    "DiscountIntervalUsageDiscountInterval",
    "DiscountIntervalUsageDiscountIntervalFilter",
    "FixedFeeQuantitySchedule",
    "MaximumInterval",
    "MaximumIntervalFilter",
    "MinimumInterval",
    "MinimumIntervalFilter",
    "PendingSubscriptionChange",
    "PriceInterval",
    "PriceIntervalFixedFeeQuantityTransition",
    "RedeemedCoupon",
    "TrialInfo",
    "ChangedResources",
]


class AdjustmentIntervalAdjustmentPlanPhaseUsageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentIntervalAdjustmentPlanPhaseUsageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["usage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentIntervalAdjustmentPlanPhaseUsageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""

    usage_discount: float
    """
    The number of usage units by which to discount the price this adjustment applies
    to in a given billing period.
    """


class AdjustmentIntervalAdjustmentPlanPhaseAmountDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentIntervalAdjustmentPlanPhaseAmountDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["amount_discount"]

    amount_discount: str
    """
    The amount by which to discount the prices this adjustment applies to in a given
    billing period.
    """

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentIntervalAdjustmentPlanPhaseAmountDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""


class AdjustmentIntervalAdjustmentPlanPhasePercentageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentIntervalAdjustmentPlanPhasePercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["percentage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentIntervalAdjustmentPlanPhasePercentageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    percentage_discount: float
    """
    The percentage (as a value between 0 and 1) by which to discount the price
    intervals this adjustment applies to in a given billing period.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""


class AdjustmentIntervalAdjustmentPlanPhaseMinimumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentIntervalAdjustmentPlanPhaseMinimumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["minimum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentIntervalAdjustmentPlanPhaseMinimumAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    item_id: str
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: str
    """
    The minimum amount to charge in a given billing period for the prices this
    adjustment applies to.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""


class AdjustmentIntervalAdjustmentPlanPhaseMaximumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentIntervalAdjustmentPlanPhaseMaximumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["maximum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentIntervalAdjustmentPlanPhaseMaximumAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the prices this
    adjustment applies to.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""


AdjustmentIntervalAdjustment: TypeAlias = Annotated[
    Union[
        AdjustmentIntervalAdjustmentPlanPhaseUsageDiscountAdjustment,
        AdjustmentIntervalAdjustmentPlanPhaseAmountDiscountAdjustment,
        AdjustmentIntervalAdjustmentPlanPhasePercentageDiscountAdjustment,
        AdjustmentIntervalAdjustmentPlanPhaseMinimumAdjustment,
        AdjustmentIntervalAdjustmentPlanPhaseMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class AdjustmentInterval(BaseModel):
    id: str

    adjustment: AdjustmentIntervalAdjustment

    applies_to_price_interval_ids: List[str]
    """The price interval IDs that this adjustment applies to."""

    end_date: Optional[datetime] = None
    """The end date of the adjustment interval."""

    start_date: datetime
    """The start date of the adjustment interval."""


class BillingCycleAnchorConfiguration(BaseModel):
    day: int
    """The day of the month on which the billing cycle is anchored.

    If the maximum number of days in a month is greater than this value, the last
    day of the month is the billing cycle day (e.g. billing_cycle_day=31 for April
    means the billing period begins on the 30th.
    """

    month: Optional[int] = None
    """The month on which the billing cycle is anchored (e.g.

    a quarterly price anchored in February would have cycles starting February, May,
    August, and November).
    """

    year: Optional[int] = None
    """The year on which the billing cycle is anchored (e.g.

    a 2 year billing cycle anchored on 2021 would have cycles starting on 2021,
    2023, 2025, etc.).
    """


class DiscountIntervalAmountDiscountIntervalFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class DiscountIntervalAmountDiscountInterval(BaseModel):
    amount_discount: str
    """Only available if discount_type is `amount`."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["amount"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    filters: List[DiscountIntervalAmountDiscountIntervalFilter]
    """The filters that determine which prices this discount interval applies to."""

    start_date: datetime
    """The start date of the discount interval."""


class DiscountIntervalPercentageDiscountIntervalFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class DiscountIntervalPercentageDiscountInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["percentage"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    filters: List[DiscountIntervalPercentageDiscountIntervalFilter]
    """The filters that determine which prices this discount interval applies to."""

    percentage_discount: float
    """
    Only available if discount_type is `percentage`.This is a number between 0
    and 1.
    """

    start_date: datetime
    """The start date of the discount interval."""


class DiscountIntervalUsageDiscountIntervalFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class DiscountIntervalUsageDiscountInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["usage"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    filters: List[DiscountIntervalUsageDiscountIntervalFilter]
    """The filters that determine which prices this discount interval applies to."""

    start_date: datetime
    """The start date of the discount interval."""

    usage_discount: float
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


DiscountInterval: TypeAlias = Annotated[
    Union[
        DiscountIntervalAmountDiscountInterval,
        DiscountIntervalPercentageDiscountInterval,
        DiscountIntervalUsageDiscountInterval,
    ],
    PropertyInfo(discriminator="discount_type"),
]


class FixedFeeQuantitySchedule(BaseModel):
    end_date: Optional[datetime] = None

    price_id: str

    quantity: float

    start_date: datetime


class MaximumIntervalFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MaximumInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this maximum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the maximum interval."""

    filters: List[MaximumIntervalFilter]
    """The filters that determine which prices this maximum interval applies to."""

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the price intervals
    this transform applies to.
    """

    start_date: datetime
    """The start date of the maximum interval."""


class MinimumIntervalFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MinimumInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this minimum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the minimum interval."""

    filters: List[MinimumIntervalFilter]
    """The filters that determine which prices this minimum interval applies to."""

    minimum_amount: str
    """
    The minimum amount to charge in a given billing period for the price intervals
    this minimum applies to.
    """

    start_date: datetime
    """The start date of the minimum interval."""


class PendingSubscriptionChange(BaseModel):
    id: str


class PriceIntervalFixedFeeQuantityTransition(BaseModel):
    effective_date: datetime

    price_id: str

    quantity: int


class PriceInterval(BaseModel):
    id: str

    billing_cycle_day: int
    """The day of the month that Orb bills for this price"""

    current_billing_period_end_date: Optional[datetime] = None
    """The end of the current billing period.

    This is an exclusive timestamp, such that the instant returned is exactly the
    end of the billing period. Set to null if this price interval is not currently
    active.
    """

    current_billing_period_start_date: Optional[datetime] = None
    """The start date of the current billing period.

    This is an inclusive timestamp; the instant returned is exactly the beginning of
    the billing period. Set to null if this price interval is not currently active.
    """

    end_date: Optional[datetime] = None
    """The end date of the price interval.

    This is the date that Orb stops billing for this price.
    """

    filter: Optional[str] = None
    """An additional filter to apply to usage queries."""

    fixed_fee_quantity_transitions: Optional[List[PriceIntervalFixedFeeQuantityTransition]] = None
    """The fixed fee quantity transitions for this price interval.

    This is only relevant for fixed fees.
    """

    price: Price
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    For more on the types of prices, see
    [the core concepts documentation](/core-concepts#plan-and-price)
    """

    start_date: datetime
    """The start date of the price interval.

    This is the date that Orb starts billing for this price.
    """

    usage_customer_ids: Optional[List[str]] = None
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this price interval.
    """


class RedeemedCoupon(BaseModel):
    coupon_id: str

    end_date: Optional[datetime] = None

    start_date: datetime


class TrialInfo(BaseModel):
    end_date: Optional[datetime] = None


class ChangedResources(BaseModel):
    created_credit_notes: List[CreditNote]
    """The credit notes that were created as part of this operation."""

    created_invoices: List[Invoice]
    """The invoices that were created as part of this operation."""

    voided_credit_notes: List[CreditNote]
    """The credit notes that were voided as part of this operation."""

    voided_invoices: List[Invoice]
    """The invoices that were voided as part of this operation."""


class SubscriptionSchedulePlanChangeResponse(BaseModel):
    id: str

    active_plan_phase_order: Optional[int] = None
    """
    The current plan phase that is active, only if the subscription's plan has
    phases.
    """

    adjustment_intervals: List[AdjustmentInterval]
    """
    The adjustment intervals for this subscription sorted by the start_date of the
    adjustment interval.
    """

    auto_collection: Optional[bool] = None
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. This property defaults to
    the plan's behavior. If null, defaults to the customer's setting.
    """

    billing_cycle_anchor_configuration: BillingCycleAnchorConfiguration

    billing_cycle_day: int
    """The day of the month on which the billing cycle is anchored.

    If the maximum number of days in a month is greater than this value, the last
    day of the month is the billing cycle day (e.g. billing_cycle_day=31 for April
    means the billing period begins on the 30th.
    """

    created_at: datetime

    current_billing_period_end_date: Optional[datetime] = None
    """The end of the current billing period.

    This is an exclusive timestamp, such that the instant returned is not part of
    the billing period. Set to null for subscriptions that are not currently active.
    """

    current_billing_period_start_date: Optional[datetime] = None
    """The start date of the current billing period.

    This is an inclusive timestamp; the instant returned is exactly the beginning of
    the billing period. Set to null if the subscription is not currently active.
    """

    customer: Customer
    """
    A customer is a buyer of your products, and the other party to the billing
    relationship.

    In Orb, customers are assigned system generated identifiers automatically, but
    it's often desirable to have these match existing identifiers in your system. To
    avoid having to denormalize Orb ID information, you can pass in an
    `external_customer_id` with your own identifier. See
    [Customer ID Aliases](/events-and-metrics/customer-aliases) for further
    information about how these aliases work in Orb.

    In addition to having an identifier in your system, a customer may exist in a
    payment provider solution like Stripe. Use the `payment_provider_id` and the
    `payment_provider` enum field to express this mapping.

    A customer also has a timezone (from the standard
    [IANA timezone database](https://www.iana.org/time-zones)), which defaults to
    your account's timezone. See [Timezone localization](/essentials/timezones) for
    information on what this timezone parameter influences within Orb.
    """

    default_invoice_memo: Optional[str] = None
    """Determines the default memo on this subscriptions' invoices.

    Note that if this is not provided, it is determined by the plan configuration.
    """

    discount_intervals: List[DiscountInterval]
    """The discount intervals for this subscription sorted by the start_date."""

    end_date: Optional[datetime] = None
    """The date Orb stops billing for this subscription."""

    fixed_fee_quantity_schedule: List[FixedFeeQuantitySchedule]

    invoicing_threshold: Optional[str] = None

    maximum_intervals: List[MaximumInterval]
    """The maximum intervals for this subscription sorted by the start_date."""

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum_intervals: List[MinimumInterval]
    """The minimum intervals for this subscription sorted by the start_date."""

    name: str
    """The name of the subscription."""

    net_terms: int
    """
    Determines the difference between the invoice issue date for subscription
    invoices as the date that they are due. A value of `0` here represents that the
    invoice is due on issue, whereas a value of `30` represents that the customer
    has a month to pay the invoice.
    """

    pending_subscription_change: Optional[PendingSubscriptionChange] = None
    """A pending subscription change if one exists on this subscription."""

    plan: Optional[Plan] = None
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be
    subscribed to by a customer. Plans define the billing behavior of the
    subscription. You can see more about how to configure prices in the
    [Price resource](/reference/price).
    """

    price_intervals: List[PriceInterval]
    """The price intervals for this subscription."""

    redeemed_coupon: Optional[RedeemedCoupon] = None

    start_date: datetime
    """The date Orb starts billing for this subscription."""

    status: Literal["active", "ended", "upcoming"]

    trial_info: TrialInfo

    changed_resources: Optional[ChangedResources] = None
    """The resources that were changed as part of this operation.

    Only present when fetched through the subscription changes API or if the
    `include_changed_resources` parameter was passed in the request.
    """
