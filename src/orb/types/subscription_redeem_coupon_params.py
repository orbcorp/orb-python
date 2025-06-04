# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionRedeemCouponParams"]


class SubscriptionRedeemCouponParams(TypedDict, total=False):
    change_option: Required[Literal["requested_date", "end_of_subscription_term", "immediate"]]

    allow_invoice_credit_or_void: Optional[bool]
    """
    If false, this request will fail if it would void an issued invoice or create a
    credit note. Consider using this as a safety mechanism if you do not expect
    existing invoices to be changed.
    """

    change_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date that the coupon discount should take effect.

    This parameter can only be passed if the `change_option` is `requested_date`.
    """

    coupon_id: Optional[str]
    """Coupon ID to be redeemed for this subscription."""

    coupon_redemption_code: Optional[str]
    """Redemption code of the coupon to be redeemed for this subscription."""
