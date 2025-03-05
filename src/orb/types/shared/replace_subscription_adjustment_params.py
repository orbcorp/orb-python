# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ReplaceSubscriptionAdjustmentParams",
    "Adjustment",
    "AdjustmentNewPercentageDiscount",
    "AdjustmentNewUsageDiscount",
    "AdjustmentNewAmountDiscount",
    "AdjustmentNewMinimum",
    "AdjustmentNewMaximum",
]


class AdjustmentNewPercentageDiscount(BaseModel):
    adjustment_type: Literal["percentage_discount"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    percentage_discount: float

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewUsageDiscount(BaseModel):
    adjustment_type: Literal["usage_discount"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    usage_discount: float

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewAmountDiscount(BaseModel):
    adjustment_type: Literal["amount_discount"]

    amount_discount: str

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewMinimum(BaseModel):
    adjustment_type: Literal["minimum"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    item_id: str
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: str

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewMaximum(BaseModel):
    adjustment_type: Literal["maximum"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    maximum_amount: str

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


Adjustment: TypeAlias = Annotated[
    Union[
        AdjustmentNewPercentageDiscount,
        AdjustmentNewUsageDiscount,
        AdjustmentNewAmountDiscount,
        AdjustmentNewMinimum,
        AdjustmentNewMaximum,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class ReplaceSubscriptionAdjustmentParams(BaseModel):
    adjustment: Adjustment
    """The definition of a new adjustment to create and add to the subscription."""

    replaces_adjustment_id: str
    """The id of the adjustment on the plan to replace in the subscription."""
