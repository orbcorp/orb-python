# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["NewAmountDiscount", "Filter"]


class Filter(TypedDict, total=False):
    field: Required[Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]]
    """The property of the price to filter on."""

    operator: Required[Literal["includes", "excludes"]]
    """Should prices that match the filter be included or excluded."""

    values: Required[SequenceNotStr[str]]
    """The IDs or values that match this filter."""


class NewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_all: Optional[Literal[True]]
    """If set, the adjustment will apply to every price on the subscription."""

    applies_to_item_ids: Optional[SequenceNotStr[str]]
    """The set of item IDs to which this adjustment applies."""

    applies_to_price_ids: Optional[SequenceNotStr[str]]
    """The set of price IDs to which this adjustment applies."""

    currency: Optional[str]
    """If set, only prices in the specified currency will have the adjustment applied."""

    filters: Optional[Iterable[Filter]]
    """A list of filters that determine which prices this adjustment will apply to."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """

    price_type: Optional[Literal["usage", "fixed_in_advance", "fixed_in_arrears", "fixed", "in_arrears"]]
    """If set, only prices of the specified type will have the adjustment applied."""
