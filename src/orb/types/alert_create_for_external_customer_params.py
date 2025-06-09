# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .threshold_param import ThresholdParam

__all__ = ["AlertCreateForExternalCustomerParams"]


class AlertCreateForExternalCustomerParams(TypedDict, total=False):
    currency: Required[str]
    """The case sensitive currency or custom pricing unit to use for this alert."""

    type: Required[Literal["credit_balance_depleted", "credit_balance_dropped", "credit_balance_recovered"]]
    """The type of alert to create. This must be a valid alert type."""

    thresholds: Optional[Iterable[ThresholdParam]]
    """The thresholds that define the values at which the alert will be triggered."""
