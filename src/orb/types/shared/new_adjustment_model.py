# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "NewAdjustmentModel",
    "NewPercentageDiscount",
    "NewUsageDiscount",
    "NewAmountDiscount",
    "NewMinimum",
    "NewMaximum",
]


class NewPercentageDiscount(BaseModel):
    adjustment_type: Literal["percentage_discount"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    percentage_discount: float

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewUsageDiscount(BaseModel):
    adjustment_type: Literal["usage_discount"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    usage_discount: float

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewAmountDiscount(BaseModel):
    adjustment_type: Literal["amount_discount"]

    amount_discount: str

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewMinimum(BaseModel):
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


class NewMaximum(BaseModel):
    adjustment_type: Literal["maximum"]

    applies_to_price_ids: List[str]
    """The set of price IDs to which this adjustment applies."""

    maximum_amount: str

    is_invoice_level: Optional[bool] = None
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


NewAdjustmentModel: TypeAlias = Annotated[
    Union[NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum],
    PropertyInfo(discriminator="adjustment_type"),
]
