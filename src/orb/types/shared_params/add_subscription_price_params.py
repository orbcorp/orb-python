# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .discount_override_model import DiscountOverrideModel
from .new_allocation_price_model import NewAllocationPriceModel
from .new_subscription_price_model import NewSubscriptionPriceModel

__all__ = ["AddSubscriptionPriceParams"]


class AddSubscriptionPriceParams(TypedDict, total=False):
    allocation_price: Optional[NewAllocationPriceModel]
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[Iterable[DiscountOverrideModel]]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for this price.
    """

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The end date of the price interval.

    This is the date that the price will stop billing on the subscription. If null,
    billing will end when the phase or subscription ends.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    maximum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for this price.
    """

    minimum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for this price.
    """

    plan_phase_order: Optional[int]
    """The phase to add this price to."""

    price: Optional[NewSubscriptionPriceModel]
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription. If null,
    billing will start when the phase or subscription starts.
    """
