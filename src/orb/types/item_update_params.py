# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemUpdateParams", "ExternalConnection"]


class ItemUpdateParams(TypedDict, total=False):
    external_connections: Optional[Iterable[ExternalConnection]]

    name: Optional[str]


class ExternalConnection(TypedDict, total=False):
    external_connection_name: Required[
        Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]
    ]

    external_entity_id: Required[str]
