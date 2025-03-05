# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "AddCreditLedgerEntryRequest",
    "AddIncrementCreditLedgerEntryRequestParams",
    "AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings",
    "AddDecrementCreditLedgerEntryRequestParams",
    "AddExpirationChangeCreditLedgerEntryRequestParams",
    "AddVoidCreditLedgerEntryRequestParams",
    "AddAmendmentCreditLedgerEntryRequestParams",
]


class AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings(BaseModel):
    auto_collection: bool
    """
    Whether the credits purchase invoice should auto collect with the customer's
    saved payment method.
    """

    net_terms: int
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0.
    """

    memo: Optional[str] = None
    """An optional memo to display on the invoice."""

    require_successful_payment: Optional[bool] = None
    """
    If true, the new credit block will require that the corresponding invoice is
    paid before it can be drawn down from.
    """


class AddIncrementCreditLedgerEntryRequestParams(BaseModel):
    amount: float
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    entry_type: Literal["increment"]

    currency: Optional[str] = None
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str] = None
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    effective_date: Optional[datetime] = None
    """
    An ISO 8601 format date that denotes when this credit balance should become
    available for use.
    """

    expiry_date: Optional[datetime] = None
    """An ISO 8601 format date that denotes when this credit balance should expire."""

    invoice_settings: Optional[AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings] = None
    """
    Passing `invoice_settings` automatically generates an invoice for the newly
    added credits. If `invoice_settings` is passed, you must specify
    per_unit_cost_basis, as the calculation of the invoice total is done on that
    basis.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str] = None
    """Can only be specified when entry_type=increment.

    How much, in the customer's currency, a customer paid for a single credit in
    this block
    """


class AddDecrementCreditLedgerEntryRequestParams(BaseModel):
    amount: float
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    entry_type: Literal["decrement"]

    currency: Optional[str] = None
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str] = None
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddExpirationChangeCreditLedgerEntryRequestParams(BaseModel):
    entry_type: Literal["expiration_change"]

    expiry_date: Optional[datetime] = None
    """An ISO 8601 format date that identifies the origination credit block to expire"""

    target_expiry_date: date
    """
    A future date (specified in YYYY-MM-DD format) used for expiration change,
    denoting when credits transferred (as part of a partial block expiration) should
    expire.
    """

    amount: Optional[float] = None
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    block_id: Optional[str] = None
    """
    The ID of the block affected by an expiration_change, used to differentiate
    between multiple blocks with the same `expiry_date`.
    """

    currency: Optional[str] = None
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str] = None
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddVoidCreditLedgerEntryRequestParams(BaseModel):
    amount: float
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    block_id: str
    """The ID of the block to void."""

    entry_type: Literal["void"]

    currency: Optional[str] = None
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str] = None
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    void_reason: Optional[Literal["refund"]] = None
    """Can only be specified when `entry_type=void`. The reason for the void."""


class AddAmendmentCreditLedgerEntryRequestParams(BaseModel):
    amount: float
    """The number of credits to effect.

    Note that this is required for increment, decrement or void operations.
    """

    block_id: str
    """The ID of the block to reverse a decrement from."""

    entry_type: Literal["amendment"]

    currency: Optional[str] = None
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str] = None
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


AddCreditLedgerEntryRequest: TypeAlias = Annotated[
    Union[
        AddIncrementCreditLedgerEntryRequestParams,
        AddDecrementCreditLedgerEntryRequestParams,
        AddExpirationChangeCreditLedgerEntryRequestParams,
        AddVoidCreditLedgerEntryRequestParams,
        AddAmendmentCreditLedgerEntryRequestParams,
    ],
    PropertyInfo(discriminator="entry_type"),
]
