# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    amount: Optional[str]

    amount_gt: Annotated[Optional[str], PropertyInfo(alias="amount[gt]")]

    amount_lt: Annotated[Optional[str], PropertyInfo(alias="amount[lt]")]

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    customer_id: Optional[str]

    date_type: Optional[Literal["due_date", "invoice_date"]]

    due_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]

    due_date_window: Optional[str]
    """Filters invoices by their due dates within a specific time range in the past.

    Specify the range as a number followed by 'd' (days) or 'm' (months). For
    example, '7d' filters invoices due in the last 7 days, and '2m' filters those
    due in the last 2 months.
    """

    due_date_gt: Annotated[Union[str, date, None], PropertyInfo(alias="due_date[gt]", format="iso8601")]

    due_date_lt: Annotated[Union[str, date, None], PropertyInfo(alias="due_date[lt]", format="iso8601")]

    external_customer_id: Optional[str]

    invoice_date_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="invoice_date[gt]", format="iso8601")]

    invoice_date_gte: Annotated[Union[str, datetime, None], PropertyInfo(alias="invoice_date[gte]", format="iso8601")]

    invoice_date_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="invoice_date[lt]", format="iso8601")]

    invoice_date_lte: Annotated[Union[str, datetime, None], PropertyInfo(alias="invoice_date[lte]", format="iso8601")]

    is_recurring: Optional[bool]

    limit: int
    """The number of items to fetch. Defaults to 20."""

    status: Optional[List[Literal["draft", "issued", "paid", "synced", "void"]]]

    subscription_id: Optional[str]
