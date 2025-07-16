# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .plan import Plan
from .._utils import PropertyInfo
from .._models import BaseModel
from .customer import Customer
from .shared.price_interval import PriceInterval
from .shared.maximum_interval import MaximumInterval
from .shared.minimum_interval import MinimumInterval
from .shared.coupon_redemption import CouponRedemption
from .shared.adjustment_interval import AdjustmentInterval
from .shared.subscription_trial_info import SubscriptionTrialInfo
from .shared.usage_discount_interval import UsageDiscountInterval
from .shared.amount_discount_interval import AmountDiscountInterval
from .shared.percentage_discount_interval import PercentageDiscountInterval
from .shared.subscription_change_minified import SubscriptionChangeMinified
from .shared.fixed_fee_quantity_schedule_entry import FixedFeeQuantityScheduleEntry
from .shared.billing_cycle_anchor_configuration import BillingCycleAnchorConfiguration

__all__ = ["Subscription", "DiscountInterval"]

DiscountInterval: TypeAlias = Annotated[
    Union[AmountDiscountInterval, PercentageDiscountInterval, UsageDiscountInterval],
    PropertyInfo(discriminator="discount_type"),
]


class Subscription(BaseModel):
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
    """The discount intervals for this subscription sorted by the start_date.

    This field is deprecated in favor of `adjustment_intervals`.
    """

    end_date: Optional[datetime] = None
    """The date Orb stops billing for this subscription."""

    fixed_fee_quantity_schedule: List[FixedFeeQuantityScheduleEntry]

    invoicing_threshold: Optional[str] = None

    maximum_intervals: List[MaximumInterval]
    """The maximum intervals for this subscription sorted by the start_date.

    This field is deprecated in favor of `adjustment_intervals`.
    """

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum_intervals: List[MinimumInterval]
    """The minimum intervals for this subscription sorted by the start_date.

    This field is deprecated in favor of `adjustment_intervals`.
    """

    name: str
    """The name of the subscription."""

    net_terms: int
    """
    Determines the difference between the invoice issue date for subscription
    invoices as the date that they are due. A value of `0` here represents that the
    invoice is due on issue, whereas a value of `30` represents that the customer
    has a month to pay the invoice.
    """

    pending_subscription_change: Optional[SubscriptionChangeMinified] = None
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

    redeemed_coupon: Optional[CouponRedemption] = None

    start_date: datetime
    """The date Orb starts billing for this subscription."""

    status: Literal["active", "ended", "upcoming"]

    trial_info: SubscriptionTrialInfo
