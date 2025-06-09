# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["NewDimensionalPriceConfiguration"]


class NewDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str] = None
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str] = None
    """The external id of the dimensional price group to include this price in"""
