# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .shared.plan_minified_model import PlanMinifiedModel

__all__ = ["SubscriptionFetchScheduleResponse"]


class SubscriptionFetchScheduleResponse(BaseModel):
    created_at: datetime

    end_date: Optional[datetime] = None

    plan: PlanMinifiedModel

    start_date: datetime
