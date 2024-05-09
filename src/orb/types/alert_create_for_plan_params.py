# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AlertCreateForPlanParams", "Threshold"]


class AlertCreateForPlanParams(TypedDict, total=False):
    thresholds: Required[Iterable[Threshold]]
    """The thresholds for the alert."""

    type: Required[str]
    """The thresholds that define the values at which the alert will be triggered."""

    metric_id: Optional[str]
    """The metric to track usage for."""

    plan_version: Optional[int]
    """The plan version to create alerts for.

    If not specified, the default will be the plan's active plan version.
    """


class Threshold(TypedDict, total=False):
    value: Required[float]
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """
