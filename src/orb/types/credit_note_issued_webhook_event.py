# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.credit_note import CreditNote

__all__ = ["CreditNoteIssuedWebhookEvent"]


class CreditNoteIssuedWebhookEvent(BaseModel):
    """Issued when a credit note is created."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    credit_note: CreditNote
    """
    The [Credit Note](/invoicing/credit-notes) resource represents a credit that has
    been applied to a particular invoice.
    """

    properties: object

    type: Literal["credit_note.issued"]
    """The event this payload describes."""
