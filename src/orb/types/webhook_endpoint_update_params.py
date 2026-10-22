# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookEndpointUpdateParams"]


class WebhookEndpointUpdateParams(TypedDict, total=False):
    enabled_event_types: Optional[SequenceNotStr[str]]
    """The webhook event types to send to this endpoint.

    Null sends all event types; omit to leave them unchanged.
    """

    payload_style: Optional[Literal["expanded", "standard"]]
    """The payload style of the webhook events sent to this endpoint.

    Applies to events created after the change; omit to leave it unchanged.
    """

    url: Optional[str]
    """The HTTPS URL that Orb sends webhook events to."""
