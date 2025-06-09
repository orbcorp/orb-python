# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .bulk_bps_tier import BulkBPSTier

__all__ = ["BulkBPSConfig"]


class BulkBPSConfig(TypedDict, total=False):
    tiers: Required[Iterable[BulkBPSTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """
