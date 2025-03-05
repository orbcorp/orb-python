# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.usage_model import UsageModel
from .shared.pagination_metadata import PaginationMetadata
from .shared.billable_metric_simple_model import BillableMetricSimpleModel

__all__ = [
    "SubscriptionUsage",
    "UngroupedSubscriptionUsage",
    "UngroupedSubscriptionUsageData",
    "GroupedSubscriptionUsage",
    "GroupedSubscriptionUsageData",
    "GroupedSubscriptionUsageDataMetricGroup",
]


class UngroupedSubscriptionUsageData(BaseModel):
    billable_metric: BillableMetricSimpleModel

    usage: List[UsageModel]

    view_mode: Literal["periodic", "cumulative"]


class UngroupedSubscriptionUsage(BaseModel):
    data: List[UngroupedSubscriptionUsageData]


class GroupedSubscriptionUsageDataMetricGroup(BaseModel):
    property_key: str

    property_value: str


class GroupedSubscriptionUsageData(BaseModel):
    billable_metric: BillableMetricSimpleModel

    metric_group: GroupedSubscriptionUsageDataMetricGroup

    usage: List[UsageModel]

    view_mode: Literal["periodic", "cumulative"]


class GroupedSubscriptionUsage(BaseModel):
    data: List[GroupedSubscriptionUsageData]

    pagination_metadata: Optional[PaginationMetadata] = None


SubscriptionUsage: TypeAlias = Union[UngroupedSubscriptionUsage, GroupedSubscriptionUsage]
