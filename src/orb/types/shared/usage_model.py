# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["UsageModel"]


class UsageModel(BaseModel):
    quantity: float

    timeframe_end: datetime

    timeframe_start: datetime
