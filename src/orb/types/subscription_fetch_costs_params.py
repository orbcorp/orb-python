# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from typing import Optional, Union

from datetime import datetime

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SubscriptionFetchCostsParams"]


class SubscriptionFetchCostsParams(TypedDict, total=False):
    currency: Optional[str]
    """The currency or custom pricing unit to use."""

    timeframe_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Costs returned are exclusive of `timeframe_end`."""

    timeframe_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Costs returned are inclusive of `timeframe_start`."""

    view_mode: Optional[Literal["periodic", "cumulative"]]
    """
    Controls whether Orb returns cumulative costs since the start of the billing
    period, or incremental day-by-day costs. If your customer has minimums or
    discounts, it's strongly recommended that you use the default cumulative
    behavior.
    """
