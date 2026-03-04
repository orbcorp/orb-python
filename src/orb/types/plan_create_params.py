# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.bulk_config import BulkConfig
from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.unit_config import UnitConfig
from .shared_params.matrix_config import MatrixConfig
from .shared_params.tiered_config import TieredConfig
from .shared_params.package_config import PackageConfig
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
from .shared_params.matrix_with_allocation_config import MatrixWithAllocationConfig
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
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackagePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable",
    "PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount",
    "PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier",
    "PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice",
    "PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig",
    "PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation",
    "PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig",
    "PricePrice",
    "PricePriceNewPlanBulkWithFiltersPrice",
    "PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig",
    "PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "PricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "PricePriceNewPlanBulkWithFiltersPriceConversionRateConfig",
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


class PriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[Iterable[PriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation]]
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

    conversion_rate_config: Optional[PriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig]
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


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation]]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["tiered"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[TieredConfig]
    """Configuration for tiered pricing"""

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

    conversion_rate_config: Optional[PriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig]
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


class PriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationBulkPrice(TypedDict, total=False):
    bulk_config: Required[BulkConfig]
    """Configuration for bulk pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[Iterable[PriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation]]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["bulk"]]
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

    conversion_rate_config: Optional[PriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig]
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


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter(
    TypedDict, total=False
):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier(
    TypedDict, total=False
):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    """Configuration for bulk_with_filters pricing"""

    filters: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter]
    ]
    """Property filters to apply (all must match)"""

    tiers: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier]
    ]
    """Bulk tiers for rating based on total usage volume"""


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig
    ]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["package"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    package_config: Required[PackageConfig]
    """Configuration for package pricing"""

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

    conversion_rate_config: Optional[PriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig]
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


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[Iterable[PriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation]]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    matrix_config: Required[MatrixConfig]
    """Configuration for matrix pricing"""

    model_type: Required[Literal["matrix"]]
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

    conversion_rate_config: Optional[PriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig]
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


class PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable(
    TypedDict, total=False
):
    """Configuration for a single threshold"""

    threshold: Required[str]

    total_amount: Required[str]
    """Total amount for this threshold"""


class PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig(
    TypedDict, total=False
):
    """Configuration for threshold_total_amount pricing"""

    consumption_table: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable
        ]
    ]
    """
    When the quantity consumed passes a provided threshold, the configured total
    will be charged
    """

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""


PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["threshold_total_amount"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    threshold_total_amount_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig
    ]
    """Configuration for threshold_total_amount pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier(TypedDict, total=False):
    """Configuration for a single tier with business logic"""

    per_unit: Required[str]
    """Price per package"""

    tier_lower_bound: Required[str]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig(TypedDict, total=False):
    """Configuration for tiered_package pricing"""

    package_size: Required[str]

    tiers: Required[Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier]]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds. The tier bounds are defined
    based on the total quantity rather than the number of packages, so they must be
    multiples of the package size.
    """


PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["tiered_package"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_package_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig
    ]
    """Configuration for tiered_package pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    minimum_amount: Required[str]

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig(
    TypedDict, total=False
):
    """Configuration for tiered_with_minimum pricing"""

    tiers: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier]
    ]
    """Tiered pricing with a minimum amount dependent on the volume tier.

    Tiers are defined using exclusive lower bounds.
    """

    hide_zero_amount_tiers: bool
    """If true, tiers with an accrued amount of 0 will not be included in the rating."""

    prorate: bool
    """If true, the unit price will be prorated to the billing period"""


PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["tiered_with_minimum"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_minimum_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig
    ]
    """Configuration for tiered_with_minimum pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier(TypedDict, total=False):
    """Configuration for a single tier"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig(TypedDict, total=False):
    """Configuration for grouped_tiered pricing"""

    grouping_key: Required[str]
    """The billable metric property used to group before tiering"""

    tiers: Required[Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier]]
    """
    Apply tiered pricing to each segment generated after grouping with the provided
    key
    """


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_tiered_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig
    ]
    """Configuration for grouped_tiered pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["grouped_tiered"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    minimum_amount: Required[str]

    per_unit: Required[str]

    tier_lower_bound: Required[str]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig(
    TypedDict, total=False
):
    """Configuration for tiered_package_with_minimum pricing"""

    package_size: Required[float]

    tiers: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier
        ]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["tiered_package_with_minimum"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_package_with_minimum_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig
    ]
    """Configuration for tiered_package_with_minimum pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig(
    TypedDict, total=False
):
    """Configuration for package_with_allocation pricing"""

    allocation: Required[str]

    package_amount: Required[str]

    package_size: Required[str]


PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["package_with_allocation"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    package_with_allocation_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig
    ]
    """Configuration for package_with_allocation pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig(TypedDict, total=False):
    """Configuration for unit_with_percent pricing"""

    percent: Required[str]
    """What percent, out of 100, of the calculated total to charge"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["unit_with_percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    unit_with_percent_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig
    ]
    """Configuration for unit_with_percent pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    matrix_with_allocation_config: Required[MatrixWithAllocationConfig]
    """Configuration for matrix_with_allocation pricing"""

    model_type: Required[Literal["matrix_with_allocation"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tiered with proration tier"""

    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for tiered_with_proration pricing"""

    tiers: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier]
    ]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig
    ]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for unit_with_proration pricing"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["unit_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    unit_with_proration_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig
    ]
    """Configuration for unit_with_proration pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig(
    TypedDict, total=False
):
    """Configuration for grouped_allocation pricing"""

    allocation: Required[str]
    """Usage allocation per group"""

    grouping_key: Required[str]
    """How to determine the groups that should each be allocated some quantity"""

    overage_unit_rate: Required[str]
    """Unit rate for post-allocation"""


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_allocation_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig
    ]
    """Configuration for grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["grouped_allocation"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier(
    TypedDict, total=False
):
    """Configuration for a single bulk pricing tier with proration"""

    unit_amount: Required[str]
    """Cost per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for bulk_with_proration pricing"""

    tiers: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier]
    ]
    """Bulk tiers for rating based on total usage volume"""


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig
    ]
    """Configuration for bulk_with_proration pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["bulk_with_proration"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig(
    TypedDict, total=False
):
    """Configuration for grouped_with_prorated_minimum pricing"""

    grouping_key: Required[str]
    """How to determine the groups that should each have a minimum"""

    minimum: Required[str]
    """The minimum amount to charge per group"""

    unit_rate: Required[str]
    """The amount to charge per unit"""


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig
    ]
    """Configuration for grouped_with_prorated_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["grouped_with_prorated_minimum"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor(
    TypedDict, total=False
):
    """Configuration for a scaling factor"""

    scaling_factor: Required[str]

    scaling_value: Required[str]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount(
    TypedDict, total=False
):
    """Configuration for a unit amount"""

    pricing_value: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig(
    TypedDict, total=False
):
    """Configuration for grouped_with_metered_minimum pricing"""

    grouping_key: Required[str]
    """Used to partition the usage into groups.

    The minimum amount is applied to each group.
    """

    minimum_unit_amount: Required[str]
    """The minimum amount to charge per group per unit"""

    pricing_key: Required[str]
    """Used to determine the unit rate"""

    scaling_factors: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor
        ]
    ]
    """Scale the unit rates by the scaling factor."""

    scaling_key: Required[str]
    """Used to determine the unit rate scaling factor"""

    unit_amounts: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount
        ]
    ]
    """Apply per unit pricing to each pricing value.

    The minimum amount is applied any unmatched usage.
    """


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_metered_minimum_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig
    ]
    """Configuration for grouped_with_metered_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["grouped_with_metered_minimum"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(
    TypedDict, total=False
):
    """Configuration for grouped_with_min_max_thresholds pricing"""

    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
    ]
    """Configuration for grouped_with_min_max_thresholds pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount(
    TypedDict, total=False
):
    """Configuration for a unit amount item"""

    dimension_value: Required[str]
    """The dimension value"""

    display_name: Required[str]
    """Display name for this dimension value"""

    unit_amount: Required[str]
    """Per unit amount"""


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig(
    TypedDict, total=False
):
    """Configuration for matrix_with_display_name pricing"""

    dimension: Required[str]
    """Used to determine the unit rate"""

    unit_amounts: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount
        ]
    ]
    """Apply per unit pricing to each dimension value"""


PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    matrix_with_display_name_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig
    ]
    """Configuration for matrix_with_display_name pricing"""

    model_type: Required[Literal["matrix_with_display_name"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    per_unit: Required[str]
    """Per package"""

    tier_lower_bound: Required[str]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig(
    TypedDict, total=False
):
    """Configuration for grouped_tiered_package pricing"""

    grouping_key: Required[str]
    """The event property used to group before tiering"""

    package_size: Required[str]

    tiers: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_tiered_package_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig
    ]
    """Configuration for grouped_tiered_package pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["grouped_tiered_package"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig(
    TypedDict, total=False
):
    """Configuration for max_group_tiered_package pricing"""

    grouping_key: Required[str]
    """
    The event property used to group before tiering the group with the highest value
    """

    package_size: Required[str]

    tiers: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier
        ]
    ]
    """Apply tiered pricing to the largest group after grouping with the provided key."""


PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    max_group_tiered_package_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig
    ]
    """Configuration for max_group_tiered_package pricing"""

    model_type: Required[Literal["max_group_tiered_package"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    """Configuration for a single matrix scaling factor"""

    first_dimension_value: Required[str]

    scaling_factor: Required[str]

    second_dimension_value: Optional[str]


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig(
    TypedDict, total=False
):
    """Configuration for scalable_matrix_with_unit_pricing pricing"""

    first_dimension: Required[str]
    """Used to determine the unit rate"""

    matrix_scaling_factors: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor
        ]
    ]
    """Apply a scaling factor to each dimension"""

    unit_price: Required[str]
    """The final unit price to rate against the output of the matrix"""

    grouping_key: Optional[str]
    """The property used to group this price"""

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""

    second_dimension: Optional[str]
    """Used to determine the unit rate (optional)"""


PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["scalable_matrix_with_unit_pricing"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_unit_pricing_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig
    ]
    """Configuration for scalable_matrix_with_unit_pricing pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    """Configuration for a single matrix scaling factor"""

    first_dimension_value: Required[str]

    scaling_factor: Required[str]

    second_dimension_value: Optional[str]


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier entry with business logic"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig(
    TypedDict, total=False
):
    """Configuration for scalable_matrix_with_tiered_pricing pricing"""

    first_dimension: Required[str]
    """Used for the scalable matrix first dimension"""

    matrix_scaling_factors: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor
        ]
    ]
    """Apply a scaling factor to each dimension"""

    tiers: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier
        ]
    ]

    second_dimension: Optional[str]
    """Used for the scalable matrix second dimension (optional)"""


PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["scalable_matrix_with_tiered_pricing"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig
    ]
    """Configuration for scalable_matrix_with_tiered_pricing pricing"""

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue(
    TypedDict, total=False
):
    """Configuration for a dimension value entry"""

    grouping_key: Required[str]
    """Grouping key value"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Unit amount for this combination"""


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig(
    TypedDict, total=False
):
    """Configuration for cumulative_grouped_bulk pricing"""

    dimension_values: Required[
        Iterable[
            PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue
        ]
    ]
    """Each tier lower bound must have the same group of values."""

    group: Required[str]


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig
    ]
    """Configuration for cumulative_grouped_bulk pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["cumulative_grouped_bulk"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(
    TypedDict, total=False
):
    """Configuration for cumulative_grouped_allocation pricing"""

    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig(
    TypedDict, total=False
):
    """Configuration for minimum_composite pricing"""

    minimum_amount: Required[str]
    """The minimum amount to apply"""

    prorated: bool
    """If true, subtotals from this price are prorated based on the service period"""


PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    minimum_composite_config: Required[
        PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig
    ]
    """Configuration for minimum_composite pricing"""

    model_type: Required[Literal["minimum_composite"]]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

    percent: Required[float]
    """What percent of the component subtotals to charge"""


PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig
    ]
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


class PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


class PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig]
    """Configuration for event_output pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

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

    conversion_rate_config: Optional[
        PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig
    ]
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


PriceLicenseAllocationPrice: TypeAlias = Union[
    PriceLicenseAllocationPriceNewLicenseAllocationUnitPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationTieredPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationBulkPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationPackagePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice,
    PriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice,
    PriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice,
]


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


class PricePriceNewPlanPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

    percent: Required[float]
    """What percent of the component subtotals to charge"""


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
