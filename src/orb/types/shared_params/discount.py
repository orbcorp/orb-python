# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .trial_discount import TrialDiscount
from .usage_discount import UsageDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["Discount", "TieredPercentageDiscount", "TieredPercentageDiscountTier", "TieredPercentageDiscountFilter"]


class TieredPercentageDiscountTier(TypedDict, total=False):
    """One band of a tiered percentage discount.

    Bounds are denominated in the discount's currency.
    `lower_bound` is the exclusive start of the band and `upper_bound` is the inclusive end;
    `upper_bound` is null only for the open-ended final tier.
    """

    lower_bound: Required[float]
    """Exclusive lower bound of cumulative spend for this tier."""

    percentage: Required[float]
    """
    The percentage (between 0 and 1) discounted from spend that falls within this
    tier.
    """

    upper_bound: Optional[float]
    """
    Inclusive upper bound of cumulative spend for this tier; null for the final
    open-ended tier.
    """


class TieredPercentageDiscountFilter(TypedDict, total=False):
    field: Required[Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]]
    """The property of the price to filter on."""

    operator: Required[Literal["includes", "excludes"]]
    """Should prices that match the filter be included or excluded."""

    values: Required[SequenceNotStr[str]]
    """The IDs or values that match this filter."""


class TieredPercentageDiscount(TypedDict, total=False):
    discount_type: Required[Literal["tiered_percentage"]]

    tiers: Required[Iterable[TieredPercentageDiscountTier]]
    """Only available if discount_type is `tiered_percentage`.

    The ordered, contiguous bands of cumulative eligible spend, each discounted at
    its own percentage (progressive fill-a-tier).
    """

    applies_to_price_ids: Optional[SequenceNotStr[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    filters: Optional[Iterable[TieredPercentageDiscountFilter]]
    """The filters that determine which prices to apply this discount to."""

    reason: Optional[str]


Discount: TypeAlias = Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount, TieredPercentageDiscount]
