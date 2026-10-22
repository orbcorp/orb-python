# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookEndpointWithSecret"]


class WebhookEndpointWithSecret(BaseModel):
    """
    A newly created webhook endpoint, along with the secret used to sign its webhook events.
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

    payload_style: Literal["expanded", "standard"]
    """The payload style of the webhook events sent to this endpoint.

    `standard` payloads include each object's own fields and references to related
    objects, without invoice line items or subscription price intervals. `expanded`
    payloads include every object fully expanded.
    """

    secret: str
    """The secret used to sign the webhook events sent to this endpoint.

    Only returned when the endpoint is created.
    """

    url: str
    """The HTTPS URL that Orb sends webhook events to."""
