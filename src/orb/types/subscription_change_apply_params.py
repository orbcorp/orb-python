# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionChangeApplyParams"]


class SubscriptionChangeApplyParams(TypedDict, total=False):
    description: Optional[str]
    """Description to apply to the balance transaction representing this credit."""

    mark_as_paid: Optional[bool]
    """Mark all pending invoices that are payable as paid.

    If amount is also provided, mark as paid and credit the difference to the
    customer's balance.
    """

    payment_external_id: Optional[str]
    """An optional external ID to associate with the payment.

    Only applicable when mark_as_paid is true.
    """

    payment_notes: Optional[str]
    """Optional notes about the payment. Only applicable when mark_as_paid is true."""

    payment_received_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """A date string to specify the date the payment was received.

    Only applicable when mark_as_paid is true. If not provided, defaults to the
    current date.
    """

    previously_collected_amount: Optional[str]
    """Amount already collected to apply to the customer's balance.

    If mark_as_paid is also provided, credit the difference to the customer's
    balance.
    """
