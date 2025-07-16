# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .tax_amount import TaxAmount
from .customer_minified import CustomerMinified

__all__ = [
    "CreditNote",
    "LineItem",
    "LineItemDiscount",
    "MaximumAmountAdjustment",
    "MaximumAmountAdjustmentAppliesToPrice",
    "Discount",
    "DiscountAppliesToPrice",
]


class LineItemDiscount(BaseModel):
    id: str

    amount_applied: str

    applies_to_price_ids: List[str]

    discount_type: Literal["percentage", "amount"]

    percentage_discount: float

    amount_discount: Optional[str] = None

    reason: Optional[str] = None


class LineItem(BaseModel):
    id: str
    """The Orb id of this resource."""

    amount: str
    """The amount of the line item, including any line item minimums and discounts."""

    item_id: str
    """The id of the item associated with this line item."""

    name: str
    """The name of the corresponding invoice line item."""

    quantity: Optional[float] = None
    """An optional quantity credited."""

    subtotal: str
    """The amount of the line item, excluding any line item minimums and discounts."""

    tax_amounts: List[TaxAmount]
    """Any tax amounts applied onto the line item."""

    discounts: Optional[List[LineItemDiscount]] = None
    """Any line item discounts from the invoice's line item."""

    end_time_exclusive: Optional[datetime] = None
    """The end time of the service period for this credit note line item."""

    start_time_inclusive: Optional[datetime] = None
    """The start time of the service period for this credit note line item."""


class MaximumAmountAdjustmentAppliesToPrice(BaseModel):
    id: str

    name: str


class MaximumAmountAdjustment(BaseModel):
    amount_applied: str

    discount_type: Literal["percentage"]

    percentage_discount: float

    applies_to_prices: Optional[List[MaximumAmountAdjustmentAppliesToPrice]] = None

    reason: Optional[str] = None


class DiscountAppliesToPrice(BaseModel):
    id: str

    name: str


class Discount(BaseModel):
    amount_applied: str

    discount_type: Literal["percentage"]

    percentage_discount: float

    applies_to_prices: Optional[List[DiscountAppliesToPrice]] = None

    reason: Optional[str] = None


class CreditNote(BaseModel):
    id: str
    """The Orb id of this credit note."""

    created_at: datetime
    """The creation time of the resource in Orb."""

    credit_note_number: str
    """The unique identifier for credit notes."""

    credit_note_pdf: Optional[str] = None
    """A URL to a PDF of the credit note."""

    customer: CustomerMinified

    invoice_id: str
    """The id of the invoice resource that this credit note is applied to."""

    line_items: List[LineItem]
    """All of the line items associated with this credit note."""

    maximum_amount_adjustment: Optional[MaximumAmountAdjustment] = None
    """The maximum amount applied on the original invoice"""

    memo: Optional[str] = None
    """An optional memo supplied on the credit note."""

    minimum_amount_refunded: Optional[str] = None
    """Any credited amount from the applied minimum on the invoice."""

    reason: Optional[Literal["Duplicate", "Fraudulent", "Order change", "Product unsatisfactory"]] = None

    subtotal: str
    """The total prior to any creditable invoice-level discounts or minimums."""

    total: str
    """The total including creditable invoice-level discounts or minimums, and tax."""

    type: Literal["refund", "adjustment"]

    voided_at: Optional[datetime] = None
    """The time at which the credit note was voided in Orb, if applicable."""

    discounts: Optional[List[Discount]] = None
    """Any discounts applied on the original invoice."""
