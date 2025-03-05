# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .discount_override_model import DiscountOverrideModel
from .new_allocation_price_model import NewAllocationPriceModel
from .new_subscription_price_model import NewSubscriptionPriceModel

__all__ = ["ReplaceSubscriptionPriceParams"]


class ReplaceSubscriptionPriceParams(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the subscription."""

    allocation_price: Optional[NewAllocationPriceModel]
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[Iterable[DiscountOverrideModel]]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for the replacement price.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    fixed_price_quantity: Optional[float]
    """The new quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for the replacement price.
    """

    minimum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for the replacement price.
    """

    price: Optional[NewSubscriptionPriceModel]
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""
