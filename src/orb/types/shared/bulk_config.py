# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .bulk_tier import BulkTier

__all__ = ["BulkConfig"]


class BulkConfig(BaseModel):
    tiers: List[BulkTier]
    """Bulk tiers for rating based on total usage volume"""
