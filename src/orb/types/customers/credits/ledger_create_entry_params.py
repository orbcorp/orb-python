# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "LedgerCreateEntryParams",
    "AddIncrementCreditLedgerEntryRequestParams",
    "AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings",
    "AddDecrementCreditLedgerEntryRequestParams",
    "AddExpirationChangeCreditLedgerEntryRequestParams",
    "AddVoidCreditLedgerEntryRequestParams",
    "AddAmendmentCreditLedgerEntryRequestParams",
]


class AddIncrementCreditLedgerEntryRequestParams(TypedDict, total=False):
    amount: Required[float]
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    entry_type: Required[Literal["increment"]]

    currency: Optional[str]
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str]
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    effective_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    An ISO 8601 format date that denotes when this credit balance should become
    available for use.
    """

    expiry_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """An ISO 8601 format date that denotes when this credit balance should expire."""

    invoice_settings: Optional[AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings]
    """
    Passing `invoice_settings` automatically generates an invoice for the newly
    added credits. If `invoice_settings` is passed, you must specify
    per_unit_cost_basis, as the calculation of the invoice total is done on that
    basis.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str]
    """Can only be specified when entry_type=increment.

    How much, in USD, a customer paid for a single credit in this block
    """


class AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings(TypedDict, total=False):
    auto_collection: Required[bool]
    """
    Whether the credits purchase invoice should auto collect with the customer's
    saved payment method.
    """

    net_terms: Required[int]
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0.
    """

    memo: Optional[str]
    """An optional memo to display on the invoice."""


class AddDecrementCreditLedgerEntryRequestParams(TypedDict, total=False):
    amount: Required[float]
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    entry_type: Required[Literal["decrement"]]

    currency: Optional[str]
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str]
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddExpirationChangeCreditLedgerEntryRequestParams(TypedDict, total=False):
    entry_type: Required[Literal["expiration_change"]]

    expiry_date: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]
    """An ISO 8601 format date that identifies the origination credit block to expire"""

    target_expiry_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """
    A future date (specified in YYYY-MM-DD format) used for expiration change,
    denoting when credits transferred (as part of a partial block expiration) should
    expire.
    """

    amount: Optional[float]
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    block_id: Optional[str]
    """
    The ID of the block affected by an expiration_change, used to differentiate
    between multiple blocks with the same `expiry_date`.
    """

    currency: Optional[str]
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str]
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddVoidCreditLedgerEntryRequestParams(TypedDict, total=False):
    amount: Required[float]
    """The number of credits to effect.

    Note that this is required for increment, decrement, void, or undo operations.
    """

    block_id: Required[str]
    """The ID of the block to void."""

    entry_type: Required[Literal["void"]]

    currency: Optional[str]
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str]
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    void_reason: Optional[Literal["refund"]]
    """Can only be specified when `entry_type=void`. The reason for the void."""


class AddAmendmentCreditLedgerEntryRequestParams(TypedDict, total=False):
    amount: Required[float]
    """The number of credits to effect.

    Note that this is required for increment, decrement or void operations.
    """

    block_id: Required[str]
    """The ID of the block to reverse a decrement from."""

    entry_type: Required[Literal["amendment"]]

    currency: Optional[str]
    """The currency or custom pricing unit to use for this ledger entry.

    If this is a real-world currency, it must match the customer's invoicing
    currency.
    """

    description: Optional[str]
    """Optional metadata that can be specified when adding ledger results via the API.

    For example, this can be used to note an increment refers to trial credits, or
    for noting corrections as a result of an incident, etc.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


LedgerCreateEntryParams = Union[
    AddIncrementCreditLedgerEntryRequestParams,
    AddDecrementCreditLedgerEntryRequestParams,
    AddExpirationChangeCreditLedgerEntryRequestParams,
    AddVoidCreditLedgerEntryRequestParams,
    AddAmendmentCreditLedgerEntryRequestParams,
]
