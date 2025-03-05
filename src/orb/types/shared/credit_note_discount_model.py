# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CreditNoteDiscountModel", "AppliesToPrice"]


class AppliesToPrice(BaseModel):
    id: str

    name: str


class CreditNoteDiscountModel(BaseModel):
    amount_applied: str

    discount_type: Literal["percentage"]

    percentage_discount: float

    applies_to_prices: Optional[List[AppliesToPrice]] = None

    reason: Optional[str] = None
