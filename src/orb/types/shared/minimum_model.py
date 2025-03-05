# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["MinimumModel"]


class MinimumModel(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""
