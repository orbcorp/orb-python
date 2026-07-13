# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.custom_expiration import CustomExpiration

__all__ = ["CreditListResponse", "Filter", "CreditAllocation", "CreditAllocationFilter", "CreditCommitment"]


class Filter(BaseModel):
    """A PriceFilter that only allows item_id field for block filters."""

    field: Literal["item_id"]
    """The property of the price the block applies to. Only item_id is supported."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class CreditAllocationFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class CreditAllocation(BaseModel):
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

    filters: Optional[List[CreditAllocationFilter]] = None

    license_type_id: Optional[str] = None


class CreditCommitment(BaseModel):
    """
    The subscription commitment whose true-up rolled forward into this credit block.
    Present only when `credit_block_source` is `commitment`.
    """

    id: str
    """The ID of the subscription commitment this block was rolled forward from."""

    subscription_id: Optional[str] = None
    """The subscription the commitment belongs to."""


class CreditListResponse(BaseModel):
    id: str

    balance: float

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

    filters: List[Filter]

    maximum_initial_balance: Optional[float] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]

    credit_allocation: Optional[CreditAllocation] = None
    """The credit allocation that funded a block.

    Extends the allocation resource serialized on prices with the catalog-item
    attribution of the funding price.
    """

    credit_commitment: Optional[CreditCommitment] = None
    """
    The subscription commitment whose true-up rolled forward into this credit block.
    Present only when `credit_block_source` is `commitment`.
    """
