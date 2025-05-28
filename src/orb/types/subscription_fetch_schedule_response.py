# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SubscriptionFetchScheduleResponse", "Plan"]


class Plan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


class SubscriptionFetchScheduleResponse(BaseModel):
    created_at: datetime

    end_date: Optional[datetime] = None

    plan: Optional[Plan] = None

    start_date: datetime
