# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Item", "ExternalConnection"]


class ExternalConnection(BaseModel):
    external_connection_name: Literal[
        "stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok", "numeral"
    ]
    """The name of the external system this item is connected to."""

    external_entity_id: str
    """The identifier of this item in the external system."""


class Item(BaseModel):
    id: str
    """The Orb-assigned unique identifier for the item."""

    created_at: datetime
    """The time at which the item was created."""

    external_connections: List[ExternalConnection]
    """
    A list of external connections for this item, used to sync with external
    invoicing and tax systems.
    """

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    name: str
    """The name of the item."""

    archived_at: Optional[datetime] = None
    """The time at which the item was archived. If null, the item is not archived."""
