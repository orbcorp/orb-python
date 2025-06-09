# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["MonetaryMinimumAdjustment"]


class MonetaryMinimumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["minimum"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[TransformPriceFilter]
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

    reason: Optional[str] = None
    """The reason for the adjustment."""
