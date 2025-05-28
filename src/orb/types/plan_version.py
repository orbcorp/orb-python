# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .price import Price
from .._utils import PropertyInfo
from .._models import BaseModel
from .plan_version_phase import PlanVersionPhase

__all__ = [
    "PlanVersion",
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


class PlanVersion(BaseModel):
    adjustments: List[Adjustment]
    """Adjustments for this plan.

    If the plan has phases, this includes adjustments across all phases of the plan.
    """

    created_at: datetime

    plan_phases: Optional[List[PlanVersionPhase]] = None

    prices: List[Price]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    version: int
