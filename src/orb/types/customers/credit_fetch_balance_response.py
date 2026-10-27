# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CreditFetchBalanceResponse"]


class CreditFetchBalanceResponse(BaseModel):
    balance: float
    """
    The customer's available credit balance: the sum of `balance` across their
    `active` credit blocks.
    """

    currency: Optional[str] = None
    """The currency or custom pricing unit the balances are denominated in.

    Null when no `currency` is passed and the customer has no credit ledger, in
    which case every balance is `0`.
    """

    next_expiry_balance: Optional[float] = None
    """The balance that expires on `next_expiry_date`.

    Null if `next_expiry_date` is null.
    """

    next_expiry_date: Optional[datetime] = None
    """The earliest `expiry_date` among active credit blocks.

    Null if none of them expire.
    """

    pending_payment_balance: float
    """The total balance of credit blocks in `pending_payment` status.

    Not included in `balance` until the invoice that funds them is paid.
    """
