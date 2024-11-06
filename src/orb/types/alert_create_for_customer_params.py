# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional, Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["AlertCreateForCustomerParams", "Threshold"]


class AlertCreateForCustomerParams(TypedDict, total=False):
    currency: Required[str]
    """The case sensitive currency or custom pricing unit to use for this alert."""

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

    thresholds: Optional[Iterable[Threshold]]
    """The thresholds that define the values at which the alert will be triggered."""


class Threshold(TypedDict, total=False):
    value: Required[float]
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """
