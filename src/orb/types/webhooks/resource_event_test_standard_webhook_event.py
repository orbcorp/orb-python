# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResourceEventTestStandardWebhookEvent", "Properties"]


class Properties(BaseModel):
    message: Optional[str] = None


class ResourceEventTestStandardWebhookEvent(BaseModel):
    """Issued when a test webhook is sent."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    payload_style: Literal["expanded", "standard"]
    """
    The serialization style this payload was rendered in, as configured on the
    endpoint.
    """

    properties: Properties

    type: Literal["resource_event.test"]
    """The event this payload describes."""
