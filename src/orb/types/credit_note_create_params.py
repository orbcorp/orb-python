# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CreditNoteCreateParams", "LineItem"]


class CreditNoteCreateParams(TypedDict, total=False):
    line_items: Required[Iterable[LineItem]]

    reason: Required[Literal["duplicate", "fraudulent", "order_change", "product_unsatisfactory"]]
    """An optional reason for the credit note."""

    end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    A date string to specify the global credit note service period end date in the
    customer's timezone. This will be applied to all line items that don't have
    their own individual service periods specified. If not provided, line items will
    use their original invoice line item service periods. This date is inclusive.
    """

    memo: Optional[str]
    """An optional memo to attach to the credit note."""

    start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    A date string to specify the global credit note service period start date in the
    customer's timezone. This will be applied to all line items that don't have
    their own individual service periods specified. If not provided, line items will
    use their original invoice line item service periods. This date is inclusive.
    """


class LineItem(TypedDict, total=False):
    amount: Required[str]
    """The total amount in the invoice's currency to credit this line item."""

    invoice_line_item_id: Required[str]
    """The ID of the line item to credit."""

    end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    A date string to specify this line item's credit note service period end date in
    the customer's timezone. If provided, this will be used for this specific line
    item. If not provided, will use the global end_date if available, otherwise
    defaults to the original invoice line item's end date. This date is inclusive.
    """

    start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    A date string to specify this line item's credit note service period start date
    in the customer's timezone. If provided, this will be used for this specific
    line item. If not provided, will use the global start_date if available,
    otherwise defaults to the original invoice line item's start date. This date is
    inclusive.
    """
