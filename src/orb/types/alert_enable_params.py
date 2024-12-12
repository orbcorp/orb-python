# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AlertEnableParams"]


class AlertEnableParams(TypedDict, total=False):
    subscription_id: Optional[str]
    """Used to update the status of a plan alert scoped to this subscription_id"""
