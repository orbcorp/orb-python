# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .custom_expiration import CustomExpiration

__all__ = ["NewAllocationPrice", "Filter"]


class Filter(TypedDict, total=False):
    """A PriceFilter that only allows item_id field for block filters."""

    field: Required[Literal["item_id"]]
    """The property of the price the block applies to. Only item_id is supported."""

    operator: Required[Literal["includes", "excludes"]]
    """Should prices that match the filter be included or excluded."""

    values: Required[SequenceNotStr[str]]
    """The IDs or values that match this filter."""


class NewAllocationPrice(TypedDict, total=False):
    amount: Required[str]
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Required[Literal["one_time", "monthly", "quarterly", "semi_annual", "annual"]]
    """The cadence at which to allocate the amount to the customer."""

    currency: Required[str]
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    custom_expiration: Optional[CustomExpiration]
    """The custom expiration for the allocation."""

    expires_at_end_of_cadence: Optional[bool]
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period. Set to null if using custom_expiration.
    """

    filters: Optional[Iterable[Filter]]
    """The filters that determine which items the allocation applies to."""

    item_id: Optional[str]
    """
    The item ID that line items representing charges for this allocation will be
    associated with. If not provided, the default allocation item for the currency
    will be used (e.g. 'Included Allocation (USD)').
    """

    per_unit_cost_basis: str
    """The (per-unit) cost basis of each created block.

    If non-zero, a customer will be invoiced according to the quantity and per unit
    cost basis specified for the allocation each cadence.
    """
