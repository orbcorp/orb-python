# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceLineItemCreateParams"]


class InvoiceLineItemCreateParams(TypedDict, total=False):
    amount: Required[str]
    """The total amount in the invoice's currency to add to the line item."""

    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date string to specify the line item's end date in the customer's timezone."""

    invoice_id: Required[str]
    """The id of the Invoice to add this line item."""

    name: Required[str]
    """The item name associated with this line item.

    If an item with the same name exists in Orb, that item will be associated with
    the line item.
    """

    quantity: Required[float]
    """The number of units on the line item"""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date string to specify the line item's start date in the customer's timezone."""
