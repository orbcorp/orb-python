# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Coupon"]


class Coupon(BaseModel):
    id: str
    """Also referred to as coupon_id in this documentation."""

    archived_at: Optional[datetime]
    """An archived coupon can no longer be redeemed.

    Active coupons will have a value of null for `archived_at`; this field will be
    non-null for archived coupons.
    """

    discount: object

    duration_in_months: Optional[int]
    """
    This allows for a coupon's discount to apply for a limited time (determined in
    months); a `null` value here means "unlimited time".
    """

    max_redemptions: Optional[int]
    """
    The maximum number of redemptions allowed for this coupon before it is
    exhausted; `null` here means "unlimited".
    """

    redemption_code: str
    """This string can be used to redeem this coupon for a given subscription."""

    times_redeemed: int
    """The number of times this coupon has been redeemed."""
