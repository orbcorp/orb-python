# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "LedgerCreateEntryByExternalIDResponse",
    "IncrementLedgerEntry",
    "IncrementLedgerEntryCreditBlock",
    "IncrementLedgerEntryCustomer",
    "DecrementLedgerEntry",
    "DecrementLedgerEntryCreditBlock",
    "DecrementLedgerEntryCustomer",
    "ExpirationChangeLedgerEntry",
    "ExpirationChangeLedgerEntryCreditBlock",
    "ExpirationChangeLedgerEntryCustomer",
    "CreditBlockExpiryLedgerEntry",
    "CreditBlockExpiryLedgerEntryCreditBlock",
    "CreditBlockExpiryLedgerEntryCustomer",
    "VoidLedgerEntry",
    "VoidLedgerEntryCreditBlock",
    "VoidLedgerEntryCustomer",
    "VoidInitiatedLedgerEntry",
    "VoidInitiatedLedgerEntryCreditBlock",
    "VoidInitiatedLedgerEntryCustomer",
    "AmendmentLedgerEntry",
    "AmendmentLedgerEntryCreditBlock",
    "AmendmentLedgerEntryCustomer",
]


class IncrementLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class IncrementLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class IncrementLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: IncrementLedgerEntryCreditBlock

    currency: str

    customer: IncrementLedgerEntryCustomer

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


class DecrementLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class DecrementLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class DecrementLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: DecrementLedgerEntryCreditBlock

    currency: str

    customer: DecrementLedgerEntryCustomer

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


class ExpirationChangeLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class ExpirationChangeLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class ExpirationChangeLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: ExpirationChangeLedgerEntryCreditBlock

    currency: str

    customer: ExpirationChangeLedgerEntryCustomer

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

    new_block_expiry_date: datetime

    starting_balance: float


class CreditBlockExpiryLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class CreditBlockExpiryLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class CreditBlockExpiryLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: CreditBlockExpiryLedgerEntryCreditBlock

    currency: str

    customer: CreditBlockExpiryLedgerEntryCustomer

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


class VoidLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class VoidLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class VoidLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: VoidLedgerEntryCreditBlock

    currency: str

    customer: VoidLedgerEntryCustomer

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


class VoidInitiatedLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class VoidInitiatedLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class VoidInitiatedLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: VoidInitiatedLedgerEntryCreditBlock

    currency: str

    customer: VoidInitiatedLedgerEntryCustomer

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


class AmendmentLedgerEntryCreditBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None


class AmendmentLedgerEntryCustomer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class AmendmentLedgerEntry(BaseModel):
    id: str

    amount: float

    created_at: datetime

    credit_block: AmendmentLedgerEntryCreditBlock

    currency: str

    customer: AmendmentLedgerEntryCustomer

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


LedgerCreateEntryByExternalIDResponse = Union[
    IncrementLedgerEntry,
    DecrementLedgerEntry,
    ExpirationChangeLedgerEntry,
    CreditBlockExpiryLedgerEntry,
    VoidLedgerEntry,
    VoidInitiatedLedgerEntry,
    AmendmentLedgerEntry,
]
