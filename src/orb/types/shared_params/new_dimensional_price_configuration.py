# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["NewDimensionalPriceConfiguration"]


class NewDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[SequenceNotStr[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""
