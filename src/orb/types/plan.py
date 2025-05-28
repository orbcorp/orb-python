# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .price import Price
from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.discount import Discount

__all__ = [
    "Plan",
    "Adjustment",
    "AdjustmentPlanPhaseUsageDiscountAdjustment",
    "AdjustmentPlanPhaseUsageDiscountAdjustmentFilter",
    "AdjustmentPlanPhaseAmountDiscountAdjustment",
    "AdjustmentPlanPhaseAmountDiscountAdjustmentFilter",
    "AdjustmentPlanPhasePercentageDiscountAdjustment",
    "AdjustmentPlanPhasePercentageDiscountAdjustmentFilter",
    "AdjustmentPlanPhaseMinimumAdjustment",
    "AdjustmentPlanPhaseMinimumAdjustmentFilter",
    "AdjustmentPlanPhaseMaximumAdjustment",
    "AdjustmentPlanPhaseMaximumAdjustmentFilter",
    "BasePlan",
    "Maximum",
    "MaximumFilter",
    "Minimum",
    "MinimumFilter",
    "PlanPhase",
    "PlanPhaseMaximum",
    "PlanPhaseMaximumFilter",
    "PlanPhaseMinimum",
    "PlanPhaseMinimumFilter",
    "Product",
    "TrialConfig",
]


class AdjustmentPlanPhaseUsageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentPlanPhaseUsageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["usage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentPlanPhaseUsageDiscountAdjustmentFilter]
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


class AdjustmentPlanPhaseAmountDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentPlanPhaseAmountDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["amount_discount"]

    amount_discount: str
    """
    The amount by which to discount the prices this adjustment applies to in a given
    billing period.
    """

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentPlanPhaseAmountDiscountAdjustmentFilter]
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


class AdjustmentPlanPhasePercentageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentPlanPhasePercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["percentage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentPlanPhasePercentageDiscountAdjustmentFilter]
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


class AdjustmentPlanPhaseMinimumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentPlanPhaseMinimumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["minimum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentPlanPhaseMinimumAdjustmentFilter]
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


class AdjustmentPlanPhaseMaximumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentPlanPhaseMaximumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["maximum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentPlanPhaseMaximumAdjustmentFilter]
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


Adjustment: TypeAlias = Annotated[
    Union[
        AdjustmentPlanPhaseUsageDiscountAdjustment,
        AdjustmentPlanPhaseAmountDiscountAdjustment,
        AdjustmentPlanPhasePercentageDiscountAdjustment,
        AdjustmentPlanPhaseMinimumAdjustment,
        AdjustmentPlanPhaseMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class BasePlan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


class MaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Maximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Minimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class PlanPhaseMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PlanPhaseMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[PlanPhaseMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class PlanPhaseMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PlanPhaseMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[PlanPhaseMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class PlanPhase(BaseModel):
    id: str

    description: Optional[str] = None

    discount: Optional[Discount] = None

    duration: Optional[int] = None
    """How many terms of length `duration_unit` this phase is active for.

    If null, this phase is evergreen and active indefinitely
    """

    duration_unit: Optional[Literal["daily", "monthly", "quarterly", "semi_annual", "annual"]] = None

    maximum: Optional[PlanPhaseMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[PlanPhaseMinimum] = None

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
    id: str

    adjustments: List[Adjustment]
    """Adjustments for this plan.

    If the plan has phases, this includes adjustments across all phases of the plan.
    """

    base_plan: Optional[BasePlan] = None

    base_plan_id: Optional[str] = None
    """
    The parent plan id if the given plan was created by overriding one or more of
    the parent's prices
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
