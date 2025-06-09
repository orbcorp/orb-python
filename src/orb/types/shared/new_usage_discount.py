# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["NewUsageDiscount"]


class NewUsageDiscount(BaseModel):
    adjustment_type: Literal["usage_discount"]

    usage_discount: float

    applies_to_all: Optional[Literal[True]] = None
    """If set, the adjustment will apply to every price on the subscription."""

    applies_to_item_ids: Optional[List[str]] = None
    """The set of item IDs to which this adjustment applies."""

    applies_to_price_ids: Optional[List[str]] = None
    """The set of price IDs to which this adjustment applies."""

    currency: Optional[str] = None
    """If set, only prices in the specified currency will have the adjustment applied."""

    filters: Optional[List[TransformPriceFilter]] = None
    """A list of filters that determine which prices this adjustment will apply to."""

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """

    price_type: Optional[Literal["usage", "fixed_in_advance", "fixed_in_arrears", "fixed", "in_arrears"]] = None
    """If set, only prices of the specified type will have the adjustment applied."""
