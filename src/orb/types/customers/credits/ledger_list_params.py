# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["LedgerListParams"]


class LedgerListParams(TypedDict, total=False):
    created_at_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[gt]", format="iso8601")]

    created_at_gte: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[gte]", format="iso8601")]

    created_at_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[lt]", format="iso8601")]

    created_at_lte: Annotated[Union[str, datetime, None], PropertyInfo(alias="created_at[lte]", format="iso8601")]

    currency: Optional[str]
    """The ledger currency or custom pricing unit to use."""

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    entry_status: Optional[Literal["committed", "pending"]]

    entry_type: Optional[
        Literal[
            "increment", "decrement", "expiration_change", "credit_block_expiry", "void", "void_initiated", "amendment"
        ]
    ]

    limit: int
    """The number of items to fetch. Defaults to 20."""

    minimum_amount: Optional[str]
