# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionAccountingSyncSucceededWebhookEvent", "AccountingSyncRecord", "Properties", "Transaction"]


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

    provider_customer_id: Optional[str] = None

    status: Optional[str] = None

    sync_action: Optional[str] = None

    transaction_record_id: Optional[str] = None


class Properties(BaseModel):
    connection_type: str


class Transaction(BaseModel):
    id: str
    """The ID of the payment attempt."""

    amount: str
    """The amount of the payment attempt."""

    created_at: datetime
    """The time at which the payment attempt was created."""

    payment_provider: Optional[Literal["stripe", "adyen"]] = None
    """The payment provider that attempted to collect the payment."""

    payment_provider_id: Optional[str] = None
    """The ID of the payment attempt in the payment provider."""

    receipt_pdf: Optional[str] = None
    """URL to the downloadable PDF version of the receipt.

    This field will be `null` for payment attempts that did not succeed.
    """

    succeeded: bool
    """Whether the payment attempt succeeded."""


class TransactionAccountingSyncSucceededWebhookEvent(BaseModel):
    """Issued when a transaction accounting sync succeeds."""

    id: str
    """The ID of this webhook event."""

    accounting_sync_record: AccountingSyncRecord

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    transaction: Transaction

    type: Literal["transaction.accounting_sync_succeeded"]
    """The event this payload describes."""
