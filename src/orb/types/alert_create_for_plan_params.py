# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .threshold_param import ThresholdParam

__all__ = ["AlertCreateForPlanParams", "PriceFilter"]


class AlertCreateForPlanParams(TypedDict, total=False):
    thresholds: Required[Iterable[ThresholdParam]]
    """The thresholds that define the values at which the alert will be triggered."""

    type: Required[Literal["usage_exceeded", "cost_exceeded", "spend_exceeded"]]
    """The type of alert to create. This must be a valid alert type."""

    currency: Optional[str]
    """The case sensitive currency or custom pricing unit the alert is denominated in.

    Required for spend_exceeded alerts and when grouping_keys is set.
    """

    grouping_keys: Optional[SequenceNotStr[str]]
    """The property keys to group cost alerts by.

    Only applicable for cost_exceeded alerts.
    """

    metric_id: Optional[str]
    """The metric to track usage for."""

    plan_version: Optional[int]
    """The plan version to create alerts for.

    If not specified, the default will be the plan's active plan version.
    """

    price_filters: Optional[Iterable[PriceFilter]]
    """Filters to scope which prices are included in alert evaluation.

    Supports filtering by price_id, item_id, or price_type with includes/excludes
    operators. Only applicable to spend_exceeded alerts and to cost_exceeded alerts
    with grouping_keys set.
    """


class PriceFilter(TypedDict, total=False):
    field: Required[Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]]
    """The property of the price to filter on."""

    operator: Required[Literal["includes", "excludes"]]
    """Should prices that match the filter be included or excluded."""

    values: Required[SequenceNotStr[str]]
    """The IDs or values that match this filter."""
