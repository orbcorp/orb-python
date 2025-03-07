# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertCreateForSubscriptionParams", "Threshold"]


class AlertCreateForSubscriptionParams(TypedDict, total=False):
    thresholds: Required[Iterable[Threshold]]
    """The thresholds that define the values at which the alert will be triggered."""

    type: Required[Literal["usage_exceeded", "cost_exceeded"]]
    """The type of alert to create. This must be a valid alert type."""

    metric_id: Optional[str]
    """The metric to track usage for."""


class Threshold(TypedDict, total=False):
    value: Required[float]
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """
