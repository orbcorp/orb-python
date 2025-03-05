# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .plan_model import PlanModel
from .customer_model import CustomerModel
from .price_interval_model import PriceIntervalModel
from .maximum_interval_model import MaximumIntervalModel
from .minimum_interval_model import MinimumIntervalModel
from .coupon_redemption_model import CouponRedemptionModel
from .adjustment_interval_model import AdjustmentIntervalModel
from .subscription_trial_info_model import SubscriptionTrialInfoModel
from .usage_discount_interval_model import UsageDiscountIntervalModel
from .amount_discount_interval_model import AmountDiscountIntervalModel
from .percentage_discount_interval_model import PercentageDiscountIntervalModel
from .fixed_fee_quantity_schedule_entry_model import FixedFeeQuantityScheduleEntryModel
from .billing_cycle_anchor_configuration_model import BillingCycleAnchorConfigurationModel

__all__ = ["SubscriptionModel", "DiscountInterval"]

DiscountInterval: TypeAlias = Annotated[
    Union[AmountDiscountIntervalModel, PercentageDiscountIntervalModel, UsageDiscountIntervalModel],
    PropertyInfo(discriminator="discount_type"),
]


class SubscriptionModel(BaseModel):
    id: str

    active_plan_phase_order: Optional[int] = None
    """
    The current plan phase that is active, only if the subscription's plan has
    phases.
    """

    adjustment_intervals: List[AdjustmentIntervalModel]
    """The adjustment intervals for this subscription."""

    auto_collection: Optional[bool] = None
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. This property defaults to
    the plan's behavior. If null, defaults to the customer's setting.
    """

    billing_cycle_anchor_configuration: BillingCycleAnchorConfigurationModel

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

    customer: CustomerModel
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
    """The discount intervals for this subscription."""

    end_date: Optional[datetime] = None
    """The date Orb stops billing for this subscription."""

    fixed_fee_quantity_schedule: List[FixedFeeQuantityScheduleEntryModel]

    invoicing_threshold: Optional[str] = None

    maximum_intervals: List[MaximumIntervalModel]
    """The maximum intervals for this subscription."""

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum_intervals: List[MinimumIntervalModel]
    """The minimum intervals for this subscription."""

    net_terms: int
    """
    Determines the difference between the invoice issue date for subscription
    invoices as the date that they are due. A value of `0` here represents that the
    invoice is due on issue, whereas a value of `30` represents that the customer
    has a month to pay the invoice.
    """

    plan: PlanModel
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be
    subscribed to by a customer. Plans define the billing behavior of the
    subscription. You can see more about how to configure prices in the
    [Price resource](/reference/price).
    """

    price_intervals: List[PriceIntervalModel]
    """The price intervals for this subscription."""

    redeemed_coupon: Optional[CouponRedemptionModel] = None

    start_date: datetime
    """The date Orb starts billing for this subscription."""

    status: Literal["active", "ended", "upcoming"]

    trial_info: SubscriptionTrialInfoModel
