# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["BulkConfigModel", "Tier"]


class Tier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class BulkConfigModel(TypedDict, total=False):
    tiers: Required[Iterable[Tier]]
    """Bulk tiers for rating based on total usage volume"""
