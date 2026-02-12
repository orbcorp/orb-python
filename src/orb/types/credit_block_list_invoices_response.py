# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.customer_minified import CustomerMinified
from .shared.subscription_minified import SubscriptionMinified

__all__ = ["CreditBlockListInvoicesResponse", "Block", "BlockFilter", "Invoice"]


class BlockFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Block(BaseModel):
    """The Credit Block resource models prepaid credits within Orb."""

    id: str

    balance: float

    effective_date: Optional[datetime] = None

    expiry_date: Optional[datetime] = None

    filters: List[BlockFilter]

    maximum_initial_balance: Optional[float] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]


class Invoice(BaseModel):
    id: str

    customer: CustomerMinified

    invoice_number: str

    status: Literal["issued", "paid", "synced", "void", "draft"]

    subscription: Optional[SubscriptionMinified] = None


class CreditBlockListInvoicesResponse(BaseModel):
    block: Block
    """The Credit Block resource models prepaid credits within Orb."""

    invoices: List[Invoice]
