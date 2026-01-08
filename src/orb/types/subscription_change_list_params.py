# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SubscriptionChangeListParams"]


class SubscriptionChangeListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    customer_id: Optional[str]

    external_customer_id: Optional[str]

    limit: int
    """The number of items to fetch. Defaults to 20."""

    status: Optional[Literal["pending", "applied", "cancelled"]]
