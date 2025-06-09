# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .transform_price_filter import TransformPriceFilter

__all__ = ["NewPercentageDiscount"]


class NewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    percentage_discount: Required[float]

    applies_to_all: Optional[Literal[True]]
    """If set, the adjustment will apply to every price on the subscription."""

    applies_to_item_ids: Optional[List[str]]
    """The set of item IDs to which this adjustment applies."""

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    currency: Optional[str]
    """If set, only prices in the specified currency will have the adjustment applied."""

    filters: Optional[Iterable[TransformPriceFilter]]
    """A list of filters that determine which prices this adjustment will apply to."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """

    price_type: Optional[Literal["usage", "fixed_in_advance", "fixed_in_arrears", "fixed", "in_arrears"]]
    """If set, only prices of the specified type will have the adjustment applied."""
