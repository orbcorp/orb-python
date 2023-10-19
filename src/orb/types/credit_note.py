# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreditNote", "Customer", "LineItem", "LineItemSubLineItem"]


class Customer(BaseModel):
    id: str

    external_customer_id: Optional[str]


class LineItemSubLineItem(BaseModel):
    amount: str

    name: str

    quantity: Optional[float]


class LineItem(BaseModel):
    id: str
    """The Orb id of this resource."""

    amount: str
    """The amount of the line item, including any line item minimums and discounts."""

    discounts: List[object]
    """Any line items discounts from the invoice's line item."""

    name: str
    """The name of the corresponding invoice line item."""

    quantity: Optional[float]
    """An optional quantity credited."""

    sub_line_items: List[LineItemSubLineItem]
    """Any sub line items that may be credited."""

    subtotal: str
    """The amount of the line item, excluding any line item minimums and discounts."""

    tax_amounts: List[object]
    """Any tax amounts applied onto the line item."""


class CreditNote(BaseModel):
    id: str
    """The Orb id of this credit note."""

    created_at: datetime
    """The creation time of the resource in Orb."""

    credit_note_number: str
    """The unique identifier for credit notes."""

    credit_note_pdf: Optional[str]
    """A URL to a PDF of the credit note."""

    customer: Customer

    discounts: List[object]
    """Any discounts applied on the original invoice."""

    invoice_id: str
    """The id of the invoice resource that this credit note is applied to."""

    line_items: List[LineItem]
    """All of the line items associated with this credit note."""

    maximum_amount_adjustment: Optional[object]
    """The maximum amount applied on the original invoice"""

    memo: Optional[str]
    """An optional memo supplied on the credit note."""

    minimum_amount_refunded: Optional[str]
    """Any credited amount from the applied minimum on the invoice."""

    reason: Literal["Duplicate", "Fraudulent", "Order change", "Product unsatisfactory"]

    subtotal: str
    """The total prior to any creditable invoice-level discounts or minimums."""

    total: str
    """The total including creditable invoice-level discounts or minimums, and tax."""

    type: Literal["refund", "adjustment"]

    voided_at: Optional[datetime]
    """The time at which the credit note was voided in Orb, if applicable."""
