# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.custom_expiration import CustomExpiration

__all__ = [
    "CreditBlockAccountingSyncSucceededWebhookEvent",
    "AccountingSyncRecord",
    "Block",
    "BlockFilter",
    "BlockCreditAllocation",
    "BlockCreditAllocationFilter",
    "BlockCreditCommitment",
    "Properties",
]


class AccountingSyncRecord(BaseModel):
    id: str

    customer_id: str

    record_type: Literal[
        "customer",
        "invoice",
        "transaction",
        "customer_balance_transaction",
        "credit_note",
        "subscription",
        "sales_order",
        "block",
    ]

    block_id: Optional[str] = None

    error_details: Optional[Dict[str, object]] = None

    invoice_id: Optional[str] = None

    provider_customer_id: Optional[str] = None

    status: Optional[str] = None

    sync_action: Optional[str] = None


class BlockFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BlockCreditAllocationFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BlockCreditAllocation(BaseModel):
    """The credit allocation that funded a block.

    Extends the allocation resource
    serialized on prices with the catalog-item attribution of the funding price.
    """

    allows_rollover: bool

    currency: str

    custom_expiration: Optional[CustomExpiration] = None

    item_id: str
    """
    The ID of the catalog item this block was allocated from, derived from the
    allocation's price.
    """

    filters: Optional[List[BlockCreditAllocationFilter]] = None

    license_type_id: Optional[str] = None


class BlockCreditCommitment(BaseModel):
    """
    The subscription commitment whose true-up rolled forward into this credit block.
    Present only when `credit_block_source` is `commitment`.
    """

    id: str
    """The ID of the subscription commitment this block was rolled forward from."""

    subscription_id: Optional[str] = None
    """The subscription the commitment belongs to."""


class Block(BaseModel):
    """The Credit Block resource models prepaid credits within Orb."""

    id: str

    balance: str

    credit_block_source: Literal["allocation", "top_up", "commitment", "manual"]
    """
    How this credit block was created: `allocation` (a subscription's recurring
    credit allocation), `top_up` (an automatic balance-threshold top-up),
    `commitment` (a subscription commitment true-up rolled forward as credit), or
    `manual` (a manual credit ledger increment, including credits voided or expired
    off another block).
    """

    effective_date: Optional[datetime] = None

    expiry_date: Optional[datetime] = None

    filters: List[BlockFilter]

    maximum_initial_balance: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]

    credit_allocation: Optional[BlockCreditAllocation] = None
    """The credit allocation that funded a block.

    Extends the allocation resource serialized on prices with the catalog-item
    attribution of the funding price.
    """

    credit_commitment: Optional[BlockCreditCommitment] = None
    """
    The subscription commitment whose true-up rolled forward into this credit block.
    Present only when `credit_block_source` is `commitment`.
    """


class Properties(BaseModel):
    connection_type: str


class CreditBlockAccountingSyncSucceededWebhookEvent(BaseModel):
    """Issued when a credit block accounting sync succeeds."""

    id: str
    """The ID of this webhook event."""

    accounting_sync_record: AccountingSyncRecord

    block: Block
    """The Credit Block resource models prepaid credits within Orb."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    type: Literal["credit_block.accounting_sync_succeeded"]
    """The event this payload describes."""
