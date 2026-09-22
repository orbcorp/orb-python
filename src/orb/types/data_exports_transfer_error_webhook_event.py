# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DataExportsTransferErrorWebhookEvent", "Properties"]


class Properties(BaseModel):
    description: str

    destination_name: str

    resources: List[str]

    rows_transferred: int

    transfer_blamed_party: str

    transfer_ended_at: datetime

    transfer_started_at: datetime


class DataExportsTransferErrorWebhookEvent(BaseModel):
    """Issued when a data export transfer fails."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    type: Literal["data_exports.transfer_error"]
    """The event this payload describes."""
