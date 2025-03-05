# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pagination_metadata import PaginationMetadata
from .credit_ledger_entry_model import CreditLedgerEntryModel

__all__ = ["CreditLedgerEntriesModel"]


class CreditLedgerEntriesModel(BaseModel):
    data: List[CreditLedgerEntryModel]

    pagination_metadata: PaginationMetadata
