# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["NewAccountingSyncConfigurationModel", "AccountingProvider"]


class AccountingProvider(TypedDict, total=False):
    external_provider_id: Required[str]

    provider_type: Required[str]


class NewAccountingSyncConfigurationModel(TypedDict, total=False):
    accounting_providers: Optional[Iterable[AccountingProvider]]

    excluded: Optional[bool]
