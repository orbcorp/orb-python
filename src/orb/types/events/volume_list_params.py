# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VolumeListParams"]


class VolumeListParams(TypedDict, total=False):
    timeframe_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The start of the timeframe, inclusive, in which to return event volume.

    All datetime values are converted to UTC time. If the specified time isn't
    hour-aligned, the response includes the event volume count for the hour the time
    falls in.
    """

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    timeframe_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the timeframe, exclusive, in which to return event volume.

    If not specified, the current time is used. All datetime values are converted to
    UTC time.If the specified time isn't hour-aligned, the response includes the
    event volumecount for the hour the time falls in.
    """
