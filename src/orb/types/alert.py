# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Alert", "Customer", "Metric", "Plan", "Subscription", "Threshold"]


class Customer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class Metric(BaseModel):
    id: str


class Plan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None

    plan_version: str


class Subscription(BaseModel):
    id: str


class Threshold(BaseModel):
    value: float
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """


class Alert(BaseModel):
    id: str
    """Also referred to as alert_id in this documentation."""

    created_at: datetime
    """The creation time of the resource in Orb."""

    currency: Optional[str] = None
    """The name of the currency the credit balance or invoice cost is denominated in."""

    customer: Optional[Customer] = None
    """The customer the alert applies to."""

    enabled: bool
    """Whether the alert is enabled or disabled."""

    metric: Optional[Metric] = None
    """The metric the alert applies to."""

    plan: Optional[Plan] = None
    """The plan the alert applies to."""

    subscription: Optional[Subscription] = None
    """The subscription the alert applies to."""

    thresholds: Optional[List[Threshold]] = None
    """
    The thresholds that define the conditions under which the alert will be
    triggered.
    """

    type: Literal[
        "usage_exceeded",
        "cost_exceeded",
        "credit_balance_depleted",
        "credit_balance_dropped",
        "credit_balance_recovered",
    ]
    """The type of alert. This must be a valid alert type."""
