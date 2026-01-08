# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SubscriptionChangeListResponse"]


class SubscriptionChangeListResponse(BaseModel):
    id: str

    expiration_time: datetime
    """
    Subscription change will be cancelled at this time and can no longer be applied.
    """

    status: Literal["pending", "applied", "cancelled"]

    subscription_id: Optional[str] = None

    applied_at: Optional[datetime] = None
    """When this change was applied."""

    cancelled_at: Optional[datetime] = None
    """When this change was cancelled."""
