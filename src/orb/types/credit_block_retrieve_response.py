# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreditBlockRetrieveResponse", "Filter"]


class Filter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class CreditBlockRetrieveResponse(BaseModel):
    """The Credit Block resource models prepaid credits within Orb."""

    id: str

    balance: float

    effective_date: Optional[datetime] = None

    expiry_date: Optional[datetime] = None

    filters: List[Filter]

    maximum_initial_balance: Optional[float] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]
