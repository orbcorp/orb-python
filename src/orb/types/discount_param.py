# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DiscountParam"]


class DiscountParam(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """
