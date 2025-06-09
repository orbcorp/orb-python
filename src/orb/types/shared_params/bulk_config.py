# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .bulk_tier import BulkTier

__all__ = ["BulkConfig"]


class BulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[BulkTier]]
    """Bulk tiers for rating based on total usage volume"""
