# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["Discount", "PercentageDiscount", "TrialDiscount", "UsageDiscount", "AmountDiscount"]


class PercentageDiscount(TypedDict, total=False):
    applies_to_price_ids: Required[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Required[Literal["percentage"]]

    percentage_discount: Required[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    reason: Optional[str]


class TrialDiscount(TypedDict, total=False):
    applies_to_price_ids: Required[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Required[Literal["trial"]]

    reason: Optional[str]

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    trial_percentage_discount: Optional[float]
    """Only available if discount_type is `trial`"""


class UsageDiscount(TypedDict, total=False):
    applies_to_price_ids: Required[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Required[Literal["usage"]]

    usage_discount: Required[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """

    reason: Optional[str]


class AmountDiscount(TypedDict, total=False):
    amount_discount: Required[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Required[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Required[Literal["amount"]]

    reason: Optional[str]


Discount = Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount]
