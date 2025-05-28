# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionUpdateFixedFeeQuantityParams"]


class SubscriptionUpdateFixedFeeQuantityParams(TypedDict, total=False):
    price_id: Required[str]
    """Price for which the quantity should be updated. Must be a fixed fee."""

    quantity: Required[float]

    allow_invoice_credit_or_void: Optional[bool]
    """
    If false, this request will fail if it would void an issued invoice or create a
    credit note. Consider using this as a safety mechanism if you do not expect
    existing invoices to be changed.
    """

    change_option: Literal["immediate", "upcoming_invoice", "effective_date"]
    """Determines when the change takes effect.

    Note that if `effective_date` is specified, this defaults to `effective_date`.
    Otherwise, this defaults to `immediate` unless it's explicitly set to
    `upcoming_invoice`.
    """

    effective_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    The date that the quantity change should take effect, localized to the
    customer's timezone. If this parameter is not passed in, the quantity change is
    effective according to `change_option`.
    """
