# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InvoiceUpdateParams"]


class InvoiceUpdateParams(TypedDict, total=False):
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
    """The net terms determines the due date of the invoice.

    Due date is calculated based on the invoice or issuance date, depending on the
    account's configured due date calculation method. A value of '0' here represents
    that the invoice is due on issue, whereas a value of '30' represents that the
    customer has 30 days to pay the invoice. Do not set this field if you want to
    set a custom due date.
    """
