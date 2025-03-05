# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TieredConfigModel", "Tier"]


class Tier(BaseModel):
    first_unit: float
    """Inclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""

    last_unit: Optional[float] = None
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class TieredConfigModel(BaseModel):
    tiers: List[Tier]
    """Tiers for rating based on total usage quantities into the specified tier"""
