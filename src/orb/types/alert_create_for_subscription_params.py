# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .threshold_param import ThresholdParam

__all__ = ["AlertCreateForSubscriptionParams", "PriceFilter", "ThresholdOverride"]


class AlertCreateForSubscriptionParams(TypedDict, total=False):
    thresholds: Required[Iterable[ThresholdParam]]
    """The thresholds that define the values at which the alert will be triggered."""

    type: Required[Literal["usage_exceeded", "cost_exceeded"]]
    """The type of alert to create. This must be a valid alert type."""

    currency: Optional[str]
    """
    The case sensitive currency or custom pricing unit to use for grouped cost
    alerts. Required when grouping_keys is set.
    """

    grouping_keys: Optional[SequenceNotStr[str]]
    """The property keys to group cost alerts by.

    Only applicable for cost_exceeded alerts.
    """

    metric_id: Optional[str]
    """The metric to track usage for."""

    price_filters: Optional[Iterable[PriceFilter]]
    """Filters to scope which prices are included in grouped cost alert evaluation.

    Supports filtering by price_id, item_id, or price_type with includes/excludes
    operators. Only applicable when grouping_keys is set.
    """

    threshold_overrides: Optional[Iterable[ThresholdOverride]]
    """Per-group threshold overrides.

    Each override maps a specific combination of grouping_keys values to a list of
    thresholds that fully replaces the default thresholds for that group. An empty
    thresholds list silences the group. Groups without an override use the default
    thresholds. Only applicable when grouping_keys is set.
    """


class PriceFilter(TypedDict, total=False):
    field: Required[Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]]
    """The property of the price to filter on."""

    operator: Required[Literal["includes", "excludes"]]
    """Should prices that match the filter be included or excluded."""

    values: Required[SequenceNotStr[str]]
    """The IDs or values that match this filter."""


class ThresholdOverride(TypedDict, total=False):
    """Per-group threshold override on a grouped cost alert.

    - An empty `thresholds` list silences alerts for this group (never fires).
    - A non-empty list fully replaces the default thresholds for this group.
    """

    group_values: Required[SequenceNotStr[str]]
    """The values of the grouping keys that identify this group.

    The list length must match the alert's grouping_keys, and values appear in the
    same order as grouping_keys.
    """

    thresholds: Required[Iterable[ThresholdParam]]
    """The thresholds to apply to this group.

    An empty list silences alerts for this group. A non-empty list fully replaces
    the default thresholds for this group.
    """
