# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.credit_note import CreditNote

__all__ = ["CreditNoteMarkedAsVoidStandardWebhookEvent"]


class CreditNoteMarkedAsVoidStandardWebhookEvent(BaseModel):
    """Issued when a credit note is marked as void."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    credit_note: CreditNote
    """
    The [Credit Note](/invoicing/credit-notes) resource represents a credit that has
    been applied to a particular invoice.
    """

    payload_style: Literal["expanded", "standard"]
    """
    The serialization style this payload was rendered in, as configured on the
    endpoint.
    """

    properties: object

    type: Literal["credit_note.marked_as_void"]
    """The event this payload describes."""
