# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventUnmatchedEventWebhookEvent", "Properties", "PropertiesEvent"]


class PropertiesEvent(BaseModel):
    customer_id: Optional[str] = None

    event_name: str

    external_customer_id: Optional[str] = None

    idempotency_key: str

    properties: Dict[str, object]

    timestamp: datetime


class Properties(BaseModel):
    event: PropertiesEvent


class EventUnmatchedEventWebhookEvent(BaseModel):
    """Issued when an event does not match any customer."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    type: Literal["event.unmatched_event"]
    """The event this payload describes."""
