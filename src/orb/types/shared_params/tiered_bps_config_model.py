# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TieredBpsConfigModel", "Tier"]


class Tier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class TieredBpsConfigModel(TypedDict, total=False):
    tiers: Required[Iterable[Tier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """
