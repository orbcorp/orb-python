# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = ["InvoiceAccountingSyncFailedWebhookEvent", "AccountingSyncRecord", "Properties"]


class AccountingSyncRecord(BaseModel):
    id: str

    customer_id: str

    record_type: Literal[
        "customer",
        "invoice",
        "transaction",
        "customer_balance_transaction",
        "credit_note",
        "subscription",
        "sales_order",
        "block",
    ]

    error_details: Optional[Dict[str, object]] = None

    invoice_id: Optional[str] = None

    provider_customer_id: Optional[str] = None

    status: Optional[str] = None

    sync_action: Optional[str] = None


class Properties(BaseModel):
    connection_type: str

    failure_reason: str


class InvoiceAccountingSyncFailedWebhookEvent(BaseModel):
    """Issued when an invoice accounting sync fails."""

    id: str
    """The ID of this webhook event."""

    accounting_sync_record: AccountingSyncRecord

    created_at: datetime
    """The time at which this event was created, to the second."""

    invoice: Invoice
    """
    An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity,
    representing the request for payment for a single subscription. This includes a
    set of line items, which correspond to prices in the subscription's plan and can
    represent fixed recurring fees or usage-based fees. They are generated at the
    end of a billing period, or as the result of an action, such as a cancellation.
    """

    properties: Properties

    type: Literal["invoice.accounting_sync_failed"]
    """The event this payload describes."""
