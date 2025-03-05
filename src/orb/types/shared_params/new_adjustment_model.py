# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "NewAdjustmentModel",
    "NewPercentageDiscount",
    "NewUsageDiscount",
    "NewAmountDiscount",
    "NewMinimum",
    "NewMaximum",
]


class NewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    percentage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    usage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewMinimum(TypedDict, total=False):
    adjustment_type: Required[Literal["minimum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    item_id: Required[str]
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class NewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    maximum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


NewAdjustmentModel: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]
