# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .accounting_provider_config_param import AccountingProviderConfigParam

__all__ = ["NewAccountingSyncConfigurationParam"]


class NewAccountingSyncConfigurationParam(TypedDict, total=False):
    accounting_providers: Optional[Iterable[AccountingProviderConfigParam]]

    excluded: Optional[bool]
