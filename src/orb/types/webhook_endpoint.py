# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookEndpoint"]


class WebhookEndpoint(BaseModel):
    """
    A webhook endpoint is an HTTPS URL that Orb sends [webhook events](/integrations-and-exports/webhooks) to.
    """

    id: str
    """The Orb-assigned unique identifier for the webhook endpoint."""

    created_at: datetime
    """The time the webhook endpoint was created."""

    enabled: bool
    """Whether Orb sends webhook events to this endpoint."""

    enabled_event_types: Optional[List[str]] = None
    """The webhook event types sent to this endpoint.

    If null, all event types are sent.
    """

    url: str
    """The HTTPS URL that Orb sends webhook events to."""
