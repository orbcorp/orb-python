# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SubscriptionFetchScheduleResponse", "Plan"]


class Plan(BaseModel):
    id: Optional[str]

    external_plan_id: Optional[str]
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str]


class SubscriptionFetchScheduleResponse(BaseModel):
    end_date: Optional[datetime]

    plan: Plan

    start_date: datetime
