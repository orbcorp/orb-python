# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NewAmountDiscount", "Filter"]


class Filter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class NewAmountDiscount(BaseModel):
    adjustment_type: Literal["amount_discount"]

    amount_discount: str

    applies_to_all: Optional[Literal[True]] = None
    """If set, the adjustment will apply to every price on the subscription."""

    applies_to_item_ids: Optional[List[str]] = None
    """The set of item IDs to which this adjustment applies."""

    applies_to_price_ids: Optional[List[str]] = None
    """The set of price IDs to which this adjustment applies."""

    currency: Optional[str] = None
    """If set, only prices in the specified currency will have the adjustment applied."""

    filters: Optional[List[Filter]] = None
    """A list of filters that determine which prices this adjustment will apply to."""

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """

    price_type: Optional[Literal["usage", "fixed_in_advance", "fixed_in_arrears", "fixed", "in_arrears"]] = None
    """If set, only prices of the specified type will have the adjustment applied."""
