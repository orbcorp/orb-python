# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.threshold_model import ThresholdModel

__all__ = ["AlertUpdateParams"]


class AlertUpdateParams(TypedDict, total=False):
    thresholds: Required[Iterable[ThresholdModel]]
    """The thresholds that define the values at which the alert will be triggered."""
