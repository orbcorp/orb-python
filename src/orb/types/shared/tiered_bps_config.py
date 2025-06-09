# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .bps_tier import BPSTier
from ..._models import BaseModel

__all__ = ["TieredBPSConfig"]


class TieredBPSConfig(BaseModel):
    tiers: List[BPSTier]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """
