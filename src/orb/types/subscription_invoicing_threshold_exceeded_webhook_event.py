# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.customer_minified import CustomerMinified

__all__ = ["SubscriptionInvoicingThresholdExceededWebhookEvent", "Properties", "Subscription", "SubscriptionPlan"]


class Properties(BaseModel):
    evaluated_amount: str

    invoice_id: str

    invoicing_threshold: str

    threshold_invoice_created: bool


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
    """A lightweight subscription representation for webhook payloads.

    This avoids the expensive to_subscription_params() call required for full serialization.
    """

    id: str

    customer: CustomerMinified

    end_date: Optional[datetime] = None

    plan: Optional[SubscriptionPlan] = None

    start_date: datetime

    status: Literal["active", "ended", "upcoming"]


class SubscriptionInvoicingThresholdExceededWebhookEvent(BaseModel):
    """
    Issued when a subscription's invoicing threshold is exceeded and an evaluation is performed.
    """

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    subscription: Subscription
    """A lightweight subscription representation for webhook payloads.

    This avoids the expensive to_subscription_params() call required for full
    serialization.
    """

    type: Literal["subscription.invoicing_threshold_exceeded"]
    """The event this payload describes."""
