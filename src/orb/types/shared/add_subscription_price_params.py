# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .discount_override_model import DiscountOverrideModel
from .new_allocation_price_model import NewAllocationPriceModel
from .new_subscription_price_model import NewSubscriptionPriceModel

__all__ = ["AddSubscriptionPriceParams"]


class AddSubscriptionPriceParams(BaseModel):
    allocation_price: Optional[NewAllocationPriceModel] = None
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[List[DiscountOverrideModel]] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for this price.
    """

    end_date: Optional[datetime] = None
    """The end date of the price interval.

    This is the date that the price will stop billing on the subscription. If null,
    billing will end when the phase or subscription ends.
    """

    external_price_id: Optional[str] = None
    """The external price id of the price to add to the subscription."""

    maximum_amount: Optional[str] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for this price.
    """

    minimum_amount: Optional[str] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for this price.
    """

    plan_phase_order: Optional[int] = None
    """The phase to add this price to."""

    price: Optional[NewSubscriptionPriceModel] = None
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str] = None
    """The id of the price to add to the subscription."""

    start_date: Optional[datetime] = None
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription. If null,
    billing will start when the phase or subscription starts.
    """
