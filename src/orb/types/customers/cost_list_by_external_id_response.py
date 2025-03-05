# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..price import Price
from ..._models import BaseModel

__all__ = ["CostListByExternalIDResponse", "Data", "DataPerPriceCost"]


class DataPerPriceCost(BaseModel):
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


class Data(BaseModel):
    per_price_costs: List[DataPerPriceCost]

    subtotal: str
    """Total costs for the timeframe, excluding any minimums and discounts."""

    timeframe_end: datetime

    timeframe_start: datetime

    total: str
    """Total costs for the timeframe, including any minimums and discounts."""


class CostListByExternalIDResponse(BaseModel):
    data: List[Data]
