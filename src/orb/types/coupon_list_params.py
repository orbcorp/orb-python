# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CouponListParams"]


class CouponListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    redemption_code: Optional[str]
    """Filter to coupons matching this redemption code."""

    show_archived: Optional[bool]
    """
    Show archived coupons as well (by default, this endpoint only returns active
    coupons).
    """
