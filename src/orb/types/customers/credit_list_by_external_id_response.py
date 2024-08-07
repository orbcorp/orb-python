# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreditListByExternalIDResponse"]


class CreditListByExternalIDResponse(BaseModel):
    id: str

    balance: float

    effective_date: Optional[datetime] = None

    expiry_date: Optional[datetime] = None

    maximum_initial_balance: Optional[float] = None

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]
