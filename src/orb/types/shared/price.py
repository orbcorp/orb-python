# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .maximum import Maximum
from .minimum import Minimum
from ..._utils import PropertyInfo
from .discount import Discount
from ..._models import BaseModel
from .item_slim import ItemSlim
from .allocation import Allocation
from .bulk_config import BulkConfig
from .unit_config import UnitConfig
from .matrix_config import MatrixConfig
from .tiered_config import TieredConfig
from .package_config import PackageConfig
from .billable_metric_tiny import BillableMetricTiny
from .transform_price_filter import TransformPriceFilter
from .billing_cycle_configuration import BillingCycleConfiguration
from .unit_conversion_rate_config import UnitConversionRateConfig
from .matrix_with_allocation_config import MatrixWithAllocationConfig
from .tiered_conversion_rate_config import TieredConversionRateConfig
from .dimensional_price_configuration import DimensionalPriceConfiguration

__all__ = [
    "Price",
    "UnitPrice",
    "UnitPriceConversionRateConfig",
    "TieredPrice",
    "TieredPriceConversionRateConfig",
    "BulkPrice",
    "BulkPriceConversionRateConfig",
    "PackagePrice",
    "PackagePriceConversionRateConfig",
    "MatrixPrice",
    "MatrixPriceConversionRateConfig",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceConversionRateConfig",
    "ThresholdTotalAmountPriceThresholdTotalAmountConfig",
    "ThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable",
    "TieredPackagePrice",
    "TieredPackagePriceConversionRateConfig",
    "TieredPackagePriceTieredPackageConfig",
    "TieredPackagePriceTieredPackageConfigTier",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceConversionRateConfig",
    "TieredWithMinimumPriceTieredWithMinimumConfig",
    "TieredWithMinimumPriceTieredWithMinimumConfigTier",
    "GroupedTieredPrice",
    "GroupedTieredPriceConversionRateConfig",
    "GroupedTieredPriceGroupedTieredConfig",
    "GroupedTieredPriceGroupedTieredConfigTier",
    "TieredPackageWithMinimumPrice",
    "TieredPackageWithMinimumPriceConversionRateConfig",
    "TieredPackageWithMinimumPriceTieredPackageWithMinimumConfig",
    "TieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceConversionRateConfig",
    "PackageWithAllocationPricePackageWithAllocationConfig",
    "UnitWithPercentPrice",
    "UnitWithPercentPriceConversionRateConfig",
    "UnitWithPercentPriceUnitWithPercentConfig",
    "MatrixWithAllocationPrice",
    "MatrixWithAllocationPriceConversionRateConfig",
    "TieredWithProrationPrice",
    "TieredWithProrationPriceConversionRateConfig",
    "TieredWithProrationPriceTieredWithProrationConfig",
    "TieredWithProrationPriceTieredWithProrationConfigTier",
    "UnitWithProrationPrice",
    "UnitWithProrationPriceConversionRateConfig",
    "UnitWithProrationPriceUnitWithProrationConfig",
    "GroupedAllocationPrice",
    "GroupedAllocationPriceConversionRateConfig",
    "GroupedAllocationPriceGroupedAllocationConfig",
    "BulkWithProrationPrice",
    "BulkWithProrationPriceBulkWithProrationConfig",
    "BulkWithProrationPriceBulkWithProrationConfigTier",
    "BulkWithProrationPriceConversionRateConfig",
    "GroupedWithProratedMinimumPrice",
    "GroupedWithProratedMinimumPriceConversionRateConfig",
    "GroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig",
    "GroupedWithMeteredMinimumPrice",
    "GroupedWithMeteredMinimumPriceConversionRateConfig",
    "GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig",
    "GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor",
    "GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount",
    "GroupedWithMinMaxThresholdsPrice",
    "GroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "GroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "MatrixWithDisplayNamePrice",
    "MatrixWithDisplayNamePriceConversionRateConfig",
    "MatrixWithDisplayNamePriceMatrixWithDisplayNameConfig",
    "MatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount",
    "GroupedTieredPackagePrice",
    "GroupedTieredPackagePriceConversionRateConfig",
    "GroupedTieredPackagePriceGroupedTieredPackageConfig",
    "GroupedTieredPackagePriceGroupedTieredPackageConfigTier",
    "MaxGroupTieredPackagePrice",
    "MaxGroupTieredPackagePriceConversionRateConfig",
    "MaxGroupTieredPackagePriceMaxGroupTieredPackageConfig",
    "MaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier",
    "ScalableMatrixWithUnitPricingPrice",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "ScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig",
    "ScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor",
    "ScalableMatrixWithTieredPricingPrice",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig",
    "ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor",
    "ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier",
    "CumulativeGroupedBulkPrice",
    "CumulativeGroupedBulkPriceConversionRateConfig",
    "CumulativeGroupedBulkPriceCumulativeGroupedBulkConfig",
    "CumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue",
    "MinimumCompositePrice",
    "MinimumCompositePriceConversionRateConfig",
    "MinimumCompositePriceMinimumConfig",
]

UnitPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    unit_config: UnitConfig
    """Configuration for unit pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_config: TieredConfig
    """Configuration for tiered pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


BulkPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    bulk_config: BulkConfig
    """Configuration for bulk pricing"""

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


PackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[PackagePriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    package_config: PackageConfig
    """Configuration for package pricing"""

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MatrixPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    matrix_config: MatrixConfig
    """Configuration for matrix pricing"""

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


ThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable(BaseModel):
    threshold: str
    """Quantity threshold"""

    total_amount: str
    """Total amount for this threshold"""


class ThresholdTotalAmountPriceThresholdTotalAmountConfig(BaseModel):
    consumption_table: List[ThresholdTotalAmountPriceThresholdTotalAmountConfigConsumptionTable]
    """
    When the quantity consumed passes a provided threshold, the configured total
    will be charged
    """

    prorate: Optional[bool] = None
    """If true, the unit price will be prorated to the billing period"""


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ThresholdTotalAmountPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    threshold_total_amount_config: ThresholdTotalAmountPriceThresholdTotalAmountConfig
    """Configuration for threshold_total_amount pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredPackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPackagePriceTieredPackageConfigTier(BaseModel):
    per_unit: str
    """Price per package"""

    tier_lower_bound: str
    """Tier lower bound"""


class TieredPackagePriceTieredPackageConfig(BaseModel):
    package_size: str
    """Package size"""

    tiers: List[TieredPackagePriceTieredPackageConfigTier]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds. The tier bounds are defined
    based on the total quantity rather than the number of packages, so they must be
    multiples of the package size.
    """


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPackagePriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_package_config: TieredPackagePriceTieredPackageConfig
    """Configuration for tiered_package pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredWithMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredWithMinimumPriceTieredWithMinimumConfigTier(BaseModel):
    minimum_amount: str
    """Minimum amount"""

    tier_lower_bound: str
    """Tier lower bound"""

    unit_amount: str
    """Per unit amount"""


class TieredWithMinimumPriceTieredWithMinimumConfig(BaseModel):
    tiers: List[TieredWithMinimumPriceTieredWithMinimumConfigTier]
    """Tiered pricing with a minimum amount dependent on the volume tier.

    Tiers are defined using exclusive lower bounds.
    """

    hide_zero_amount_tiers: Optional[bool] = None
    """If true, tiers with an accrued amount of 0 will not be included in the rating."""

    prorate: Optional[bool] = None
    """If true, the unit price will be prorated to the billing period"""


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredWithMinimumPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_with_minimum_config: TieredWithMinimumPriceTieredWithMinimumConfig
    """Configuration for tiered_with_minimum pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedTieredPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedTieredPriceGroupedTieredConfigTier(BaseModel):
    tier_lower_bound: str
    """Tier lower bound"""

    unit_amount: str
    """Per unit amount"""


class GroupedTieredPriceGroupedTieredConfig(BaseModel):
    grouping_key: str
    """The billable metric property used to group before tiering"""

    tiers: List[GroupedTieredPriceGroupedTieredConfigTier]
    """
    Apply tiered pricing to each segment generated after grouping with the provided
    key
    """


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_config: GroupedTieredPriceGroupedTieredConfig
    """Configuration for grouped_tiered pricing"""

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier(BaseModel):
    minimum_amount: str
    """Minimum amount"""

    per_unit: str
    """Price per package"""

    tier_lower_bound: str
    """Tier lower bound"""


class TieredPackageWithMinimumPriceTieredPackageWithMinimumConfig(BaseModel):
    package_size: float
    """Package size"""

    tiers: List[TieredPackageWithMinimumPriceTieredPackageWithMinimumConfigTier]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPackageWithMinimumPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package_with_minimum"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_package_with_minimum_config: TieredPackageWithMinimumPriceTieredPackageWithMinimumConfig
    """Configuration for tiered_package_with_minimum pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


PackageWithAllocationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class PackageWithAllocationPricePackageWithAllocationConfig(BaseModel):
    allocation: str
    """Usage allocation"""

    package_amount: str
    """Price per package"""

    package_size: str
    """Package size"""


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[PackageWithAllocationPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    package_with_allocation_config: PackageWithAllocationPricePackageWithAllocationConfig
    """Configuration for package_with_allocation pricing"""

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


UnitWithPercentPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitWithPercentPriceUnitWithPercentConfig(BaseModel):
    percent: str
    """What percent, out of 100, of the calculated total to charge"""

    unit_amount: str
    """Rate per unit of usage"""


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitWithPercentPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_percent"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    unit_with_percent_config: UnitWithPercentPriceUnitWithPercentConfig
    """Configuration for unit_with_percent pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MatrixWithAllocationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixWithAllocationPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    matrix_with_allocation_config: MatrixWithAllocationConfig
    """Configuration for matrix_with_allocation pricing"""

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_allocation"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredWithProrationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredWithProrationPriceTieredWithProrationConfigTier(BaseModel):
    tier_lower_bound: str
    """Inclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""


class TieredWithProrationPriceTieredWithProrationConfig(BaseModel):
    tiers: List[TieredWithProrationPriceTieredWithProrationConfigTier]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredWithProrationPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_proration"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_with_proration_config: TieredWithProrationPriceTieredWithProrationConfig
    """Configuration for tiered_with_proration pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


UnitWithProrationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitWithProrationPriceUnitWithProrationConfig(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitWithProrationPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_proration"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    unit_with_proration_config: UnitWithProrationPriceUnitWithProrationConfig
    """Configuration for unit_with_proration pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedAllocationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedAllocationPriceGroupedAllocationConfig(BaseModel):
    allocation: str
    """Usage allocation per group"""

    grouping_key: str
    """How to determine the groups that should each be allocated some quantity"""

    overage_unit_rate: str
    """Unit rate for post-allocation"""


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedAllocationPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_allocation_config: GroupedAllocationPriceGroupedAllocationConfig
    """Configuration for grouped_allocation pricing"""

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_allocation"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class BulkWithProrationPriceBulkWithProrationConfigTier(BaseModel):
    unit_amount: str
    """Cost per unit"""

    tier_lower_bound: Optional[str] = None
    """The lower bound for this tier"""


class BulkWithProrationPriceBulkWithProrationConfig(BaseModel):
    tiers: List[BulkWithProrationPriceBulkWithProrationConfigTier]
    """Bulk tiers for rating based on total usage volume"""


BulkWithProrationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    bulk_with_proration_config: BulkWithProrationPriceBulkWithProrationConfig
    """Configuration for bulk_with_proration pricing"""

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkWithProrationPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk_with_proration"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig(BaseModel):
    grouping_key: str
    """How to determine the groups that should each have a minimum"""

    minimum: str
    """The minimum amount to charge per group"""

    unit_rate: str
    """The amount to charge per unit"""


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithProratedMinimumPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_prorated_minimum_config: GroupedWithProratedMinimumPriceGroupedWithProratedMinimumConfig
    """Configuration for grouped_with_prorated_minimum pricing"""

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_prorated_minimum"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor(BaseModel):
    scaling_factor: str
    """Scaling factor"""

    scaling_value: str
    """Scaling value"""


class GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount(BaseModel):
    pricing_value: str
    """Pricing value"""

    unit_amount: str
    """Per unit amount"""


class GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig(BaseModel):
    grouping_key: str
    """Used to partition the usage into groups.

    The minimum amount is applied to each group.
    """

    minimum_unit_amount: str
    """The minimum amount to charge per group per unit"""

    pricing_key: str
    """Used to determine the unit rate"""

    scaling_factors: List[GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigScalingFactor]
    """Scale the unit rates by the scaling factor."""

    scaling_key: str
    """Used to determine the unit rate scaling factor"""

    unit_amounts: List[GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfigUnitAmount]
    """Apply per unit pricing to each pricing value.

    The minimum amount is applied any unmatched usage.
    """


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMeteredMinimumPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_metered_minimum_config: GroupedWithMeteredMinimumPriceGroupedWithMeteredMinimumConfig
    """Configuration for grouped_with_metered_minimum pricing"""

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_metered_minimum"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(BaseModel):
    grouping_key: str
    """The event property used to group before applying thresholds"""

    maximum_charge: str
    """The maximum amount to charge each group"""

    minimum_charge: str
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: str
    """The base price charged per group"""


class GroupedWithMinMaxThresholdsPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMinMaxThresholdsPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_min_max_thresholds_config: GroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
    """Configuration for grouped_with_min_max_thresholds pricing"""

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_min_max_thresholds"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount(BaseModel):
    dimension_value: str
    """The dimension value"""

    display_name: str
    """Display name for this dimension value"""

    unit_amount: str
    """Per unit amount"""


class MatrixWithDisplayNamePriceMatrixWithDisplayNameConfig(BaseModel):
    dimension: str
    """Used to determine the unit rate"""

    unit_amounts: List[MatrixWithDisplayNamePriceMatrixWithDisplayNameConfigUnitAmount]
    """Apply per unit pricing to each dimension value"""


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixWithDisplayNamePriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    matrix_with_display_name_config: MatrixWithDisplayNamePriceMatrixWithDisplayNameConfig
    """Configuration for matrix_with_display_name pricing"""

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_display_name"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedTieredPackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedTieredPackagePriceGroupedTieredPackageConfigTier(BaseModel):
    per_unit: str
    """Price per package"""

    tier_lower_bound: str
    """Tier lower bound"""


class GroupedTieredPackagePriceGroupedTieredPackageConfig(BaseModel):
    grouping_key: str
    """The event property used to group before tiering"""

    package_size: str
    """Package size"""

    tiers: List[GroupedTieredPackagePriceGroupedTieredPackageConfigTier]
    """Apply tiered pricing after rounding up the quantity to the package size.

    Tiers are defined using exclusive lower bounds.
    """


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPackagePriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_package_config: GroupedTieredPackagePriceGroupedTieredPackageConfig
    """Configuration for grouped_tiered_package pricing"""

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered_package"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier(BaseModel):
    tier_lower_bound: str
    """Tier lower bound"""

    unit_amount: str
    """Per unit amount"""


class MaxGroupTieredPackagePriceMaxGroupTieredPackageConfig(BaseModel):
    grouping_key: str
    """
    The event property used to group before tiering the group with the highest value
    """

    package_size: str
    """Package size"""

    tiers: List[MaxGroupTieredPackagePriceMaxGroupTieredPackageConfigTier]
    """Apply tiered pricing to the largest group after grouping with the provided key."""


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MaxGroupTieredPackagePriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    max_group_tiered_package_config: MaxGroupTieredPackagePriceMaxGroupTieredPackageConfig
    """Configuration for max_group_tiered_package pricing"""

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["max_group_tiered_package"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


ScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor(BaseModel):
    first_dimension_value: str
    """First dimension value"""

    scaling_factor: str
    """Scaling factor"""

    second_dimension_value: Optional[str] = None
    """Second dimension value (optional)"""


class ScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig(BaseModel):
    first_dimension: str
    """Used to determine the unit rate"""

    matrix_scaling_factors: List[
        ScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfigMatrixScalingFactor
    ]
    """Apply a scaling factor to each dimension"""

    unit_price: str
    """The final unit price to rate against the output of the matrix"""

    prorate: Optional[bool] = None
    """If true, the unit price will be prorated to the billing period"""

    second_dimension: Optional[str] = None
    """Used to determine the unit rate (optional)"""


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ScalableMatrixWithUnitPricingPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["scalable_matrix_with_unit_pricing"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    scalable_matrix_with_unit_pricing_config: ScalableMatrixWithUnitPricingPriceScalableMatrixWithUnitPricingConfig
    """Configuration for scalable_matrix_with_unit_pricing pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


ScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor(BaseModel):
    first_dimension_value: str
    """First dimension value"""

    scaling_factor: str
    """Scaling factor"""

    second_dimension_value: Optional[str] = None
    """Second dimension value (optional)"""


class ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier(BaseModel):
    tier_lower_bound: str
    """Tier lower bound"""

    unit_amount: str
    """Per unit amount"""


class ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig(BaseModel):
    first_dimension: str
    """Used for the scalable matrix first dimension"""

    matrix_scaling_factors: List[
        ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigMatrixScalingFactor
    ]
    """Apply a scaling factor to each dimension"""

    tiers: List[ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfigTier]
    """Tier pricing structure"""

    second_dimension: Optional[str] = None
    """Used for the scalable matrix second dimension (optional)"""


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ScalableMatrixWithTieredPricingPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["scalable_matrix_with_tiered_pricing"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    scalable_matrix_with_tiered_pricing_config: (
        ScalableMatrixWithTieredPricingPriceScalableMatrixWithTieredPricingConfig
    )
    """Configuration for scalable_matrix_with_tiered_pricing pricing"""

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


CumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class CumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue(BaseModel):
    grouping_key: str
    """Grouping key value"""

    tier_lower_bound: str
    """Tier lower bound"""

    unit_amount: str
    """Unit amount for this combination"""


class CumulativeGroupedBulkPriceCumulativeGroupedBulkConfig(BaseModel):
    dimension_values: List[CumulativeGroupedBulkPriceCumulativeGroupedBulkConfigDimensionValue]
    """Each tier lower bound must have the same group of values."""

    group: str
    """Grouping key name"""


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[CumulativeGroupedBulkPriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    cumulative_grouped_bulk_config: CumulativeGroupedBulkPriceCumulativeGroupedBulkConfig
    """Configuration for cumulative_grouped_bulk pricing"""

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["cumulative_grouped_bulk"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MinimumCompositePriceConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MinimumCompositePriceMinimumConfig(BaseModel):
    minimum_amount: str
    """The minimum amount to apply"""

    prorated: Optional[bool] = None
    """If true, subtotals from this price are prorated based on the service period"""


class MinimumCompositePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    billing_mode: Literal["in_advance", "in_arrear"]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MinimumCompositePriceConversionRateConfig] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    minimum_config: MinimumCompositePriceMinimumConfig
    """Configuration for minimum pricing"""

    price_model_type: Literal["minimum"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price", "composite_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


Price: TypeAlias = Annotated[
    Union[
        UnitPrice,
        TieredPrice,
        BulkPrice,
        PackagePrice,
        MatrixPrice,
        ThresholdTotalAmountPrice,
        TieredPackagePrice,
        TieredWithMinimumPrice,
        GroupedTieredPrice,
        TieredPackageWithMinimumPrice,
        PackageWithAllocationPrice,
        UnitWithPercentPrice,
        MatrixWithAllocationPrice,
        TieredWithProrationPrice,
        UnitWithProrationPrice,
        GroupedAllocationPrice,
        BulkWithProrationPrice,
        GroupedWithProratedMinimumPrice,
        GroupedWithMeteredMinimumPrice,
        GroupedWithMinMaxThresholdsPrice,
        MatrixWithDisplayNamePrice,
        GroupedTieredPackagePrice,
        MaxGroupTieredPackagePrice,
        ScalableMatrixWithUnitPricingPrice,
        ScalableMatrixWithTieredPricingPrice,
        CumulativeGroupedBulkPrice,
        MinimumCompositePrice,
    ],
    PropertyInfo(discriminator="price_model_type"),
]
