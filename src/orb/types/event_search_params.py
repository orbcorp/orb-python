# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EventSearchParams"]


class EventSearchParams(TypedDict, total=False):
    event_ids: Required[SequenceNotStr[str]]
    """This is an explicit array of IDs to filter by.

    Note that an event's ID is the idempotency_key that was originally used for
    ingestion, and this only supports events that have not been amended. Values in
    this array will be treated case sensitively.
    """

    timeframe_end: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The end of the timeframe, exclusive, in which to search events.

    If not specified, the current time is used.
    """

    timeframe_start: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The start of the timeframe, inclusive, in which to search events.

    If not specified, the one week ago is used.
    """
