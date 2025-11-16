# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.new_maximum import NewMaximum
from ..shared_params.new_minimum import NewMinimum
from ..shared_params.new_usage_discount import NewUsageDiscount
from ..shared_params.new_amount_discount import NewAmountDiscount
from ..shared_params.new_plan_bulk_price import NewPlanBulkPrice
from ..shared_params.new_plan_unit_price import NewPlanUnitPrice
from ..shared_params.new_allocation_price import NewAllocationPrice
from ..shared_params.new_plan_matrix_price import NewPlanMatrixPrice
from ..shared_params.new_plan_tiered_price import NewPlanTieredPrice
from ..shared_params.new_plan_package_price import NewPlanPackagePrice
from ..shared_params.new_percentage_discount import NewPercentageDiscount
from ..shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from ..shared_params.new_plan_grouped_tiered_price import NewPlanGroupedTieredPrice
from ..shared_params.new_plan_tiered_package_price import NewPlanTieredPackagePrice
from ..shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from ..shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from ..shared_params.new_plan_minimum_composite_price import NewPlanMinimumCompositePrice
from ..shared_params.new_plan_unit_with_percent_price import NewPlanUnitWithPercentPrice
from ..shared_params.new_plan_grouped_allocation_price import NewPlanGroupedAllocationPrice
from ..shared_params.new_plan_bulk_with_proration_price import NewPlanBulkWithProrationPrice
from ..shared_params.new_plan_tiered_with_minimum_price import NewPlanTieredWithMinimumPrice
from ..shared_params.new_plan_unit_with_proration_price import NewPlanUnitWithProrationPrice
from ..shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration
from ..shared_params.new_plan_grouped_tiered_package_price import NewPlanGroupedTieredPackagePrice
from ..shared_params.new_plan_matrix_with_allocation_price import NewPlanMatrixWithAllocationPrice
from ..shared_params.new_plan_threshold_total_amount_price import NewPlanThresholdTotalAmountPrice
from ..shared_params.new_plan_cumulative_grouped_bulk_price import NewPlanCumulativeGroupedBulkPrice
from ..shared_params.new_plan_package_with_allocation_price import NewPlanPackageWithAllocationPrice
from ..shared_params.new_plan_matrix_with_display_name_price import NewPlanMatrixWithDisplayNamePrice
from ..shared_params.new_plan_max_group_tiered_package_price import NewPlanMaxGroupTieredPackagePrice
from ..shared_params.new_plan_tiered_package_with_minimum_price import NewPlanTieredPackageWithMinimumPrice
from ..shared_params.new_plan_grouped_with_metered_minimum_price import NewPlanGroupedWithMeteredMinimumPrice
from ..shared_params.new_plan_grouped_with_prorated_minimum_price import NewPlanGroupedWithProratedMinimumPrice
from ..shared_params.new_plan_scalable_matrix_with_unit_pricing_price import NewPlanScalableMatrixWithUnitPricingPrice
from ..shared_params.new_plan_scalable_matrix_with_tiered_pricing_price import (
    NewPlanScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "ExternalPlanIDCreatePlanVersionParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddPrice",
    "AddPricePrice",
    "AddPricePriceNewPlanBulkWithFiltersPrice",
    "AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig",
    "AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "AddPricePriceNewPlanBulkWithFiltersPriceConversionRateConfig",
    "AddPricePriceNewPlanTieredWithProrationPrice",
    "AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig",
    "AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier",
    "AddPricePriceNewPlanTieredWithProrationPriceConversionRateConfig",
    "AddPricePriceNewPlanGroupedWithMinMaxThresholdsPrice",
    "AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "AddPricePriceNewPlanCumulativeGroupedAllocationPrice",
    "AddPricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "AddPricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig",
    "AddPricePriceNewPlanPercentCompositePrice",
    "AddPricePriceNewPlanPercentCompositePricePercentConfig",
    "AddPricePriceNewPlanPercentCompositePriceConversionRateConfig",
    "AddPricePriceNewPlanEventOutputPrice",
    "AddPricePriceNewPlanEventOutputPriceEventOutputConfig",
    "AddPricePriceNewPlanEventOutputPriceConversionRateConfig",
    "RemoveAdjustment",
    "RemovePrice",
    "ReplaceAdjustment",
    "ReplaceAdjustmentAdjustment",
    "ReplacePrice",
    "ReplacePricePrice",
    "ReplacePricePriceNewPlanBulkWithFiltersPrice",
    "ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig",
    "ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "ReplacePricePriceNewPlanBulkWithFiltersPriceConversionRateConfig",
    "ReplacePricePriceNewPlanTieredWithProrationPrice",
    "ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig",
    "ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier",
    "ReplacePricePriceNewPlanTieredWithProrationPriceConversionRateConfig",
    "ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPrice",
    "ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "ReplacePricePriceNewPlanCumulativeGroupedAllocationPrice",
    "ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig",
    "ReplacePricePriceNewPlanPercentCompositePrice",
    "ReplacePricePriceNewPlanPercentCompositePricePercentConfig",
    "ReplacePricePriceNewPlanPercentCompositePriceConversionRateConfig",
    "ReplacePricePriceNewPlanEventOutputPrice",
    "ReplacePricePriceNewPlanEventOutputPriceEventOutputConfig",
    "ReplacePricePriceNewPlanEventOutputPriceConversionRateConfig",
]


class ExternalPlanIDCreatePlanVersionParams(TypedDict, total=False):
    version: Required[int]
    """New version number."""

    add_adjustments: Optional[Iterable[AddAdjustment]]
    """Additional adjustments to be added to the plan."""

    add_prices: Optional[Iterable[AddPrice]]
    """Additional prices to be added to the plan."""

    remove_adjustments: Optional[Iterable[RemoveAdjustment]]
    """Adjustments to be removed from the plan."""

    remove_prices: Optional[Iterable[RemovePrice]]
    """Prices to be removed from the plan."""

    replace_adjustments: Optional[Iterable[ReplaceAdjustment]]
    """Adjustments to be replaced with additional adjustments on the plan."""

    replace_prices: Optional[Iterable[ReplacePrice]]
    """Prices to be replaced with additional prices on the plan."""

    set_as_default: Optional[bool]
    """Set this new plan version as the default"""


AddAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this adjustment to."""


class AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    filters: Required[Iterable[AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


AddPricePriceNewPlanBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    conversion_rate_config: Optional[AddPricePriceNewPlanBulkWithFiltersPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier]]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


AddPricePriceNewPlanTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig]
    """Configuration for tiered_with_proration pricing"""

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

    conversion_rate_config: Optional[AddPricePriceNewPlanTieredWithProrationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
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

    conversion_rate_config: Optional[AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class AddPricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


AddPricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        AddPricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

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

    conversion_rate_config: Optional[AddPricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class AddPricePriceNewPlanPercentCompositePricePercentConfig(TypedDict, total=False):
    percent: Required[float]
    """What percent of the component subtotals to charge"""


AddPricePriceNewPlanPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[AddPricePriceNewPlanPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[AddPricePriceNewPlanPercentCompositePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class AddPricePriceNewPlanEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


AddPricePriceNewPlanEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[AddPricePriceNewPlanEventOutputPriceEventOutputConfig]
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

    conversion_rate_config: Optional[AddPricePriceNewPlanEventOutputPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


AddPricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanTieredPrice,
    NewPlanBulkPrice,
    AddPricePriceNewPlanBulkWithFiltersPrice,
    NewPlanPackagePrice,
    NewPlanMatrixPrice,
    NewPlanThresholdTotalAmountPrice,
    NewPlanTieredPackagePrice,
    NewPlanTieredWithMinimumPrice,
    NewPlanGroupedTieredPrice,
    NewPlanTieredPackageWithMinimumPrice,
    NewPlanPackageWithAllocationPrice,
    NewPlanUnitWithPercentPrice,
    NewPlanMatrixWithAllocationPrice,
    AddPricePriceNewPlanTieredWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    AddPricePriceNewPlanGroupedWithMinMaxThresholdsPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    AddPricePriceNewPlanCumulativeGroupedAllocationPrice,
    NewPlanMinimumCompositePrice,
    AddPricePriceNewPlanPercentCompositePrice,
    AddPricePriceNewPlanEventOutputPrice,
]


class AddPrice(TypedDict, total=False):
    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this price to."""

    price: Optional[AddPricePrice]
    """New plan price request body params."""


class RemoveAdjustment(TypedDict, total=False):
    adjustment_id: Required[str]
    """The id of the adjustment to remove from on the plan."""

    plan_phase_order: Optional[int]
    """The phase to remove this adjustment from."""


class RemovePrice(TypedDict, total=False):
    price_id: Required[str]
    """The id of the price to remove from the plan."""

    plan_phase_order: Optional[int]
    """The phase to remove this price from."""


ReplaceAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class ReplaceAdjustment(TypedDict, total=False):
    adjustment: Required[ReplaceAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this adjustment from."""


class ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    filters: Required[Iterable[ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


ReplacePricePriceNewPlanBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanBulkWithFiltersPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier]]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


ReplacePricePriceNewPlanTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig]
    """Configuration for tiered_with_proration pricing"""

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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanTieredWithProrationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class ReplacePricePriceNewPlanPercentCompositePricePercentConfig(TypedDict, total=False):
    percent: Required[float]
    """What percent of the component subtotals to charge"""


ReplacePricePriceNewPlanPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[ReplacePricePriceNewPlanPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanPercentCompositePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class ReplacePricePriceNewPlanEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


ReplacePricePriceNewPlanEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[ReplacePricePriceNewPlanEventOutputPriceEventOutputConfig]
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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanEventOutputPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


ReplacePricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanTieredPrice,
    NewPlanBulkPrice,
    ReplacePricePriceNewPlanBulkWithFiltersPrice,
    NewPlanPackagePrice,
    NewPlanMatrixPrice,
    NewPlanThresholdTotalAmountPrice,
    NewPlanTieredPackagePrice,
    NewPlanTieredWithMinimumPrice,
    NewPlanGroupedTieredPrice,
    NewPlanTieredPackageWithMinimumPrice,
    NewPlanPackageWithAllocationPrice,
    NewPlanUnitWithPercentPrice,
    NewPlanMatrixWithAllocationPrice,
    ReplacePricePriceNewPlanTieredWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    ReplacePricePriceNewPlanCumulativeGroupedAllocationPrice,
    NewPlanMinimumCompositePrice,
    ReplacePricePriceNewPlanPercentCompositePrice,
    ReplacePricePriceNewPlanEventOutputPrice,
]


class ReplacePrice(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the plan."""

    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this price from."""

    price: Optional[ReplacePricePrice]
    """New plan price request body params."""
