# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import List, Optional

from typing_extensions import Literal, TypeAlias

from .shared.pagination_metadata import PaginationMetadata

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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


SubscriptionUsage: TypeAlias = Union[UngroupedSubscriptionUsage, GroupedSubscriptionUsage]
