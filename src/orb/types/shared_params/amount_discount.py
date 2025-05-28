# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AmountDiscount"]


class AmountDiscount(TypedDict, total=False):
    amount_discount: Required[str]
    """Only available if discount_type is `amount`."""

    discount_type: Required[Literal["amount"]]

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    reason: Optional[str]
