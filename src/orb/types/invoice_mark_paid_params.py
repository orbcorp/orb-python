# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from typing import Union, Optional

from datetime import date

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["InvoiceMarkPaidParams"]


class InvoiceMarkPaidParams(TypedDict, total=False):
    payment_received_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """A date string to specify the date of the payment."""

    external_id: Optional[str]
    """An optional external ID to associate with the payment."""

    notes: Optional[str]
    """An optional note to associate with the payment."""
