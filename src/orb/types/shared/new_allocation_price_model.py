# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NewAllocationPriceModel"]


class NewAllocationPriceModel(BaseModel):
    amount: str
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]
    """The cadence at which to allocate the amount to the customer."""

    currency: str
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    expires_at_end_of_cadence: bool
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period.
    """
