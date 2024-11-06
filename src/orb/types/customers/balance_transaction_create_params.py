# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["BalanceTransactionCreateParams"]


class BalanceTransactionCreateParams(TypedDict, total=False):
    amount: Required[str]

    type: Required[Literal["increment", "decrement"]]

    description: Optional[str]
    """An optional description that can be specified around this entry."""
