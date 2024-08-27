# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CouponCreateParams", "Discount", "DiscountNewCouponPercentageDiscount", "DiscountNewCouponAmountDiscount"]


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


class DiscountNewCouponPercentageDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage"]]

    percentage_discount: Required[float]


class DiscountNewCouponAmountDiscount(TypedDict, total=False):
    amount_discount: Required[str]

    discount_type: Required[Literal["amount"]]


Discount: TypeAlias = Union[DiscountNewCouponPercentageDiscount, DiscountNewCouponAmountDiscount]
