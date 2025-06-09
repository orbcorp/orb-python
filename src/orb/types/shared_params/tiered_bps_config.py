# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .bps_tier import BPSTier

__all__ = ["TieredBPSConfig"]


class TieredBPSConfig(TypedDict, total=False):
    tiers: Required[Iterable[BPSTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """
