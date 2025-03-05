# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BulkBpsConfigModel", "Tier"]


class Tier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class BulkBpsConfigModel(TypedDict, total=False):
    tiers: Required[Iterable[Tier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """
