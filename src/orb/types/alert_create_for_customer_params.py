# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AlertCreateForCustomerParams", "Threshold"]


class AlertCreateForCustomerParams(TypedDict, total=False):
    currency: Required[str]
    """The case sensitive currency or custom pricing unit to use for this alert."""

    type: Required[str]
    """The thresholds that define the values at which the alert will be triggered."""

    thresholds: Optional[Iterable[Threshold]]
    """The thresholds for the alert."""


class Threshold(TypedDict, total=False):
    value: Required[float]
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """
