# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .plan import Plan
from .._models import BaseModel

__all__ = ["PlanEditedWebhookEvent", "Properties", "PropertiesPreviousAttributes"]


class PropertiesPreviousAttributes(BaseModel):
    """metadata values are non-null on the wire, as on the price event."""

    description: Optional[str] = None

    external_plan_id: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    status: Optional[Literal["active", "archived", "draft"]] = None


class Properties(BaseModel):
    previous_attributes: PropertiesPreviousAttributes
    """metadata values are non-null on the wire, as on the price event."""


class PlanEditedWebhookEvent(BaseModel):
    """
    Issued when a plan's name, description, external plan ID, metadata or status is edited.
    """

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    payload_style: Literal["expanded", "standard"]
    """
    The serialization style this payload was rendered in, as configured on the
    endpoint.
    """

    plan: Plan
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be
    subscribed to by a customer. Plans define the billing behavior of the
    subscription. You can see more about how to configure prices in the
    [Price resource](/reference/price).
    """

    properties: Properties

    type: Literal["plan.edited"]
    """The event this payload describes."""
