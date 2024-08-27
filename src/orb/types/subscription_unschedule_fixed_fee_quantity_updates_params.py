# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionUnscheduleFixedFeeQuantityUpdatesParams"]


class SubscriptionUnscheduleFixedFeeQuantityUpdatesParams(TypedDict, total=False):
    price_id: Required[str]
    """Price for which the updates should be cleared. Must be a fixed fee."""
