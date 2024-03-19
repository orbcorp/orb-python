# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Coupon", "Discount", "DiscountPercentageDiscount", "DiscountAmountDiscount"]


class DiscountPercentageDiscount(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["percentage"]

    percentage_discount: float
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    reason: Optional[str] = None


class DiscountAmountDiscount(BaseModel):
    amount_discount: str
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["amount"]

    reason: Optional[str] = None


Discount = Union[DiscountPercentageDiscount, DiscountAmountDiscount]


class Coupon(BaseModel):
    id: str
    """Also referred to as coupon_id in this documentation."""

    archived_at: Optional[datetime] = None
    """An archived coupon can no longer be redeemed.

    Active coupons will have a value of null for `archived_at`; this field will be
    non-null for archived coupons.
    """

    discount: Discount

    duration_in_months: Optional[int] = None
    """
    This allows for a coupon's discount to apply for a limited time (determined in
    months); a `null` value here means "unlimited time".
    """

    max_redemptions: Optional[int] = None
    """
    The maximum number of redemptions allowed for this coupon before it is
    exhausted; `null` here means "unlimited".
    """

    redemption_code: str
    """This string can be used to redeem this coupon for a given subscription."""

    times_redeemed: int
    """The number of times this coupon has been redeemed."""
