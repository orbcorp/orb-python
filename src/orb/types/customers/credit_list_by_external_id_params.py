# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CreditListByExternalIDParams"]


class CreditListByExternalIDParams(TypedDict, total=False):
    currency: Optional[str]
    """The ledger currency or custom pricing unit to use."""

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""
