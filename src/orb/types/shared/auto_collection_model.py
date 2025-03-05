# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AutoCollectionModel"]


class AutoCollectionModel(BaseModel):
    enabled: Optional[bool] = None
    """True only if auto-collection is enabled for this invoice."""

    next_attempt_at: Optional[datetime] = None
    """
    If the invoice is scheduled for auto-collection, this field will reflect when
    the next attempt will occur. If dunning has been exhausted, or auto-collection
    is not enabled for this invoice, this field will be `null`.
    """

    num_attempts: Optional[int] = None
    """Number of auto-collection payment attempts."""

    previously_attempted_at: Optional[datetime] = None
    """
    If Orb has ever attempted payment auto-collection for this invoice, this field
    will reflect when that attempt occurred. In conjunction with `next_attempt_at`,
    this can be used to tell whether the invoice is currently in dunning (that is,
    `previously_attempted_at` is non-null, and `next_attempt_time` is non-null), or
    if dunning has been exhausted (`previously_attempted_at` is non-null, but
    `next_attempt_time` is null).
    """
