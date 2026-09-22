# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .billable_metric import BillableMetric

__all__ = ["BillableMetricEditedWebhookEvent", "Properties", "PropertiesPreviousAttributes"]


class PropertiesPreviousAttributes(BaseModel):
    """metadata values are non-null on the wire, as on the price event."""

    description: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    name: Optional[str] = None


class Properties(BaseModel):
    previous_attributes: PropertiesPreviousAttributes
    """metadata values are non-null on the wire, as on the price event."""


class BillableMetricEditedWebhookEvent(BaseModel):
    """Issued when a billable metric is edited."""

    id: str
    """The ID of this webhook event."""

    billable_metric: BillableMetric
    """
    The Metric resource represents a calculation of a quantity based on events.
    Metrics are defined by the query that transforms raw usage events into
    meaningful values for your customers.
    """

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    type: Literal["billable_metric.edited"]
    """The event this payload describes."""
