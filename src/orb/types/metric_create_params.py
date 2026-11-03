# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MetricCreateParams"]


class MetricCreateParams(TypedDict, total=False):
    description: Required[Optional[str]]
    """A description of the metric."""

    item_id: Required[str]
    """The id of the item"""

    name: Required[str]
    """The name of the metric."""

    sql: Required[str]
    """A sql string defining the metric."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    status: Literal["active", "draft"]
    """The status of the metric to create (either active or draft).

    If not specified, this defaults to active. A draft metric's `sql` and `item_id`
    can be changed until it's published.
    """
