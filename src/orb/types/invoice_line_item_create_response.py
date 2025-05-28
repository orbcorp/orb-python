# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .price import Price
from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.discount import Discount

__all__ = [
    "InvoiceLineItemCreateResponse",
    "Adjustment",
    "AdjustmentMonetaryUsageDiscountAdjustment",
    "AdjustmentMonetaryUsageDiscountAdjustmentFilter",
    "AdjustmentMonetaryAmountDiscountAdjustment",
    "AdjustmentMonetaryAmountDiscountAdjustmentFilter",
    "AdjustmentMonetaryPercentageDiscountAdjustment",
    "AdjustmentMonetaryPercentageDiscountAdjustmentFilter",
    "AdjustmentMonetaryMinimumAdjustment",
    "AdjustmentMonetaryMinimumAdjustmentFilter",
    "AdjustmentMonetaryMaximumAdjustment",
    "AdjustmentMonetaryMaximumAdjustmentFilter",
    "Maximum",
    "MaximumFilter",
    "Minimum",
    "MinimumFilter",
    "SubLineItem",
    "SubLineItemMatrixSubLineItem",
    "SubLineItemMatrixSubLineItemGrouping",
    "SubLineItemMatrixSubLineItemMatrixConfig",
    "SubLineItemTierSubLineItem",
    "SubLineItemTierSubLineItemGrouping",
    "SubLineItemTierSubLineItemTierConfig",
    "SubLineItemOtherSubLineItem",
    "SubLineItemOtherSubLineItemGrouping",
    "TaxAmount",
]


class AdjustmentMonetaryUsageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentMonetaryUsageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["usage_discount"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentMonetaryUsageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""

    usage_discount: float
    """
    The number of usage units by which to discount the price this adjustment applies
    to in a given billing period.
    """


class AdjustmentMonetaryAmountDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentMonetaryAmountDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["amount_discount"]

    amount: str
    """The value applied by an adjustment."""

    amount_discount: str
    """
    The amount by which to discount the prices this adjustment applies to in a given
    billing period.
    """

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentMonetaryAmountDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


class AdjustmentMonetaryPercentageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentMonetaryPercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["percentage_discount"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentMonetaryPercentageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    percentage_discount: float
    """
    The percentage (as a value between 0 and 1) by which to discount the price
    intervals this adjustment applies to in a given billing period.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


class AdjustmentMonetaryMinimumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentMonetaryMinimumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["minimum"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentMonetaryMinimumAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    item_id: str
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: str
    """
    The minimum amount to charge in a given billing period for the prices this
    adjustment applies to.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


class AdjustmentMonetaryMaximumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class AdjustmentMonetaryMaximumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["maximum"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[AdjustmentMonetaryMaximumAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the prices this
    adjustment applies to.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


Adjustment: TypeAlias = Annotated[
    Union[
        AdjustmentMonetaryUsageDiscountAdjustment,
        AdjustmentMonetaryAmountDiscountAdjustment,
        AdjustmentMonetaryPercentageDiscountAdjustment,
        AdjustmentMonetaryMinimumAdjustment,
        AdjustmentMonetaryMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class MaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Maximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Minimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class SubLineItemMatrixSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class SubLineItemMatrixSubLineItemMatrixConfig(BaseModel):
    dimension_values: List[Optional[str]]
    """The ordered dimension values for this line item."""


class SubLineItemMatrixSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemMatrixSubLineItemGrouping] = None

    matrix_config: SubLineItemMatrixSubLineItemMatrixConfig

    name: str

    quantity: float

    type: Literal["matrix"]


class SubLineItemTierSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class SubLineItemTierSubLineItemTierConfig(BaseModel):
    first_unit: float

    last_unit: Optional[float] = None

    unit_amount: str


class SubLineItemTierSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemTierSubLineItemGrouping] = None

    name: str

    quantity: float

    tier_config: SubLineItemTierSubLineItemTierConfig

    type: Literal["tier"]


class SubLineItemOtherSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class SubLineItemOtherSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemOtherSubLineItemGrouping] = None

    name: str

    quantity: float

    type: Literal["'null'"]


SubLineItem: TypeAlias = Annotated[
    Union[SubLineItemMatrixSubLineItem, SubLineItemTierSubLineItem, SubLineItemOtherSubLineItem],
    PropertyInfo(discriminator="type"),
]


class TaxAmount(BaseModel):
    amount: str
    """The amount of additional tax incurred by this tax rate."""

    tax_rate_description: str
    """The human-readable description of the applied tax rate."""

    tax_rate_percentage: Optional[str] = None
    """The tax rate percentage, out of 100."""


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

    discount: Optional[Discount] = None

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

    maximum: Optional[Maximum] = None
    """This field is deprecated in favor of `adjustments`."""

    maximum_amount: Optional[str] = None
    """This field is deprecated in favor of `adjustments`."""

    minimum: Optional[Minimum] = None
    """This field is deprecated in favor of `adjustments`."""

    minimum_amount: Optional[str] = None
    """This field is deprecated in favor of `adjustments`."""

    name: str
    """The name of the price associated with this line item."""

    partially_invoiced_amount: str
    """Any amount applied from a partial invoice"""

    price: Optional[Price] = None
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
    """The line amount before before any adjustments."""

    tax_amounts: List[TaxAmount]
    """An array of tax rates and their incurred tax amounts.

    Empty if no tax integration is configured.
    """

    usage_customer_ids: Optional[List[str]] = None
    """
    A list of customer ids that were used to calculate the usage for this line item.
    """
