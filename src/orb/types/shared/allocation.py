# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .custom_expiration import CustomExpiration

__all__ = ["Allocation"]


class Allocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[CustomExpiration] = None
