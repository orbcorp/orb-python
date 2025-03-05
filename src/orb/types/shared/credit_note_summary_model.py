# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CreditNoteSummaryModel"]


class CreditNoteSummaryModel(BaseModel):
    id: str

    credit_note_number: str

    memo: Optional[str] = None
    """An optional memo supplied on the credit note."""

    reason: str

    total: str

    type: str

    voided_at: Optional[datetime] = None
    """
    If the credit note has a status of `void`, this gives a timestamp when the
    credit note was voided.
    """
