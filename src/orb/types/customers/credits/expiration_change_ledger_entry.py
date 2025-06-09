# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .affected_block import AffectedBlock
from ...shared.customer_minified import CustomerMinified

__all__ = ["ExpirationChangeLedgerEntry"]


class ExpirationChangeLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlock

    currency: str

    customer: CustomerMinified

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["expiration_change"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    new_block_expiry_date: Optional[datetime] = None

    starting_balance: float
