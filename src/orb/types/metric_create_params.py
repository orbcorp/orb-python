# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

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

    metadata: Optional[object]
    """
    User-specified key value pairs, often useful for referencing internal resources
    or IDs. Returned as-is in the metric resource.
    """
