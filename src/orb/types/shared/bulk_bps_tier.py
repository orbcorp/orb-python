# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BulkBPSTier"]


class BulkBPSTier(BaseModel):
    bps: float
    """Basis points to rate on"""

    maximum_amount: Optional[str] = None
    """Upper bound for tier"""

    per_unit_maximum: Optional[str] = None
    """The maximum amount to charge for any one event"""
