# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CustomerCreatePortalSessionByExternalIDResponse"]


class CustomerCreatePortalSessionByExternalIDResponse(BaseModel):
    id: str

    created_at: datetime

    customer_id: str

    expires_at: Optional[datetime] = None

    url: str
