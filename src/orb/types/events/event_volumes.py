# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["EventVolumes", "Data"]


class Data(BaseModel):
    count: int
    """The number of events ingested with a timestamp between the timeframe"""

    timeframe_end: datetime

    timeframe_start: datetime


class EventVolumes(BaseModel):
    data: List[Data]
