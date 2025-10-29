# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .custom_expiration import CustomExpiration

__all__ = ["Allocation", "Filter"]


class Filter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Allocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[CustomExpiration] = None

    filters: Optional[List[Filter]] = None
