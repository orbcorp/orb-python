# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InvoiceCostDataExportedWebhookEvent", "Properties"]


class Properties(BaseModel):
    exported_date: datetime

    s3_bucket: str

    s3_key: str


class InvoiceCostDataExportedWebhookEvent(BaseModel):
    """Issued when invoice cost data is exported."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    invoice: str

    properties: Properties

    type: Literal["invoice.cost_data_exported"]
    """The event this payload describes."""
