# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .conversion_rate_tier import ConversionRateTier

__all__ = ["ConversionRateTieredConfig"]


class ConversionRateTieredConfig(BaseModel):
    tiers: List[ConversionRateTier]
    """Tiers for rating based on total usage quantities into the specified tier"""
