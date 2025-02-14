# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionTriggerPhaseParams"]


class SubscriptionTriggerPhaseParams(TypedDict, total=False):
    allow_invoice_credit_or_void: Optional[bool]
    """
    If false, this request will fail if it would void an issued invoice or create a
    credit note. Consider using this as a safety mechanism if you do not expect
    existing invoices to be changed.
    """

    effective_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The date on which the phase change should take effect.

    If not provided, defaults to today in the customer's timezone.
    """
