# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Discount", "PercentageDiscount", "TrialDiscount", "UsageDiscount", "AmountDiscount"]


class PercentageDiscount(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["percentage"]

    percentage_discount: float
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    reason: Optional[str] = None


class TrialDiscount(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["trial"]

    reason: Optional[str] = None

    trial_amount_discount: Optional[str] = None
    """Only available if discount_type is `trial`"""

    trial_percentage_discount: Optional[float] = None
    """Only available if discount_type is `trial`"""


class UsageDiscount(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["usage"]

    usage_discount: float
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """

    reason: Optional[str] = None


class AmountDiscount(BaseModel):
    amount_discount: str
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: List[str]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Literal["amount"]

    reason: Optional[str] = None


Discount = Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount]
