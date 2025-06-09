# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .threshold_param import ThresholdParam

__all__ = ["AlertCreateForSubscriptionParams"]


class AlertCreateForSubscriptionParams(TypedDict, total=False):
    thresholds: Required[Iterable[ThresholdParam]]
    """The thresholds that define the values at which the alert will be triggered."""

    type: Required[Literal["usage_exceeded", "cost_exceeded"]]
    """The type of alert to create. This must be a valid alert type."""

    metric_id: Optional[str]
    """The metric to track usage for."""
