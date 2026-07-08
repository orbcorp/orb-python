# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountingProviderConfigParam"]


class AccountingProviderConfigParam(TypedDict, total=False):
    external_provider_id: Required[str]

    provider_type: Required[Literal["quickbooks", "netsuite"]]
