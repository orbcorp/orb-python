# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .threshold_model import ThresholdModel

__all__ = ["CreateCustomerAlertRequest"]


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

    thresholds: Optional[List[ThresholdModel]] = None
    """The thresholds that define the values at which the alert will be triggered."""
