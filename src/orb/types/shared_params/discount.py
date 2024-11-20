# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .trial_discount import TrialDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["Discount", "UsageDiscount"]


class UsageDiscount(TypedDict, total=False):
    applies_to_price_ids: Required[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    discount_type: Required[Literal["usage"]]

    usage_discount: Required[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """

    reason: Optional[str]


Discount: TypeAlias = Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount]
