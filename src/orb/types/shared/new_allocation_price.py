# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .custom_expiration import CustomExpiration

__all__ = ["NewAllocationPrice", "Filter"]


class Filter(BaseModel):
    """A PriceFilter that only allows item_id field for block filters."""

    field: Literal["item_id"]
    """The property of the price the block applies to. Only item_id is supported."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class NewAllocationPrice(BaseModel):
    amount: str
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual"]
    """The cadence at which to allocate the amount to the customer."""

    currency: str
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    custom_expiration: Optional[CustomExpiration] = None
    """The custom expiration for the allocation."""

    expires_at_end_of_cadence: Optional[bool] = None
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period. Set to null if using custom_expiration.
    """

    filters: Optional[List[Filter]] = None
    """The filters that determine which items the allocation applies to."""

    item_id: Optional[str] = None
    """
    The item ID that line items representing charges for this allocation will be
    associated with. If not provided, the default allocation item for the currency
    will be used (e.g. 'Included Allocation (USD)').
    """

    per_unit_cost_basis: Optional[str] = None
    """The (per-unit) cost basis of each created block.

    If non-zero, a customer will be invoiced according to the quantity and per unit
    cost basis specified for the allocation each cadence.
    """
