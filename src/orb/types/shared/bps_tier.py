# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BPSTier"]


class BPSTier(BaseModel):
    bps: float
    """Per-event basis point rate"""

    minimum_amount: str
    """Exclusive tier starting value"""

    maximum_amount: Optional[str] = None
    """Inclusive tier ending value"""

    per_unit_maximum: Optional[str] = None
    """Per unit maximum to charge"""
