# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionUpdateTrialParams"]


class SubscriptionUpdateTrialParams(TypedDict, total=False):
    trial_end_date: Required[
        Annotated[Union[Union[str, datetime], Literal["immediate"]], PropertyInfo(format="iso8601")]
    ]
    """
    The new date that the trial should end, or the literal string `immediate` to end
    the trial immediately.
    """

    shift: bool
    """
    If true, shifts subsequent price and adjustment intervals (preserving their
    durations, but adjusting their absolute dates).
    """
