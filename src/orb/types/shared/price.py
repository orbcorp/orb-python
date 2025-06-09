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
from .matrix_with_allocation_config import MatrixWithAllocationConfig
from .dimensional_price_configuration import DimensionalPriceConfiguration

__all__ = [
    "Price",
    "UnitPrice",
    "PackagePrice",
    "MatrixPrice",
    "TieredPrice",
    "TieredBPSPrice",
    "BPSPrice",
    "BulkBPSPrice",
    "BulkPrice",
    "ThresholdTotalAmountPrice",
    "TieredPackagePrice",
    "GroupedTieredPrice",
    "TieredWithMinimumPrice",
    "TieredPackageWithMinimumPrice",
    "PackageWithAllocationPrice",
    "UnitWithPercentPrice",
    "MatrixWithAllocationPrice",
    "TieredWithProrationPrice",
    "UnitWithProrationPrice",
    "GroupedAllocationPrice",
    "GroupedWithProratedMinimumPrice",
    "GroupedWithMeteredMinimumPrice",
    "MatrixWithDisplayNamePrice",
    "BulkWithProrationPrice",
    "GroupedTieredPackagePrice",
    "MaxGroupTieredPackagePrice",
    "ScalableMatrixWithUnitPricingPrice",
    "ScalableMatrixWithTieredPricingPrice",
    "CumulativeGroupedBulkPrice",
]


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    unit_config: UnitConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    tiered_config: TieredConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredBPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    tiered_bps_config: TieredBPSConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class BPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bps_config: BPSConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class BulkBPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_bps_config: BulkBPSConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_config: BulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    threshold_total_amount_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    tiered_package_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    tiered_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    tiered_package_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    unit_with_percent_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    tiered_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    unit_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_with_proration_config: Dict[str, object]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    scalable_matrix_with_unit_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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

    scalable_matrix_with_tiered_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

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
    ],
    PropertyInfo(discriminator="price_model_type"),
]
