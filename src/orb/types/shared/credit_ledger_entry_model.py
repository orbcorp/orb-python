# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .affected_block_model import AffectedBlockModel
from .customer_minified_model import CustomerMinifiedModel

__all__ = [
    "CreditLedgerEntryModel",
    "IncrementLedgerEntry",
    "DecrementLedgerEntry",
    "ExpirationChangeLedgerEntry",
    "CreditBlockExpiryLedgerEntry",
    "VoidLedgerEntry",
    "VoidInitiatedLedgerEntry",
    "AmendmentLedgerEntry",
]


class IncrementLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["increment"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    starting_balance: float


class DecrementLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["decrement"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    starting_balance: float

    event_id: Optional[str] = None

    invoice_id: Optional[str] = None

    price_id: Optional[str] = None


class ExpirationChangeLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

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


class CreditBlockExpiryLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["credit_block_expiry"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    starting_balance: float


class VoidLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["void"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    starting_balance: float

    void_amount: float

    void_reason: Optional[str] = None


class VoidInitiatedLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["void_initiated"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    new_block_expiry_date: datetime

    starting_balance: float

    void_amount: float

    void_reason: Optional[str] = None


class AmendmentLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AffectedBlockModel

    currency: str

    customer: CustomerMinifiedModel

    description: Optional[str] = None

    ending_balance: float

    entry_status: Literal["committed", "pending"]

    entry_type: Literal["amendment"]

    ledger_sequence_number: int

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    starting_balance: float


CreditLedgerEntryModel: TypeAlias = Annotated[
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
