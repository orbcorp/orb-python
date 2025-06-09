# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["PlanPhaseMaximumAdjustment"]


class PlanPhaseMaximumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["maximum"]

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[TransformPriceFilter]
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
