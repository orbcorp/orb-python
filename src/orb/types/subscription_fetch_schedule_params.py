# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from typing import Optional, Union

from datetime import datetime

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SubscriptionFetchScheduleParams"]


class SubscriptionFetchScheduleParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    start_date_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="start_date[gt]", format="iso8601")]

    start_date_gte: Annotated[Union[str, datetime, None], PropertyInfo(alias="start_date[gte]", format="iso8601")]

    start_date_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="start_date[lt]", format="iso8601")]

    start_date_lte: Annotated[Union[str, datetime, None], PropertyInfo(alias="start_date[lte]", format="iso8601")]
