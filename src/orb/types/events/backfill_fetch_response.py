# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BackfillFetchResponse"]


class BackfillFetchResponse(BaseModel):
    id: str

    close_time: Optional[datetime] = None
    """If in the future, the time at which the backfill will automatically close.

    If in the past, the time at which the backfill was closed.
    """

    created_at: datetime

    customer_id: Optional[str] = None
    """The customer ID this backfill is scoped to.

    If null, this backfill is not scoped to a single customer.
    """

    reverted_at: Optional[datetime] = None
    """The time at which this backfill was reverted."""

    status: Literal["pending", "reflected", "pending_revert", "reverted"]
    """The status of the backfill."""

    timeframe_end: datetime

    timeframe_start: datetime
