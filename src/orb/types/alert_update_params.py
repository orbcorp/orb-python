# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .threshold_param import ThresholdParam

__all__ = ["AlertUpdateParams", "PriceFilter", "ThresholdOverride"]


class AlertUpdateParams(TypedDict, total=False):
    thresholds: Required[Iterable[ThresholdParam]]
    """The thresholds that define the values at which the alert will be triggered."""

    price_filters: Optional[Iterable[PriceFilter]]
    """Replaces the price filters on a grouped cost alert; an empty list clears them.

    Only applicable to cost alerts with grouping_keys. Omit to leave unchanged.
    """

    threshold_overrides: Optional[Iterable[ThresholdOverride]]
    """
    Replaces the per-group threshold overrides on a grouped cost alert; an empty
    list clears them. Only applicable to cost alerts with grouping_keys. Omit to
    leave unchanged.
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
