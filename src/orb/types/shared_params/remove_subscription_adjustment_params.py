# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RemoveSubscriptionAdjustmentParams"]


class RemoveSubscriptionAdjustmentParams(TypedDict, total=False):
    adjustment_id: Required[str]
    """The id of the adjustment to remove on the subscription."""
