# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BulkTier"]


class BulkTier(BaseModel):
    unit_amount: str
    """Amount per unit"""

    maximum_units: Optional[float] = None
    """Upper bound for this tier"""
