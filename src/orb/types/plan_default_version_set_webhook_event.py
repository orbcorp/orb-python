# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PlanDefaultVersionSetWebhookEvent", "Plan", "Properties"]


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
    new_default_version_number: int

    previous_default_version_number: int


class PlanDefaultVersionSetWebhookEvent(BaseModel):
    """Issued when a plan's default version is set."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    plan: Plan

    properties: Properties

    type: Literal["plan.default_version_set"]
    """The event this payload describes."""
