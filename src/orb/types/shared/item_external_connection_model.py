# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ItemExternalConnectionModel"]


class ItemExternalConnectionModel(BaseModel):
    external_connection_name: Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]

    external_entity_id: str
