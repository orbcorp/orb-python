# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionFetchUsageParams"]


class SubscriptionFetchUsageParams(TypedDict, total=False):
    billable_metric_id: Optional[str]
    """
    When specified in conjunction with `group_by`, this parameter filters usage to a
    single billable metric. Note that both `group_by` and `billable_metric_id` must
    be specified together.
    """

    first_dimension_key: Optional[str]

    first_dimension_value: Optional[str]

    granularity: Optional[Literal["day"]]
    """This determines the windowing of usage reporting."""

    group_by: Optional[str]
    """Groups per-price usage by the key provided."""

    second_dimension_key: Optional[str]

    second_dimension_value: Optional[str]

    timeframe_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Usage returned is exclusive of `timeframe_end`."""

    timeframe_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Usage returned is inclusive of `timeframe_start`."""

    view_mode: Optional[Literal["periodic", "cumulative"]]
    """
    Controls whether Orb returns cumulative usage since the start of the billing
    period, or incremental day-by-day usage. If your customer has minimums or
    discounts, it's strongly recommended that you use the default cumulative
    behavior.
    """
