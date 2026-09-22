# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.credit_note import CreditNote

__all__ = ["CreditNoteAccountingSyncFailedWebhookEvent", "AccountingSyncRecord", "Properties"]


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

    credit_note_id: Optional[str] = None

    error_details: Optional[Dict[str, object]] = None

    provider_customer_id: Optional[str] = None

    status: Optional[str] = None

    sync_action: Optional[str] = None


class Properties(BaseModel):
    connection_type: str

    failure_reason: str


class CreditNoteAccountingSyncFailedWebhookEvent(BaseModel):
    """Issued when a credit note accounting sync fails."""

    id: str
    """The ID of this webhook event."""

    accounting_sync_record: AccountingSyncRecord

    created_at: datetime
    """The time at which this event was created, to the second."""

    credit_note: CreditNote
    """
    The [Credit Note](/invoicing/credit-notes) resource represents a credit that has
    been applied to a particular invoice.
    """

    properties: Properties

    type: Literal["credit_note.accounting_sync_failed"]
    """The event this payload describes."""
