# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["AlertUpdateParams", "Threshold"]


class AlertUpdateParams(TypedDict, total=False):
    thresholds: Required[Iterable[Threshold]]
    """The thresholds that define the values at which the alert will be triggered."""


class Threshold(TypedDict, total=False):
    value: Required[float]
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """
