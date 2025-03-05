# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from .discount import Discount
from ..._models import BaseModel
from .maximum_model import MaximumModel
from .minimum_model import MinimumModel
from .item_slim_model import ItemSlimModel
from .allocation_model import AllocationModel
from .bps_config_model import BpsConfigModel
from .bulk_config_model import BulkConfigModel
from .unit_config_model import UnitConfigModel
from .matrix_config_model import MatrixConfigModel
from .tiered_config_model import TieredConfigModel
from .package_config_model import PackageConfigModel
from .bulk_bps_config_model import BulkBpsConfigModel
from .tiered_bps_config_model import TieredBpsConfigModel
from .billable_metric_tiny_model import BillableMetricTinyModel
from .billing_cycle_configuration_model import BillingCycleConfigurationModel
from .custom_rating_function_config_model import CustomRatingFunctionConfigModel
from .matrix_with_allocation_config_model import MatrixWithAllocationConfigModel
from .dimensional_price_configuration_model import DimensionalPriceConfigurationModel

__all__ = [
    "PriceModel",
    "UnitPrice",
    "PackagePrice",
    "MatrixPrice",
    "TieredPrice",
    "TieredBpsPrice",
    "BpsPrice",
    "BulkBpsPrice",
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

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_config: UnitConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str

    package_config: PackageConfigModel

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    matrix_config: MatrixConfigModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_config: TieredConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class TieredBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_bps_config: TieredBpsConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class BpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    bps_config: BpsConfigModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class BulkBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    bulk_bps_config: BulkBpsConfigModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    bulk_config: BulkConfigModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    threshold_total_amount_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_config: CustomRatingFunctionConfigModel

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_minimum_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_with_minimum_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    package_with_allocation_config: CustomRatingFunctionConfigModel

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_percent"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_percent_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    matrix_with_allocation_config: MatrixWithAllocationConfigModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_proration"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_proration_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_proration"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_proration_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_allocation_config: CustomRatingFunctionConfigModel

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_allocation"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_prorated_minimum_config: CustomRatingFunctionConfigModel

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_prorated_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_metered_minimum_config: CustomRatingFunctionConfigModel

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_metered_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    matrix_with_display_name_config: CustomRatingFunctionConfigModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_display_name"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    bulk_with_proration_config: CustomRatingFunctionConfigModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk_with_proration"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_package_config: CustomRatingFunctionConfigModel

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    max_group_tiered_package_config: CustomRatingFunctionConfigModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["max_group_tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["scalable_matrix_with_unit_pricing"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    scalable_matrix_with_unit_pricing_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["scalable_matrix_with_tiered_pricing"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    scalable_matrix_with_tiered_pricing_config: CustomRatingFunctionConfigModel

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTinyModel] = None

    billing_cycle_configuration: BillingCycleConfigurationModel

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[AllocationModel] = None

    cumulative_grouped_bulk_config: CustomRatingFunctionConfigModel

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BillingCycleConfigurationModel] = None

    item: ItemSlimModel

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["cumulative_grouped_bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfigurationModel] = None


PriceModel: TypeAlias = Annotated[
    Union[
        UnitPrice,
        PackagePrice,
        MatrixPrice,
        TieredPrice,
        TieredBpsPrice,
        BpsPrice,
        BulkBpsPrice,
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
