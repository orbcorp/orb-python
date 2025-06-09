# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DiscountOverrideParam"]


class DiscountOverrideParam(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """
