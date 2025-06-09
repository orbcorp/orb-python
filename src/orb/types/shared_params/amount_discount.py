# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .transform_price_filter import TransformPriceFilter

__all__ = ["AmountDiscount"]


class AmountDiscount(TypedDict, total=False):
    amount_discount: Required[str]
    """Only available if discount_type is `amount`."""

    discount_type: Required[Literal["amount"]]

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    filters: Optional[Iterable[TransformPriceFilter]]
    """The filters that determine which prices to apply this discount to."""

    reason: Optional[str]
