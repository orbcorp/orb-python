# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .discount_override_model import DiscountOverrideModel
from .new_allocation_price_model import NewAllocationPriceModel
from .new_subscription_price_model import NewSubscriptionPriceModel

__all__ = ["ReplaceSubscriptionPriceParams"]


class ReplaceSubscriptionPriceParams(BaseModel):
    replaces_price_id: str
    """The id of the price on the plan to replace in the subscription."""

    allocation_price: Optional[NewAllocationPriceModel] = None
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[List[DiscountOverrideModel]] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for the replacement price.
    """

    external_price_id: Optional[str] = None
    """The external price id of the price to add to the subscription."""

    fixed_price_quantity: Optional[float] = None
    """The new quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for the replacement price.
    """

    minimum_amount: Optional[str] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for the replacement price.
    """

    price: Optional[NewSubscriptionPriceModel] = None
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str] = None
    """The id of the price to add to the subscription."""
