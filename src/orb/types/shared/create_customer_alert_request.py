# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreateCustomerAlertRequest", "Threshold"]


class Threshold(BaseModel):
    value: float
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """


class CreateCustomerAlertRequest(BaseModel):
    currency: str
    """The case sensitive currency or custom pricing unit to use for this alert."""

    type: Literal[
        "usage_exceeded",
        "cost_exceeded",
        "credit_balance_depleted",
        "credit_balance_dropped",
        "credit_balance_recovered",
    ]
    """The type of alert to create. This must be a valid alert type."""

    thresholds: Optional[List[Threshold]] = None
    """The thresholds that define the values at which the alert will be triggered."""
