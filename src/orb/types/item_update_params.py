# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemUpdateParams", "ExternalConnection"]


class ItemUpdateParams(TypedDict, total=False):
    external_connections: Required[Optional[Iterable[ExternalConnection]]]

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class ExternalConnection(TypedDict, total=False):
    external_connection_name: Required[
        Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]
    ]

    external_entity_id: Required[str]
