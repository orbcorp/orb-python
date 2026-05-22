# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.new_usage_discount import NewUsageDiscount
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared.billing_cycle_relative_date import BillingCycleRelativeDate
from .shared_params.new_allocation_price import NewAllocationPrice
from .shared_params.new_floating_bulk_price import NewFloatingBulkPrice
from .shared_params.new_floating_unit_price import NewFloatingUnitPrice
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .shared_params.new_floating_matrix_price import NewFloatingMatrixPrice
from .shared_params.new_floating_tiered_price import NewFloatingTieredPrice
from .shared_params.new_floating_package_price import NewFloatingPackagePrice
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_floating_grouped_tiered_price import NewFloatingGroupedTieredPrice
from .shared_params.new_floating_tiered_package_price import NewFloatingTieredPackagePrice
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration
from .shared_params.new_floating_minimum_composite_price import NewFloatingMinimumCompositePrice
from .shared_params.new_floating_unit_with_percent_price import NewFloatingUnitWithPercentPrice
from .shared_params.new_floating_grouped_allocation_price import NewFloatingGroupedAllocationPrice
from .shared_params.new_floating_bulk_with_proration_price import NewFloatingBulkWithProrationPrice
from .shared_params.new_floating_tiered_with_minimum_price import NewFloatingTieredWithMinimumPrice
from .shared_params.new_floating_unit_with_proration_price import NewFloatingUnitWithProrationPrice
from .shared_params.new_floating_tiered_with_proration_price import NewFloatingTieredWithProrationPrice
from .shared_params.new_floating_grouped_tiered_package_price import NewFloatingGroupedTieredPackagePrice
from .shared_params.new_floating_matrix_with_allocation_price import NewFloatingMatrixWithAllocationPrice
from .shared_params.new_floating_threshold_total_amount_price import NewFloatingThresholdTotalAmountPrice
from .shared_params.new_floating_cumulative_grouped_bulk_price import NewFloatingCumulativeGroupedBulkPrice
from .shared_params.new_floating_package_with_allocation_price import NewFloatingPackageWithAllocationPrice
from .shared_params.new_floating_matrix_with_display_name_price import NewFloatingMatrixWithDisplayNamePrice
from .shared_params.new_floating_max_group_tiered_package_price import NewFloatingMaxGroupTieredPackagePrice
from .shared_params.new_floating_tiered_package_with_minimum_price import NewFloatingTieredPackageWithMinimumPrice
from .shared_params.new_floating_grouped_with_metered_minimum_price import NewFloatingGroupedWithMeteredMinimumPrice
from .shared_params.new_floating_grouped_with_prorated_minimum_price import NewFloatingGroupedWithProratedMinimumPrice
from .shared_params.new_floating_scalable_matrix_with_unit_pricing_price import (
    NewFloatingScalableMatrixWithUnitPricingPrice,
)
from .shared_params.new_floating_scalable_matrix_with_tiered_pricing_price import (
    NewFloatingScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "SubscriptionPriceIntervalsParams",
    "Add",
    "AddDiscount",
    "AddDiscountAmountDiscountCreationParams",
    "AddDiscountPercentageDiscountCreationParams",
    "AddDiscountUsageDiscountCreationParams",
    "AddFixedFeeQuantityTransition",
    "AddPrice",
    "AddPriceNewFloatingBulkWithFiltersPrice",
    "AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfig",
    "AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "AddPriceNewFloatingBulkWithFiltersPriceConversionRateConfig",
    "AddPriceNewFloatingMatrixWithThresholdDiscountsPrice",
    "AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfig",
    "AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigMatrixValue",
    "AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigThresholdDiscountGroup",
    "AddPriceNewFloatingMatrixWithThresholdDiscountsPriceConversionRateConfig",
    "AddPriceNewFloatingGroupedWithMinMaxThresholdsPrice",
    "AddPriceNewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "AddPriceNewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "AddPriceNewFloatingCumulativeGroupedAllocationPrice",
    "AddPriceNewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "AddPriceNewFloatingCumulativeGroupedAllocationPriceConversionRateConfig",
    "AddPriceNewFloatingDailyCreditAllowancePrice",
    "AddPriceNewFloatingDailyCreditAllowancePriceDailyCreditAllowanceConfig",
    "AddPriceNewFloatingDailyCreditAllowancePriceDailyCreditAllowanceConfigMatrixValue",
    "AddPriceNewFloatingDailyCreditAllowancePriceConversionRateConfig",
    "AddPriceNewFloatingMeteredAllowancePrice",
    "AddPriceNewFloatingMeteredAllowancePriceMeteredAllowanceConfig",
    "AddPriceNewFloatingMeteredAllowancePriceConversionRateConfig",
    "AddPriceNewFloatingPercentCompositePrice",
    "AddPriceNewFloatingPercentCompositePricePercentConfig",
    "AddPriceNewFloatingPercentCompositePriceConversionRateConfig",
    "AddPriceNewFloatingEventOutputPrice",
    "AddPriceNewFloatingEventOutputPriceEventOutputConfig",
    "AddPriceNewFloatingEventOutputPriceConversionRateConfig",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
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

    can_defer_billing: Optional[bool]
    """
    If set, the default value to use for added/edited price intervals with an
    end_date set.
    """

    edit: Iterable[Edit]
    """A list of price intervals to edit on the subscription."""

    edit_adjustments: Iterable[EditAdjustment]
    """A list of adjustments to edit on the subscription."""


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


class AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    """Configuration for bulk_with_filters pricing"""

    filters: Required[Iterable[AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


AddPriceNewFloatingBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[AddPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfig]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk_with_filters"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingBulkWithFiltersPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigMatrixValue(
    TypedDict, total=False
):
    first_dimension_value: Required[str]

    unit_amount: Required[str]

    second_dimension_value: Optional[str]


class AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigThresholdDiscountGroup(
    TypedDict, total=False
):
    above_threshold_discount_percentage: Required[str]
    """Discount rate applied to spend above the threshold."""

    below_threshold_discount_percentage: Required[str]
    """Discount rate applied to spend at or below the threshold.

    Set to 0 for no baseline discount.
    """

    cell_coordinates: Required[str]
    """Semicolon-separated list of matrix cell coordinates targeted by this group.

    Each coordinate is `first,second` when the matrix has two dimensions, or just
    `first` for a single-dimension matrix. Example: `blue,circle;green,triangle`.
    """

    threshold_amount: Required[str]

    description: Optional[str]


class AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfig(TypedDict, total=False):
    """Configuration for matrix_with_threshold_discounts pricing"""

    default_unit_amount: Required[str]
    """Unit price used for usage that does not match any defined matrix cell."""

    first_dimension: Required[str]
    """First matrix dimension key."""

    matrix_values: Required[
        Iterable[AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigMatrixValue]
    ]
    """Per-cell unit prices."""

    second_dimension: Optional[str]
    """Optional second matrix dimension key."""

    threshold_discount_groups: Iterable[
        AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigThresholdDiscountGroup
    ]


AddPriceNewFloatingMatrixWithThresholdDiscountsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingMatrixWithThresholdDiscountsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_threshold_discounts_config: Required[
        AddPriceNewFloatingMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfig
    ]
    """Configuration for matrix_with_threshold_discounts pricing"""

    model_type: Required[Literal["matrix_with_threshold_discounts"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingMatrixWithThresholdDiscountsPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    """Configuration for grouped_with_min_max_thresholds pricing"""

    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


AddPriceNewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_min_max_thresholds_config: Required[
        AddPriceNewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
    ]
    """Configuration for grouped_with_min_max_thresholds pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_min_max_thresholds"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    """Configuration for cumulative_grouped_allocation pricing"""

    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


AddPriceNewFloatingCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        AddPriceNewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["cumulative_grouped_allocation"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingCumulativeGroupedAllocationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingDailyCreditAllowancePriceDailyCreditAllowanceConfigMatrixValue(TypedDict, total=False):
    """Per-dimension credit price for the daily credit allowance model."""

    dimension_values: Required[SequenceNotStr[Optional[str]]]
    """One or two matrix keys to filter usage to this value by.

    For example, ["model"] could be used to apply a different credit rate to each AI
    model.
    """

    unit_amount: Required[str]
    """Credits charged per unit of usage matching the specified dimension_values"""


class AddPriceNewFloatingDailyCreditAllowancePriceDailyCreditAllowanceConfig(TypedDict, total=False):
    """Configuration for daily_credit_allowance pricing"""

    daily_allowance: Required[str]
    """Credits granted per day. Lose-it-or-use-it; does not roll over."""

    default_unit_amount: Required[str]
    """
    Default per-unit credit rate for any usage not bucketed into a specified
    matrix_value
    """

    dimensions: Required[SequenceNotStr[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    event_day_property: Required[str]
    """Event property whose value identifies the day bucket the event belongs to (e.g.

    'event_day' set to an ISO date string in the customer's timezone). The allowance
    resets per distinct value of this property.
    """

    matrix_values: Required[Iterable[AddPriceNewFloatingDailyCreditAllowancePriceDailyCreditAllowanceConfigMatrixValue]]
    """Per-dimension credit rates"""


AddPriceNewFloatingDailyCreditAllowancePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingDailyCreditAllowancePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    daily_credit_allowance_config: Required[AddPriceNewFloatingDailyCreditAllowancePriceDailyCreditAllowanceConfig]
    """Configuration for daily_credit_allowance pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["daily_credit_allowance"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingDailyCreditAllowancePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingMeteredAllowancePriceMeteredAllowanceConfig(TypedDict, total=False):
    """Configuration for metered_allowance pricing"""

    allowance_grouping_value: Required[str]
    """
    The grouping_key value whose summed quantity represents the allowance for this
    period (e.g. 'storage_snapshot' emitting 3 × avg storage). Capped at consumption
    — credit can never exceed actual usage.
    """

    consumption_grouping_value: Required[str]
    """The grouping_key value whose summed quantity represents consumption (e.g.

    'download'). Charged at unit_amount.
    """

    grouping_key: Required[str]
    """
    Event property used to partition the metric into consumption and allowance
    quantities (e.g. 'event_name'). The metric is queried with this key and the two
    values below select which partition is which.
    """

    unit_amount: Required[str]
    """Per-unit price applied to gross consumption and to the allowance credit."""

    allowance_display_name: str
    """Sub-line label for the credit row (e.g. 'Up to 3x free egress')."""

    consumption_display_name: str
    """Sub-line label for the gross consumption row (e.g. 'bytes gotten')."""


AddPriceNewFloatingMeteredAllowancePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingMeteredAllowancePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    metered_allowance_config: Required[AddPriceNewFloatingMeteredAllowancePriceMeteredAllowanceConfig]
    """Configuration for metered_allowance pricing"""

    model_type: Required[Literal["metered_allowance"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingMeteredAllowancePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

    percent: Required[float]
    """What percent of the component subtotals to charge"""


AddPriceNewFloatingPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[AddPriceNewFloatingPercentCompositePricePercentConfig]
    """Configuration for percent pricing"""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingPercentCompositePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class AddPriceNewFloatingEventOutputPriceEventOutputConfig(TypedDict, total=False):
    """Configuration for event_output pricing"""

    unit_rating_key: Required[str]
    """The key in the event data to extract the unit rate from."""

    default_unit_rate: Optional[str]
    """
    If provided, this amount will be used as the unit rate when an event does not
    have a value for the `unit_rating_key`. If not provided, events missing a unit
    rate will be ignored.
    """

    grouping_key: Optional[str]
    """An optional key in the event data to group by (e.g., event ID).

    All events will also be grouped by their unit rate.
    """


AddPriceNewFloatingEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceNewFloatingEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    event_output_config: Required[AddPriceNewFloatingEventOutputPriceEventOutputConfig]
    """Configuration for event_output pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["event_output"]]
    """The pricing model type"""

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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[AddPriceNewFloatingEventOutputPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


AddPrice: TypeAlias = Union[
    NewFloatingUnitPrice,
    NewFloatingTieredPrice,
    NewFloatingBulkPrice,
    AddPriceNewFloatingBulkWithFiltersPrice,
    NewFloatingPackagePrice,
    NewFloatingMatrixPrice,
    NewFloatingThresholdTotalAmountPrice,
    NewFloatingTieredPackagePrice,
    NewFloatingTieredWithMinimumPrice,
    NewFloatingGroupedTieredPrice,
    NewFloatingTieredPackageWithMinimumPrice,
    NewFloatingPackageWithAllocationPrice,
    NewFloatingUnitWithPercentPrice,
    NewFloatingMatrixWithAllocationPrice,
    AddPriceNewFloatingMatrixWithThresholdDiscountsPrice,
    NewFloatingTieredWithProrationPrice,
    NewFloatingUnitWithProrationPrice,
    NewFloatingGroupedAllocationPrice,
    NewFloatingBulkWithProrationPrice,
    NewFloatingGroupedWithProratedMinimumPrice,
    NewFloatingGroupedWithMeteredMinimumPrice,
    AddPriceNewFloatingGroupedWithMinMaxThresholdsPrice,
    NewFloatingMatrixWithDisplayNamePrice,
    NewFloatingGroupedTieredPackagePrice,
    NewFloatingMaxGroupTieredPackagePrice,
    NewFloatingScalableMatrixWithUnitPricingPrice,
    NewFloatingScalableMatrixWithTieredPricingPrice,
    NewFloatingCumulativeGroupedBulkPrice,
    AddPriceNewFloatingCumulativeGroupedAllocationPrice,
    AddPriceNewFloatingDailyCreditAllowancePrice,
    AddPriceNewFloatingMeteredAllowancePrice,
    NewFloatingMinimumCompositePrice,
    AddPriceNewFloatingPercentCompositePrice,
    AddPriceNewFloatingEventOutputPrice,
]


class Add(TypedDict, total=False):
    start_date: Required[
        Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    ]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription.
    """

    allocation_price: Optional[NewAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

    can_defer_billing: Optional[bool]
    """
    If true, an in-arrears price interval ending mid-cycle will defer billing the
    final line item until the next scheduled invoice. If false, it will be billed on
    its end date.
    """

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

    metric_parameter_overrides: Optional[Dict[str, object]]
    """Override values for parameterized billable metric variables.

    Keys are parameter names, values are the override values (number or string).
    """

    minimum_amount: Optional[float]
    """
    The minimum amount that will be billed for this price interval for a given
    billing period.
    """

    price: Optional[AddPrice]
    """New floating price request body params."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""

    usage_customer_ids: Optional[SequenceNotStr[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


AddAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class AddAdjustment(TypedDict, total=False):
    start_date: Required[
        Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    ]
    """The start date of the adjustment interval.

    This is the date that the adjustment will start affecting prices on the
    subscription. The adjustment will apply to invoice dates that overlap with this
    `start_date`. This `start_date` is treated as inclusive for in-advance prices,
    and exclusive for in-arrears prices.
    """

    adjustment: Optional[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    adjustment_id: Optional[str]
    """The ID of the adjustment to add to the subscription.

    Adjustment IDs can be re-used from existing subscriptions or plans, but
    adjustments associated with coupon redemptions cannot be re-used.
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

    can_defer_billing: Optional[bool]
    """
    If true, an in-arrears price interval ending mid-cycle will defer billing the
    final line item until the next scheduled invoice. If false, it will be billed on
    its end date.
    """

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The updated end date of this price interval.

    If not specified, the end date will not be updated.
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

    metric_parameter_overrides: Optional[Dict[str, object]]
    """Override values for parameterized billable metric variables.

    Keys are parameter names, values are the override values (number or string).
    """

    start_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    """The updated start date of this price interval.

    If not specified, the start date will not be updated.
    """

    usage_customer_ids: Optional[SequenceNotStr[str]]
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

    If not specified, the end date will not be updated.
    """

    start_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    """The updated start date of this adjustment interval.

    If not specified, the start date will not be updated.
    """
