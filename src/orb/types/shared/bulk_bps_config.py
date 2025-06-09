# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .bulk_bps_tier import BulkBPSTier

__all__ = ["BulkBPSConfig"]


class BulkBPSConfig(BaseModel):
    tiers: List[BulkBPSTier]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """
