# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["EventSearchParams"]


class EventSearchParams(TypedDict, total=False):
    event_ids: Required[List[str]]
    """This is an explicit array of IDs to filter by.

    Note that an event's ID is the idempotency_key that was originally used for
    ingestion. Values in this array will be treated case sensitively.
    """
