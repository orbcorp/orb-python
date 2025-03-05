# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .threshold_model import ThresholdModel
from .customer_minified_model import CustomerMinifiedModel
from .subscription_minified_model import SubscriptionMinifiedModel

__all__ = ["AlertModel", "Metric", "Plan"]


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


class AlertModel(BaseModel):
    id: str
    """Also referred to as alert_id in this documentation."""

    created_at: datetime
    """The creation time of the resource in Orb."""

    currency: Optional[str] = None
    """The name of the currency the credit balance or invoice cost is denominated in."""

    customer: Optional[CustomerMinifiedModel] = None
    """The customer the alert applies to."""

    enabled: bool
    """Whether the alert is enabled or disabled."""

    metric: Optional[Metric] = None
    """The metric the alert applies to."""

    plan: Optional[Plan] = None
    """The plan the alert applies to."""

    subscription: Optional[SubscriptionMinifiedModel] = None
    """The subscription the alert applies to."""

    thresholds: Optional[List[ThresholdModel]] = None
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
