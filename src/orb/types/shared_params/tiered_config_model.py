# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TieredConfigModel", "Tier"]


class Tier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class TieredConfigModel(TypedDict, total=False):
    tiers: Required[Iterable[Tier]]
    """Tiers for rating based on total usage quantities into the specified tier"""
