# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventSearchParams"]


class EventSearchParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    timestamp_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="timestamp[gt]", format="iso8601")]

    timestamp_gte: Annotated[Union[str, datetime, None], PropertyInfo(alias="timestamp[gte]", format="iso8601")]

    timestamp_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="timestamp[lt]", format="iso8601")]

    timestamp_lte: Annotated[Union[str, datetime, None], PropertyInfo(alias="timestamp[lte]", format="iso8601")]

    event_ids: Optional[List[str]]
    """This is an explicit array of IDs to filter by.

    Note that an event's ID is the idempotency_key that was originally used for
    ingestion. Values in this array will be treated case sensitively.
    """

    invoice_id: Optional[str]
    """This is an issued Orb invoice ID (see also List Invoices).

    Orb will fetch all events that were used to calculate the invoice. In the common
    case, this will be a list of events whose timestamp property falls within the
    billing period specified by the invoice.
    """
