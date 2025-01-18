# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..price import Price
from ..._models import BaseModel

__all__ = ["CostListByExternalIDResponse", "Data", "DataPerPriceCost"]


class DataPerPriceCost(BaseModel):
    price: Price
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    For more on the types of prices, see
    [the core concepts documentation](/core-concepts#plan-and-price)
    """

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
