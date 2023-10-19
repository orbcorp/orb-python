# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CouponCreateParams"]


class CouponCreateParams(TypedDict, total=False):
    discount: Required[object]

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
