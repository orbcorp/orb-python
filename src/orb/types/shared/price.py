# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
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
from .bps_config import BPSConfig
from .bulk_config import BulkConfig
from .unit_config import UnitConfig
from .matrix_config import MatrixConfig
from .tiered_config import TieredConfig
from .package_config import PackageConfig
from .bulk_bps_config import BulkBPSConfig
from .tiered_bps_config import TieredBPSConfig
from .billable_metric_tiny import BillableMetricTiny
from .billing_cycle_configuration import BillingCycleConfiguration
from .unit_conversion_rate_config import UnitConversionRateConfig
from .matrix_with_allocation_config import MatrixWithAllocationConfig
from .tiered_conversion_rate_config import TieredConversionRateConfig
from .dimensional_price_configuration import DimensionalPriceConfiguration

__all__ = [
    "Price",
    "UnitPrice",
    "UnitPriceUnnamedTypeWithobjectParent84",
    "PackagePrice",
    "PackagePriceUnnamedTypeWithobjectParent85",
    "MatrixPrice",
    "MatrixPriceUnnamedTypeWithobjectParent86",
    "TieredPrice",
    "TieredPriceUnnamedTypeWithobjectParent87",
    "TieredBPSPrice",
    "TieredBPSPriceUnnamedTypeWithobjectParent88",
    "BPSPrice",
    "BPSPriceUnnamedTypeWithobjectParent89",
    "BulkBPSPrice",
    "BulkBPSPriceUnnamedTypeWithobjectParent90",
    "BulkPrice",
    "BulkPriceUnnamedTypeWithobjectParent91",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceUnnamedTypeWithobjectParent92",
    "TieredPackagePrice",
    "TieredPackagePriceUnnamedTypeWithobjectParent93",
    "GroupedTieredPrice",
    "GroupedTieredPriceUnnamedTypeWithobjectParent94",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceUnnamedTypeWithobjectParent95",
    "TieredPackageWithMinimumPrice",
    "TieredPackageWithMinimumPriceUnnamedTypeWithobjectParent96",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceUnnamedTypeWithobjectParent97",
    "UnitWithPercentPrice",
    "UnitWithPercentPriceUnnamedTypeWithobjectParent98",
    "MatrixWithAllocationPrice",
    "MatrixWithAllocationPriceUnnamedTypeWithobjectParent99",
    "TieredWithProrationPrice",
    "TieredWithProrationPriceUnnamedTypeWithobjectParent100",
    "UnitWithProrationPrice",
    "UnitWithProrationPriceUnnamedTypeWithobjectParent101",
    "GroupedAllocationPrice",
    "GroupedAllocationPriceUnnamedTypeWithobjectParent102",
    "GroupedWithProratedMinimumPrice",
    "GroupedWithProratedMinimumPriceUnnamedTypeWithobjectParent103",
    "GroupedWithMeteredMinimumPrice",
    "GroupedWithMeteredMinimumPriceUnnamedTypeWithobjectParent104",
    "MatrixWithDisplayNamePrice",
    "MatrixWithDisplayNamePriceUnnamedTypeWithobjectParent105",
    "BulkWithProrationPrice",
    "BulkWithProrationPriceUnnamedTypeWithobjectParent106",
    "GroupedTieredPackagePrice",
    "GroupedTieredPackagePriceUnnamedTypeWithobjectParent107",
    "MaxGroupTieredPackagePrice",
    "MaxGroupTieredPackagePriceUnnamedTypeWithobjectParent108",
    "ScalableMatrixWithUnitPricingPrice",
    "ScalableMatrixWithUnitPricingPriceUnnamedTypeWithobjectParent109",
    "ScalableMatrixWithTieredPricingPrice",
    "ScalableMatrixWithTieredPricingPriceUnnamedTypeWithobjectParent110",
    "CumulativeGroupedBulkPrice",
    "CumulativeGroupedBulkPriceUnnamedTypeWithobjectParent111",
    "GroupedWithMinMaxThresholdsPrice",
    "GroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent112",
]

UnitPriceUnnamedTypeWithobjectParent84: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitPriceUnnamedTypeWithobjectParent84] = None

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


PackagePriceUnnamedTypeWithobjectParent85: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[PackagePriceUnnamedTypeWithobjectParent85] = None

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


MatrixPriceUnnamedTypeWithobjectParent86: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixPriceUnnamedTypeWithobjectParent86] = None

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


TieredPriceUnnamedTypeWithobjectParent87: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPriceUnnamedTypeWithobjectParent87] = None

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


TieredBPSPriceUnnamedTypeWithobjectParent88: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredBPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredBPSPriceUnnamedTypeWithobjectParent88] = None

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

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    tiered_bps_config: TieredBPSConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


BPSPriceUnnamedTypeWithobjectParent89: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bps_config: BPSConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BPSPriceUnnamedTypeWithobjectParent89] = None

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

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


BulkBPSPriceUnnamedTypeWithobjectParent90: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkBPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_bps_config: BulkBPSConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkBPSPriceUnnamedTypeWithobjectParent90] = None

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

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    replaces_price_id: Optional[str] = None
    """The price id this price replaces.

    This price will take the place of the replaced price in plan version migrations.
    """

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


BulkPriceUnnamedTypeWithobjectParent91: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_config: BulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkPriceUnnamedTypeWithobjectParent91] = None

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


ThresholdTotalAmountPriceUnnamedTypeWithobjectParent92: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ThresholdTotalAmountPriceUnnamedTypeWithobjectParent92] = None

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


TieredPackagePriceUnnamedTypeWithobjectParent93: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPackagePriceUnnamedTypeWithobjectParent93] = None

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


GroupedTieredPriceUnnamedTypeWithobjectParent94: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPriceUnnamedTypeWithobjectParent94] = None

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


TieredWithMinimumPriceUnnamedTypeWithobjectParent95: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredWithMinimumPriceUnnamedTypeWithobjectParent95] = None

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


TieredPackageWithMinimumPriceUnnamedTypeWithobjectParent96: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredPackageWithMinimumPriceUnnamedTypeWithobjectParent96] = None

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


PackageWithAllocationPriceUnnamedTypeWithobjectParent97: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[PackageWithAllocationPriceUnnamedTypeWithobjectParent97] = None

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


UnitWithPercentPriceUnnamedTypeWithobjectParent98: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitWithPercentPriceUnnamedTypeWithobjectParent98] = None

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


MatrixWithAllocationPriceUnnamedTypeWithobjectParent99: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixWithAllocationPriceUnnamedTypeWithobjectParent99] = None

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


TieredWithProrationPriceUnnamedTypeWithobjectParent100: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredWithProrationPriceUnnamedTypeWithobjectParent100] = None

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


UnitWithProrationPriceUnnamedTypeWithobjectParent101: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[UnitWithProrationPriceUnnamedTypeWithobjectParent101] = None

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


GroupedAllocationPriceUnnamedTypeWithobjectParent102: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedAllocationPriceUnnamedTypeWithobjectParent102] = None

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


GroupedWithProratedMinimumPriceUnnamedTypeWithobjectParent103: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithProratedMinimumPriceUnnamedTypeWithobjectParent103] = None

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


GroupedWithMeteredMinimumPriceUnnamedTypeWithobjectParent104: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMeteredMinimumPriceUnnamedTypeWithobjectParent104] = None

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


MatrixWithDisplayNamePriceUnnamedTypeWithobjectParent105: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MatrixWithDisplayNamePriceUnnamedTypeWithobjectParent105] = None

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


BulkWithProrationPriceUnnamedTypeWithobjectParent106: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_with_proration_config: Dict[str, object]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkWithProrationPriceUnnamedTypeWithobjectParent106] = None

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


GroupedTieredPackagePriceUnnamedTypeWithobjectParent107: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPackagePriceUnnamedTypeWithobjectParent107] = None

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


MaxGroupTieredPackagePriceUnnamedTypeWithobjectParent108: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[MaxGroupTieredPackagePriceUnnamedTypeWithobjectParent108] = None

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


ScalableMatrixWithUnitPricingPriceUnnamedTypeWithobjectParent109: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ScalableMatrixWithUnitPricingPriceUnnamedTypeWithobjectParent109] = None

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


ScalableMatrixWithTieredPricingPriceUnnamedTypeWithobjectParent110: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[ScalableMatrixWithTieredPricingPriceUnnamedTypeWithobjectParent110] = None

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


CumulativeGroupedBulkPriceUnnamedTypeWithobjectParent111: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[CumulativeGroupedBulkPriceUnnamedTypeWithobjectParent111] = None

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


GroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent112: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class GroupedWithMinMaxThresholdsPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent112] = None

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


Price: TypeAlias = Annotated[
    Union[
        UnitPrice,
        PackagePrice,
        MatrixPrice,
        TieredPrice,
        TieredBPSPrice,
        BPSPrice,
        BulkBPSPrice,
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
    ],
    PropertyInfo(discriminator="price_model_type"),
]
