# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["Minimum"]


class Minimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TransformPriceFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""
