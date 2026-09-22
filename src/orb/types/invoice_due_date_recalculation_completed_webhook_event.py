# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceDueDateRecalculationCompletedWebhookEvent", "Properties"]


class Properties(BaseModel):
    completed_at: datetime

    started_at: datetime


class InvoiceDueDateRecalculationCompletedWebhookEvent(BaseModel):
    """Issued when an invoice due date recalculation is completed."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    type: Literal["invoice_due_date_recalculation.completed"]
    """The event this payload describes."""
