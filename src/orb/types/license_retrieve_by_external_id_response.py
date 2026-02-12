# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LicenseRetrieveByExternalIDResponse"]


class LicenseRetrieveByExternalIDResponse(BaseModel):
    id: str

    end_date: Optional[datetime] = None

    external_license_id: str

    license_type_id: str

    start_date: datetime

    status: Literal["active", "inactive"]

    subscription_id: str
