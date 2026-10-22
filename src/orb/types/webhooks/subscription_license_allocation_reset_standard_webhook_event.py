# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.customer_minified import CustomerMinified

__all__ = [
    "SubscriptionLicenseAllocationResetStandardWebhookEvent",
    "Properties",
    "PropertiesResetAllocation",
    "Subscription",
    "SubscriptionPlan",
]


class PropertiesResetAllocation(BaseModel):
    """A license allocation replenished at the start of a billing period."""

    allocation_amount: str

    license_type_id: str

    pricing_unit_id: str


class Properties(BaseModel):
    """Fires at the start of a billing period when license allocations are replenished.

    Allocations
    sharing a billing period are batched into one message.
    """

    reset_allocations: List[PropertiesResetAllocation]

    timeframe_end: datetime

    timeframe_start: datetime


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
    The subscription in a license or grouped cost webhook payload: its status, dates, plan and customer.
    """

    id: str

    customer: CustomerMinified

    end_date: Optional[datetime] = None

    plan: Optional[SubscriptionPlan] = None

    start_date: datetime

    status: Literal["active", "ended", "upcoming"]


class SubscriptionLicenseAllocationResetStandardWebhookEvent(BaseModel):
    """Issued when a license allocation is reset."""

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
    """Fires at the start of a billing period when license allocations are replenished.

    Allocations sharing a billing period are batched into one message.
    """

    subscription: Subscription
    """
    The subscription in a license or grouped cost webhook payload: its status,
    dates, plan and customer.
    """

    type: Literal["subscription.license_allocation_reset"]
    """The event this payload describes."""
