# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["MonetaryUsageDiscountAdjustment"]


class MonetaryUsageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["usage_discount"]

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

    reason: Optional[str] = None
    """The reason for the adjustment."""

    replaces_adjustment_id: Optional[str] = None
    """The adjustment id this adjustment replaces.

    This adjustment will take the place of the replaced adjustment in plan version
    migrations.
    """

    usage_discount: float
    """
    The number of usage units by which to discount the price this adjustment applies
    to in a given billing period.
    """
