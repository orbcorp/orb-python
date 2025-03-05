# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .new_adjustment_model import NewAdjustmentModel

__all__ = ["ReplaceSubscriptionAdjustmentParams"]


class ReplaceSubscriptionAdjustmentParams(TypedDict, total=False):
    adjustment: Required[NewAdjustmentModel]
    """The definition of a new adjustment to create and add to the subscription."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the subscription."""
