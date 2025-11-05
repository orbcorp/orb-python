# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tier import Tier
from ..._models import BaseModel

__all__ = ["TieredConfig"]


class TieredConfig(BaseModel):
    tiers: List[Tier]
    """Tiers for rating based on total usage quantities into the specified tier"""

    prorated: Optional[bool] = None
    """If true, subtotals from this price are prorated based on the service period"""
