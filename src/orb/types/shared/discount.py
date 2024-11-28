# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .trial_discount import TrialDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["Discount", "UsageDiscount"]


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


Discount: TypeAlias = Annotated[
    Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount], PropertyInfo(discriminator="discount_type")
]
