# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MetricEventsDroppedByWatermarkWebhookEvent", "Properties"]


class Properties(BaseModel):
    """
    `window_start` and `window_end` are ISO-8601 strings rather than datetimes: the untyped
    message called `.isoformat()` on them, so they keep microseconds where the webhook JSON
    provider would have truncated them.
    """

    dropped: int

    event_name: str

    total: int

    window_end: str

    window_start: str


class MetricEventsDroppedByWatermarkWebhookEvent(BaseModel):
    """Issued when metric events are dropped by watermark threshold."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties
    """
    `window_start` and `window_end` are ISO-8601 strings rather than datetimes: the
    untyped message called `.isoformat()` on them, so they keep microseconds where
    the webhook JSON provider would have truncated them.
    """

    type: Literal["metric.events_dropped_by_watermark"]
    """The event this payload describes."""
