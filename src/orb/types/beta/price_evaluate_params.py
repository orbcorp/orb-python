# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PriceEvaluateParams"]


class PriceEvaluateParams(TypedDict, total=False):
    timeframe_end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The exclusive upper bound for event timestamps"""

    timeframe_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The inclusive lower bound for event timestamps"""

    customer_id: Optional[str]
    """The ID of the customer to which this evaluation is scoped."""

    external_customer_id: Optional[str]
    """The external customer ID of the customer to which this evaluation is scoped."""

    filter: Optional[str]
    """
    A boolean
    [computed property](../guides/extensibility/advanced-metrics#computed-properties)
    used to filter the underlying billable metric
    """

    grouping_keys: List[str]
    """
    Properties (or
    [computed properties](../guides/extensibility/advanced-metrics#computed-properties))
    used to group the underlying billable metric
    """
