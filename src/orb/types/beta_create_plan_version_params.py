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
    "BetaCreatePlanVersionParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddPrice",
    "AddPriceLicenseAllocationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation",
    "AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig",
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
    "ReplacePriceLicenseAllocationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation",
    "ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig",
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


class BetaCreatePlanVersionParams(TypedDict, total=False):
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig]
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig]
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPrice(TypedDict, total=False):
    bulk_config: Required[BulkConfig]
    """Configuration for bulk pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig]
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter(
    TypedDict, total=False
):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier(
    TypedDict, total=False
):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig(
    TypedDict, total=False
):
    """Configuration for bulk_with_filters pricing"""

    filters: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter]
    ]
    """Property filters to apply (all must match)"""

    tiers: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier]
    ]
    """Bulk tiers for rating based on total usage volume"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig
    ]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation]
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

    conversion_rate_config: Optional[AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig]
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig]
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable(
    TypedDict, total=False
):
    """Configuration for a single threshold"""

    threshold: Required[str]

    total_amount: Required[str]
    """Total amount for this threshold"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig(
    TypedDict, total=False
):
    """Configuration for threshold_total_amount pricing"""

    consumption_table: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable
        ]
    ]
    """
    When the quantity consumed passes a provided threshold, the configured total
    will be charged
    """

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""


AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier with business logic"""

    per_unit: Required[str]
    """Price per package"""

    tier_lower_bound: Required[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig(TypedDict, total=False):
    """Configuration for tiered_package pricing"""

    package_size: Required[str]

    tiers: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds. The tier bounds are defined
    based on the total quantity rather than the number of packages, so they must be
    multiples of the package size.
    """


AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    minimum_amount: Required[str]

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig(
    TypedDict, total=False
):
    """Configuration for tiered_with_minimum pricing"""

    tiers: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier]
    ]
    """Tiered pricing with a minimum amount dependent on the volume tier.

    Tiers are defined using exclusive lower bounds.
    """

    hide_zero_amount_tiers: bool
    """If true, tiers with an accrued amount of 0 will not be included in the rating."""

    prorate: bool
    """If true, the unit price will be prorated to the billing period"""


AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig(TypedDict, total=False):
    """Configuration for grouped_tiered pricing"""

    grouping_key: Required[str]
    """The billable metric property used to group before tiering"""

    tiers: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier]
    ]
    """
    Apply tiered pricing to each segment generated after grouping with the provided
    key
    """


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_tiered_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig
    ]
    """Configuration for grouped_tiered pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    minimum_amount: Required[str]

    per_unit: Required[str]

    tier_lower_bound: Required[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig(
    TypedDict, total=False
):
    """Configuration for tiered_package_with_minimum pricing"""

    package_size: Required[float]

    tiers: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier
        ]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig(
    TypedDict, total=False
):
    """Configuration for package_with_allocation pricing"""

    allocation: Required[str]

    package_amount: Required[str]

    package_size: Required[str]


AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig(
    TypedDict, total=False
):
    """Configuration for unit_with_percent pricing"""

    percent: Required[str]
    """What percent, out of 100, of the calculated total to charge"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tiered with proration tier"""

    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for tiered_with_proration pricing"""

    tiers: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier
        ]
    ]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for unit_with_proration pricing"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig(
    TypedDict, total=False
):
    """Configuration for grouped_allocation pricing"""

    allocation: Required[str]
    """Usage allocation per group"""

    grouping_key: Required[str]
    """How to determine the groups that should each be allocated some quantity"""

    overage_unit_rate: Required[str]
    """Unit rate for post-allocation"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_allocation_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig
    ]
    """Configuration for grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier(
    TypedDict, total=False
):
    """Configuration for a single bulk pricing tier with proration"""

    unit_amount: Required[str]
    """Cost per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for bulk_with_proration pricing"""

    tiers: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier]
    ]
    """Bulk tiers for rating based on total usage volume"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig
    ]
    """Configuration for bulk_with_proration pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig(
    TypedDict, total=False
):
    """Configuration for grouped_with_prorated_minimum pricing"""

    grouping_key: Required[str]
    """How to determine the groups that should each have a minimum"""

    minimum: Required[str]
    """The minimum amount to charge per group"""

    unit_rate: Required[str]
    """The amount to charge per unit"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig
    ]
    """Configuration for grouped_with_prorated_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor(
    TypedDict, total=False
):
    """Configuration for a scaling factor"""

    scaling_factor: Required[str]

    scaling_value: Required[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount(
    TypedDict, total=False
):
    """Configuration for a unit amount"""

    pricing_value: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig(
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
            AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor
        ]
    ]
    """Scale the unit rates by the scaling factor."""

    scaling_key: Required[str]
    """Used to determine the unit rate scaling factor"""

    unit_amounts: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount
        ]
    ]
    """Apply per unit pricing to each pricing value.

    The minimum amount is applied any unmatched usage.
    """


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_metered_minimum_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig
    ]
    """Configuration for grouped_with_metered_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
    ]
    """Configuration for grouped_with_min_max_thresholds pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount(
    TypedDict, total=False
):
    """Configuration for a unit amount item"""

    dimension_value: Required[str]
    """The dimension value"""

    display_name: Required[str]
    """Display name for this dimension value"""

    unit_amount: Required[str]
    """Per unit amount"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig(
    TypedDict, total=False
):
    """Configuration for matrix_with_display_name pricing"""

    dimension: Required[str]
    """Used to determine the unit rate"""

    unit_amounts: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount
        ]
    ]
    """Apply per unit pricing to each dimension value"""


AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    matrix_with_display_name_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    per_unit: Required[str]
    """Per package"""

    tier_lower_bound: Required[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig(
    TypedDict, total=False
):
    """Configuration for grouped_tiered_package pricing"""

    grouping_key: Required[str]
    """The event property used to group before tiering"""

    package_size: Required[str]

    tiers: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier
        ]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_tiered_package_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig
    ]
    """Configuration for grouped_tiered_package pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig(
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
            AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier
        ]
    ]
    """Apply tiered pricing to the largest group after grouping with the provided key."""


AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    max_group_tiered_package_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    """Configuration for a single matrix scaling factor"""

    first_dimension_value: Required[str]

    scaling_factor: Required[str]

    second_dimension_value: Optional[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig(
    TypedDict, total=False
):
    """Configuration for scalable_matrix_with_unit_pricing pricing"""

    first_dimension: Required[str]
    """Used to determine the unit rate"""

    matrix_scaling_factors: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor
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


AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    """Configuration for a single matrix scaling factor"""

    first_dimension_value: Required[str]

    scaling_factor: Required[str]

    second_dimension_value: Optional[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier entry with business logic"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig(
    TypedDict, total=False
):
    """Configuration for scalable_matrix_with_tiered_pricing pricing"""

    first_dimension: Required[str]
    """Used for the scalable matrix first dimension"""

    matrix_scaling_factors: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor
        ]
    ]
    """Apply a scaling factor to each dimension"""

    tiers: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier
        ]
    ]

    second_dimension: Optional[str]
    """Used for the scalable matrix second dimension (optional)"""


AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation
        ]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue(
    TypedDict, total=False
):
    """Configuration for a dimension value entry"""

    grouping_key: Required[str]
    """Grouping key value"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Unit amount for this combination"""


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig(
    TypedDict, total=False
):
    """Configuration for cumulative_grouped_bulk pricing"""

    dimension_values: Required[
        Iterable[
            AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue
        ]
    ]
    """Each tier lower bound must have the same group of values."""

    group: Required[str]


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig
    ]
    """Configuration for cumulative_grouped_bulk pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig(
    TypedDict, total=False
):
    """Configuration for minimum_composite pricing"""

    minimum_amount: Required[str]
    """The minimum amount to apply"""

    prorated: bool
    """If true, subtotals from this price are prorated based on the service period"""


AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    minimum_composite_config: Required[
        AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

    percent: Required[float]
    """What percent of the component subtotals to charge"""


AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


class AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig]
    """Configuration for event_output pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation]
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
        AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig
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


AddPriceLicenseAllocationPrice: TypeAlias = Union[
    AddPriceLicenseAllocationPriceNewLicenseAllocationUnitPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationBulkPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationPackagePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice,
    AddPriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice,
]


class AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class AddPricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    """Configuration for bulk_with_filters pricing"""

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


class AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    """Configuration for a single tiered with proration tier"""

    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class AddPricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    """Configuration for tiered_with_proration pricing"""

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


class AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    """Configuration for grouped_with_min_max_thresholds pricing"""

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


class AddPricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    """Configuration for cumulative_grouped_allocation pricing"""

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


class AddPricePriceNewPlanPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

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


class AddPricePriceNewPlanEventOutputPriceEventOutputConfig(TypedDict, total=False):
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

    license_allocation_price: Optional[AddPriceLicenseAllocationPrice]
    """The license allocation price to add to the plan."""

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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPrice(TypedDict, total=False):
    bulk_config: Required[BulkConfig]
    """Configuration for bulk pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter(
    TypedDict, total=False
):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier(
    TypedDict, total=False
):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig(
    TypedDict, total=False
):
    """Configuration for bulk_with_filters pricing"""

    filters: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigFilter]
    ]
    """Property filters to apply (all must match)"""

    tiers: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfigTier]
    ]
    """Bulk tiers for rating based on total usage volume"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceBulkWithFiltersConfig
    ]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePriceLicenseAllocation]
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

    conversion_rate_config: Optional[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceLicenseAllocation]
    ]
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

    conversion_rate_config: Optional[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable(
    TypedDict, total=False
):
    """Configuration for a single threshold"""

    threshold: Required[str]

    total_amount: Required[str]
    """Total amount for this threshold"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig(
    TypedDict, total=False
):
    """Configuration for threshold_total_amount pricing"""

    consumption_table: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable
        ]
    ]
    """
    When the quantity consumed passes a provided threshold, the configured total
    will be charged
    """

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceThresholdTotalAmountConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier with business logic"""

    per_unit: Required[str]
    """Price per package"""

    tier_lower_bound: Required[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig(
    TypedDict, total=False
):
    """Configuration for tiered_package pricing"""

    package_size: Required[str]

    tiers: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfigTier]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds. The tier bounds are defined
    based on the total quantity rather than the number of packages, so they must be
    multiples of the package size.
    """


ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceTieredPackageConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    minimum_amount: Required[str]

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig(
    TypedDict, total=False
):
    """Configuration for tiered_with_minimum pricing"""

    tiers: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfigTier
        ]
    ]
    """Tiered pricing with a minimum amount dependent on the volume tier.

    Tiers are defined using exclusive lower bounds.
    """

    hide_zero_amount_tiers: bool
    """If true, tiers with an accrued amount of 0 will not be included in the rating."""

    prorate: bool
    """If true, the unit price will be prorated to the billing period"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceTieredWithMinimumConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig(
    TypedDict, total=False
):
    """Configuration for grouped_tiered pricing"""

    grouping_key: Required[str]
    """The billable metric property used to group before tiering"""

    tiers: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfigTier]
    ]
    """
    Apply tiered pricing to each segment generated after grouping with the provided
    key
    """


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_tiered_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceGroupedTieredConfig
    ]
    """Configuration for grouped_tiered pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    minimum_amount: Required[str]

    per_unit: Required[str]

    tier_lower_bound: Required[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig(
    TypedDict, total=False
):
    """Configuration for tiered_package_with_minimum pricing"""

    package_size: Required[float]

    tiers: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier
        ]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceTieredPackageWithMinimumConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig(
    TypedDict, total=False
):
    """Configuration for package_with_allocation pricing"""

    allocation: Required[str]

    package_amount: Required[str]

    package_size: Required[str]


ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPricePackageWithAllocationConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig(
    TypedDict, total=False
):
    """Configuration for unit_with_percent pricing"""

    percent: Required[str]
    """What percent, out of 100, of the calculated total to charge"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceUnitWithPercentConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tiered with proration tier"""

    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for tiered_with_proration pricing"""

    tiers: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfigTier
        ]
    ]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceTieredWithProrationConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for unit_with_proration pricing"""

    unit_amount: Required[str]
    """Rate per unit of usage"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceUnitWithProrationConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig(
    TypedDict, total=False
):
    """Configuration for grouped_allocation pricing"""

    allocation: Required[str]
    """Usage allocation per group"""

    grouping_key: Required[str]
    """How to determine the groups that should each be allocated some quantity"""

    overage_unit_rate: Required[str]
    """Unit rate for post-allocation"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_allocation_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceGroupedAllocationConfig
    ]
    """Configuration for grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier(
    TypedDict, total=False
):
    """Configuration for a single bulk pricing tier with proration"""

    unit_amount: Required[str]
    """Cost per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig(
    TypedDict, total=False
):
    """Configuration for bulk_with_proration pricing"""

    tiers: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfigTier
        ]
    ]
    """Bulk tiers for rating based on total usage volume"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceBulkWithProrationConfig
    ]
    """Configuration for bulk_with_proration pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig(
    TypedDict, total=False
):
    """Configuration for grouped_with_prorated_minimum pricing"""

    grouping_key: Required[str]
    """How to determine the groups that should each have a minimum"""

    minimum: Required[str]
    """The minimum amount to charge per group"""

    unit_rate: Required[str]
    """The amount to charge per unit"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig
    ]
    """Configuration for grouped_with_prorated_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor(
    TypedDict, total=False
):
    """Configuration for a scaling factor"""

    scaling_factor: Required[str]

    scaling_value: Required[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount(
    TypedDict, total=False
):
    """Configuration for a unit amount"""

    pricing_value: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig(
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
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor
        ]
    ]
    """Scale the unit rates by the scaling factor."""

    scaling_key: Required[str]
    """Used to determine the unit rate scaling factor"""

    unit_amounts: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount
        ]
    ]
    """Apply per unit pricing to each pricing value.

    The minimum amount is applied any unmatched usage.
    """


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = (
    Union[UnitConversionRateConfig, TieredConversionRateConfig]
)


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_metered_minimum_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig
    ]
    """Configuration for grouped_with_metered_minimum pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
    ]
    """Configuration for grouped_with_min_max_thresholds pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceLicenseAllocation
        ]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount(
    TypedDict, total=False
):
    """Configuration for a unit amount item"""

    dimension_value: Required[str]
    """The dimension value"""

    display_name: Required[str]
    """Display name for this dimension value"""

    unit_amount: Required[str]
    """Per unit amount"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig(
    TypedDict, total=False
):
    """Configuration for matrix_with_display_name pricing"""

    dimension: Required[str]
    """Used to determine the unit rate"""

    unit_amounts: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount
        ]
    ]
    """Apply per unit pricing to each dimension value"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    matrix_with_display_name_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceMatrixWithDisplayNameConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    per_unit: Required[str]
    """Per package"""

    tier_lower_bound: Required[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig(
    TypedDict, total=False
):
    """Configuration for grouped_tiered_package pricing"""

    grouping_key: Required[str]
    """The event property used to group before tiering"""

    package_size: Required[str]

    tiers: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfigTier
        ]
    ]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_tiered_package_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceGroupedTieredPackageConfig
    ]
    """Configuration for grouped_tiered_package pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]
    """Per unit amount"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig(
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
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier
        ]
    ]
    """Apply tiered pricing to the largest group after grouping with the provided key."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    max_group_tiered_package_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceMaxGroupTieredPackageConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    """Configuration for a single matrix scaling factor"""

    first_dimension_value: Required[str]

    scaling_factor: Required[str]

    second_dimension_value: Optional[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig(
    TypedDict, total=False
):
    """Configuration for scalable_matrix_with_unit_pricing pricing"""

    first_dimension: Required[str]
    """Used to determine the unit rate"""

    matrix_scaling_factors: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor
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


ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceLicenseAllocation
        ]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor(
    TypedDict, total=False
):
    """Configuration for a single matrix scaling factor"""

    first_dimension_value: Required[str]

    scaling_factor: Required[str]

    second_dimension_value: Optional[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier(
    TypedDict, total=False
):
    """Configuration for a single tier entry with business logic"""

    tier_lower_bound: Required[str]

    unit_amount: Required[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig(
    TypedDict, total=False
):
    """Configuration for scalable_matrix_with_tiered_pricing pricing"""

    first_dimension: Required[str]
    """Used for the scalable matrix first dimension"""

    matrix_scaling_factors: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor
        ]
    ]
    """Apply a scaling factor to each dimension"""

    tiers: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier
        ]
    ]

    second_dimension: Optional[str]
    """Used for the scalable matrix second dimension (optional)"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice(
    TypedDict, total=False
):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceLicenseAllocation
        ]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue(
    TypedDict, total=False
):
    """Configuration for a dimension value entry"""

    grouping_key: Required[str]
    """Grouping key value"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Unit amount for this combination"""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig(
    TypedDict, total=False
):
    """Configuration for cumulative_grouped_bulk pricing"""

    dimension_values: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue
        ]
    ]
    """Each tier lower bound must have the same group of values."""

    group: Required[str]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceCumulativeGroupedBulkConfig
    ]
    """Configuration for cumulative_grouped_bulk pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[
            ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceLicenseAllocation
        ]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig(
    TypedDict, total=False
):
    """Configuration for minimum_composite pricing"""

    minimum_amount: Required[str]
    """The minimum amount to apply"""

    prorated: bool
    """If true, subtotals from this price are prorated based on the service period"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    minimum_composite_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceMinimumCompositeConfig
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation(
    TypedDict, total=False
):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

    percent: Required[float]
    """What percent of the component subtotals to charge"""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceLicenseAllocation]
    ]
    """License allocations to associate with this price.

    Each entry defines a per-license credit pool granted each cadence. Requires
    license_type_id or license_type_configuration to be set.
    """

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePricePercentConfig]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePriceConversionRateConfig
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation(TypedDict, total=False):
    amount: Required[str]
    """The amount of credits granted per active license per cadence."""

    currency: Required[str]
    """The currency of the license allocation."""

    write_off_overage: Optional[bool]
    """When True, overage beyond the allocation is written off."""


ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceEventOutputConfig
    ]
    """Configuration for event_output pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    license_allocations: Required[
        Iterable[ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceLicenseAllocation]
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
        ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPriceConversionRateConfig
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


ReplacePriceLicenseAllocationPrice: TypeAlias = Union[
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithFiltersPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackagePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationThresholdTotalAmountPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackagePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithMinimumPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredPackageWithMinimumPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationPackageWithAllocationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithPercentPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithAllocationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationTieredWithProrationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationUnitWithProrationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedAllocationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationBulkWithProrationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithProratedMinimumPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMeteredMinimumPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedWithMinMaxThresholdsPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationMatrixWithDisplayNamePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationGroupedTieredPackagePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationMaxGroupTieredPackagePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithUnitPricingPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationScalableMatrixWithTieredPricingPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedBulkPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationCumulativeGroupedAllocationPrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationMinimumCompositePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationPercentCompositePrice,
    ReplacePriceLicenseAllocationPriceNewLicenseAllocationEventOutputPrice,
]


class ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    """Configuration for a single property filter"""

    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    """Configuration for a single bulk pricing tier"""

    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class ReplacePricePriceNewPlanBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    """Configuration for bulk_with_filters pricing"""

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


class ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    """Configuration for a single tiered with proration tier"""

    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class ReplacePricePriceNewPlanTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    """Configuration for tiered_with_proration pricing"""

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


class ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(TypedDict, total=False):
    """Configuration for grouped_with_min_max_thresholds pricing"""

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


class ReplacePricePriceNewPlanCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(TypedDict, total=False):
    """Configuration for cumulative_grouped_allocation pricing"""

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


class ReplacePricePriceNewPlanPercentCompositePricePercentConfig(TypedDict, total=False):
    """Configuration for percent pricing"""

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


class ReplacePricePriceNewPlanEventOutputPriceEventOutputConfig(TypedDict, total=False):
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

    license_allocation_price: Optional[ReplacePriceLicenseAllocationPrice]
    """The license allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this price from."""

    price: Optional[ReplacePricePrice]
    """New plan price request body params."""
