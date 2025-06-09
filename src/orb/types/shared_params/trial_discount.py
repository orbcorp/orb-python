# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .transform_price_filter import TransformPriceFilter

__all__ = ["TrialDiscount"]


class TrialDiscount(TypedDict, total=False):
    discount_type: Required[Literal["trial"]]

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    filters: Optional[Iterable[TransformPriceFilter]]
    """The filters that determine which prices to apply this discount to."""

    reason: Optional[str]

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    trial_percentage_discount: Optional[float]
    """Only available if discount_type is `trial`"""
