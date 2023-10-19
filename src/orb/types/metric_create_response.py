# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MetricCreateResponse", "Item", "ItemExternalConnection"]


class ItemExternalConnection(BaseModel):
    external_connection_name: Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]

    external_entity_id: str


class Item(BaseModel):
    id: str

    created_at: datetime

    external_connections: List[ItemExternalConnection]

    name: str


class MetricCreateResponse(BaseModel):
    id: str

    description: Optional[str]

    item: Item
    """The Item resource represents a sellable product or good.

    Items are associated with all line items, billable metrics, and prices and are
    used for defining external sync behavior for invoices and tax calculation
    purposes.
    """

    metadata: Dict[str, str]

    name: str

    status: Literal["active", "draft", "archived"]
