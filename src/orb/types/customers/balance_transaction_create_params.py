# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BalanceTransactionCreateParams"]


class BalanceTransactionCreateParams(TypedDict, total=False):
    amount: Required[str]

    type: Required[Literal["increment", "decrement"]]

    description: Optional[str]
    """An optional description that can be specified around this entry."""
