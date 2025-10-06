# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ItemSlim"]


class ItemSlim(BaseModel):
    id: str
    """The Orb-assigned unique identifier for the item."""

    name: str
    """The name of the item."""
