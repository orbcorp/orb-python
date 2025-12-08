# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .mutated_subscription import MutatedSubscription

__all__ = ["SubscriptionChangeRetrieveResponse"]


class SubscriptionChangeRetrieveResponse(BaseModel):
    """
    A subscription change represents a desired new subscription / pending change to an existing subscription. It
    is a way to first preview the effects on the subscription as well as any changes/creation of invoices
    (see `subscription.changed_resources`).
    """

    id: str

    change_type: str
    """The type of change (e.g., 'schedule_plan_change', 'create_subscription')."""

    expiration_time: datetime
    """
    Subscription change will be cancelled at this time and can no longer be applied.
    """

    status: Literal["pending", "applied", "cancelled"]

    subscription: Optional[MutatedSubscription] = None

    applied_at: Optional[datetime] = None
    """When this change was applied."""

    billing_cycle_alignment: Optional[str] = None
    """Billing cycle alignment for plan changes."""

    cancelled_at: Optional[datetime] = None
    """When this change was cancelled."""

    change_option: Optional[str] = None
    """
    How the change is scheduled (e.g., 'immediate', 'end_of_subscription_term',
    'requested_date').
    """

    effective_date: Optional[datetime] = None
    """When this change will take effect."""

    plan_id: Optional[str] = None
    """The target plan ID for plan changes."""
