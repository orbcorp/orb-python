# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .shared import PaginationMetadata
from .._models import BaseModel

__all__ = [
    "SubscriptionUsage",
    "UngroupedSubscriptionUsage",
    "UngroupedSubscriptionUsageData",
    "UngroupedSubscriptionUsageDataBillableMetric",
    "UngroupedSubscriptionUsageDataUsage",
    "GroupedSubscriptionUsage",
    "GroupedSubscriptionUsageData",
    "GroupedSubscriptionUsageDataBillableMetric",
    "GroupedSubscriptionUsageDataMetricGroup",
    "GroupedSubscriptionUsageDataUsage",
]


class UngroupedSubscriptionUsageDataBillableMetric(BaseModel):
    id: str

    name: str


class UngroupedSubscriptionUsageDataUsage(BaseModel):
    quantity: float

    timeframe_end: datetime

    timeframe_start: datetime


class UngroupedSubscriptionUsageData(BaseModel):
    billable_metric: UngroupedSubscriptionUsageDataBillableMetric

    usage: List[UngroupedSubscriptionUsageDataUsage]

    view_mode: Literal["periodic", "cumulative"]


class UngroupedSubscriptionUsage(BaseModel):
    data: List[UngroupedSubscriptionUsageData]


class GroupedSubscriptionUsageDataBillableMetric(BaseModel):
    id: str

    name: str


class GroupedSubscriptionUsageDataMetricGroup(BaseModel):
    property_key: str

    property_value: str


class GroupedSubscriptionUsageDataUsage(BaseModel):
    quantity: float

    timeframe_end: datetime

    timeframe_start: datetime


class GroupedSubscriptionUsageData(BaseModel):
    billable_metric: GroupedSubscriptionUsageDataBillableMetric

    metric_group: GroupedSubscriptionUsageDataMetricGroup

    usage: List[GroupedSubscriptionUsageDataUsage]

    view_mode: Literal["periodic", "cumulative"]


class GroupedSubscriptionUsage(BaseModel):
    data: List[GroupedSubscriptionUsageData]

    pagination_metadata: Optional[PaginationMetadata] = None


SubscriptionUsage = Union[UngroupedSubscriptionUsage, GroupedSubscriptionUsage]
