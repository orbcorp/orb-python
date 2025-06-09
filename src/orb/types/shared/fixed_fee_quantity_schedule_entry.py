# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["FixedFeeQuantityScheduleEntry"]


class FixedFeeQuantityScheduleEntry(BaseModel):
    end_date: Optional[datetime] = None

    price_id: str

    quantity: float

    start_date: datetime
