# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookEndpointUpdateParams"]


class WebhookEndpointUpdateParams(TypedDict, total=False):
    enabled_event_types: Optional[SequenceNotStr[str]]
    """The webhook event types to send to this endpoint.

    Null sends all event types; omit to leave them unchanged.
    """

    url: Optional[str]
    """The HTTPS URL that Orb sends webhook events to."""
