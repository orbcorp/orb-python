# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CreditNoteCreateParams", "LineItem"]


class CreditNoteCreateParams(TypedDict, total=False):
    line_items: Required[Iterable[LineItem]]

    reason: Required[Literal["duplicate", "fraudulent", "order_change", "product_unsatisfactory"]]
    """An optional reason for the credit note."""

    memo: Optional[str]
    """An optional memo to attach to the credit note."""


class LineItem(TypedDict, total=False):
    amount: Required[str]
    """The total amount in the invoice's currency to credit this line item."""

    invoice_line_item_id: Required[str]
    """The ID of the line item to credit."""
