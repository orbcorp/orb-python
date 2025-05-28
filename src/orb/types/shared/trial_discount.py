# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TrialDiscount"]


class TrialDiscount(BaseModel):
    discount_type: Literal["trial"]

    applies_to_price_ids: Optional[List[str]] = None
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    reason: Optional[str] = None

    trial_amount_discount: Optional[str] = None
    """Only available if discount_type is `trial`"""

    trial_percentage_discount: Optional[float] = None
    """Only available if discount_type is `trial`"""
