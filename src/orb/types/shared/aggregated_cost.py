# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .per_price_cost import PerPriceCost

__all__ = ["AggregatedCost"]


class AggregatedCost(BaseModel):
    per_price_costs: List[PerPriceCost]

    subtotal: str
    """Total costs for the timeframe, excluding any minimums and discounts."""

    timeframe_end: datetime

    timeframe_start: datetime

    total: str
    """Total costs for the timeframe, including any minimums and discounts."""
