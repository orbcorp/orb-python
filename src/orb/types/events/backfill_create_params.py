# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BackfillCreateParams"]


class BackfillCreateParams(TypedDict, total=False):
    timeframe_end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The (exclusive) end of the usage timeframe affected by this backfill.

    By default, Orb allows backfills up to 31 days in duration at a time. Reach out
    to discuss extending this limit and your use case.
    """

    timeframe_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The (inclusive) start of the usage timeframe affected by this backfill.

    By default, Orb allows backfills up to 31 days in duration at a time. Reach out
    to discuss extending this limit and your use case.
    """

    close_time: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The time at which no more events will be accepted for this backfill.

    The backfill will automatically begin reflecting throughout Orb at the close
    time. If not specified, it will default to 1 day after the creation of the
    backfill.
    """

    customer_id: Optional[str]
    """The Orb-generated ID of the customer to which this backfill is scoped.

    Omitting this field will scope the backfill to all customers.
    """

    deprecation_filter: Optional[str]
    """
    A boolean
    [computed property](/extensibility/advanced-metrics#computed-properties) used to
    filter the set of events to deprecate
    """

    external_customer_id: Optional[str]
    """The external customer ID of the customer to which this backfill is scoped.

    Omitting this field will scope the backfill to all customers.
    """

    replace_existing_events: bool
    """
    If true, replaces all existing events in the timeframe with the newly ingested
    events. If false, adds the newly ingested events to the existing events.
    """
