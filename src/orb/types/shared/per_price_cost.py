# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .price import Price
from ..._models import BaseModel

__all__ = ["PerPriceCost"]


class PerPriceCost(BaseModel):
    price: Price
    """The price object"""

    price_id: str
    """The price the cost is associated with"""

    subtotal: str
    """Price's contributions for the timeframe, excluding any minimums and discounts."""

    total: str
    """Price's contributions for the timeframe, including minimums and discounts."""

    quantity: Optional[float] = None
    """The price's quantity for the timeframe"""
