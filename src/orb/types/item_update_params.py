# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal, Required

from typing import Optional, Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ItemUpdateParams", "ExternalConnection"]


class ItemUpdateParams(TypedDict, total=False):
    external_connections: Optional[Iterable[ExternalConnection]]

    name: Optional[str]


class ExternalConnection(TypedDict, total=False):
    external_connection_name: Required[
        Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]
    ]

    external_entity_id: Required[str]
