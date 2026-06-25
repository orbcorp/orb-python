# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .trial_discount import TrialDiscount
from .usage_discount import UsageDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["Discount", "TieredPercentageDiscount", "TieredPercentageDiscountTier", "TieredPercentageDiscountFilter"]


class TieredPercentageDiscountTier(BaseModel):
    """One band of a tiered percentage discount.

    Bounds are denominated in the discount's currency.
    `lower_bound` is the exclusive start of the band and `upper_bound` is the inclusive end;
    `upper_bound` is null only for the open-ended final tier.
    """

    lower_bound: float
    """Exclusive lower bound of cumulative spend for this tier."""

    percentage: float
    """
    The percentage (between 0 and 1) discounted from spend that falls within this
    tier.
    """

    upper_bound: Optional[float] = None
    """
    Inclusive upper bound of cumulative spend for this tier; null for the final
    open-ended tier.
    """


class TieredPercentageDiscountFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPercentageDiscount(BaseModel):
    discount_type: Literal["tiered_percentage"]

    tiers: List[TieredPercentageDiscountTier]
    """Only available if discount_type is `tiered_percentage`.

    The ordered, contiguous bands of cumulative eligible spend, each discounted at
    its own percentage (progressive fill-a-tier).
    """

    applies_to_price_ids: Optional[List[str]] = None
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    filters: Optional[List[TieredPercentageDiscountFilter]] = None
    """The filters that determine which prices to apply this discount to."""

    reason: Optional[str] = None


Discount: TypeAlias = Annotated[
    Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount, TieredPercentageDiscount],
    PropertyInfo(discriminator="discount_type"),
]
