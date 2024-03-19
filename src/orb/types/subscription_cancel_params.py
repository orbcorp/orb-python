# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionCancelParams"]


class SubscriptionCancelParams(TypedDict, total=False):
    cancel_option: Required[Literal["end_of_subscription_term", "immediate", "requested_date"]]
    """Determines the timing of subscription cancellation"""

    cancellation_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date that the cancellation should take effect.

    This parameter can only be passed if the `cancel_option` is `requested_date`.
    """
