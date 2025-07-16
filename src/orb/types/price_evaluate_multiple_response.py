# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .evaluate_price_group import EvaluatePriceGroup

__all__ = ["PriceEvaluateMultipleResponse", "Data"]


class Data(BaseModel):
    currency: str
    """The currency of the price"""

    price_groups: List[EvaluatePriceGroup]
    """The computed price groups associated with input price."""

    external_price_id: Optional[str] = None
    """The external ID of the price"""

    inline_price_index: Optional[int] = None
    """The index of the inline price"""

    price_id: Optional[str] = None
    """The ID of the price"""


class PriceEvaluateMultipleResponse(BaseModel):
    data: List[Data]
