# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .tier import Tier
from ..._models import BaseModel

__all__ = ["TieredConfig"]


class TieredConfig(BaseModel):
    tiers: List[Tier]
    """Tiers for rating based on total usage quantities into the specified tier"""
