# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AffectedBlock"]


class AffectedBlock(BaseModel):
    id: str

    expiry_date: Optional[datetime] = None

    per_unit_cost_basis: Optional[str] = None
