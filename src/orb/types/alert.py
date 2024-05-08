# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Alert", "Threshold"]


class Threshold(BaseModel):
    value: int
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
    """The name of the currency the credit balance for this alert is denominated in."""

    customer: Optional[Dict[str, Optional[str]]] = None
    """The customer that the alert is scoped to."""

    enabled: bool
    """Whether the alert is enabled or disabled."""

    metric: Optional[Dict[str, Optional[str]]] = None

    plan: Optional[Dict[str, Optional[str]]] = None
    """The plan that the alert is scoped to."""

    subscription: Optional[Dict[str, Optional[str]]] = None

    thresholds: Optional[List[Threshold]] = None
    """
    The thresholds that define the conditions under which the alert will be
    triggered.
    """

    type: Literal["credit_balance_depleted", "credit_balance_dropped", "credit_balance_recovered"]
    """The type of alert. This must be a valid alert type."""
