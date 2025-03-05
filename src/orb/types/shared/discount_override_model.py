# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DiscountOverrideModel"]


class DiscountOverrideModel(BaseModel):
    discount_type: Literal["percentage", "usage", "amount"]

    amount_discount: Optional[str] = None
    """Only available if discount_type is `amount`."""

    percentage_discount: Optional[float] = None
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    usage_discount: Optional[float] = None
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """
