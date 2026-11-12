# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    status: Optional[List[Literal["scheduling", "scheduled", "completed", "skipped", "failed"]]]
    """Only return subscriptions with one of these statuses."""

    subscription_id: Optional[SequenceNotStr[str]]
    """Only return these subscriptions. Up to 100 IDs."""
