# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .tier_config import TierConfig
from .sub_line_item_grouping import SubLineItemGrouping

__all__ = ["TierSubLineItem"]


class TierSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemGrouping] = None

    name: str

    quantity: float

    tier_config: TierConfig

    type: Literal["tier"]
