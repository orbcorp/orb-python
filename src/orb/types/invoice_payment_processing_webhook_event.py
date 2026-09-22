# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = ["InvoicePaymentProcessingWebhookEvent", "Properties"]


class Properties(BaseModel):
    payment_provider_id: Optional[str] = None

    payment_provider: Optional[str] = None


class InvoicePaymentProcessingWebhookEvent(BaseModel):
    """Issued when an invoice payment is being processed."""

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

    type: Literal["invoice.payment_processing"]
    """The event this payload describes."""
