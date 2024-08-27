# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BalanceTransactionListParams"]


class BalanceTransactionListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    operation_time_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="operation_time[gt]", format="iso8601")]

    operation_time_gte: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="operation_time[gte]", format="iso8601")
    ]

    operation_time_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="operation_time[lt]", format="iso8601")]

    operation_time_lte: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="operation_time[lte]", format="iso8601")
    ]
