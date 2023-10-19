# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PlanUpdateParams"]


class PlanUpdateParams(TypedDict, total=False):
    external_plan_id: Optional[str]
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    metadata: Optional[object]
