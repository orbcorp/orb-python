# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BalanceTransactionCreateResponse", "CreditNote", "Invoice"]


class CreditNote(BaseModel):
    id: str
    """The id of the Credit note"""


class Invoice(BaseModel):
    id: str
    """The Invoice id"""


class BalanceTransactionCreateResponse(BaseModel):
    id: str
    """A unique id for this transaction."""

    action: Literal[
        "applied_to_invoice",
        "manual_adjustment",
        "prorated_refund",
        "revert_prorated_refund",
        "return_from_voiding",
        "credit_note_applied",
        "credit_note_voided",
        "overpayment_refund",
    ]

    amount: str
    """The value of the amount changed in the transaction."""

    created_at: datetime
    """The creation time of this transaction."""

    credit_note: Optional[CreditNote] = None

    description: Optional[str] = None
    """An optional description provided for manual customer balance adjustments."""

    ending_balance: str
    """
    The new value of the customer's balance prior to the transaction, in the
    customer's currency.
    """

    invoice: Optional[Invoice] = None

    starting_balance: str
    """
    The original value of the customer's balance prior to the transaction, in the
    customer's currency.
    """

    type: Literal["increment", "decrement"]
