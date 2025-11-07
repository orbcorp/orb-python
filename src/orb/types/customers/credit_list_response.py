# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreditListResponse", "Filter"]


class Filter(BaseModel):
    field: Literal["item_id"]
    """The property of the price the block applies to. Only item_id is supported."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class CreditListResponse(BaseModel):
    id: str

    balance: float

    effective_date: Optional[datetime] = None

    expiry_date: Optional[datetime] = None

    filters: List[Filter]

    maximum_initial_balance: Optional[float] = None

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]
