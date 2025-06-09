# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BPSTier"]


class BPSTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Exclusive tier starting value"""

    maximum_amount: Optional[str]
    """Inclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""
