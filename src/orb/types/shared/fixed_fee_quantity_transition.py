# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["FixedFeeQuantityTransition"]


class FixedFeeQuantityTransition(BaseModel):
    effective_date: datetime

    price_id: str

    quantity: int
