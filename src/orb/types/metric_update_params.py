# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["MetricUpdateParams"]


class MetricUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """A description of the metric."""

    item_id: Optional[str]
    """The id of the item to associate the metric with.

    Prices created on the metric afterwards use the new item; existing prices keep
    the item they were created with.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    name: Optional[str]
    """The name of the metric."""

    sql: Optional[str]
    """A new sql string defining the metric.

    Can only be changed while the metric is in `draft` status and no price uses it.
    If the metric has parameters, the new sql must use the same ones.
    """
