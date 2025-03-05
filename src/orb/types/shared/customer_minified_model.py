# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CustomerMinifiedModel"]


class CustomerMinifiedModel(BaseModel):
    id: str

    external_customer_id: Optional[str] = None
