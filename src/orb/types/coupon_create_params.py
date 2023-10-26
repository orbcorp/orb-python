# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CouponCreateParams", "Discount", "DiscountPercentageDiscount", "DiscountAmountDiscount"]


class CouponCreateParams(TypedDict, total=False):
    discount: Required[Discount]

    redemption_code: Required[str]
    """This string can be used to redeem this coupon for a given subscription."""

    duration_in_months: Optional[int]
    """
    This allows for a coupon's discount to apply for a limited time (determined in
    months); a `null` value here means "unlimited time".
    """

    max_redemptions: Optional[int]
    """
    The maximum number of redemptions allowed for this coupon before it is
    exhausted;`null` here means "unlimited".
    """


class DiscountPercentageDiscount(TypedDict, total=False):
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


class DiscountAmountDiscount(TypedDict, total=False):
    amount_discount: Required[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Required[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Required[Literal["amount"]]

    reason: Optional[str]


Discount = Union[DiscountPercentageDiscount, DiscountAmountDiscount]
