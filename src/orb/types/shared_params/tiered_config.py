# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tier import Tier

__all__ = ["TieredConfig"]


class TieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[Tier]]
    """Tiers for rating based on total usage quantities into the specified tier"""

    prorated: bool
    """If true, subtotals from this price are prorated based on the service period"""
