# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageUpdateParams", "Event"]


class UsageUpdateParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """Events to update"""

    timeframe_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """This bound is exclusive (i.e. events before this timestamp will be updated)"""

    timeframe_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """This bound is inclusive (i.e.

    events with this timestamp onward, inclusive will be updated)
    """


class Event(TypedDict, total=False):
    event_name: Required[str]
    """A name to meaningfully identify the action or event type."""

    properties: Required[object]
    """A dictionary of custom properties.

    Values in this dictionary must be numeric, boolean, or strings. Nested
    dictionaries are disallowed.
    """

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """An ISO 8601 format date with no timezone offset (i.e.

    UTC). This should represent the time that usage was recorded, and is
    particularly important to attribute usage to a given billing period.
    """

    customer_id: Optional[str]
    """The Orb Customer identifier"""

    external_customer_id: Optional[str]
    """
    An alias for the Orb customer, whose mapping is specified when creating the
    customer
    """
