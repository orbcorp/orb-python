# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DimensionalPriceGroupListParams"]


class DimensionalPriceGroupListParams(TypedDict, total=False):
    billable_metric_id: Optional[str]
    """Filter to groups that use this billable metric."""

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""
