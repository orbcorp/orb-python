# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ReplaceSubscriptionAdjustmentParams",
    "Adjustment",
    "AdjustmentNewPercentageDiscount",
    "AdjustmentNewUsageDiscount",
    "AdjustmentNewAmountDiscount",
    "AdjustmentNewMinimum",
    "AdjustmentNewMaximum",
]


class AdjustmentNewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    percentage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    usage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AdjustmentNewMinimum(TypedDict, total=False):
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


class AdjustmentNewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    maximum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


Adjustment: TypeAlias = Union[
    AdjustmentNewPercentageDiscount,
    AdjustmentNewUsageDiscount,
    AdjustmentNewAmountDiscount,
    AdjustmentNewMinimum,
    AdjustmentNewMaximum,
]


class ReplaceSubscriptionAdjustmentParams(TypedDict, total=False):
    adjustment: Required[Adjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the subscription."""
