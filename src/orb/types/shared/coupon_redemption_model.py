# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CouponRedemptionModel"]


class CouponRedemptionModel(BaseModel):
    coupon_id: str

    end_date: Optional[datetime] = None

    start_date: datetime
