# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.discount import Discount

__all__ = [
    "Price",
    "UnitPrice",
    "UnitPriceBillableMetric",
    "UnitPriceBillingCycleConfiguration",
    "UnitPriceCreditAllocation",
    "UnitPriceCreditAllocationCustomExpiration",
    "UnitPriceInvoicingCycleConfiguration",
    "UnitPriceItem",
    "UnitPriceMaximum",
    "UnitPriceMaximumFilter",
    "UnitPriceMinimum",
    "UnitPriceMinimumFilter",
    "UnitPriceUnitConfig",
    "UnitPriceDimensionalPriceConfiguration",
    "PackagePrice",
    "PackagePriceBillableMetric",
    "PackagePriceBillingCycleConfiguration",
    "PackagePriceCreditAllocation",
    "PackagePriceCreditAllocationCustomExpiration",
    "PackagePriceInvoicingCycleConfiguration",
    "PackagePriceItem",
    "PackagePriceMaximum",
    "PackagePriceMaximumFilter",
    "PackagePriceMinimum",
    "PackagePriceMinimumFilter",
    "PackagePricePackageConfig",
    "PackagePriceDimensionalPriceConfiguration",
    "MatrixPrice",
    "MatrixPriceBillableMetric",
    "MatrixPriceBillingCycleConfiguration",
    "MatrixPriceCreditAllocation",
    "MatrixPriceCreditAllocationCustomExpiration",
    "MatrixPriceInvoicingCycleConfiguration",
    "MatrixPriceItem",
    "MatrixPriceMatrixConfig",
    "MatrixPriceMatrixConfigMatrixValue",
    "MatrixPriceMaximum",
    "MatrixPriceMaximumFilter",
    "MatrixPriceMinimum",
    "MatrixPriceMinimumFilter",
    "MatrixPriceDimensionalPriceConfiguration",
    "TieredPrice",
    "TieredPriceBillableMetric",
    "TieredPriceBillingCycleConfiguration",
    "TieredPriceCreditAllocation",
    "TieredPriceCreditAllocationCustomExpiration",
    "TieredPriceInvoicingCycleConfiguration",
    "TieredPriceItem",
    "TieredPriceMaximum",
    "TieredPriceMaximumFilter",
    "TieredPriceMinimum",
    "TieredPriceMinimumFilter",
    "TieredPriceTieredConfig",
    "TieredPriceTieredConfigTier",
    "TieredPriceDimensionalPriceConfiguration",
    "TieredBpsPrice",
    "TieredBpsPriceBillableMetric",
    "TieredBpsPriceBillingCycleConfiguration",
    "TieredBpsPriceCreditAllocation",
    "TieredBpsPriceCreditAllocationCustomExpiration",
    "TieredBpsPriceInvoicingCycleConfiguration",
    "TieredBpsPriceItem",
    "TieredBpsPriceMaximum",
    "TieredBpsPriceMaximumFilter",
    "TieredBpsPriceMinimum",
    "TieredBpsPriceMinimumFilter",
    "TieredBpsPriceTieredBpsConfig",
    "TieredBpsPriceTieredBpsConfigTier",
    "TieredBpsPriceDimensionalPriceConfiguration",
    "BpsPrice",
    "BpsPriceBillableMetric",
    "BpsPriceBillingCycleConfiguration",
    "BpsPriceBpsConfig",
    "BpsPriceCreditAllocation",
    "BpsPriceCreditAllocationCustomExpiration",
    "BpsPriceInvoicingCycleConfiguration",
    "BpsPriceItem",
    "BpsPriceMaximum",
    "BpsPriceMaximumFilter",
    "BpsPriceMinimum",
    "BpsPriceMinimumFilter",
    "BpsPriceDimensionalPriceConfiguration",
    "BulkBpsPrice",
    "BulkBpsPriceBillableMetric",
    "BulkBpsPriceBillingCycleConfiguration",
    "BulkBpsPriceBulkBpsConfig",
    "BulkBpsPriceBulkBpsConfigTier",
    "BulkBpsPriceCreditAllocation",
    "BulkBpsPriceCreditAllocationCustomExpiration",
    "BulkBpsPriceInvoicingCycleConfiguration",
    "BulkBpsPriceItem",
    "BulkBpsPriceMaximum",
    "BulkBpsPriceMaximumFilter",
    "BulkBpsPriceMinimum",
    "BulkBpsPriceMinimumFilter",
    "BulkBpsPriceDimensionalPriceConfiguration",
    "BulkPrice",
    "BulkPriceBillableMetric",
    "BulkPriceBillingCycleConfiguration",
    "BulkPriceBulkConfig",
    "BulkPriceBulkConfigTier",
    "BulkPriceCreditAllocation",
    "BulkPriceCreditAllocationCustomExpiration",
    "BulkPriceInvoicingCycleConfiguration",
    "BulkPriceItem",
    "BulkPriceMaximum",
    "BulkPriceMaximumFilter",
    "BulkPriceMinimum",
    "BulkPriceMinimumFilter",
    "BulkPriceDimensionalPriceConfiguration",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceBillableMetric",
    "ThresholdTotalAmountPriceBillingCycleConfiguration",
    "ThresholdTotalAmountPriceCreditAllocation",
    "ThresholdTotalAmountPriceCreditAllocationCustomExpiration",
    "ThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "ThresholdTotalAmountPriceItem",
    "ThresholdTotalAmountPriceMaximum",
    "ThresholdTotalAmountPriceMaximumFilter",
    "ThresholdTotalAmountPriceMinimum",
    "ThresholdTotalAmountPriceMinimumFilter",
    "ThresholdTotalAmountPriceDimensionalPriceConfiguration",
    "TieredPackagePrice",
    "TieredPackagePriceBillableMetric",
    "TieredPackagePriceBillingCycleConfiguration",
    "TieredPackagePriceCreditAllocation",
    "TieredPackagePriceCreditAllocationCustomExpiration",
    "TieredPackagePriceInvoicingCycleConfiguration",
    "TieredPackagePriceItem",
    "TieredPackagePriceMaximum",
    "TieredPackagePriceMaximumFilter",
    "TieredPackagePriceMinimum",
    "TieredPackagePriceMinimumFilter",
    "TieredPackagePriceDimensionalPriceConfiguration",
    "GroupedTieredPrice",
    "GroupedTieredPriceBillableMetric",
    "GroupedTieredPriceBillingCycleConfiguration",
    "GroupedTieredPriceCreditAllocation",
    "GroupedTieredPriceCreditAllocationCustomExpiration",
    "GroupedTieredPriceInvoicingCycleConfiguration",
    "GroupedTieredPriceItem",
    "GroupedTieredPriceMaximum",
    "GroupedTieredPriceMaximumFilter",
    "GroupedTieredPriceMinimum",
    "GroupedTieredPriceMinimumFilter",
    "GroupedTieredPriceDimensionalPriceConfiguration",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceBillableMetric",
    "TieredWithMinimumPriceBillingCycleConfiguration",
    "TieredWithMinimumPriceCreditAllocation",
    "TieredWithMinimumPriceCreditAllocationCustomExpiration",
    "TieredWithMinimumPriceInvoicingCycleConfiguration",
    "TieredWithMinimumPriceItem",
    "TieredWithMinimumPriceMaximum",
    "TieredWithMinimumPriceMaximumFilter",
    "TieredWithMinimumPriceMinimum",
    "TieredWithMinimumPriceMinimumFilter",
    "TieredWithMinimumPriceDimensionalPriceConfiguration",
    "TieredPackageWithMinimumPrice",
    "TieredPackageWithMinimumPriceBillableMetric",
    "TieredPackageWithMinimumPriceBillingCycleConfiguration",
    "TieredPackageWithMinimumPriceCreditAllocation",
    "TieredPackageWithMinimumPriceCreditAllocationCustomExpiration",
    "TieredPackageWithMinimumPriceInvoicingCycleConfiguration",
    "TieredPackageWithMinimumPriceItem",
    "TieredPackageWithMinimumPriceMaximum",
    "TieredPackageWithMinimumPriceMaximumFilter",
    "TieredPackageWithMinimumPriceMinimum",
    "TieredPackageWithMinimumPriceMinimumFilter",
    "TieredPackageWithMinimumPriceDimensionalPriceConfiguration",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceBillableMetric",
    "PackageWithAllocationPriceBillingCycleConfiguration",
    "PackageWithAllocationPriceCreditAllocation",
    "PackageWithAllocationPriceCreditAllocationCustomExpiration",
    "PackageWithAllocationPriceInvoicingCycleConfiguration",
    "PackageWithAllocationPriceItem",
    "PackageWithAllocationPriceMaximum",
    "PackageWithAllocationPriceMaximumFilter",
    "PackageWithAllocationPriceMinimum",
    "PackageWithAllocationPriceMinimumFilter",
    "PackageWithAllocationPriceDimensionalPriceConfiguration",
    "UnitWithPercentPrice",
    "UnitWithPercentPriceBillableMetric",
    "UnitWithPercentPriceBillingCycleConfiguration",
    "UnitWithPercentPriceCreditAllocation",
    "UnitWithPercentPriceCreditAllocationCustomExpiration",
    "UnitWithPercentPriceInvoicingCycleConfiguration",
    "UnitWithPercentPriceItem",
    "UnitWithPercentPriceMaximum",
    "UnitWithPercentPriceMaximumFilter",
    "UnitWithPercentPriceMinimum",
    "UnitWithPercentPriceMinimumFilter",
    "UnitWithPercentPriceDimensionalPriceConfiguration",
    "MatrixWithAllocationPrice",
    "MatrixWithAllocationPriceBillableMetric",
    "MatrixWithAllocationPriceBillingCycleConfiguration",
    "MatrixWithAllocationPriceCreditAllocation",
    "MatrixWithAllocationPriceCreditAllocationCustomExpiration",
    "MatrixWithAllocationPriceInvoicingCycleConfiguration",
    "MatrixWithAllocationPriceItem",
    "MatrixWithAllocationPriceMatrixWithAllocationConfig",
    "MatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue",
    "MatrixWithAllocationPriceMaximum",
    "MatrixWithAllocationPriceMaximumFilter",
    "MatrixWithAllocationPriceMinimum",
    "MatrixWithAllocationPriceMinimumFilter",
    "MatrixWithAllocationPriceDimensionalPriceConfiguration",
    "TieredWithProrationPrice",
    "TieredWithProrationPriceBillableMetric",
    "TieredWithProrationPriceBillingCycleConfiguration",
    "TieredWithProrationPriceCreditAllocation",
    "TieredWithProrationPriceCreditAllocationCustomExpiration",
    "TieredWithProrationPriceInvoicingCycleConfiguration",
    "TieredWithProrationPriceItem",
    "TieredWithProrationPriceMaximum",
    "TieredWithProrationPriceMaximumFilter",
    "TieredWithProrationPriceMinimum",
    "TieredWithProrationPriceMinimumFilter",
    "TieredWithProrationPriceDimensionalPriceConfiguration",
    "UnitWithProrationPrice",
    "UnitWithProrationPriceBillableMetric",
    "UnitWithProrationPriceBillingCycleConfiguration",
    "UnitWithProrationPriceCreditAllocation",
    "UnitWithProrationPriceCreditAllocationCustomExpiration",
    "UnitWithProrationPriceInvoicingCycleConfiguration",
    "UnitWithProrationPriceItem",
    "UnitWithProrationPriceMaximum",
    "UnitWithProrationPriceMaximumFilter",
    "UnitWithProrationPriceMinimum",
    "UnitWithProrationPriceMinimumFilter",
    "UnitWithProrationPriceDimensionalPriceConfiguration",
    "GroupedAllocationPrice",
    "GroupedAllocationPriceBillableMetric",
    "GroupedAllocationPriceBillingCycleConfiguration",
    "GroupedAllocationPriceCreditAllocation",
    "GroupedAllocationPriceCreditAllocationCustomExpiration",
    "GroupedAllocationPriceInvoicingCycleConfiguration",
    "GroupedAllocationPriceItem",
    "GroupedAllocationPriceMaximum",
    "GroupedAllocationPriceMaximumFilter",
    "GroupedAllocationPriceMinimum",
    "GroupedAllocationPriceMinimumFilter",
    "GroupedAllocationPriceDimensionalPriceConfiguration",
    "GroupedWithProratedMinimumPrice",
    "GroupedWithProratedMinimumPriceBillableMetric",
    "GroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "GroupedWithProratedMinimumPriceCreditAllocation",
    "GroupedWithProratedMinimumPriceCreditAllocationCustomExpiration",
    "GroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "GroupedWithProratedMinimumPriceItem",
    "GroupedWithProratedMinimumPriceMaximum",
    "GroupedWithProratedMinimumPriceMaximumFilter",
    "GroupedWithProratedMinimumPriceMinimum",
    "GroupedWithProratedMinimumPriceMinimumFilter",
    "GroupedWithProratedMinimumPriceDimensionalPriceConfiguration",
    "GroupedWithMeteredMinimumPrice",
    "GroupedWithMeteredMinimumPriceBillableMetric",
    "GroupedWithMeteredMinimumPriceBillingCycleConfiguration",
    "GroupedWithMeteredMinimumPriceCreditAllocation",
    "GroupedWithMeteredMinimumPriceCreditAllocationCustomExpiration",
    "GroupedWithMeteredMinimumPriceInvoicingCycleConfiguration",
    "GroupedWithMeteredMinimumPriceItem",
    "GroupedWithMeteredMinimumPriceMaximum",
    "GroupedWithMeteredMinimumPriceMaximumFilter",
    "GroupedWithMeteredMinimumPriceMinimum",
    "GroupedWithMeteredMinimumPriceMinimumFilter",
    "GroupedWithMeteredMinimumPriceDimensionalPriceConfiguration",
    "MatrixWithDisplayNamePrice",
    "MatrixWithDisplayNamePriceBillableMetric",
    "MatrixWithDisplayNamePriceBillingCycleConfiguration",
    "MatrixWithDisplayNamePriceCreditAllocation",
    "MatrixWithDisplayNamePriceCreditAllocationCustomExpiration",
    "MatrixWithDisplayNamePriceInvoicingCycleConfiguration",
    "MatrixWithDisplayNamePriceItem",
    "MatrixWithDisplayNamePriceMaximum",
    "MatrixWithDisplayNamePriceMaximumFilter",
    "MatrixWithDisplayNamePriceMinimum",
    "MatrixWithDisplayNamePriceMinimumFilter",
    "MatrixWithDisplayNamePriceDimensionalPriceConfiguration",
    "BulkWithProrationPrice",
    "BulkWithProrationPriceBillableMetric",
    "BulkWithProrationPriceBillingCycleConfiguration",
    "BulkWithProrationPriceCreditAllocation",
    "BulkWithProrationPriceCreditAllocationCustomExpiration",
    "BulkWithProrationPriceInvoicingCycleConfiguration",
    "BulkWithProrationPriceItem",
    "BulkWithProrationPriceMaximum",
    "BulkWithProrationPriceMaximumFilter",
    "BulkWithProrationPriceMinimum",
    "BulkWithProrationPriceMinimumFilter",
    "BulkWithProrationPriceDimensionalPriceConfiguration",
    "GroupedTieredPackagePrice",
    "GroupedTieredPackagePriceBillableMetric",
    "GroupedTieredPackagePriceBillingCycleConfiguration",
    "GroupedTieredPackagePriceCreditAllocation",
    "GroupedTieredPackagePriceCreditAllocationCustomExpiration",
    "GroupedTieredPackagePriceInvoicingCycleConfiguration",
    "GroupedTieredPackagePriceItem",
    "GroupedTieredPackagePriceMaximum",
    "GroupedTieredPackagePriceMaximumFilter",
    "GroupedTieredPackagePriceMinimum",
    "GroupedTieredPackagePriceMinimumFilter",
    "GroupedTieredPackagePriceDimensionalPriceConfiguration",
    "MaxGroupTieredPackagePrice",
    "MaxGroupTieredPackagePriceBillableMetric",
    "MaxGroupTieredPackagePriceBillingCycleConfiguration",
    "MaxGroupTieredPackagePriceCreditAllocation",
    "MaxGroupTieredPackagePriceCreditAllocationCustomExpiration",
    "MaxGroupTieredPackagePriceInvoicingCycleConfiguration",
    "MaxGroupTieredPackagePriceItem",
    "MaxGroupTieredPackagePriceMaximum",
    "MaxGroupTieredPackagePriceMaximumFilter",
    "MaxGroupTieredPackagePriceMinimum",
    "MaxGroupTieredPackagePriceMinimumFilter",
    "MaxGroupTieredPackagePriceDimensionalPriceConfiguration",
    "ScalableMatrixWithUnitPricingPrice",
    "ScalableMatrixWithUnitPricingPriceBillableMetric",
    "ScalableMatrixWithUnitPricingPriceBillingCycleConfiguration",
    "ScalableMatrixWithUnitPricingPriceCreditAllocation",
    "ScalableMatrixWithUnitPricingPriceCreditAllocationCustomExpiration",
    "ScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration",
    "ScalableMatrixWithUnitPricingPriceItem",
    "ScalableMatrixWithUnitPricingPriceMaximum",
    "ScalableMatrixWithUnitPricingPriceMaximumFilter",
    "ScalableMatrixWithUnitPricingPriceMinimum",
    "ScalableMatrixWithUnitPricingPriceMinimumFilter",
    "ScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration",
    "ScalableMatrixWithTieredPricingPrice",
    "ScalableMatrixWithTieredPricingPriceBillableMetric",
    "ScalableMatrixWithTieredPricingPriceBillingCycleConfiguration",
    "ScalableMatrixWithTieredPricingPriceCreditAllocation",
    "ScalableMatrixWithTieredPricingPriceCreditAllocationCustomExpiration",
    "ScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration",
    "ScalableMatrixWithTieredPricingPriceItem",
    "ScalableMatrixWithTieredPricingPriceMaximum",
    "ScalableMatrixWithTieredPricingPriceMaximumFilter",
    "ScalableMatrixWithTieredPricingPriceMinimum",
    "ScalableMatrixWithTieredPricingPriceMinimumFilter",
    "ScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration",
    "CumulativeGroupedBulkPrice",
    "CumulativeGroupedBulkPriceBillableMetric",
    "CumulativeGroupedBulkPriceBillingCycleConfiguration",
    "CumulativeGroupedBulkPriceCreditAllocation",
    "CumulativeGroupedBulkPriceCreditAllocationCustomExpiration",
    "CumulativeGroupedBulkPriceInvoicingCycleConfiguration",
    "CumulativeGroupedBulkPriceItem",
    "CumulativeGroupedBulkPriceMaximum",
    "CumulativeGroupedBulkPriceMaximumFilter",
    "CumulativeGroupedBulkPriceMinimum",
    "CumulativeGroupedBulkPriceMinimumFilter",
    "CumulativeGroupedBulkPriceDimensionalPriceConfiguration",
]


class UnitPriceBillableMetric(BaseModel):
    id: str


class UnitPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[UnitPriceCreditAllocationCustomExpiration] = None


class UnitPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitPriceItem(BaseModel):
    id: str

    name: str


class UnitPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class UnitPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[UnitPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class UnitPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class UnitPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[UnitPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class UnitPriceUnitConfig(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""


class UnitPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitPriceBillableMetric] = None

    billing_cycle_configuration: UnitPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[UnitPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[UnitPriceInvoicingCycleConfiguration] = None

    item: UnitPriceItem

    maximum: Optional[UnitPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[UnitPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_config: UnitPriceUnitConfig

    dimensional_price_configuration: Optional[UnitPriceDimensionalPriceConfiguration] = None


class PackagePriceBillableMetric(BaseModel):
    id: str


class PackagePriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class PackagePriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class PackagePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[PackagePriceCreditAllocationCustomExpiration] = None


class PackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class PackagePriceItem(BaseModel):
    id: str

    name: str


class PackagePriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PackagePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[PackagePriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class PackagePriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PackagePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[PackagePriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class PackagePricePackageConfig(BaseModel):
    package_amount: str
    """A currency amount to rate usage by"""

    package_size: int
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class PackagePriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[PackagePriceBillableMetric] = None

    billing_cycle_configuration: PackagePriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[PackagePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[PackagePriceInvoicingCycleConfiguration] = None

    item: PackagePriceItem

    maximum: Optional[PackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[PackagePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str

    package_config: PackagePricePackageConfig

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[PackagePriceDimensionalPriceConfiguration] = None


class MatrixPriceBillableMetric(BaseModel):
    id: str


class MatrixPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[MatrixPriceCreditAllocationCustomExpiration] = None


class MatrixPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixPriceItem(BaseModel):
    id: str

    name: str


class MatrixPriceMatrixConfigMatrixValue(BaseModel):
    dimension_values: List[Optional[str]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: str
    """Unit price for the specified dimension_values"""


class MatrixPriceMatrixConfig(BaseModel):
    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[MatrixPriceMatrixConfigMatrixValue]
    """Matrix values for specified matrix grouping keys"""


class MatrixPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MatrixPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MatrixPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MatrixPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MatrixPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MatrixPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class MatrixPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[MatrixPriceBillableMetric] = None

    billing_cycle_configuration: MatrixPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[MatrixPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[MatrixPriceInvoicingCycleConfiguration] = None

    item: MatrixPriceItem

    matrix_config: MatrixPriceMatrixConfig

    maximum: Optional[MatrixPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MatrixPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[MatrixPriceDimensionalPriceConfiguration] = None


class TieredPriceBillableMetric(BaseModel):
    id: str


class TieredPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[TieredPriceCreditAllocationCustomExpiration] = None


class TieredPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPriceItem(BaseModel):
    id: str

    name: str


class TieredPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[TieredPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class TieredPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TieredPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class TieredPriceTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredPriceTieredConfig(BaseModel):
    tiers: List[TieredPriceTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPriceBillableMetric] = None

    billing_cycle_configuration: TieredPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[TieredPriceInvoicingCycleConfiguration] = None

    item: TieredPriceItem

    maximum: Optional[TieredPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[TieredPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_config: TieredPriceTieredConfig

    dimensional_price_configuration: Optional[TieredPriceDimensionalPriceConfiguration] = None


class TieredBpsPriceBillableMetric(BaseModel):
    id: str


class TieredBpsPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredBpsPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredBpsPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[TieredBpsPriceCreditAllocationCustomExpiration] = None


class TieredBpsPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredBpsPriceItem(BaseModel):
    id: str

    name: str


class TieredBpsPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredBpsPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[TieredBpsPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class TieredBpsPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredBpsPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TieredBpsPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class TieredBpsPriceTieredBpsConfigTier(BaseModel):
    bps: float
    """Per-event basis point rate"""

    minimum_amount: str
    """Exclusive tier starting value"""

    maximum_amount: Optional[str] = None
    """Inclusive tier ending value"""

    per_unit_maximum: Optional[str] = None
    """Per unit maximum to charge"""


class TieredBpsPriceTieredBpsConfig(BaseModel):
    tiers: List[TieredBpsPriceTieredBpsConfigTier]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class TieredBpsPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class TieredBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredBpsPriceBillableMetric] = None

    billing_cycle_configuration: TieredBpsPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredBpsPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[TieredBpsPriceInvoicingCycleConfiguration] = None

    item: TieredBpsPriceItem

    maximum: Optional[TieredBpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[TieredBpsPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_bps_config: TieredBpsPriceTieredBpsConfig

    dimensional_price_configuration: Optional[TieredBpsPriceDimensionalPriceConfiguration] = None


class BpsPriceBillableMetric(BaseModel):
    id: str


class BpsPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BpsPriceBpsConfig(BaseModel):
    bps: float
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str] = None
    """Optional currency amount maximum to cap spend per event"""


class BpsPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BpsPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[BpsPriceCreditAllocationCustomExpiration] = None


class BpsPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BpsPriceItem(BaseModel):
    id: str

    name: str


class BpsPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BpsPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[BpsPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class BpsPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BpsPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[BpsPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class BpsPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class BpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BpsPriceBillableMetric] = None

    billing_cycle_configuration: BpsPriceBillingCycleConfiguration

    bps_config: BpsPriceBpsConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BpsPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BpsPriceInvoicingCycleConfiguration] = None

    item: BpsPriceItem

    maximum: Optional[BpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[BpsPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[BpsPriceDimensionalPriceConfiguration] = None


class BulkBpsPriceBillableMetric(BaseModel):
    id: str


class BulkBpsPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkBpsPriceBulkBpsConfigTier(BaseModel):
    bps: float
    """Basis points to rate on"""

    maximum_amount: Optional[str] = None
    """Upper bound for tier"""

    per_unit_maximum: Optional[str] = None
    """The maximum amount to charge for any one event"""


class BulkBpsPriceBulkBpsConfig(BaseModel):
    tiers: List[BulkBpsPriceBulkBpsConfigTier]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class BulkBpsPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkBpsPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[BulkBpsPriceCreditAllocationCustomExpiration] = None


class BulkBpsPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkBpsPriceItem(BaseModel):
    id: str

    name: str


class BulkBpsPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BulkBpsPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[BulkBpsPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class BulkBpsPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BulkBpsPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[BulkBpsPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class BulkBpsPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class BulkBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BulkBpsPriceBillableMetric] = None

    billing_cycle_configuration: BulkBpsPriceBillingCycleConfiguration

    bulk_bps_config: BulkBpsPriceBulkBpsConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BulkBpsPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BulkBpsPriceInvoicingCycleConfiguration] = None

    item: BulkBpsPriceItem

    maximum: Optional[BulkBpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[BulkBpsPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[BulkBpsPriceDimensionalPriceConfiguration] = None


class BulkPriceBillableMetric(BaseModel):
    id: str


class BulkPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkPriceBulkConfigTier(BaseModel):
    unit_amount: str
    """Amount per unit"""

    maximum_units: Optional[float] = None
    """Upper bound for this tier"""


class BulkPriceBulkConfig(BaseModel):
    tiers: List[BulkPriceBulkConfigTier]
    """Bulk tiers for rating based on total usage volume"""


class BulkPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[BulkPriceCreditAllocationCustomExpiration] = None


class BulkPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkPriceItem(BaseModel):
    id: str

    name: str


class BulkPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BulkPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[BulkPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class BulkPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BulkPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[BulkPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class BulkPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BulkPriceBillableMetric] = None

    billing_cycle_configuration: BulkPriceBillingCycleConfiguration

    bulk_config: BulkPriceBulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BulkPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BulkPriceInvoicingCycleConfiguration] = None

    item: BulkPriceItem

    maximum: Optional[BulkPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[BulkPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[BulkPriceDimensionalPriceConfiguration] = None


class ThresholdTotalAmountPriceBillableMetric(BaseModel):
    id: str


class ThresholdTotalAmountPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ThresholdTotalAmountPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ThresholdTotalAmountPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[ThresholdTotalAmountPriceCreditAllocationCustomExpiration] = None


class ThresholdTotalAmountPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ThresholdTotalAmountPriceItem(BaseModel):
    id: str

    name: str


class ThresholdTotalAmountPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class ThresholdTotalAmountPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[ThresholdTotalAmountPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class ThresholdTotalAmountPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class ThresholdTotalAmountPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[ThresholdTotalAmountPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class ThresholdTotalAmountPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[ThresholdTotalAmountPriceBillableMetric] = None

    billing_cycle_configuration: ThresholdTotalAmountPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[ThresholdTotalAmountPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[ThresholdTotalAmountPriceInvoicingCycleConfiguration] = None

    item: ThresholdTotalAmountPriceItem

    maximum: Optional[ThresholdTotalAmountPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[ThresholdTotalAmountPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    threshold_total_amount_config: Dict[str, object]

    dimensional_price_configuration: Optional[ThresholdTotalAmountPriceDimensionalPriceConfiguration] = None


class TieredPackagePriceBillableMetric(BaseModel):
    id: str


class TieredPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPackagePriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPackagePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[TieredPackagePriceCreditAllocationCustomExpiration] = None


class TieredPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPackagePriceItem(BaseModel):
    id: str

    name: str


class TieredPackagePriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPackagePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[TieredPackagePriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class TieredPackagePriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPackagePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TieredPackagePriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class TieredPackagePriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPackagePriceBillableMetric] = None

    billing_cycle_configuration: TieredPackagePriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredPackagePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[TieredPackagePriceInvoicingCycleConfiguration] = None

    item: TieredPackagePriceItem

    maximum: Optional[TieredPackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[TieredPackagePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_config: Dict[str, object]

    dimensional_price_configuration: Optional[TieredPackagePriceDimensionalPriceConfiguration] = None


class GroupedTieredPriceBillableMetric(BaseModel):
    id: str


class GroupedTieredPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedTieredPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedTieredPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[GroupedTieredPriceCreditAllocationCustomExpiration] = None


class GroupedTieredPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedTieredPriceItem(BaseModel):
    id: str

    name: str


class GroupedTieredPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedTieredPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[GroupedTieredPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class GroupedTieredPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedTieredPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[GroupedTieredPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class GroupedTieredPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[GroupedTieredPriceBillableMetric] = None

    billing_cycle_configuration: GroupedTieredPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[GroupedTieredPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_config: Dict[str, object]

    invoicing_cycle_configuration: Optional[GroupedTieredPriceInvoicingCycleConfiguration] = None

    item: GroupedTieredPriceItem

    maximum: Optional[GroupedTieredPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[GroupedTieredPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[GroupedTieredPriceDimensionalPriceConfiguration] = None


class TieredWithMinimumPriceBillableMetric(BaseModel):
    id: str


class TieredWithMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredWithMinimumPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredWithMinimumPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[TieredWithMinimumPriceCreditAllocationCustomExpiration] = None


class TieredWithMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredWithMinimumPriceItem(BaseModel):
    id: str

    name: str


class TieredWithMinimumPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredWithMinimumPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[TieredWithMinimumPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class TieredWithMinimumPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredWithMinimumPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TieredWithMinimumPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class TieredWithMinimumPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredWithMinimumPriceBillableMetric] = None

    billing_cycle_configuration: TieredWithMinimumPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredWithMinimumPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[TieredWithMinimumPriceInvoicingCycleConfiguration] = None

    item: TieredWithMinimumPriceItem

    maximum: Optional[TieredWithMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[TieredWithMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[TieredWithMinimumPriceDimensionalPriceConfiguration] = None


class TieredPackageWithMinimumPriceBillableMetric(BaseModel):
    id: str


class TieredPackageWithMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPackageWithMinimumPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPackageWithMinimumPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[TieredPackageWithMinimumPriceCreditAllocationCustomExpiration] = None


class TieredPackageWithMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredPackageWithMinimumPriceItem(BaseModel):
    id: str

    name: str


class TieredPackageWithMinimumPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPackageWithMinimumPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[TieredPackageWithMinimumPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class TieredPackageWithMinimumPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredPackageWithMinimumPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TieredPackageWithMinimumPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class TieredPackageWithMinimumPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPackageWithMinimumPriceBillableMetric] = None

    billing_cycle_configuration: TieredPackageWithMinimumPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredPackageWithMinimumPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[TieredPackageWithMinimumPriceInvoicingCycleConfiguration] = None

    item: TieredPackageWithMinimumPriceItem

    maximum: Optional[TieredPackageWithMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[TieredPackageWithMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[TieredPackageWithMinimumPriceDimensionalPriceConfiguration] = None


class PackageWithAllocationPriceBillableMetric(BaseModel):
    id: str


class PackageWithAllocationPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class PackageWithAllocationPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class PackageWithAllocationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[PackageWithAllocationPriceCreditAllocationCustomExpiration] = None


class PackageWithAllocationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class PackageWithAllocationPriceItem(BaseModel):
    id: str

    name: str


class PackageWithAllocationPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PackageWithAllocationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[PackageWithAllocationPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class PackageWithAllocationPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PackageWithAllocationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[PackageWithAllocationPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class PackageWithAllocationPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[PackageWithAllocationPriceBillableMetric] = None

    billing_cycle_configuration: PackageWithAllocationPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[PackageWithAllocationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[PackageWithAllocationPriceInvoicingCycleConfiguration] = None

    item: PackageWithAllocationPriceItem

    maximum: Optional[PackageWithAllocationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[PackageWithAllocationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    package_with_allocation_config: Dict[str, object]

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[PackageWithAllocationPriceDimensionalPriceConfiguration] = None


class UnitWithPercentPriceBillableMetric(BaseModel):
    id: str


class UnitWithPercentPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitWithPercentPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitWithPercentPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[UnitWithPercentPriceCreditAllocationCustomExpiration] = None


class UnitWithPercentPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitWithPercentPriceItem(BaseModel):
    id: str

    name: str


class UnitWithPercentPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class UnitWithPercentPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[UnitWithPercentPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class UnitWithPercentPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class UnitWithPercentPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[UnitWithPercentPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class UnitWithPercentPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitWithPercentPriceBillableMetric] = None

    billing_cycle_configuration: UnitWithPercentPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[UnitWithPercentPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[UnitWithPercentPriceInvoicingCycleConfiguration] = None

    item: UnitWithPercentPriceItem

    maximum: Optional[UnitWithPercentPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[UnitWithPercentPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_percent"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_percent_config: Dict[str, object]

    dimensional_price_configuration: Optional[UnitWithPercentPriceDimensionalPriceConfiguration] = None


class MatrixWithAllocationPriceBillableMetric(BaseModel):
    id: str


class MatrixWithAllocationPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixWithAllocationPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixWithAllocationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[MatrixWithAllocationPriceCreditAllocationCustomExpiration] = None


class MatrixWithAllocationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixWithAllocationPriceItem(BaseModel):
    id: str

    name: str


class MatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue(BaseModel):
    dimension_values: List[Optional[str]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: str
    """Unit price for the specified dimension_values"""


class MatrixWithAllocationPriceMatrixWithAllocationConfig(BaseModel):
    allocation: float
    """Allocation to be used to calculate the price"""

    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[MatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue]
    """Matrix values for specified matrix grouping keys"""


class MatrixWithAllocationPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MatrixWithAllocationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MatrixWithAllocationPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MatrixWithAllocationPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MatrixWithAllocationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MatrixWithAllocationPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class MatrixWithAllocationPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[MatrixWithAllocationPriceBillableMetric] = None

    billing_cycle_configuration: MatrixWithAllocationPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[MatrixWithAllocationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[MatrixWithAllocationPriceInvoicingCycleConfiguration] = None

    item: MatrixWithAllocationPriceItem

    matrix_with_allocation_config: MatrixWithAllocationPriceMatrixWithAllocationConfig

    maximum: Optional[MatrixWithAllocationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MatrixWithAllocationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[MatrixWithAllocationPriceDimensionalPriceConfiguration] = None


class TieredWithProrationPriceBillableMetric(BaseModel):
    id: str


class TieredWithProrationPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredWithProrationPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredWithProrationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[TieredWithProrationPriceCreditAllocationCustomExpiration] = None


class TieredWithProrationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class TieredWithProrationPriceItem(BaseModel):
    id: str

    name: str


class TieredWithProrationPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredWithProrationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[TieredWithProrationPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class TieredWithProrationPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class TieredWithProrationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[TieredWithProrationPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class TieredWithProrationPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredWithProrationPriceBillableMetric] = None

    billing_cycle_configuration: TieredWithProrationPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredWithProrationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[TieredWithProrationPriceInvoicingCycleConfiguration] = None

    item: TieredWithProrationPriceItem

    maximum: Optional[TieredWithProrationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[TieredWithProrationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_proration"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[TieredWithProrationPriceDimensionalPriceConfiguration] = None


class UnitWithProrationPriceBillableMetric(BaseModel):
    id: str


class UnitWithProrationPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitWithProrationPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitWithProrationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[UnitWithProrationPriceCreditAllocationCustomExpiration] = None


class UnitWithProrationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class UnitWithProrationPriceItem(BaseModel):
    id: str

    name: str


class UnitWithProrationPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class UnitWithProrationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[UnitWithProrationPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class UnitWithProrationPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class UnitWithProrationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[UnitWithProrationPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class UnitWithProrationPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitWithProrationPriceBillableMetric] = None

    billing_cycle_configuration: UnitWithProrationPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[UnitWithProrationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[UnitWithProrationPriceInvoicingCycleConfiguration] = None

    item: UnitWithProrationPriceItem

    maximum: Optional[UnitWithProrationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[UnitWithProrationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_proration"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[UnitWithProrationPriceDimensionalPriceConfiguration] = None


class GroupedAllocationPriceBillableMetric(BaseModel):
    id: str


class GroupedAllocationPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedAllocationPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedAllocationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[GroupedAllocationPriceCreditAllocationCustomExpiration] = None


class GroupedAllocationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedAllocationPriceItem(BaseModel):
    id: str

    name: str


class GroupedAllocationPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedAllocationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[GroupedAllocationPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class GroupedAllocationPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedAllocationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[GroupedAllocationPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class GroupedAllocationPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[GroupedAllocationPriceBillableMetric] = None

    billing_cycle_configuration: GroupedAllocationPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[GroupedAllocationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_allocation_config: Dict[str, object]

    invoicing_cycle_configuration: Optional[GroupedAllocationPriceInvoicingCycleConfiguration] = None

    item: GroupedAllocationPriceItem

    maximum: Optional[GroupedAllocationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[GroupedAllocationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_allocation"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[GroupedAllocationPriceDimensionalPriceConfiguration] = None


class GroupedWithProratedMinimumPriceBillableMetric(BaseModel):
    id: str


class GroupedWithProratedMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedWithProratedMinimumPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedWithProratedMinimumPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[GroupedWithProratedMinimumPriceCreditAllocationCustomExpiration] = None


class GroupedWithProratedMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedWithProratedMinimumPriceItem(BaseModel):
    id: str

    name: str


class GroupedWithProratedMinimumPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedWithProratedMinimumPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[GroupedWithProratedMinimumPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class GroupedWithProratedMinimumPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedWithProratedMinimumPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[GroupedWithProratedMinimumPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class GroupedWithProratedMinimumPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[GroupedWithProratedMinimumPriceBillableMetric] = None

    billing_cycle_configuration: GroupedWithProratedMinimumPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[GroupedWithProratedMinimumPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_prorated_minimum_config: Dict[str, object]

    invoicing_cycle_configuration: Optional[GroupedWithProratedMinimumPriceInvoicingCycleConfiguration] = None

    item: GroupedWithProratedMinimumPriceItem

    maximum: Optional[GroupedWithProratedMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[GroupedWithProratedMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_prorated_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[GroupedWithProratedMinimumPriceDimensionalPriceConfiguration] = None


class GroupedWithMeteredMinimumPriceBillableMetric(BaseModel):
    id: str


class GroupedWithMeteredMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedWithMeteredMinimumPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedWithMeteredMinimumPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[GroupedWithMeteredMinimumPriceCreditAllocationCustomExpiration] = None


class GroupedWithMeteredMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedWithMeteredMinimumPriceItem(BaseModel):
    id: str

    name: str


class GroupedWithMeteredMinimumPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedWithMeteredMinimumPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[GroupedWithMeteredMinimumPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class GroupedWithMeteredMinimumPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedWithMeteredMinimumPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[GroupedWithMeteredMinimumPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class GroupedWithMeteredMinimumPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[GroupedWithMeteredMinimumPriceBillableMetric] = None

    billing_cycle_configuration: GroupedWithMeteredMinimumPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[GroupedWithMeteredMinimumPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_with_metered_minimum_config: Dict[str, object]

    invoicing_cycle_configuration: Optional[GroupedWithMeteredMinimumPriceInvoicingCycleConfiguration] = None

    item: GroupedWithMeteredMinimumPriceItem

    maximum: Optional[GroupedWithMeteredMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[GroupedWithMeteredMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_with_metered_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[GroupedWithMeteredMinimumPriceDimensionalPriceConfiguration] = None


class MatrixWithDisplayNamePriceBillableMetric(BaseModel):
    id: str


class MatrixWithDisplayNamePriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixWithDisplayNamePriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixWithDisplayNamePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[MatrixWithDisplayNamePriceCreditAllocationCustomExpiration] = None


class MatrixWithDisplayNamePriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MatrixWithDisplayNamePriceItem(BaseModel):
    id: str

    name: str


class MatrixWithDisplayNamePriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MatrixWithDisplayNamePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MatrixWithDisplayNamePriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MatrixWithDisplayNamePriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MatrixWithDisplayNamePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MatrixWithDisplayNamePriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class MatrixWithDisplayNamePriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[MatrixWithDisplayNamePriceBillableMetric] = None

    billing_cycle_configuration: MatrixWithDisplayNamePriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[MatrixWithDisplayNamePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[MatrixWithDisplayNamePriceInvoicingCycleConfiguration] = None

    item: MatrixWithDisplayNamePriceItem

    matrix_with_display_name_config: Dict[str, object]

    maximum: Optional[MatrixWithDisplayNamePriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MatrixWithDisplayNamePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_display_name"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[MatrixWithDisplayNamePriceDimensionalPriceConfiguration] = None


class BulkWithProrationPriceBillableMetric(BaseModel):
    id: str


class BulkWithProrationPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkWithProrationPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkWithProrationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[BulkWithProrationPriceCreditAllocationCustomExpiration] = None


class BulkWithProrationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class BulkWithProrationPriceItem(BaseModel):
    id: str

    name: str


class BulkWithProrationPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BulkWithProrationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[BulkWithProrationPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class BulkWithProrationPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class BulkWithProrationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[BulkWithProrationPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class BulkWithProrationPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BulkWithProrationPriceBillableMetric] = None

    billing_cycle_configuration: BulkWithProrationPriceBillingCycleConfiguration

    bulk_with_proration_config: Dict[str, object]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BulkWithProrationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[BulkWithProrationPriceInvoicingCycleConfiguration] = None

    item: BulkWithProrationPriceItem

    maximum: Optional[BulkWithProrationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[BulkWithProrationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk_with_proration"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[BulkWithProrationPriceDimensionalPriceConfiguration] = None


class GroupedTieredPackagePriceBillableMetric(BaseModel):
    id: str


class GroupedTieredPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedTieredPackagePriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedTieredPackagePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[GroupedTieredPackagePriceCreditAllocationCustomExpiration] = None


class GroupedTieredPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class GroupedTieredPackagePriceItem(BaseModel):
    id: str

    name: str


class GroupedTieredPackagePriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedTieredPackagePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[GroupedTieredPackagePriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class GroupedTieredPackagePriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class GroupedTieredPackagePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[GroupedTieredPackagePriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class GroupedTieredPackagePriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[GroupedTieredPackagePriceBillableMetric] = None

    billing_cycle_configuration: GroupedTieredPackagePriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[GroupedTieredPackagePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_package_config: Dict[str, object]

    invoicing_cycle_configuration: Optional[GroupedTieredPackagePriceInvoicingCycleConfiguration] = None

    item: GroupedTieredPackagePriceItem

    maximum: Optional[GroupedTieredPackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[GroupedTieredPackagePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[GroupedTieredPackagePriceDimensionalPriceConfiguration] = None


class MaxGroupTieredPackagePriceBillableMetric(BaseModel):
    id: str


class MaxGroupTieredPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MaxGroupTieredPackagePriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MaxGroupTieredPackagePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[MaxGroupTieredPackagePriceCreditAllocationCustomExpiration] = None


class MaxGroupTieredPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class MaxGroupTieredPackagePriceItem(BaseModel):
    id: str

    name: str


class MaxGroupTieredPackagePriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MaxGroupTieredPackagePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MaxGroupTieredPackagePriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MaxGroupTieredPackagePriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class MaxGroupTieredPackagePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MaxGroupTieredPackagePriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class MaxGroupTieredPackagePriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[MaxGroupTieredPackagePriceBillableMetric] = None

    billing_cycle_configuration: MaxGroupTieredPackagePriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[MaxGroupTieredPackagePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[MaxGroupTieredPackagePriceInvoicingCycleConfiguration] = None

    item: MaxGroupTieredPackagePriceItem

    max_group_tiered_package_config: Dict[str, object]

    maximum: Optional[MaxGroupTieredPackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MaxGroupTieredPackagePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["max_group_tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[MaxGroupTieredPackagePriceDimensionalPriceConfiguration] = None


class ScalableMatrixWithUnitPricingPriceBillableMetric(BaseModel):
    id: str


class ScalableMatrixWithUnitPricingPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ScalableMatrixWithUnitPricingPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ScalableMatrixWithUnitPricingPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[ScalableMatrixWithUnitPricingPriceCreditAllocationCustomExpiration] = None


class ScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ScalableMatrixWithUnitPricingPriceItem(BaseModel):
    id: str

    name: str


class ScalableMatrixWithUnitPricingPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class ScalableMatrixWithUnitPricingPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[ScalableMatrixWithUnitPricingPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class ScalableMatrixWithUnitPricingPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class ScalableMatrixWithUnitPricingPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[ScalableMatrixWithUnitPricingPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class ScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[ScalableMatrixWithUnitPricingPriceBillableMetric] = None

    billing_cycle_configuration: ScalableMatrixWithUnitPricingPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[ScalableMatrixWithUnitPricingPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[ScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration] = None

    item: ScalableMatrixWithUnitPricingPriceItem

    maximum: Optional[ScalableMatrixWithUnitPricingPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[ScalableMatrixWithUnitPricingPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["scalable_matrix_with_unit_pricing"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    scalable_matrix_with_unit_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[ScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration] = None


class ScalableMatrixWithTieredPricingPriceBillableMetric(BaseModel):
    id: str


class ScalableMatrixWithTieredPricingPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ScalableMatrixWithTieredPricingPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ScalableMatrixWithTieredPricingPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[ScalableMatrixWithTieredPricingPriceCreditAllocationCustomExpiration] = None


class ScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class ScalableMatrixWithTieredPricingPriceItem(BaseModel):
    id: str

    name: str


class ScalableMatrixWithTieredPricingPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class ScalableMatrixWithTieredPricingPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[ScalableMatrixWithTieredPricingPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class ScalableMatrixWithTieredPricingPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class ScalableMatrixWithTieredPricingPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[ScalableMatrixWithTieredPricingPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class ScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[ScalableMatrixWithTieredPricingPriceBillableMetric] = None

    billing_cycle_configuration: ScalableMatrixWithTieredPricingPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[ScalableMatrixWithTieredPricingPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[ScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration] = None

    item: ScalableMatrixWithTieredPricingPriceItem

    maximum: Optional[ScalableMatrixWithTieredPricingPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[ScalableMatrixWithTieredPricingPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["scalable_matrix_with_tiered_pricing"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    scalable_matrix_with_tiered_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[ScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration] = None


class CumulativeGroupedBulkPriceBillableMetric(BaseModel):
    id: str


class CumulativeGroupedBulkPriceBillingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class CumulativeGroupedBulkPriceCreditAllocationCustomExpiration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class CumulativeGroupedBulkPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str

    custom_expiration: Optional[CumulativeGroupedBulkPriceCreditAllocationCustomExpiration] = None


class CumulativeGroupedBulkPriceInvoicingCycleConfiguration(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]


class CumulativeGroupedBulkPriceItem(BaseModel):
    id: str

    name: str


class CumulativeGroupedBulkPriceMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class CumulativeGroupedBulkPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[CumulativeGroupedBulkPriceMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class CumulativeGroupedBulkPriceMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class CumulativeGroupedBulkPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[CumulativeGroupedBulkPriceMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class CumulativeGroupedBulkPriceDimensionalPriceConfiguration(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[CumulativeGroupedBulkPriceBillableMetric] = None

    billing_cycle_configuration: CumulativeGroupedBulkPriceBillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[CumulativeGroupedBulkPriceCreditAllocation] = None

    cumulative_grouped_bulk_config: Dict[str, object]

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    invoicing_cycle_configuration: Optional[CumulativeGroupedBulkPriceInvoicingCycleConfiguration] = None

    item: CumulativeGroupedBulkPriceItem

    maximum: Optional[CumulativeGroupedBulkPriceMaximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[CumulativeGroupedBulkPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["cumulative_grouped_bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[CumulativeGroupedBulkPriceDimensionalPriceConfiguration] = None


Price: TypeAlias = Annotated[
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
