# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.price import Price
from .shared.tax_amount import TaxAmount
from .shared.tier_sub_line_item import TierSubLineItem
from .shared.other_sub_line_item import OtherSubLineItem
from .shared.matrix_sub_line_item import MatrixSubLineItem
from .shared.monetary_maximum_adjustment import MonetaryMaximumAdjustment
from .shared.monetary_minimum_adjustment import MonetaryMinimumAdjustment
from .shared.monetary_usage_discount_adjustment import MonetaryUsageDiscountAdjustment
from .shared.monetary_amount_discount_adjustment import MonetaryAmountDiscountAdjustment
from .shared.monetary_percentage_discount_adjustment import MonetaryPercentageDiscountAdjustment

__all__ = [
    "InvoiceLineItemCreateResponse",
    "Adjustment",
    "AdjustmentMonetaryTieredPercentageDiscountAdjustment",
    "AdjustmentMonetaryTieredPercentageDiscountAdjustmentFilter",
    "AdjustmentMonetaryTieredPercentageDiscountAdjustmentTier",
    "SubLineItem",
]


class AdjustmentMonetaryTieredPercentageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentMonetaryTieredPercentageDiscountAdjustmentTier(BaseModel):
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


class AdjustmentMonetaryTieredPercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["tiered_percentage_discount"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentMonetaryTieredPercentageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invoice, false for adjustments that
    apply to only one price.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""

    replaces_adjustment_id: Optional[str] = None
    """The adjustment id this adjustment replaces.

    This adjustment will take the place of the replaced adjustment in plan version
    migrations.
    """

    tiers: List[AdjustmentMonetaryTieredPercentageDiscountAdjustmentTier]
    """
    The ordered, contiguous bands of cumulative eligible spend, each discounted at
    its own percentage (progressive fill-a-tier), applied to the prices this
    adjustment covers in a given billing period.
    """


Adjustment: TypeAlias = Annotated[
    Union[
        MonetaryUsageDiscountAdjustment,
        MonetaryAmountDiscountAdjustment,
        MonetaryPercentageDiscountAdjustment,
        AdjustmentMonetaryTieredPercentageDiscountAdjustment,
        MonetaryMinimumAdjustment,
        MonetaryMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]

SubLineItem: TypeAlias = Annotated[
    Union[MatrixSubLineItem, TierSubLineItem, OtherSubLineItem], PropertyInfo(discriminator="type")
]


class InvoiceLineItemCreateResponse(BaseModel):
    id: str
    """A unique ID for this line item."""

    adjusted_subtotal: str
    """
    The line amount after any adjustments and before overage conversion, credits and
    partial invoicing.
    """

    adjustments: List[Adjustment]
    """
    All adjustments applied to the line item in the order they were applied based on
    invoice calculations (ie. usage discounts -> amount discounts -> percentage
    discounts -> minimums -> maximums).
    """

    amount: str
    """
    The final amount for a line item after all adjustments and pre paid credits have
    been applied.
    """

    credits_applied: str
    """The number of prepaid credits applied."""

    end_date: datetime
    """The end date of the range of time applied for this line item's price."""

    filter: Optional[str] = None
    """An additional filter that was used to calculate the usage for this line item."""

    grouping: Optional[str] = None
    """
    [DEPRECATED] For configured prices that are split by a grouping key, this will
    be populated with the key and a value. The `amount` and `subtotal` will be the
    values for this particular grouping.
    """

    name: str
    """The name of the price associated with this line item."""

    partially_invoiced_amount: str
    """Any amount applied from a partial invoice"""

    price: Price
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    For more on the types of prices, see
    [the core concepts documentation](/core-concepts#plan-and-price)
    """

    quantity: float
    """Either the fixed fee quantity or the usage during the service period."""

    start_date: datetime
    """The start date of the range of time applied for this line item's price."""

    sub_line_items: List[SubLineItem]
    """
    For complex pricing structures, the line item can be broken down further in
    `sub_line_items`.
    """

    subtotal: str
    """The line amount before any adjustments."""

    tax_amounts: List[TaxAmount]
    """An array of tax rates and their incurred tax amounts.

    Empty if no tax integration is configured.
    """

    usage_customer_ids: Optional[List[str]] = None
    """
    A list of customer ids that were used to calculate the usage for this line item.
    """
