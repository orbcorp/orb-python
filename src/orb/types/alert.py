# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional, Dict, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Alert", "Threshold"]


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

    customer: Optional[Dict[str, Optional[str]]] = None
    """The customer the alert applies to."""

    enabled: bool
    """Whether the alert is enabled or disabled."""

    metric: Optional[Dict[str, Optional[str]]] = None
    """The metric the alert applies to."""

    plan: Optional[Dict[str, Optional[str]]] = None
    """The plan the alert applies to."""

    subscription: Optional[Dict[str, Optional[str]]] = None
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
