# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.unit_config import UnitConfig
from .shared_params.new_usage_discount import NewUsageDiscount
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared_params.new_plan_bulk_price import NewPlanBulkPrice
from .shared_params.new_plan_unit_price import NewPlanUnitPrice
from .shared_params.new_allocation_price import NewAllocationPrice
from .shared_params.new_plan_matrix_price import NewPlanMatrixPrice
from .shared_params.new_plan_tiered_price import NewPlanTieredPrice
from .shared_params.new_plan_package_price import NewPlanPackagePrice
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.new_plan_grouped_tiered_price import NewPlanGroupedTieredPrice
from .shared_params.new_plan_tiered_package_price import NewPlanTieredPackagePrice
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_plan_minimum_composite_price import NewPlanMinimumCompositePrice
from .shared_params.new_plan_unit_with_percent_price import NewPlanUnitWithPercentPrice
from .shared_params.new_plan_grouped_allocation_price import NewPlanGroupedAllocationPrice
from .shared_params.new_plan_bulk_with_proration_price import NewPlanBulkWithProrationPrice
from .shared_params.new_plan_tiered_with_minimum_price import NewPlanTieredWithMinimumPrice
from .shared_params.new_plan_unit_with_proration_price import NewPlanUnitWithProrationPrice
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration
from .shared_params.new_plan_grouped_tiered_package_price import NewPlanGroupedTieredPackagePrice
from .shared_params.new_plan_matrix_with_allocation_price import NewPlanMatrixWithAllocationPrice
from .shared_params.new_plan_threshold_total_amount_price import NewPlanThresholdTotalAmountPrice
from .shared_params.new_plan_cumulative_grouped_bulk_price import NewPlanCumulativeGroupedBulkPrice
from .shared_params.new_plan_package_with_allocation_price import NewPlanPackageWithAllocationPrice
from .shared_params.new_plan_matrix_with_display_name_price import NewPlanMatrixWithDisplayNamePrice
from .shared_params.new_plan_max_group_tiered_package_price import NewPlanMaxGroupTieredPackagePrice
from .shared_params.new_plan_tiered_package_with_minimum_price import NewPlanTieredPackageWithMinimumPrice
from .shared_params.new_plan_grouped_with_metered_minimum_price import NewPlanGroupedWithMeteredMinimumPrice
from .shared_params.new_plan_grouped_with_prorated_minimum_price import NewPlanGroupedWithProratedMinimumPrice
from .shared_params.new_plan_scalable_matrix_with_unit_pricing_price import NewPlanScalableMatrixWithUnitPricingPrice
from .shared_params.new_plan_scalable_matrix_with_tiered_pricing_price import (
    NewPlanScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "PlanCreateParams",
    "Price",
    "PriceLicenseAllocationPrice",
    "PriceLicenseAllocationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceConversionRateConfig",
    "PricePrice",
    "PricePriceNewPlanBulkWithFiltersPrice",
    "PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig",
    "PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "PricePriceNewPlanBulkWithFiltersPriceConversionRateConfig",
    "PricePriceNewPlanMatrixWithThresholdDiscountsPrice",
    "PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfig",
    "PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigMatrixValue",
    "PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigThresholdDiscountGroup",
    "PricePriceNewPlanMatrixWithThresholdDiscountsPriceConversionRateConfig",
    "PricePriceNewPlanTieredWithProrationPrice",
    "PricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig",
    "PricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier",
    "PricePriceNewPlanTieredWithProrationPriceConversionRateConfig",
    "PricePriceNewPlanGroupedWithMinMaxThresholdsPrice",
    "PricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "PricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "PricePriceNewPlanCumulativeGroupedAllocationPrice",
    "PricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "PricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig",
    "PricePriceNewPlanDailyCreditAllowancePrice",
    "PricePriceNewPlanDailyCreditAllowancePriceDailyCreditAllowanceConfig",
    "PricePriceNewPlanDailyCreditAllowancePriceDailyCreditAllowanceConfigMatrixValue",
    "PricePriceNewPlanDailyCreditAllowancePriceConversionRateConfig",
    "PricePriceNewPlanMeteredAllowancePrice",
    "PricePriceNewPlanMeteredAllowancePriceMeteredAllowanceConfig",
    "PricePriceNewPlanMeteredAllowancePriceConversionRateConfig",
    "PricePriceNewPlanPercentCompositePrice",
    "PricePriceNewPlanPercentCompositePricePercentConfig",
    "PricePriceNewPlanPercentCompositePriceConversionRateConfig",
    "PricePriceNewPlanEventOutputPrice",
    "PricePriceNewPlanEventOutputPriceEventOutputConfig",
    "PricePriceNewPlanEventOutputPriceConversionRateConfig",
    "Adjustment",
    "AdjustmentAdjustment",
    "PlanPhase",
]


class PlanCreateParams(TypedDict, total=False):
    currency: Required[str]
    """
    An ISO 4217 currency string for invoices generated by subscriptions on this
    plan.
    """

    name: Required[str]

    prices: Required[Iterable[Price]]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    adjustments: Optional[Iterable[Adjustment]]
    """Adjustments for this plan.

    If the plan has phases, this includes adjustments across all phases of the plan.
    """

    default_invoice_memo: Optional[str]
    """
    Free-form text which is available on the invoice PDF and the Orb invoice portal.
    """

    description: Optional[str]
    """An optional user-defined description of the plan."""

    external_plan_id: Optional[str]

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    net_terms: Optional[int]
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0.
    """

    plan_phases: Optional[Iterable[PlanPhase]]
    """Configuration of pre-defined phases, each with their own prices and adjustments.

    Leave unspecified for plans with a single phase.
    """

    status: Literal["active", "draft"]
    """The status of the plan to create (either active or draft).

    If not specified, this defaults to active.
    """


class PriceLicenseAllocationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class PriceLicenseAllocationPrice(TypedDict, total=False):
    """The license allocation price to add to the plan."""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[Iterable[PriceLicenseAllocationPriceLicenseAllocation]]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["unit"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    unit_config: Required[UnitConfig]
    """Configuration for unit pricing"""

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

    conversion_rate_config: Optional[PriceLicenseAllocationPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    """Configuration for bulk_with_filters pricing"""

    filters: Required[Iterable[PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


PricePriceNewPlanBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig]
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

    conversion_rate_config: Optional[PricePriceNewPlanBulkWithFiltersPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigMatrixValue(
    TypedDict, total=False
):
    first_dimension_value: Required[str]

    unit_amount: Required[str]

    second_dimension_value: Optional[str]


class PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigThresholdDiscountGroup(
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


class PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfig(TypedDict, total=False):
    """Configuration for matrix_with_threshold_discounts pricing"""

    default_unit_amount: Required[str]
    """Unit price used for usage that does not match any defined matrix cell."""

    first_dimension: Required[str]
    """First matrix dimension key."""

    matrix_values: Required[
        Iterable[PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigMatrixValue]
    ]
    """Per-cell unit prices."""

    second_dimension: Optional[str]
    """Optional second matrix dimension key."""

    threshold_discount_groups: Iterable[
        PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfigThresholdDiscountGroup
    ]


PricePriceNewPlanMatrixWithThresholdDiscountsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanMatrixWithThresholdDiscountsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_threshold_discounts_config: Required[
        PricePriceNewPlanMatrixWithThresholdDiscountsPriceMatrixWithThresholdDiscountsConfig
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

    conversion_rate_config: Optional[PricePriceNewPlanMatrixWithThresholdDiscountsPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    """Configuration for a single tiered with proration tier"""

    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class PricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    """Configuration for tiered_with_proration pricing"""

    tiers: Required[Iterable[PricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier]]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


PricePriceNewPlanTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[PricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig]
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

    conversion_rate_config: Optional[PricePriceNewPlanTieredWithProrationPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    """Configuration for grouped_with_min_max_thresholds pricing"""

    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


PricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        PricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
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

    conversion_rate_config: Optional[PricePriceNewPlanGroupedWithMinMaxThresholdsPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    """Configuration for cumulative_grouped_allocation pricing"""

    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


PricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        PricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
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

    conversion_rate_config: Optional[PricePriceNewPlanCumulativeGroupedAllocationPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanDailyCreditAllowancePriceDailyCreditAllowanceConfigMatrixValue(TypedDict, total=False):
    """Per-dimension credit price for the daily credit allowance model."""

    dimension_values: Required[SequenceNotStr[Optional[str]]]
    """One or two matrix keys to filter usage to this value by.

    For example, ["model"] could be used to apply a different credit rate to each AI
    model.
    """

    unit_amount: Required[str]
    """Credits charged per unit of usage matching the specified dimension_values"""


class PricePriceNewPlanDailyCreditAllowancePriceDailyCreditAllowanceConfig(TypedDict, total=False):
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

    matrix_values: Required[Iterable[PricePriceNewPlanDailyCreditAllowancePriceDailyCreditAllowanceConfigMatrixValue]]
    """Per-dimension credit rates"""


PricePriceNewPlanDailyCreditAllowancePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanDailyCreditAllowancePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    daily_credit_allowance_config: Required[PricePriceNewPlanDailyCreditAllowancePriceDailyCreditAllowanceConfig]
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

    conversion_rate_config: Optional[PricePriceNewPlanDailyCreditAllowancePriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanMeteredAllowancePriceMeteredAllowanceConfig(TypedDict, total=False):
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


PricePriceNewPlanMeteredAllowancePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanMeteredAllowancePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    metered_allowance_config: Required[PricePriceNewPlanMeteredAllowancePriceMeteredAllowanceConfig]
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

    conversion_rate_config: Optional[PricePriceNewPlanMeteredAllowancePriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

    percent: Required[float]
    """Fraction of the component subtotals to charge (0 < percent <= 1)."""

    maximum_amount: Optional[str]
    """Maximum amount to charge. If unset, the fee has no upper bound."""

    minimum_amount: Optional[str]
    """Minimum amount to charge. If unset, the fee is bounded below by 0."""

    prorated: bool
    """If true, the minimum_amount is prorated based on the service period.

    The maximum_amount is an absolute cap (never prorated), and the percent applied
    to upstream subtotals is never prorated either.
    """


PricePriceNewPlanPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[PricePriceNewPlanPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[PricePriceNewPlanPercentCompositePriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


class PricePriceNewPlanEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


PricePriceNewPlanEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PricePriceNewPlanEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[PricePriceNewPlanEventOutputPriceEventOutputConfig]
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

    conversion_rate_config: Optional[PricePriceNewPlanEventOutputPriceConversionRateConfig]
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

    license_type_id: Optional[str]
    """The ID of the license type to associate with this price."""

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


PricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanTieredPrice,
    NewPlanBulkPrice,
    PricePriceNewPlanBulkWithFiltersPrice,
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
    PricePriceNewPlanMatrixWithThresholdDiscountsPrice,
    PricePriceNewPlanTieredWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    PricePriceNewPlanGroupedWithMinMaxThresholdsPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    PricePriceNewPlanCumulativeGroupedAllocationPrice,
    PricePriceNewPlanDailyCreditAllowancePrice,
    PricePriceNewPlanMeteredAllowancePrice,
    NewPlanMinimumCompositePrice,
    PricePriceNewPlanPercentCompositePrice,
    PricePriceNewPlanEventOutputPrice,
]


class Price(TypedDict, total=False):
    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    license_allocation_price: Optional[PriceLicenseAllocationPrice]
    """The license allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this price to."""

    price: Optional[PricePrice]
    """New plan price request body params."""


AdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class Adjustment(TypedDict, total=False):
    adjustment: Required[AdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this adjustment to."""


class PlanPhase(TypedDict, total=False):
    order: Required[int]
    """Determines the ordering of the phase in a plan's lifecycle. 1 = first phase."""

    align_billing_with_phase_start_date: Optional[bool]
    """Align billing cycle day with phase start date."""

    duration: Optional[int]
    """How many terms of length `duration_unit` this phase is active for.

    If null, this phase is evergreen and active indefinitely
    """

    duration_unit: Optional[Literal["daily", "monthly", "quarterly", "semi_annual", "annual"]]
