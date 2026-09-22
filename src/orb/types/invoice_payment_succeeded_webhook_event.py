# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = ["InvoicePaymentSucceededWebhookEvent", "Properties"]


class Properties(BaseModel):
    """`shared_payment_token_id` is only on the wire when the payment used one."""

    payment_provider: Optional[str] = None

    payment_provider_id: Optional[str] = None

    payment_provider_transaction_id: Optional[str] = None

    shared_payment_token_id: Optional[str] = None


class InvoicePaymentSucceededWebhookEvent(BaseModel):
    """
    Issued when automated payment collection for an invoice succeeds for a configured payment gateway.
    """

    id: str
    """The ID of this webhook event."""

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
    """`shared_payment_token_id` is only on the wire when the payment used one."""

    type: Literal["invoice.payment_succeeded"]
    """The event this payload describes."""
