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
    "UnitPriceUnnamedTypeWithobjectParent79",
    "PackagePrice",
    "PackagePriceUnnamedTypeWithobjectParent80",
    "MatrixPrice",
    "MatrixPriceUnnamedTypeWithobjectParent81",
    "TieredPrice",
    "TieredPriceUnnamedTypeWithobjectParent82",
    "BulkPrice",
    "BulkPriceUnnamedTypeWithobjectParent83",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceUnnamedTypeWithobjectParent84",
    "TieredPackagePrice",
    "TieredPackagePriceUnnamedTypeWithobjectParent85",
    "GroupedTieredPrice",
    "GroupedTieredPriceUnnamedTypeWithobjectParent86",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceUnnamedTypeWithobjectParent87",
    "TieredPackageWithMinimumPrice",
    "TieredPackageWithMinimumPriceUnnamedTypeWithobjectParent88",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceUnnamedTypeWithobjectParent89",
    "UnitWithPercentPrice",
    "UnitWithPercentPriceUnnamedTypeWithobjectParent90",
    "MatrixWithAllocationPrice",
    "MatrixWithAllocationPriceUnnamedTypeWithobjectParent91",
    "TieredWithProrationPrice",
    "TieredWithProrationPriceUnnamedTypeWithobjectParent92",
    "UnitWithProrationPrice",
    "UnitWithProrationPriceUnnamedTypeWithobjectParent93",
    "GroupedAllocationPrice",
    "GroupedAllocationPriceUnnamedTypeWithobjectParent94",
    "GroupedWithProratedMinimumPrice",
    "GroupedWithProratedMinimumPriceUnnamedTypeWithobjectParent95",
    "GroupedWithMeteredMinimumPrice",
    "GroupedWithMeteredMinimumPriceUnnamedTypeWithobjectParent96",
    "MatrixWithDisplayNamePrice",
    "MatrixWithDisplayNamePriceUnnamedTypeWithobjectParent97",
    "BulkWithProrationPrice",
    "BulkWithProrationPriceUnnamedTypeWithobjectParent98",
    "GroupedTieredPackagePrice",
    "GroupedTieredPackagePriceUnnamedTypeWithobjectParent99",
    "MaxGroupTieredPackagePrice",
    "MaxGroupTieredPackagePriceUnnamedTypeWithobjectParent100",
    "ScalableMatrixWithUnitPricingPrice",
    "ScalableMatrixWithUnitPricingPriceUnnamedTypeWithobjectParent101",
    "ScalableMatrixWithTieredPricingPrice",
    "ScalableMatrixWithTieredPricingPriceUnnamedTypeWithobjectParent102",
    "CumulativeGroupedBulkPrice",
    "CumulativeGroupedBulkPriceUnnamedTypeWithobjectParent103",
    "GroupedWithMinMaxThresholdsPrice",
    "GroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent104",
    "MinimumCompositePrice",
    "MinimumCompositePriceUnnamedTypeWithobjectParent105",
    "MinimumCompositePriceMinimumConfig",
]

UnitPriceUnnamedTypeWithobjectParent79: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitPriceUnnamedTypeWithobjectParent79] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    unit_config: UnitConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


PackagePriceUnnamedTypeWithobjectParent80: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[PackagePriceUnnamedTypeWithobjectParent80] = None

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

    name: str

    package_config: PackageConfig

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MatrixPriceUnnamedTypeWithobjectParent81: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixPriceUnnamedTypeWithobjectParent81] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    matrix_config: MatrixConfig

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredPriceUnnamedTypeWithobjectParent82: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPriceUnnamedTypeWithobjectParent82] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_config: TieredConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


BulkPriceUnnamedTypeWithobjectParent83: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_config: BulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkPriceUnnamedTypeWithobjectParent83] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


ThresholdTotalAmountPriceUnnamedTypeWithobjectParent84: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ThresholdTotalAmountPriceUnnamedTypeWithobjectParent84] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    threshold_total_amount_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredPackagePriceUnnamedTypeWithobjectParent85: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPackagePriceUnnamedTypeWithobjectParent85] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_package_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedTieredPriceUnnamedTypeWithobjectParent86: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPriceUnnamedTypeWithobjectParent86] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredWithMinimumPriceUnnamedTypeWithobjectParent87: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredWithMinimumPriceUnnamedTypeWithobjectParent87] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredPackageWithMinimumPriceUnnamedTypeWithobjectParent88: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPackageWithMinimumPriceUnnamedTypeWithobjectParent88] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_package_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


PackageWithAllocationPriceUnnamedTypeWithobjectParent89: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[PackageWithAllocationPriceUnnamedTypeWithobjectParent89] = None

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

    name: str

    package_with_allocation_config: Dict[str, object]

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


UnitWithPercentPriceUnnamedTypeWithobjectParent90: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitWithPercentPriceUnnamedTypeWithobjectParent90] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    unit_with_percent_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MatrixWithAllocationPriceUnnamedTypeWithobjectParent91: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixWithAllocationPriceUnnamedTypeWithobjectParent91] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    matrix_with_allocation_config: MatrixWithAllocationConfig

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


TieredWithProrationPriceUnnamedTypeWithobjectParent92: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredWithProrationPriceUnnamedTypeWithobjectParent92] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


UnitWithProrationPriceUnnamedTypeWithobjectParent93: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitWithProrationPriceUnnamedTypeWithobjectParent93] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    unit_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedAllocationPriceUnnamedTypeWithobjectParent94: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedAllocationPriceUnnamedTypeWithobjectParent94] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_allocation_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedWithProratedMinimumPriceUnnamedTypeWithobjectParent95: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithProratedMinimumPriceUnnamedTypeWithobjectParent95] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_prorated_minimum_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedWithMeteredMinimumPriceUnnamedTypeWithobjectParent96: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMeteredMinimumPriceUnnamedTypeWithobjectParent96] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_metered_minimum_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MatrixWithDisplayNamePriceUnnamedTypeWithobjectParent97: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixWithDisplayNamePriceUnnamedTypeWithobjectParent97] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    matrix_with_display_name_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


BulkWithProrationPriceUnnamedTypeWithobjectParent98: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_with_proration_config: Dict[str, object]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkWithProrationPriceUnnamedTypeWithobjectParent98] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedTieredPackagePriceUnnamedTypeWithobjectParent99: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPackagePriceUnnamedTypeWithobjectParent99] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_package_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MaxGroupTieredPackagePriceUnnamedTypeWithobjectParent100: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MaxGroupTieredPackagePriceUnnamedTypeWithobjectParent100] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfiguration] = None

    item: ItemSlim

    max_group_tiered_package_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


ScalableMatrixWithUnitPricingPriceUnnamedTypeWithobjectParent101: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ScalableMatrixWithUnitPricingPriceUnnamedTypeWithobjectParent101] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    scalable_matrix_with_unit_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


ScalableMatrixWithTieredPricingPriceUnnamedTypeWithobjectParent102: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ScalableMatrixWithTieredPricingPriceUnnamedTypeWithobjectParent102] = None

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    scalable_matrix_with_tiered_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


CumulativeGroupedBulkPriceUnnamedTypeWithobjectParent103: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[CumulativeGroupedBulkPriceUnnamedTypeWithobjectParent103] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    cumulative_grouped_bulk_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


GroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent104: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithMinMaxThresholdsPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent104] = None

    created_at: datetime

    credit_allocation: Optional[Allocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_min_max_thresholds_config: Dict[str, object]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


MinimumCompositePriceUnnamedTypeWithobjectParent105: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MinimumCompositePriceMinimumConfig(BaseModel):
    minimum_amount: str
    """The minimum amount to apply"""

    prorated: Optional[bool] = None
    """
    By default, subtotals from minimum composite prices are prorated based on the
    service period. Set to false to disable proration.
    """


class MinimumCompositePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    composite_price_filters: Optional[List[TransformPriceFilter]] = None

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MinimumCompositePriceUnnamedTypeWithobjectParent105] = None

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

    price_model_type: Literal["minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


Price: TypeAlias = Annotated[
    Union[
        UnitPrice,
        PackagePrice,
        MatrixPrice,
        TieredPrice,
        BulkPrice,
        ThresholdTotalAmountPrice,
        TieredPackagePrice,
        GroupedTieredPrice,
        TieredWithMinimumPrice,
        TieredPackageWithMinimumPrice,
        PackageWithAllocationPrice,
        UnitWithPercentPrice,
        MatrixWithAllocationPrice,
        TieredWithProrationPrice,
        UnitWithProrationPrice,
        GroupedAllocationPrice,
        GroupedWithProratedMinimumPrice,
        GroupedWithMeteredMinimumPrice,
        MatrixWithDisplayNamePrice,
        BulkWithProrationPrice,
        GroupedTieredPackagePrice,
        MaxGroupTieredPackagePrice,
        ScalableMatrixWithUnitPricingPrice,
        ScalableMatrixWithTieredPricingPrice,
        CumulativeGroupedBulkPrice,
        GroupedWithMinMaxThresholdsPrice,
        MinimumCompositePrice,
    ],
    PropertyInfo(discriminator="price_model_type"),
]
