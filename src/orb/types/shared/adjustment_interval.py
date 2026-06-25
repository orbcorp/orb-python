# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .plan_phase_maximum_adjustment import PlanPhaseMaximumAdjustment
from .plan_phase_minimum_adjustment import PlanPhaseMinimumAdjustment
from .plan_phase_usage_discount_adjustment import PlanPhaseUsageDiscountAdjustment
from .plan_phase_amount_discount_adjustment import PlanPhaseAmountDiscountAdjustment
from .plan_phase_percentage_discount_adjustment import PlanPhasePercentageDiscountAdjustment

__all__ = [
    "AdjustmentInterval",
    "Adjustment",
    "AdjustmentPlanPhaseTieredPercentageDiscountAdjustment",
    "AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentFilter",
    "AdjustmentPlanPhaseTieredPercentageDiscountAdjustmentTier",
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


class AdjustmentInterval(BaseModel):
    id: str

    adjustment: Adjustment

    applies_to_price_interval_ids: List[str]
    """The price interval IDs that this adjustment applies to."""

    end_date: Optional[datetime] = None
    """The end date of the adjustment interval."""

    start_date: datetime
    """The start date of the adjustment interval."""
