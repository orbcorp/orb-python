# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditListParams"]


class CreditListParams(TypedDict, total=False):
    currency: Optional[str]
    """The ledger currency or custom pricing unit to use."""

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    effective_date_gt: Annotated[Union[str, datetime, None], PropertyInfo(alias="effective_date[gt]", format="iso8601")]

    effective_date_gte: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="effective_date[gte]", format="iso8601")
    ]

    effective_date_lt: Annotated[Union[str, datetime, None], PropertyInfo(alias="effective_date[lt]", format="iso8601")]

    effective_date_lte: Annotated[
        Union[str, datetime, None], PropertyInfo(alias="effective_date[lte]", format="iso8601")
    ]

    include_all_blocks: bool
    """
    If set to True, all expired and depleted blocks, as well as active block will be
    returned.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""
