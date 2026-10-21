# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.customer_minified import CustomerMinified

__all__ = ["SubscriptionPlanChangedStandardWebhookEvent", "Properties", "Subscription", "SubscriptionPlan"]


class Properties(BaseModel):
    previous_plan_id: str


class SubscriptionPlan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


class Subscription(BaseModel):
    """
    The subscription in a standard webhook payload: the fields readable without
    to_subscription_params(), which every interval, billing period and plan phase depends on.
    """

    id: str

    created_at: datetime

    customer: CustomerMinified

    end_date: Optional[datetime] = None
    """The date Orb stops billing for this subscription."""

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    name: str
    """The name of the subscription."""

    plan: Optional[SubscriptionPlan] = None

    start_date: datetime
    """The date Orb starts billing for this subscription."""

    status: Literal["active", "ended", "upcoming"]


class SubscriptionPlanChangedStandardWebhookEvent(BaseModel):
    """Issued when a subscription transitions from one plan to a different plan."""

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

    subscription: Subscription
    """
    The subscription in a standard webhook payload: the fields readable without
    to_subscription_params(), which every interval, billing period and plan phase
    depends on.
    """

    type: Literal["subscription.plan_changed"]
    """The event this payload describes."""
