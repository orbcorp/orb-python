# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PercentageDiscount"]


class PercentageDiscount(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["percentage"]

    percentage_discount: float
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    reason: Optional[str] = None
