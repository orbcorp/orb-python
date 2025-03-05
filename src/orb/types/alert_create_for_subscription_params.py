# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .shared_params.threshold_model import ThresholdModel

__all__ = ["AlertCreateForSubscriptionParams"]


class AlertCreateForSubscriptionParams(TypedDict, total=False):
    thresholds: Required[Iterable[ThresholdModel]]
    """The thresholds that define the values at which the alert will be triggered."""

    type: Required[
        Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ]
    ]
    """The type of alert to create. This must be a valid alert type."""

    metric_id: Optional[str]
    """The metric to track usage for."""
