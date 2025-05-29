# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.billing_cycle_relative_date import BillingCycleRelativeDate

__all__ = [
    "SubscriptionPriceIntervalsParams",
    "Add",
    "AddAllocationPrice",
    "AddAllocationPriceCustomExpiration",
    "AddDiscount",
    "AddDiscountAmountDiscountCreationParams",
    "AddDiscountPercentageDiscountCreationParams",
    "AddDiscountUsageDiscountCreationParams",
    "AddFixedFeeQuantityTransition",
    "AddPrice",
    "AddPriceNewFloatingUnitPrice",
    "AddPriceNewFloatingUnitPriceUnitConfig",
    "AddPriceNewFloatingUnitPriceBillingCycleConfiguration",
    "AddPriceNewFloatingUnitPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingUnitPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingPackagePrice",
    "AddPriceNewFloatingPackagePricePackageConfig",
    "AddPriceNewFloatingPackagePriceBillingCycleConfiguration",
    "AddPriceNewFloatingPackagePriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingPackagePriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingMatrixPrice",
    "AddPriceNewFloatingMatrixPriceMatrixConfig",
    "AddPriceNewFloatingMatrixPriceMatrixConfigMatrixValue",
    "AddPriceNewFloatingMatrixPriceBillingCycleConfiguration",
    "AddPriceNewFloatingMatrixPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingMatrixPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingMatrixWithAllocationPrice",
    "AddPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig",
    "AddPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue",
    "AddPriceNewFloatingMatrixWithAllocationPriceBillingCycleConfiguration",
    "AddPriceNewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingTieredPrice",
    "AddPriceNewFloatingTieredPriceTieredConfig",
    "AddPriceNewFloatingTieredPriceTieredConfigTier",
    "AddPriceNewFloatingTieredPriceBillingCycleConfiguration",
    "AddPriceNewFloatingTieredPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingTieredPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingTieredBpsPrice",
    "AddPriceNewFloatingTieredBpsPriceTieredBpsConfig",
    "AddPriceNewFloatingTieredBpsPriceTieredBpsConfigTier",
    "AddPriceNewFloatingTieredBpsPriceBillingCycleConfiguration",
    "AddPriceNewFloatingTieredBpsPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingTieredBpsPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingBpsPrice",
    "AddPriceNewFloatingBpsPriceBpsConfig",
    "AddPriceNewFloatingBpsPriceBillingCycleConfiguration",
    "AddPriceNewFloatingBpsPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingBpsPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingBulkBpsPrice",
    "AddPriceNewFloatingBulkBpsPriceBulkBpsConfig",
    "AddPriceNewFloatingBulkBpsPriceBulkBpsConfigTier",
    "AddPriceNewFloatingBulkBpsPriceBillingCycleConfiguration",
    "AddPriceNewFloatingBulkBpsPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingBulkBpsPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingBulkPrice",
    "AddPriceNewFloatingBulkPriceBulkConfig",
    "AddPriceNewFloatingBulkPriceBulkConfigTier",
    "AddPriceNewFloatingBulkPriceBillingCycleConfiguration",
    "AddPriceNewFloatingBulkPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingBulkPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingThresholdTotalAmountPrice",
    "AddPriceNewFloatingThresholdTotalAmountPriceBillingCycleConfiguration",
    "AddPriceNewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingTieredPackagePrice",
    "AddPriceNewFloatingTieredPackagePriceBillingCycleConfiguration",
    "AddPriceNewFloatingTieredPackagePriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingTieredPackagePriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingGroupedTieredPrice",
    "AddPriceNewFloatingGroupedTieredPriceBillingCycleConfiguration",
    "AddPriceNewFloatingGroupedTieredPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingGroupedTieredPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingMaxGroupTieredPackagePrice",
    "AddPriceNewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration",
    "AddPriceNewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingTieredWithMinimumPrice",
    "AddPriceNewFloatingTieredWithMinimumPriceBillingCycleConfiguration",
    "AddPriceNewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingPackageWithAllocationPrice",
    "AddPriceNewFloatingPackageWithAllocationPriceBillingCycleConfiguration",
    "AddPriceNewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingTieredPackageWithMinimumPrice",
    "AddPriceNewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration",
    "AddPriceNewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingUnitWithPercentPrice",
    "AddPriceNewFloatingUnitWithPercentPriceBillingCycleConfiguration",
    "AddPriceNewFloatingUnitWithPercentPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingUnitWithPercentPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingTieredWithProrationPrice",
    "AddPriceNewFloatingTieredWithProrationPriceBillingCycleConfiguration",
    "AddPriceNewFloatingTieredWithProrationPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingTieredWithProrationPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingUnitWithProrationPrice",
    "AddPriceNewFloatingUnitWithProrationPriceBillingCycleConfiguration",
    "AddPriceNewFloatingUnitWithProrationPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingUnitWithProrationPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingGroupedAllocationPrice",
    "AddPriceNewFloatingGroupedAllocationPriceBillingCycleConfiguration",
    "AddPriceNewFloatingGroupedAllocationPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingGroupedAllocationPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingGroupedWithProratedMinimumPrice",
    "AddPriceNewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "AddPriceNewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingGroupedWithMeteredMinimumPrice",
    "AddPriceNewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration",
    "AddPriceNewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingMatrixWithDisplayNamePrice",
    "AddPriceNewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration",
    "AddPriceNewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingBulkWithProrationPrice",
    "AddPriceNewFloatingBulkWithProrationPriceBillingCycleConfiguration",
    "AddPriceNewFloatingBulkWithProrationPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingBulkWithProrationPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingGroupedTieredPackagePrice",
    "AddPriceNewFloatingGroupedTieredPackagePriceBillingCycleConfiguration",
    "AddPriceNewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingScalableMatrixWithUnitPricingPrice",
    "AddPriceNewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration",
    "AddPriceNewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingScalableMatrixWithTieredPricingPrice",
    "AddPriceNewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration",
    "AddPriceNewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration",
    "AddPriceNewFloatingCumulativeGroupedBulkPrice",
    "AddPriceNewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration",
    "AddPriceNewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration",
    "AddPriceNewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddAdjustmentAdjustmentNewPercentageDiscount",
    "AddAdjustmentAdjustmentNewUsageDiscount",
    "AddAdjustmentAdjustmentNewAmountDiscount",
    "AddAdjustmentAdjustmentNewMinimum",
    "AddAdjustmentAdjustmentNewMaximum",
    "Edit",
    "EditFixedFeeQuantityTransition",
    "EditAdjustment",
]


class SubscriptionPriceIntervalsParams(TypedDict, total=False):
    add: Iterable[Add]
    """A list of price intervals to add to the subscription."""

    add_adjustments: Iterable[AddAdjustment]
    """A list of adjustments to add to the subscription."""

    allow_invoice_credit_or_void: Optional[bool]
    """
    If false, this request will fail if it would void an issued invoice or create a
    credit note. Consider using this as a safety mechanism if you do not expect
    existing invoices to be changed.
    """

    edit: Iterable[Edit]
    """A list of price intervals to edit on the subscription."""

    edit_adjustments: Iterable[EditAdjustment]
    """A list of adjustments to edit on the subscription."""


class AddAllocationPriceCustomExpiration(TypedDict, total=False):
    duration: Required[int]

    duration_unit: Required[Literal["day", "month"]]


class AddAllocationPrice(TypedDict, total=False):
    amount: Required[str]
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Required[Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]]
    """The cadence at which to allocate the amount to the customer."""

    currency: Required[str]
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    custom_expiration: Optional[AddAllocationPriceCustomExpiration]
    """The custom expiration for the allocation."""

    expires_at_end_of_cadence: Optional[bool]
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period. Set to null if using custom_expiration.
    """


class AddDiscountAmountDiscountCreationParams(TypedDict, total=False):
    amount_discount: Required[float]
    """Only available if discount_type is `amount`."""

    discount_type: Required[Literal["amount"]]


class AddDiscountPercentageDiscountCreationParams(TypedDict, total=False):
    discount_type: Required[Literal["percentage"]]

    percentage_discount: Required[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """


class AddDiscountUsageDiscountCreationParams(TypedDict, total=False):
    discount_type: Required[Literal["usage"]]

    usage_discount: Required[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for.
    """


AddDiscount: TypeAlias = Union[
    AddDiscountAmountDiscountCreationParams,
    AddDiscountPercentageDiscountCreationParams,
    AddDiscountUsageDiscountCreationParams,
]


class AddFixedFeeQuantityTransition(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""


class AddPriceNewFloatingUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""


class AddPriceNewFloatingUnitPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingUnitPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingUnitPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[AddPriceNewFloatingUnitPriceUnitConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingUnitPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingUnitPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingUnitPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Required[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class AddPriceNewFloatingPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[AddPriceNewFloatingPackagePricePackageConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingPackagePriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingPackagePriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class AddPriceNewFloatingMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[AddPriceNewFloatingMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""


class AddPriceNewFloatingMatrixPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMatrixPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingMatrixPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_config: Required[AddPriceNewFloatingMatrixPriceMatrixConfig]

    model_type: Required[Literal["matrix"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingMatrixPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingMatrixPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingMatrixPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class AddPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig(TypedDict, total=False):
    allocation: Required[float]
    """Allocation to be used to calculate the price"""

    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[AddPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""


class AddPriceNewFloatingMatrixWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_allocation_config: Required[AddPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig]

    model_type: Required[Literal["matrix_with_allocation"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingMatrixWithAllocationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class AddPriceNewFloatingTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPriceNewFloatingTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class AddPriceNewFloatingTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[AddPriceNewFloatingTieredPriceTieredConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingTieredPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingTieredPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingTieredPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Exclusive tier starting value"""

    maximum_amount: Optional[str]
    """Inclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class AddPriceNewFloatingTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPriceNewFloatingTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class AddPriceNewFloatingTieredBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingTieredBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[AddPriceNewFloatingTieredBpsPriceTieredBpsConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingTieredBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingTieredBpsPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingTieredBpsPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class AddPriceNewFloatingBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBpsPrice(TypedDict, total=False):
    bps_config: Required[AddPriceNewFloatingBpsPriceBpsConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bps"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingBpsPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingBpsPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class AddPriceNewFloatingBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPriceNewFloatingBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class AddPriceNewFloatingBulkBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBulkBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingBulkBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[AddPriceNewFloatingBulkBpsPriceBulkBpsConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk_bps"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingBulkBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingBulkBpsPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingBulkBpsPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class AddPriceNewFloatingBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPriceNewFloatingBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class AddPriceNewFloatingBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBulkPrice(TypedDict, total=False):
    bulk_config: Required[AddPriceNewFloatingBulkPriceBulkConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingBulkPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingBulkPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingBulkPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingThresholdTotalAmountPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["threshold_total_amount"]]

    name: Required[str]
    """The name of the price."""

    threshold_total_amount_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingThresholdTotalAmountPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_package"]]

    name: Required[str]
    """The name of the price."""

    tiered_package_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingTieredPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingTieredPackagePriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingTieredPackagePriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingGroupedTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingGroupedTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_tiered_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_tiered"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingGroupedTieredPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingGroupedTieredPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingGroupedTieredPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    max_group_tiered_package_config: Required[Dict[str, object]]

    model_type: Required[Literal["max_group_tiered_package"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingTieredWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_minimum"]]

    name: Required[str]
    """The name of the price."""

    tiered_with_minimum_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingTieredWithMinimumPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingPackageWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["package_with_allocation"]]

    name: Required[str]
    """The name of the price."""

    package_with_allocation_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingPackageWithAllocationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_package_with_minimum"]]

    name: Required[str]
    """The name of the price."""

    tiered_package_with_minimum_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingUnitWithPercentPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingUnitWithPercentPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingUnitWithPercentPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit_with_percent"]]

    name: Required[str]
    """The name of the price."""

    unit_with_percent_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingUnitWithPercentPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingUnitWithPercentPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingUnitWithPercentPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingTieredWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingTieredWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingTieredWithProrationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingTieredWithProrationPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingTieredWithProrationPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingUnitWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingUnitWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingUnitWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit_with_proration"]]

    name: Required[str]
    """The name of the price."""

    unit_with_proration_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingUnitWithProrationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingUnitWithProrationPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingUnitWithProrationPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingGroupedAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingGroupedAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_allocation_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_allocation"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingGroupedAllocationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingGroupedAllocationPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingGroupedAllocationPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_prorated_minimum_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_prorated_minimum"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPriceNewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_metered_minimum_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_metered_minimum"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPriceNewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_display_name_config: Required[Dict[str, object]]

    model_type: Required[Literal["matrix_with_display_name"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingBulkWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBulkWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingBulkWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[Dict[str, object]]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk_with_proration"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingBulkWithProrationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingBulkWithProrationPriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingBulkWithProrationPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingGroupedTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_tiered_package_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_tiered_package"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingGroupedTieredPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[AddPriceNewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_unit_pricing"]]

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_unit_pricing_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[
        AddPriceNewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPriceNewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_tiered_pricing"]]

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[
        AddPriceNewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPriceNewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPriceNewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPriceNewFloatingCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[Dict[str, object]]

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["cumulative_grouped_bulk"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPriceNewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        AddPriceNewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration
    ]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPriceNewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


AddPrice: TypeAlias = Union[
    AddPriceNewFloatingUnitPrice,
    AddPriceNewFloatingPackagePrice,
    AddPriceNewFloatingMatrixPrice,
    AddPriceNewFloatingMatrixWithAllocationPrice,
    AddPriceNewFloatingTieredPrice,
    AddPriceNewFloatingTieredBpsPrice,
    AddPriceNewFloatingBpsPrice,
    AddPriceNewFloatingBulkBpsPrice,
    AddPriceNewFloatingBulkPrice,
    AddPriceNewFloatingThresholdTotalAmountPrice,
    AddPriceNewFloatingTieredPackagePrice,
    AddPriceNewFloatingGroupedTieredPrice,
    AddPriceNewFloatingMaxGroupTieredPackagePrice,
    AddPriceNewFloatingTieredWithMinimumPrice,
    AddPriceNewFloatingPackageWithAllocationPrice,
    AddPriceNewFloatingTieredPackageWithMinimumPrice,
    AddPriceNewFloatingUnitWithPercentPrice,
    AddPriceNewFloatingTieredWithProrationPrice,
    AddPriceNewFloatingUnitWithProrationPrice,
    AddPriceNewFloatingGroupedAllocationPrice,
    AddPriceNewFloatingGroupedWithProratedMinimumPrice,
    AddPriceNewFloatingGroupedWithMeteredMinimumPrice,
    AddPriceNewFloatingMatrixWithDisplayNamePrice,
    AddPriceNewFloatingBulkWithProrationPrice,
    AddPriceNewFloatingGroupedTieredPackagePrice,
    AddPriceNewFloatingScalableMatrixWithUnitPricingPrice,
    AddPriceNewFloatingScalableMatrixWithTieredPricingPrice,
    AddPriceNewFloatingCumulativeGroupedBulkPrice,
]


class Add(TypedDict, total=False):
    start_date: Required[
        Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    ]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription.
    """

    allocation_price: Optional[AddAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[Iterable[AddDiscount]]
    """A list of discounts to initialize on the price interval."""

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The end date of the price interval.

    This is the date that the price will stop billing on the subscription.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](/extensibility/advanced-metrics#computed-properties). If
    null, usage queries will not include any additional filter.
    """

    fixed_fee_quantity_transitions: Optional[Iterable[AddFixedFeeQuantityTransition]]
    """A list of fixed fee quantity transitions to initialize on the price interval."""

    maximum_amount: Optional[float]
    """
    The maximum amount that will be billed for this price interval for a given
    billing period.
    """

    minimum_amount: Optional[float]
    """
    The minimum amount that will be billed for this price interval for a given
    billing period.
    """

    price: Optional[AddPrice]
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""

    usage_customer_ids: Optional[List[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


class AddAdjustmentAdjustmentNewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    percentage_discount: Required[float]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    usage_discount: Required[float]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewMinimum(TypedDict, total=False):
    adjustment_type: Required[Literal["minimum"]]

    item_id: Required[str]
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    maximum_amount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


AddAdjustmentAdjustment: TypeAlias = Union[
    AddAdjustmentAdjustmentNewPercentageDiscount,
    AddAdjustmentAdjustmentNewUsageDiscount,
    AddAdjustmentAdjustmentNewAmountDiscount,
    AddAdjustmentAdjustmentNewMinimum,
    AddAdjustmentAdjustmentNewMaximum,
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    start_date: Required[
        Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    ]
    """The start date of the adjustment interval.

    This is the date that the adjustment will start affecting prices on the
    subscription. The adjustment will apply to invoice dates that overlap with this
    `start_date`. This `start_date` is treated as inclusive for in-advance prices,
    and exclusive for in-arrears prices.
    """

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The end date of the adjustment interval.

    This is the date that the adjustment will stop affecting prices on the
    subscription. The adjustment will apply to invoice dates that overlap with this
    `end_date`.This `end_date` is treated as exclusive for in-advance prices, and
    inclusive for in-arrears prices.
    """


class EditFixedFeeQuantityTransition(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""


class Edit(TypedDict, total=False):
    price_interval_id: Required[str]
    """The id of the price interval to edit."""

    billing_cycle_day: Optional[int]
    """The updated billing cycle day for this price interval.

    If not specified, the billing cycle day will not be updated. Note that
    overlapping price intervals must have the same billing cycle day.
    """

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The updated end date of this price interval.

    If not specified, the start date will not be updated.
    """

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](/extensibility/advanced-metrics#computed-properties). If
    null, usage queries will not include any additional filter.
    """

    fixed_fee_quantity_transitions: Optional[Iterable[EditFixedFeeQuantityTransition]]
    """A list of fixed fee quantity transitions to use for this price interval.

    Note that this list will overwrite all existing fixed fee quantity transitions
    on the price interval.
    """

    start_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    """The updated start date of this price interval.

    If not specified, the start date will not be updated.
    """

    usage_customer_ids: Optional[List[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


class EditAdjustment(TypedDict, total=False):
    adjustment_interval_id: Required[str]
    """The id of the adjustment interval to edit."""

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The updated end date of this adjustment interval.

    If not specified, the start date will not be updated.
    """

    start_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    """The updated start date of this adjustment interval.

    If not specified, the start date will not be updated.
    """
