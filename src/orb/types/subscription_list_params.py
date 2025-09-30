# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    created_at_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[gt]", format="iso8601")]

    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[gte]", format="iso8601")]

    created_at_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[lt]", format="iso8601")]

    created_at_lte: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[lte]", format="iso8601")]

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    customer_id: Optional[SequenceNotStr[str]]

    external_customer_id: Optional[SequenceNotStr[str]]

    external_plan_id: Optional[str]

    limit: int
    """The number of items to fetch. Defaults to 20."""

    plan_id: Optional[str]

    status: Optional[Literal["active", "ended", "upcoming"]]
