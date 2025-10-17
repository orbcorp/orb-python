# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MaximumInterval", "Filter"]


class Filter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MaximumInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this maximum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the maximum interval."""

    filters: List[Filter]
    """The filters that determine which prices this maximum interval applies to."""

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the price intervals
    this transform applies to.
    """

    start_date: datetime
    """The start date of the maximum interval."""
