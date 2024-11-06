# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["CreditListByExternalIDParams"]


class CreditListByExternalIDParams(TypedDict, total=False):
    currency: Optional[str]
    """The ledger currency or custom pricing unit to use."""

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    include_all_blocks: bool
    """Include all blocks, not just active ones."""

    limit: int
    """The number of items to fetch. Defaults to 20."""
