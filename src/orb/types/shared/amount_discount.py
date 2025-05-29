# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AmountDiscount"]


class AmountDiscount(BaseModel):
    amount_discount: str
    """Only available if discount_type is `amount`."""

    discount_type: Literal["amount"]

    applies_to_price_ids: Optional[List[str]] = None
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    reason: Optional[str] = None
