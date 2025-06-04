# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TrialDiscount", "Filter"]


class Filter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TrialDiscount(BaseModel):
    discount_type: Literal["trial"]

    applies_to_price_ids: Optional[List[str]] = None
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    filters: Optional[List[Filter]] = None
    """The filters that determine which prices to apply this discount to."""

    reason: Optional[str] = None

    trial_amount_discount: Optional[str] = None
    """Only available if discount_type is `trial`"""

    trial_percentage_discount: Optional[float] = None
    """Only available if discount_type is `trial`"""
