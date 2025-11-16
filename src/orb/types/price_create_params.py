# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.bulk_config import BulkConfig
from .shared_params.unit_config import UnitConfig
from .shared_params.matrix_config import MatrixConfig
from .shared_params.tiered_config import TieredConfig
from .shared_params.package_config import PackageConfig
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.matrix_with_allocation_config import MatrixWithAllocationConfig
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "PriceCreateParams",
    "NewFloatingUnitPrice",
    "NewFloatingUnitPriceConversionRateConfig",
    "NewFloatingTieredPrice",
    "NewFloatingTieredPriceConversionRateConfig",
    "NewFloatingBulkPrice",
    "NewFloatingBulkPriceConversionRateConfig",
    "NewFloatingBulkWithFiltersPrice",
    "NewFloatingBulkWithFiltersPriceBulkWithFiltersConfig",
    "NewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "NewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "NewFloatingBulkWithFiltersPriceConversionRateConfig",
    "NewFloatingPackagePrice",
    "NewFloatingPackagePriceConversionRateConfig",
    "NewFloatingMatrixPrice",
    "NewFloatingMatrixPriceConversionRateConfig",
    "NewFloatingThresholdTotalAmountPrice",
    "NewFloatingThresholdTotalAmountPriceThresholdTotalAmountConfig",
    "NewFloatingThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfig",
    "NewFloatingTieredPackagePrice",
    "NewFloatingTieredPackagePriceTieredPackageConfig",
    "NewFloatingTieredPackagePriceTieredPackageConfigTier",
    "NewFloatingTieredPackagePriceConversionRateConfig",
    "NewFloatingTieredWithMinimumPrice",
    "NewFloatingTieredWithMinimumPriceTieredWithMinimumConfig",
    "NewFloatingTieredWithMinimumPriceTieredWithMinimumConfigTier",
    "NewFloatingTieredWithMinimumPriceConversionRateConfig",
    "NewFloatingGroupedTieredPrice",
    "NewFloatingGroupedTieredPriceGroupedTieredConfig",
    "NewFloatingGroupedTieredPriceGroupedTieredConfigTier",
    "NewFloatingGroupedTieredPriceConversionRateConfig",
    "NewFloatingTieredPackageWithMinimumPrice",
    "NewFloatingTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig",
    "NewFloatingTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfig",
    "NewFloatingPackageWithAllocationPrice",
    "NewFloatingPackageWithAllocationPricePackageWithAllocationConfig",
    "NewFloatingPackageWithAllocationPriceConversionRateConfig",
    "NewFloatingUnitWithPercentPrice",
    "NewFloatingUnitWithPercentPriceUnitWithPercentConfig",
    "NewFloatingUnitWithPercentPriceConversionRateConfig",
    "NewFloatingMatrixWithAllocationPrice",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfig",
    "NewFloatingTieredWithProrationPrice",
    "NewFloatingTieredWithProrationPriceTieredWithProrationConfig",
    "NewFloatingTieredWithProrationPriceTieredWithProrationConfigTier",
    "NewFloatingTieredWithProrationPriceConversionRateConfig",
    "NewFloatingUnitWithProrationPrice",
    "NewFloatingUnitWithProrationPriceUnitWithProrationConfig",
    "NewFloatingUnitWithProrationPriceConversionRateConfig",
    "NewFloatingGroupedAllocationPrice",
    "NewFloatingGroupedAllocationPriceGroupedAllocationConfig",
    "NewFloatingGroupedAllocationPriceConversionRateConfig",
    "NewFloatingBulkWithProrationPrice",
    "NewFloatingBulkWithProrationPriceBulkWithProrationConfig",
    "NewFloatingBulkWithProrationPriceBulkWithProrationConfigTier",
    "NewFloatingBulkWithProrationPriceConversionRateConfig",
    "NewFloatingGroupedWithProratedMinimumPrice",
    "NewFloatingGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig",
    "NewFloatingGroupedWithMeteredMinimumPrice",
    "NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig",
    "NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor",
    "NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig",
    "NewFloatingGroupedWithMinMaxThresholdsPrice",
    "NewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "NewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "NewFloatingMatrixWithDisplayNamePrice",
    "NewFloatingMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig",
    "NewFloatingMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfig",
    "NewFloatingGroupedTieredPackagePrice",
    "NewFloatingGroupedTieredPackagePriceGroupedTieredPackageConfig",
    "NewFloatingGroupedTieredPackagePriceGroupedTieredPackageConfigTier",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfig",
    "NewFloatingMaxGroupTieredPackagePrice",
    "NewFloatingMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig",
    "NewFloatingMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfig",
    "NewFloatingScalableMatrixWithUnitPricingPrice",
    "NewFloatingScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig",
    "NewFloatingScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "NewFloatingScalableMatrixWithTieredPricingPrice",
    "NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig",
    "NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor",
    "NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "NewFloatingCumulativeGroupedBulkPrice",
    "NewFloatingCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig",
    "NewFloatingCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfig",
    "NewFloatingCumulativeGroupedAllocationPrice",
    "NewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "NewFloatingCumulativeGroupedAllocationPriceConversionRateConfig",
    "NewFloatingMinimumCompositePrice",
    "NewFloatingMinimumCompositePriceMinimumConfig",
    "NewFloatingMinimumCompositePriceConversionRateConfig",
    "NewFloatingPercentCompositePrice",
    "NewFloatingPercentCompositePricePercentConfig",
    "NewFloatingPercentCompositePriceConversionRateConfig",
    "NewFloatingEventOutputPrice",
    "NewFloatingEventOutputPriceEventOutputConfig",
    "NewFloatingEventOutputPriceConversionRateConfig",
]


class NewFloatingUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingUnitPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


NewFloatingUnitPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewFloatingTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingTieredPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


NewFloatingTieredPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewFloatingBulkPrice(TypedDict, total=False):
    bulk_config: Required[BulkConfig]
    """Configuration for bulk pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingBulkPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


NewFloatingBulkPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewFloatingBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[NewFloatingBulkWithFiltersPriceBulkWithFiltersConfig]
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

    conversion_rate_config: Optional[NewFloatingBulkWithFiltersPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class NewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class NewFloatingBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    filters: Required[Iterable[NewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[NewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


NewFloatingBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingPackagePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


NewFloatingPackagePriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewFloatingMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingMatrixPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


NewFloatingMatrixPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewFloatingThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["threshold_total_amount"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    threshold_total_amount_config: Required[NewFloatingThresholdTotalAmountPriceThresholdTotalAmountConfig]
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

    conversion_rate_config: Optional[NewFloatingThresholdTotalAmountPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable(TypedDict, total=False):
    threshold: Required[str]
    """Quantity threshold"""

    total_amount: Required[str]
    """Total amount for this threshold"""


class NewFloatingThresholdTotalAmountPriceThresholdTotalAmountConfig(TypedDict, total=False):
    consumption_table: Required[
        Iterable[NewFloatingThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable]
    ]
    """
    When the quantity consumed passes a provided threshold, the configured total
    will be charged
    """

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""


NewFloatingThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_package"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_package_config: Required[NewFloatingTieredPackagePriceTieredPackageConfig]
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

    conversion_rate_config: Optional[NewFloatingTieredPackagePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredPackagePriceTieredPackageConfigTier(TypedDict, total=False):
    per_unit: Required[str]
    """Price per package"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""


class NewFloatingTieredPackagePriceTieredPackageConfig(TypedDict, total=False):
    package_size: Required[str]
    """Package size"""

    tiers: Required[Iterable[NewFloatingTieredPackagePriceTieredPackageConfigTier]]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds. The tier bounds are defined
    based on the total quantity rather than the number of packages, so they must be
    multiples of the package size.
    """


NewFloatingTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_minimum"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_minimum_config: Required[NewFloatingTieredWithMinimumPriceTieredWithMinimumConfig]
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

    conversion_rate_config: Optional[NewFloatingTieredWithMinimumPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredWithMinimumPriceTieredWithMinimumConfigTier(TypedDict, total=False):
    minimum_amount: Required[str]
    """Minimum amount"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Per unit amount"""


class NewFloatingTieredWithMinimumPriceTieredWithMinimumConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingTieredWithMinimumPriceTieredWithMinimumConfigTier]]
    """Tiered pricing with a minimum amount dependent on the volume tier.

    Tiers are defined using exclusive lower bounds.
    """

    hide_zero_amount_tiers: bool
    """If true, tiers with an accrued amount of 0 will not be included in the rating."""

    prorate: bool
    """If true, the unit price will be prorated to the billing period"""


NewFloatingTieredWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_tiered_config: Required[NewFloatingGroupedTieredPriceGroupedTieredConfig]
    """Configuration for grouped_tiered pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingGroupedTieredPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedTieredPriceGroupedTieredConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Per unit amount"""


class NewFloatingGroupedTieredPriceGroupedTieredConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """The billable metric property used to group before tiering"""

    tiers: Required[Iterable[NewFloatingGroupedTieredPriceGroupedTieredConfigTier]]
    """
    Apply tiered pricing to each segment generated after grouping with the provided
    key
    """


NewFloatingGroupedTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_package_with_minimum"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_package_with_minimum_config: Required[NewFloatingTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig]
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

    conversion_rate_config: Optional[NewFloatingTieredPackageWithMinimumPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier(TypedDict, total=False):
    minimum_amount: Required[str]
    """Minimum amount"""

    per_unit: Required[str]
    """Price per package"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""


class NewFloatingTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig(TypedDict, total=False):
    package_size: Required[float]
    """Package size"""

    tiers: Required[Iterable[NewFloatingTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier]]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


NewFloatingTieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["package_with_allocation"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    package_with_allocation_config: Required[NewFloatingPackageWithAllocationPricePackageWithAllocationConfig]
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

    conversion_rate_config: Optional[NewFloatingPackageWithAllocationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingPackageWithAllocationPricePackageWithAllocationConfig(TypedDict, total=False):
    allocation: Required[str]
    """Usage allocation"""

    package_amount: Required[str]
    """Price per package"""

    package_size: Required[str]
    """Package size"""


NewFloatingPackageWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit_with_percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    unit_with_percent_config: Required[NewFloatingUnitWithPercentPriceUnitWithPercentConfig]
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

    conversion_rate_config: Optional[NewFloatingUnitWithPercentPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingUnitWithPercentPriceUnitWithPercentConfig(TypedDict, total=False):
    percent: Required[str]
    """What percent, out of 100, of the calculated total to charge"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


NewFloatingUnitWithPercentPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingMatrixWithAllocationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


NewFloatingMatrixWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[NewFloatingTieredWithProrationPriceTieredWithProrationConfig]
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

    conversion_rate_config: Optional[NewFloatingTieredWithProrationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class NewFloatingTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingTieredWithProrationPriceTieredWithProrationConfigTier]]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


NewFloatingTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    unit_with_proration_config: Required[NewFloatingUnitWithProrationPriceUnitWithProrationConfig]
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

    conversion_rate_config: Optional[NewFloatingUnitWithProrationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingUnitWithProrationPriceUnitWithProrationConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""


NewFloatingUnitWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_allocation_config: Required[NewFloatingGroupedAllocationPriceGroupedAllocationConfig]
    """Configuration for grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingGroupedAllocationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedAllocationPriceGroupedAllocationConfig(TypedDict, total=False):
    allocation: Required[str]
    """Usage allocation per group"""

    grouping_key: Required[str]
    """How to determine the groups that should each be allocated some quantity"""

    overage_unit_rate: Required[str]
    """Unit rate for post-allocation"""


NewFloatingGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[NewFloatingBulkWithProrationPriceBulkWithProrationConfig]
    """Configuration for bulk_with_proration pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingBulkWithProrationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingBulkWithProrationPriceBulkWithProrationConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Cost per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class NewFloatingBulkWithProrationPriceBulkWithProrationConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingBulkWithProrationPriceBulkWithProrationConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


NewFloatingBulkWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_prorated_minimum_config: Required[
        NewFloatingGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig
    ]
    """Configuration for grouped_with_prorated_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """How to determine the groups that should each have a minimum"""

    minimum: Required[str]
    """The minimum amount to charge per group"""

    unit_rate: Required[str]
    """The amount to charge per unit"""


NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_metered_minimum_config: Required[
        NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig
    ]
    """Configuration for grouped_with_metered_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor(TypedDict, total=False):
    scaling_factor: Required[str]
    """Scaling factor"""

    scaling_value: Required[str]
    """Scaling value"""


class NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount(TypedDict, total=False):
    pricing_value: Required[str]
    """Pricing value"""

    unit_amount: Required[str]
    """Per unit amount"""


class NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """Used to partition the usage into groups.

    The minimum amount is applied to each group.
    """

    minimum_unit_amount: Required[str]
    """The minimum amount to charge per group per unit"""

    pricing_key: Required[str]
    """Used to determine the unit rate"""

    scaling_factors: Required[
        Iterable[NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor]
    ]
    """Scale the unit rates by the scaling factor."""

    scaling_key: Required[str]
    """Used to determine the unit rate scaling factor"""

    unit_amounts: Required[Iterable[NewFloatingGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount]]
    """Apply per unit pricing to each pricing value.

    The minimum amount is applied any unmatched usage.
    """


NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_min_max_thresholds_config: Required[
        NewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
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

    conversion_rate_config: Optional[NewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


NewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_display_name_config: Required[NewFloatingMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig]
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

    conversion_rate_config: Optional[NewFloatingMatrixWithDisplayNamePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount(TypedDict, total=False):
    dimension_value: Required[str]
    """The dimension value"""

    display_name: Required[str]
    """Display name for this dimension value"""

    unit_amount: Required[str]
    """Per unit amount"""


class NewFloatingMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig(TypedDict, total=False):
    dimension: Required[str]
    """Used to determine the unit rate"""

    unit_amounts: Required[Iterable[NewFloatingMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount]]
    """Apply per unit pricing to each dimension value"""


NewFloatingMatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_tiered_package_config: Required[NewFloatingGroupedTieredPackagePriceGroupedTieredPackageConfig]
    """Configuration for grouped_tiered_package pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingGroupedTieredPackagePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedTieredPackagePriceGroupedTieredPackageConfigTier(TypedDict, total=False):
    per_unit: Required[str]
    """Price per package"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""


class NewFloatingGroupedTieredPackagePriceGroupedTieredPackageConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """The event property used to group before tiering"""

    package_size: Required[str]
    """Package size"""

    tiers: Required[Iterable[NewFloatingGroupedTieredPackagePriceGroupedTieredPackageConfigTier]]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


NewFloatingGroupedTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    max_group_tiered_package_config: Required[NewFloatingMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig]
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

    conversion_rate_config: Optional[NewFloatingMaxGroupTieredPackagePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Per unit amount"""


class NewFloatingMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig(TypedDict, total=False):
    grouping_key: Required[str]
    """
    The event property used to group before tiering the group with the highest value
    """

    package_size: Required[str]
    """Package size"""

    tiers: Required[Iterable[NewFloatingMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier]]
    """Apply tiered pricing to the largest group after grouping with the provided key."""


NewFloatingMaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_unit_pricing"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_unit_pricing_config: Required[
        NewFloatingScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig
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

    conversion_rate_config: Optional[NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    first_dimension_value: Required[str]
    """First dimension value"""

    scaling_factor: Required[str]
    """Scaling factor"""

    second_dimension_value: Optional[str]
    """Second dimension value (optional)"""


class NewFloatingScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig(TypedDict, total=False):
    first_dimension: Required[str]
    """Used to determine the unit rate"""

    matrix_scaling_factors: Required[
        Iterable[NewFloatingScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor]
    ]
    """Apply a scaling factor to each dimension"""

    unit_price: Required[str]
    """The final unit price to rate against the output of the matrix"""

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""

    second_dimension: Optional[str]
    """Used to determine the unit rate (optional)"""


NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_tiered_pricing"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: Required[
        NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig
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

    conversion_rate_config: Optional[NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    first_dimension_value: Required[str]
    """First dimension value"""

    scaling_factor: Required[str]
    """Scaling factor"""

    second_dimension_value: Optional[str]
    """Second dimension value (optional)"""


class NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Per unit amount"""


class NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig(TypedDict, total=False):
    first_dimension: Required[str]
    """Used for the scalable matrix first dimension"""

    matrix_scaling_factors: Required[
        Iterable[
            NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor
        ]
    ]
    """Apply a scaling factor to each dimension"""

    tiers: Required[Iterable[NewFloatingScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier]]
    """Tier pricing structure"""

    second_dimension: Optional[str]
    """Used for the scalable matrix second dimension (optional)"""


NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[NewFloatingCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig]
    """Configuration for cumulative_grouped_bulk pricing"""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    conversion_rate_config: Optional[NewFloatingCumulativeGroupedBulkPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue(TypedDict, total=False):
    grouping_key: Required[str]
    """Grouping key value"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Unit amount for this combination"""


class NewFloatingCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig(TypedDict, total=False):
    dimension_values: Required[Iterable[NewFloatingCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue]]
    """Each tier lower bound must have the same group of values."""

    group: Required[str]
    """Grouping key name"""


NewFloatingCumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        NewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
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

    conversion_rate_config: Optional[NewFloatingCumulativeGroupedAllocationPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


NewFloatingCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingMinimumCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    minimum_config: Required[NewFloatingMinimumCompositePriceMinimumConfig]
    """Configuration for minimum pricing"""

    model_type: Required[Literal["minimum"]]
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

    conversion_rate_config: Optional[NewFloatingMinimumCompositePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMinimumCompositePriceMinimumConfig(TypedDict, total=False):
    minimum_amount: Required[str]
    """The minimum amount to apply"""

    prorated: bool
    """If true, subtotals from this price are prorated based on the service period"""


NewFloatingMinimumCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingPercentCompositePrice(TypedDict, total=False):
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

    percent_config: Required[NewFloatingPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[NewFloatingPercentCompositePriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingPercentCompositePricePercentConfig(TypedDict, total=False):
    percent: Required[float]
    """What percent of the component subtotals to charge"""


NewFloatingPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class NewFloatingEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    event_output_config: Required[NewFloatingEventOutputPriceEventOutputConfig]
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

    conversion_rate_config: Optional[NewFloatingEventOutputPriceConversionRateConfig]
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


NewFloatingEventOutputPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]

PriceCreateParams: TypeAlias = Union[
    NewFloatingUnitPrice,
    NewFloatingTieredPrice,
    NewFloatingBulkPrice,
    NewFloatingBulkWithFiltersPrice,
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
    NewFloatingTieredWithProrationPrice,
    NewFloatingUnitWithProrationPrice,
    NewFloatingGroupedAllocationPrice,
    NewFloatingBulkWithProrationPrice,
    NewFloatingGroupedWithProratedMinimumPrice,
    NewFloatingGroupedWithMeteredMinimumPrice,
    NewFloatingGroupedWithMinMaxThresholdsPrice,
    NewFloatingMatrixWithDisplayNamePrice,
    NewFloatingGroupedTieredPackagePrice,
    NewFloatingMaxGroupTieredPackagePrice,
    NewFloatingScalableMatrixWithUnitPricingPrice,
    NewFloatingScalableMatrixWithTieredPricingPrice,
    NewFloatingCumulativeGroupedBulkPrice,
    NewFloatingCumulativeGroupedAllocationPrice,
    NewFloatingMinimumCompositePrice,
    NewFloatingPercentCompositePrice,
    NewFloatingEventOutputPrice,
]
