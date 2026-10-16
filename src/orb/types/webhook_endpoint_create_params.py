# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookEndpointCreateParams"]


class WebhookEndpointCreateParams(TypedDict, total=False):
    url: Required[str]
    """The HTTPS URL that Orb sends webhook events to."""

    enabled_event_types: Optional[SequenceNotStr[str]]
    """The webhook event types to send to this endpoint.

    If omitted or null, all event types are sent.
    """
