# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .conversion_rate_tier import ConversionRateTier

__all__ = ["ConversionRateTieredConfig"]


class ConversionRateTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[ConversionRateTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""
