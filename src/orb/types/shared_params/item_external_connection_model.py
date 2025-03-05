# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemExternalConnectionModel"]


class ItemExternalConnectionModel(TypedDict, total=False):
    external_connection_name: Required[
        Literal["stripe", "quickbooks", "bill.com", "netsuite", "taxjar", "avalara", "anrok"]
    ]

    external_entity_id: Required[str]
