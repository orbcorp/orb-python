# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .shared_params.item_external_connection_model import ItemExternalConnectionModel

__all__ = ["ItemUpdateParams"]


class ItemUpdateParams(TypedDict, total=False):
    external_connections: Optional[Iterable[ItemExternalConnectionModel]]

    name: Optional[str]
