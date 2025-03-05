# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["NewAccountingSyncConfigurationModel", "AccountingProvider"]


class AccountingProvider(BaseModel):
    external_provider_id: str

    provider_type: str


class NewAccountingSyncConfigurationModel(BaseModel):
    accounting_providers: Optional[List[AccountingProvider]] = None

    excluded: Optional[bool] = None
