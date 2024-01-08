# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CreditListByExternalIDResponse"]


class CreditListByExternalIDResponse(BaseModel):
    id: str

    balance: float

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None
