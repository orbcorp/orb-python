# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ...._utils import PropertyInfo
from .void_ledger_entry import VoidLedgerEntry
from .amendment_ledger_entry import AmendmentLedgerEntry
from .decrement_ledger_entry import DecrementLedgerEntry
from .increment_ledger_entry import IncrementLedgerEntry
from .void_initiated_ledger_entry import VoidInitiatedLedgerEntry
from .expiration_change_ledger_entry import ExpirationChangeLedgerEntry
from .credit_block_expiry_ledger_entry import CreditBlockExpiryLedgerEntry

__all__ = ["LedgerListByExternalIDResponse"]

LedgerListByExternalIDResponse: TypeAlias = Annotated[
    Union[
        IncrementLedgerEntry,
        DecrementLedgerEntry,
        ExpirationChangeLedgerEntry,
        CreditBlockExpiryLedgerEntry,
        VoidLedgerEntry,
        VoidInitiatedLedgerEntry,
        AmendmentLedgerEntry,
    ],
    PropertyInfo(discriminator="entry_type"),
]
