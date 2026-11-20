# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceUpdateParams"]


class InvoiceUpdateParams(TypedDict, total=False):
    auto_collection: Optional[bool]
    """
    Determines whether this invoice will automatically attempt to charge a saved
    payment method, if any. Can only be modified on draft invoices. If not
    specified, the invoice's existing setting is unchanged.
    """

    due_date: Annotated[Union[Union[str, date], Union[str, datetime], None], PropertyInfo(format="iso8601")]
    """An optional custom due date for the invoice.

    If not set, the due date will be calculated based on the `net_terms` value.
    """

    invoice_date: Annotated[Union[Union[str, date], Union[str, datetime], None], PropertyInfo(format="iso8601")]
    """The date of the invoice. Can only be modified for one-off draft invoices."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    net_terms: Optional[int]
    """
    The number of days until the invoice is due, counting the start date as day 1,
    so net 30 from October 1 is due October 30. The account's
    [due date calculation method](/invoicing/payments#configuring-net-terms-and-collection-behavior)
    sets whether the start date is the invoice date or the issuance date. A value of
    '0' here represents that the invoice is due on issue. Do not set this field if
    you want to set a custom due date.
    """
