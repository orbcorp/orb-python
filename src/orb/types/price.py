# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.discount import Discount

__all__ = [
    "Price",
    "UnitPrice",
    "UnitPriceBillableMetric",
    "UnitPriceCreditAllocation",
    "UnitPriceItem",
    "UnitPriceMaximum",
    "UnitPriceMinimum",
    "UnitPriceUnitConfig",
    "PackagePrice",
    "PackagePriceBillableMetric",
    "PackagePriceCreditAllocation",
    "PackagePriceItem",
    "PackagePriceMaximum",
    "PackagePriceMinimum",
    "PackagePricePackageConfig",
    "MatrixPrice",
    "MatrixPriceBillableMetric",
    "MatrixPriceCreditAllocation",
    "MatrixPriceItem",
    "MatrixPriceMatrixConfig",
    "MatrixPriceMatrixConfigMatrixValue",
    "MatrixPriceMaximum",
    "MatrixPriceMinimum",
    "TieredPrice",
    "TieredPriceBillableMetric",
    "TieredPriceCreditAllocation",
    "TieredPriceItem",
    "TieredPriceMaximum",
    "TieredPriceMinimum",
    "TieredPriceTieredConfig",
    "TieredPriceTieredConfigTier",
    "TieredBpsPrice",
    "TieredBpsPriceBillableMetric",
    "TieredBpsPriceCreditAllocation",
    "TieredBpsPriceItem",
    "TieredBpsPriceMaximum",
    "TieredBpsPriceMinimum",
    "TieredBpsPriceTieredBpsConfig",
    "TieredBpsPriceTieredBpsConfigTier",
    "BpsPrice",
    "BpsPriceBillableMetric",
    "BpsPriceBpsConfig",
    "BpsPriceCreditAllocation",
    "BpsPriceItem",
    "BpsPriceMaximum",
    "BpsPriceMinimum",
    "BulkBpsPrice",
    "BulkBpsPriceBillableMetric",
    "BulkBpsPriceBulkBpsConfig",
    "BulkBpsPriceBulkBpsConfigTier",
    "BulkBpsPriceCreditAllocation",
    "BulkBpsPriceItem",
    "BulkBpsPriceMaximum",
    "BulkBpsPriceMinimum",
    "BulkPrice",
    "BulkPriceBillableMetric",
    "BulkPriceBulkConfig",
    "BulkPriceBulkConfigTier",
    "BulkPriceCreditAllocation",
    "BulkPriceItem",
    "BulkPriceMaximum",
    "BulkPriceMinimum",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceBillableMetric",
    "ThresholdTotalAmountPriceCreditAllocation",
    "ThresholdTotalAmountPriceItem",
    "ThresholdTotalAmountPriceMaximum",
    "ThresholdTotalAmountPriceMinimum",
    "TieredPackagePrice",
    "TieredPackagePriceBillableMetric",
    "TieredPackagePriceCreditAllocation",
    "TieredPackagePriceItem",
    "TieredPackagePriceMaximum",
    "TieredPackagePriceMinimum",
    "GroupedTieredPrice",
    "GroupedTieredPriceBillableMetric",
    "GroupedTieredPriceCreditAllocation",
    "GroupedTieredPriceItem",
    "GroupedTieredPriceMaximum",
    "GroupedTieredPriceMinimum",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceBillableMetric",
    "TieredWithMinimumPriceCreditAllocation",
    "TieredWithMinimumPriceItem",
    "TieredWithMinimumPriceMaximum",
    "TieredWithMinimumPriceMinimum",
    "TieredPackageWithMinimumPrice",
    "TieredPackageWithMinimumPriceBillableMetric",
    "TieredPackageWithMinimumPriceCreditAllocation",
    "TieredPackageWithMinimumPriceItem",
    "TieredPackageWithMinimumPriceMaximum",
    "TieredPackageWithMinimumPriceMinimum",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceBillableMetric",
    "PackageWithAllocationPriceCreditAllocation",
    "PackageWithAllocationPriceItem",
    "PackageWithAllocationPriceMaximum",
    "PackageWithAllocationPriceMinimum",
    "UnitWithPercentPrice",
    "UnitWithPercentPriceBillableMetric",
    "UnitWithPercentPriceCreditAllocation",
    "UnitWithPercentPriceItem",
    "UnitWithPercentPriceMaximum",
    "UnitWithPercentPriceMinimum",
    "MatrixWithAllocationPrice",
    "MatrixWithAllocationPriceBillableMetric",
    "MatrixWithAllocationPriceCreditAllocation",
    "MatrixWithAllocationPriceItem",
    "MatrixWithAllocationPriceMatrixWithAllocationConfig",
    "MatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue",
    "MatrixWithAllocationPriceMaximum",
    "MatrixWithAllocationPriceMinimum",
]


class UnitPriceBillableMetric(BaseModel):
    id: str


class UnitPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class UnitPriceItem(BaseModel):
    id: str

    name: str


class UnitPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class UnitPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class UnitPriceUnitConfig(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[UnitPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: UnitPriceItem

    maximum: Optional[UnitPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[UnitPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_config: UnitPriceUnitConfig


class PackagePriceBillableMetric(BaseModel):
    id: str


class PackagePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class PackagePriceItem(BaseModel):
    id: str

    name: str


class PackagePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class PackagePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

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


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[PackagePriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[PackagePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: PackagePriceItem

    maximum: Optional[PackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[PackagePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str

    package_config: PackagePricePackageConfig

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class MatrixPriceBillableMetric(BaseModel):
    id: str


class MatrixPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


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


class MatrixPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class MatrixPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[MatrixPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[MatrixPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: MatrixPriceItem

    matrix_config: MatrixPriceMatrixConfig

    maximum: Optional[MatrixPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[MatrixPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class TieredPriceBillableMetric(BaseModel):
    id: str


class TieredPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class TieredPriceItem(BaseModel):
    id: str

    name: str


class TieredPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class TieredPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class TieredPriceTieredConfigTier(BaseModel):
    first_unit: float
    """Inclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""

    last_unit: Optional[float] = None
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class TieredPriceTieredConfig(BaseModel):
    tiers: List[TieredPriceTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: TieredPriceItem

    maximum: Optional[TieredPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_config: TieredPriceTieredConfig


class TieredBpsPriceBillableMetric(BaseModel):
    id: str


class TieredBpsPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class TieredBpsPriceItem(BaseModel):
    id: str

    name: str


class TieredBpsPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class TieredBpsPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class TieredBpsPriceTieredBpsConfigTier(BaseModel):
    bps: float
    """Per-event basis point rate"""

    minimum_amount: str
    """Inclusive tier starting value"""

    maximum_amount: Optional[str] = None
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str] = None
    """Per unit maximum to charge"""


class TieredBpsPriceTieredBpsConfig(BaseModel):
    tiers: List[TieredBpsPriceTieredBpsConfigTier]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class TieredBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredBpsPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredBpsPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: TieredBpsPriceItem

    maximum: Optional[TieredBpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredBpsPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_bps_config: TieredBpsPriceTieredBpsConfig


class BpsPriceBillableMetric(BaseModel):
    id: str


class BpsPriceBpsConfig(BaseModel):
    bps: float
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str] = None
    """Optional currency amount maximum to cap spend per event"""


class BpsPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class BpsPriceItem(BaseModel):
    id: str

    name: str


class BpsPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class BpsPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class BpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BpsPriceBillableMetric] = None

    bps_config: BpsPriceBpsConfig

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BpsPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: BpsPriceItem

    maximum: Optional[BpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[BpsPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class BulkBpsPriceBillableMetric(BaseModel):
    id: str


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


class BulkBpsPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class BulkBpsPriceItem(BaseModel):
    id: str

    name: str


class BulkBpsPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class BulkBpsPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class BulkBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[BulkBpsPriceBillableMetric] = None

    bulk_bps_config: BulkBpsPriceBulkBpsConfig

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BulkBpsPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: BulkBpsPriceItem

    maximum: Optional[BulkBpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[BulkBpsPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class BulkPriceBillableMetric(BaseModel):
    id: str


class BulkPriceBulkConfigTier(BaseModel):
    unit_amount: str
    """Amount per unit"""

    maximum_units: Optional[float] = None
    """Upper bound for this tier"""


class BulkPriceBulkConfig(BaseModel):
    tiers: List[BulkPriceBulkConfigTier]
    """Bulk tiers for rating based on total usage volume"""


class BulkPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class BulkPriceItem(BaseModel):
    id: str

    name: str


class BulkPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class BulkPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BulkPriceBillableMetric] = None

    bulk_config: BulkPriceBulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[BulkPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: BulkPriceItem

    maximum: Optional[BulkPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[BulkPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class ThresholdTotalAmountPriceBillableMetric(BaseModel):
    id: str


class ThresholdTotalAmountPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class ThresholdTotalAmountPriceItem(BaseModel):
    id: str

    name: str


class ThresholdTotalAmountPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class ThresholdTotalAmountPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[ThresholdTotalAmountPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[ThresholdTotalAmountPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: ThresholdTotalAmountPriceItem

    maximum: Optional[ThresholdTotalAmountPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[ThresholdTotalAmountPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    threshold_total_amount_config: Dict[str, object]


class TieredPackagePriceBillableMetric(BaseModel):
    id: str


class TieredPackagePriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class TieredPackagePriceItem(BaseModel):
    id: str

    name: str


class TieredPackagePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class TieredPackagePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPackagePriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredPackagePriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: TieredPackagePriceItem

    maximum: Optional[TieredPackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredPackagePriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_config: Dict[str, object]


class GroupedTieredPriceBillableMetric(BaseModel):
    id: str


class GroupedTieredPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class GroupedTieredPriceItem(BaseModel):
    id: str

    name: str


class GroupedTieredPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class GroupedTieredPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[GroupedTieredPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[GroupedTieredPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    grouped_tiered_config: Dict[str, object]

    item: GroupedTieredPriceItem

    maximum: Optional[GroupedTieredPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[GroupedTieredPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["grouped_tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class TieredWithMinimumPriceBillableMetric(BaseModel):
    id: str


class TieredWithMinimumPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class TieredWithMinimumPriceItem(BaseModel):
    id: str

    name: str


class TieredWithMinimumPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class TieredWithMinimumPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredWithMinimumPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredWithMinimumPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: TieredWithMinimumPriceItem

    maximum: Optional[TieredWithMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredWithMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_minimum_config: Dict[str, object]


class TieredPackageWithMinimumPriceBillableMetric(BaseModel):
    id: str


class TieredPackageWithMinimumPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class TieredPackageWithMinimumPriceItem(BaseModel):
    id: str

    name: str


class TieredPackageWithMinimumPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class TieredPackageWithMinimumPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPackageWithMinimumPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[TieredPackageWithMinimumPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: TieredPackageWithMinimumPriceItem

    maximum: Optional[TieredPackageWithMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredPackageWithMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["tiered_package_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_with_minimum_config: Dict[str, object]


class PackageWithAllocationPriceBillableMetric(BaseModel):
    id: str


class PackageWithAllocationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class PackageWithAllocationPriceItem(BaseModel):
    id: str

    name: str


class PackageWithAllocationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class PackageWithAllocationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[PackageWithAllocationPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[PackageWithAllocationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: PackageWithAllocationPriceItem

    maximum: Optional[PackageWithAllocationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[PackageWithAllocationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    package_with_allocation_config: Dict[str, object]

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


class UnitWithPercentPriceBillableMetric(BaseModel):
    id: str


class UnitWithPercentPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


class UnitWithPercentPriceItem(BaseModel):
    id: str

    name: str


class UnitWithPercentPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class UnitWithPercentPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitWithPercentPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[UnitWithPercentPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: UnitWithPercentPriceItem

    maximum: Optional[UnitWithPercentPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[UnitWithPercentPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["unit_with_percent"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_percent_config: Dict[str, object]


class MatrixWithAllocationPriceBillableMetric(BaseModel):
    id: str


class MatrixWithAllocationPriceCreditAllocation(BaseModel):
    allows_rollover: bool

    currency: str


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


class MatrixWithAllocationPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class MatrixWithAllocationPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[MatrixWithAllocationPriceBillableMetric] = None

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    conversion_rate: Optional[float] = None

    created_at: datetime

    credit_allocation: Optional[MatrixWithAllocationPriceCreditAllocation] = None

    currency: str

    discount: Optional[Discount] = None

    external_price_id: Optional[str] = None

    fixed_price_quantity: Optional[float] = None

    item: MatrixWithAllocationPriceItem

    matrix_with_allocation_config: MatrixWithAllocationPriceMatrixWithAllocationConfig

    maximum: Optional[MatrixWithAllocationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[MatrixWithAllocationPriceMinimum] = None

    minimum_amount: Optional[str] = None

    price_model_type: Literal["matrix_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]


Price = Union[
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
]
