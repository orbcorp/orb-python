# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "AdjustmentModel",
    "PlanPhaseUsageDiscountAdjustment",
    "PlanPhaseAmountDiscountAdjustment",
    "PlanPhasePercentageDiscountAdjustment",
    "PlanPhaseMinimumAdjustment",
    "PlanPhaseMaximumAdjustment",
]


class PlanPhaseUsageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["usage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

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


class PlanPhaseAmountDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["amount_discount"]

    amount_discount: str
    """
    The amount by which to discount the prices this adjustment applies to in a given
    billing period.
    """

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    plan_phase_order: Optional[int] = None
    """The plan phase in which this adjustment is active."""

    reason: Optional[str] = None
    """The reason for the adjustment."""


class PlanPhasePercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["percentage_discount"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

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


class PlanPhaseMinimumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["minimum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

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


class PlanPhaseMaximumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["maximum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

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


AdjustmentModel: TypeAlias = Annotated[
    Union[
        PlanPhaseUsageDiscountAdjustment,
        PlanPhaseAmountDiscountAdjustment,
        PlanPhasePercentageDiscountAdjustment,
        PlanPhaseMinimumAdjustment,
        PlanPhaseMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]
