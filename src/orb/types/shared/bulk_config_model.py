# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BulkConfigModel", "Tier"]


class Tier(BaseModel):
    unit_amount: str
    """Amount per unit"""

    maximum_units: Optional[float] = None
    """Upper bound for this tier"""


class BulkConfigModel(BaseModel):
    tiers: List[Tier]
    """Bulk tiers for rating based on total usage volume"""
