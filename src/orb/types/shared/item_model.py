# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .item_external_connection_model import ItemExternalConnectionModel

__all__ = ["ItemModel"]


class ItemModel(BaseModel):
    id: str

    created_at: datetime

    external_connections: List[ItemExternalConnectionModel]

    name: str
