# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .price_model import PriceModel

__all__ = ["AggregatedCostModel", "PerPriceCost"]


class PerPriceCost(BaseModel):
    price: PriceModel
    """The price object"""

    price_id: str
    """The price the cost is associated with"""

    subtotal: str
    """Price's contributions for the timeframe, excluding any minimums and discounts."""

    total: str
    """Price's contributions for the timeframe, including minimums and discounts."""

    quantity: Optional[float] = None
    """The price's quantity for the timeframe"""


class AggregatedCostModel(BaseModel):
    per_price_costs: List[PerPriceCost]

    subtotal: str
    """Total costs for the timeframe, excluding any minimums and discounts."""

    timeframe_end: datetime

    timeframe_start: datetime

    total: str
    """Total costs for the timeframe, including any minimums and discounts."""
