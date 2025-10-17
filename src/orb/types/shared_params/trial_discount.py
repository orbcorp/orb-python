# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TrialDiscount", "Filter"]


class Filter(TypedDict, total=False):
    field: Required[Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]]
    """The property of the price to filter on."""

    operator: Required[Literal["includes", "excludes"]]
    """Should prices that match the filter be included or excluded."""

    values: Required[SequenceNotStr[str]]
    """The IDs or values that match this filter."""


class TrialDiscount(TypedDict, total=False):
    discount_type: Required[Literal["trial"]]

    applies_to_price_ids: Optional[SequenceNotStr[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    filters: Optional[Iterable[Filter]]
    """The filters that determine which prices to apply this discount to."""

    reason: Optional[str]

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    trial_percentage_discount: Optional[float]
    """Only available if discount_type is `trial`"""
