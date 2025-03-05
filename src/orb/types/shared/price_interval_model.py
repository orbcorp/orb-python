# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .price_model import PriceModel

__all__ = ["PriceIntervalModel", "FixedFeeQuantityTransition"]


class FixedFeeQuantityTransition(BaseModel):
    effective_date: datetime

    price_id: str

    quantity: int


class PriceIntervalModel(BaseModel):
    id: str

    billing_cycle_day: int
    """The day of the month that Orb bills for this price"""

    current_billing_period_end_date: Optional[datetime] = None
    """The end of the current billing period.

    This is an exclusive timestamp, such that the instant returned is exactly the
    end of the billing period. Set to null if this price interval is not currently
    active.
    """

    current_billing_period_start_date: Optional[datetime] = None
    """The start date of the current billing period.

    This is an inclusive timestamp; the instant returned is exactly the beginning of
    the billing period. Set to null if this price interval is not currently active.
    """

    end_date: Optional[datetime] = None
    """The end date of the price interval.

    This is the date that Orb stops billing for this price.
    """

    filter: Optional[str] = None
    """An additional filter to apply to usage queries."""

    fixed_fee_quantity_transitions: Optional[List[FixedFeeQuantityTransition]] = None
    """The fixed fee quantity transitions for this price interval.

    This is only relevant for fixed fees.
    """

    price: PriceModel
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    For more on the types of prices, see
    [the core concepts documentation](/core-concepts#plan-and-price)
    """

    start_date: datetime
    """The start date of the price interval.

    This is the date that Orb starts billing for this price.
    """

    usage_customer_ids: Optional[List[str]] = None
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this price interval.
    """
