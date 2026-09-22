# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PlanVersionCreatedWebhookEvent", "Plan", "Properties"]


class Plan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


class Properties(BaseModel):
    plan_version_description: Optional[str] = None

    plan_version_number: int


class PlanVersionCreatedWebhookEvent(BaseModel):
    """Issued when a new plan version is created."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    plan: Plan

    properties: Properties

    type: Literal["plan.version_created"]
    """The event this payload describes."""
