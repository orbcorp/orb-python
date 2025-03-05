# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Item", "ExternalConnection"]


class ExternalConnection(BaseModel):
    external_connection_name: Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]

    external_entity_id: str


class Item(BaseModel):
    id: str

    created_at: datetime

    external_connections: List[ExternalConnection]

    name: str
