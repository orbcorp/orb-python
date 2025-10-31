# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .custom_expiration import CustomExpiration

__all__ = ["NewAllocationPrice", "Filter"]


class Filter(TypedDict, total=False):
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
