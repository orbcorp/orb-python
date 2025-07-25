# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.discount import Discount
from .shared_params.unit_config import UnitConfig

__all__ = ["InvoiceCreateParams", "LineItem"]


class InvoiceCreateParams(TypedDict, total=False):
    currency: Required[str]
    """An ISO 4217 currency string.

    Must be the same as the customer's currency if it is set.
    """

    invoice_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Optional invoice date to set.

    Must be in the past, if not set, `invoice_date` is set to the current time in
    the customer's timezone.
    """

    line_items: Required[Iterable[LineItem]]

    customer_id: Optional[str]
    """The id of the `Customer` to create this invoice for.

    One of `customer_id` and `external_customer_id` are required.
    """

    discount: Optional[Discount]
    """An optional discount to attach to the invoice."""

    external_customer_id: Optional[str]
    """The `external_customer_id` of the `Customer` to create this invoice for.

    One of `customer_id` and `external_customer_id` are required.
    """

    memo: Optional[str]
    """An optional memo to attach to the invoice."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    net_terms: Optional[int]
    """
    Determines the difference between the invoice issue date for subscription
    invoices as the date that they are due. A value of '0' here represents that the
    invoice is due on issue, whereas a value of 30 represents that the customer has
    30 days to pay the invoice.
    """

    will_auto_issue: bool
    """When true, this invoice will be submitted for issuance upon creation.

    When false, the resulting invoice will require manual review to issue. Defaulted
    to false.
    """


class LineItem(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date string to specify the line item's end date in the customer's timezone."""

    item_id: Required[str]

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the line item."""

    quantity: Required[float]
    """The number of units on the line item"""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date string to specify the line item's start date in the customer's timezone."""

    unit_config: Required[UnitConfig]
