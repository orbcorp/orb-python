# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["CreditFetchBalanceByExternalIDParams"]


class CreditFetchBalanceByExternalIDParams(TypedDict, total=False):
    currency: Optional[str]
    """The ledger currency or custom pricing unit to use."""
