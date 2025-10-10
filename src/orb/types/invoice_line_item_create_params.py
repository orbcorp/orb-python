# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
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

    quantity: Required[float]
    """The number of units on the line item"""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date string to specify the line item's start date in the customer's timezone."""

    item_id: Optional[str]
    """The id of the item to associate with this line item.

    If provided without `name`, the item's name will be used for the price/line
    item. If provided with `name`, the item will be associated but `name` will be
    used for the line item. At least one of `name` or `item_id` must be provided.
    """

    name: Optional[str]
    """The name to use for the line item.

    If `item_id` is not provided, Orb will search for an item with this name. If
    found, that item will be associated with the line item. If not found, a new item
    will be created with this name. If `item_id` is provided, this name will be used
    for the line item, but the item association will be based on `item_id`. At least
    one of `name` or `item_id` must be provided.
    """
