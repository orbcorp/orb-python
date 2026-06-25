# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.price import Price
from .shared.maximum import Maximum
from .shared.minimum import Minimum
from .shared.discount import Discount
from .shared.plan_phase_maximum_adjustment import PlanPhaseMaximumAdjustment
from .shared.plan_phase_minimum_adjustment import PlanPhaseMinimumAdjustment
from .shared.plan_phase_usage_discount_adjustment import PlanPhaseUsageDiscountAdjustment
from .shared.plan_phase_amount_discount_adjustment import PlanPhaseAmountDiscountAdjustment
from .shared.plan_phase_percentage_discount_adjustment import PlanPhasePercentageDiscountAdjustment

__all__ = [
    "Plan",
    "Adjustment",
    "AdjustmentPlanPhaseTieredPercentageDiscountAdjustment",
    "AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentFilter",
    "AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentTier",
    "BasePlan",
    "PlanPhase",
    "Product",
    "TrialConfig",
]


class AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentTier(BaseModel):
    """One band of a tiered percentage discount.

    Bounds are denominated in the discount's currency.
    `lower_bound` is the exclusive start of the band and `upper_bound` is the inclusive end;
    `upper_bound` is null only for the open-ended final tier.
    """

    lower_bound: float
    """Exclusive lower bound of cumulative spend for this tier."""

    percentage: float
    """
    The percentage (between 0 and 1) discounted from spend that falls within this
    tier.
    """

    upper_bound: Optional[float] = None
    """
    Inclusive upper bound of cumulative spend for this tier; null for the final
    open-ended tier.
    """


class AdjustmentPlanPhaseTieredPercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["tiered_percentage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invoice, false for adjustments that
    apply to only one price.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""

    replaces_adjustment_id: Optional[str] = None
    """The adjustment id this adjustment replaces.

    This adjustment will take the place of the replaced adjustment in plan version
    migrations.
    """

    tiers: List[AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentTier]
    """
    The ordered, contiguous bands of cumulative eligible spend, each discounted at
    its own percentage (progressive fill-a-tier), applied to the prices this
    adjustment covers in a given billing period.
    """


Adjustment: TypeAlias = Annotated[
    Union[
        PlanPhaseUsageDiscountAdjustment,
        PlanPhaseAmountDiscountAdjustment,
        PlanPhasePercentageDiscountAdjustment,
        AdjustmentPlanPhaseTieredPercentageDiscountAdjustment,
        PlanPhaseMinimumAdjustment,
        PlanPhaseMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class BasePlan(BaseModel):
    """
    Legacy field representing the parent plan if the current plan is a 'child plan', overriding prices from the parent.
    """

    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


class PlanPhase(BaseModel):
    id: str

    description: Optional[str] = None

    discount: Optional[Discount] = None

    duration: Optional[int] = None
    """How many terms of length `duration_unit` this phase is active for.

    If null, this phase is evergreen and active indefinitely
    """

    duration_unit: Optional[Literal["daily", "monthly", "quarterly", "semi_annual", "annual"]] = None

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    name: str

    order: int
    """Determines the ordering of the phase in a plan's lifecycle. 1 = first phase."""


class Product(BaseModel):
    id: str

    created_at: datetime

    name: str


class TrialConfig(BaseModel):
    trial_period: Optional[int] = None

    trial_period_unit: Literal["days"]


class Plan(BaseModel):
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    id: str

    adjustments: List[Adjustment]
    """Adjustments for this plan.

    If the plan has phases, this includes adjustments across all phases of the plan.
    """

    base_plan: Optional[BasePlan] = None
    """
    Legacy field representing the parent plan if the current plan is a 'child plan',
    overriding prices from the parent.
    """

    base_plan_id: Optional[str] = None
    """
    Legacy field representing the parent plan ID if the current plan is a 'child
    plan', overriding prices from the parent.
    """

    created_at: datetime

    currency: str
    """
    An ISO 4217 currency string or custom pricing unit (`credits`) for this plan's
    prices.
    """

    default_invoice_memo: Optional[str] = None
    """
    The default memo text on the invoices corresponding to subscriptions on this
    plan. Note that each subscription may configure its own memo.
    """

    description: str

    discount: Optional[Discount] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    invoicing_currency: str
    """An ISO 4217 currency string for which this plan is billed in.

    Matches `currency` unless `currency` is a custom pricing unit.
    """

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    name: str

    net_terms: Optional[int] = None
    """Determines the difference between the invoice issue date and the due date.

    A value of "0" here signifies that invoices are due on issue, whereas a value of
    "30" means that the customer has a month to pay the invoice before its overdue.
    Note that individual subscriptions or invoices may set a different net terms
    configuration.
    """

    plan_phases: Optional[List[PlanPhase]] = None

    prices: List[Price]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    product: Product

    status: Literal["active", "archived", "draft"]

    trial_config: TrialConfig

    version: int
