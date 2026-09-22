# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.customer_minified import CustomerMinified
from .shared.subscription_minified import SubscriptionMinified

__all__ = ["InvoiceInvoiceDateElapsedWebhookEvent", "Invoice", "Properties"]


class Invoice(BaseModel):
    id: str

    customer: CustomerMinified

    invoice_number: str

    status: Literal["issued", "paid", "synced", "void", "draft"]

    subscription: Optional[SubscriptionMinified] = None


class Properties(BaseModel):
    invoice_date: datetime


class InvoiceInvoiceDateElapsedWebhookEvent(BaseModel):
    """Issued when an invoice's invoice date has elapsed."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    invoice: Invoice

    properties: Properties

    type: Literal["invoice.invoice_date_elapsed"]
    """The event this payload describes."""
