# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .shared import Discount
from .._models import BaseModel

__all__ = [
    "Price",
    "UnitPrice",
    "UnitPriceBillableMetric",
    "UnitPriceItem",
    "UnitPriceMaximum",
    "UnitPriceMinimum",
    "UnitPriceUnitConfig",
    "PackagePrice",
    "PackagePriceBillableMetric",
    "PackagePriceItem",
    "PackagePriceMaximum",
    "PackagePriceMinimum",
    "PackagePricePackageConfig",
    "MatrixPrice",
    "MatrixPriceBillableMetric",
    "MatrixPriceItem",
    "MatrixPriceMatrixConfig",
    "MatrixPriceMatrixConfigMatrixValue",
    "MatrixPriceMaximum",
    "MatrixPriceMinimum",
    "TieredPrice",
    "TieredPriceBillableMetric",
    "TieredPriceItem",
    "TieredPriceMaximum",
    "TieredPriceMinimum",
    "TieredPriceTieredConfig",
    "TieredPriceTieredConfigTier",
    "TieredBpsPrice",
    "TieredBpsPriceBillableMetric",
    "TieredBpsPriceItem",
    "TieredBpsPriceMaximum",
    "TieredBpsPriceMinimum",
    "TieredBpsPriceTieredBpsConfig",
    "TieredBpsPriceTieredBpsConfigTier",
    "BpsPrice",
    "BpsPriceBillableMetric",
    "BpsPriceBpsConfig",
    "BpsPriceItem",
    "BpsPriceMaximum",
    "BpsPriceMinimum",
    "BulkBpsPrice",
    "BulkBpsPriceBillableMetric",
    "BulkBpsPriceBulkBpsConfig",
    "BulkBpsPriceBulkBpsConfigTier",
    "BulkBpsPriceItem",
    "BulkBpsPriceMaximum",
    "BulkBpsPriceMinimum",
    "BulkPrice",
    "BulkPriceBillableMetric",
    "BulkPriceBulkConfig",
    "BulkPriceBulkConfigTier",
    "BulkPriceItem",
    "BulkPriceMaximum",
    "BulkPriceMinimum",
    "TestRatingFunctionPrice",
    "TestRatingFunctionPriceBillableMetric",
    "TestRatingFunctionPriceItem",
    "TestRatingFunctionPriceMaximum",
    "TestRatingFunctionPriceMinimum",
    "FivetranExamplePrice",
    "FivetranExamplePriceBillableMetric",
    "FivetranExamplePriceItem",
    "FivetranExamplePriceMaximum",
    "FivetranExamplePriceMinimum",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceBillableMetric",
    "ThresholdTotalAmountPriceItem",
    "ThresholdTotalAmountPriceMaximum",
    "ThresholdTotalAmountPriceMinimum",
    "TieredPackagePrice",
    "TieredPackagePriceBillableMetric",
    "TieredPackagePriceItem",
    "TieredPackagePriceMaximum",
    "TieredPackagePriceMinimum",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceBillableMetric",
    "TieredWithMinimumPriceItem",
    "TieredWithMinimumPriceMaximum",
    "TieredWithMinimumPriceMinimum",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceBillableMetric",
    "PackageWithAllocationPriceItem",
    "PackageWithAllocationPriceMaximum",
    "PackageWithAllocationPriceMinimum",
]


class UnitPriceBillableMetric(BaseModel):
    id: str


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

    scaling_factor: Optional[float] = None
    """Multiplier to scale rated quantity by"""


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: UnitPriceItem

    maximum: Optional[UnitPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[UnitPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    unit_config: UnitPriceUnitConfig


class PackagePriceBillableMetric(BaseModel):
    id: str


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

    package_size: Optional[int] = None
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[PackagePriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: PackagePriceItem

    maximum: Optional[PackagePriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[PackagePriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str

    package_config: PackagePricePackageConfig

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]


class MatrixPriceBillableMetric(BaseModel):
    id: str


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

    scaling_factor: Optional[float] = None
    """Optional multiplier to scale rated quantities by"""


class MatrixPriceMatrixConfig(BaseModel):
    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[MatrixPriceMatrixConfigMatrixValue]
    """Matrix values for specified matrix grouping keys"""

    scaling_factor: Optional[float] = None
    """
    Default optional multiplier to scale rated quantities that fall into the default
    bucket by
    """


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

    billable_metric: Optional[MatrixPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: MatrixPriceItem

    matrix_config: MatrixPriceMatrixConfig

    maximum: Optional[MatrixPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[MatrixPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]


class TieredPriceBillableMetric(BaseModel):
    id: str


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

    billable_metric: Optional[TieredPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredPriceItem

    maximum: Optional[TieredPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[TieredPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_config: TieredPriceTieredConfig


class TieredBpsPriceBillableMetric(BaseModel):
    id: str


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

    billable_metric: Optional[TieredBpsPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredBpsPriceItem

    maximum: Optional[TieredBpsPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[TieredBpsPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_bps_config: TieredBpsPriceTieredBpsConfig


class BpsPriceBillableMetric(BaseModel):
    id: str


class BpsPriceBpsConfig(BaseModel):
    bps: float
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str] = None
    """Optional currency amount maximum to cap spend per event"""


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

    billable_metric: Optional[BpsPriceBillableMetric]

    bps_config: BpsPriceBpsConfig

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: BpsPriceItem

    maximum: Optional[BpsPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[BpsPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

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

    billable_metric: Optional[BulkBpsPriceBillableMetric]

    bulk_bps_config: BulkBpsPriceBulkBpsConfig

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: BulkBpsPriceItem

    maximum: Optional[BulkBpsPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[BulkBpsPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

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

    billable_metric: Optional[BulkPriceBillableMetric]

    bulk_config: BulkPriceBulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: BulkPriceItem

    maximum: Optional[BulkPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[BulkPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]


class TestRatingFunctionPriceBillableMetric(BaseModel):
    id: str


class TestRatingFunctionPriceItem(BaseModel):
    id: str

    name: str


class TestRatingFunctionPriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class TestRatingFunctionPriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class TestRatingFunctionPrice(BaseModel):
    id: str

    billable_metric: Optional[TestRatingFunctionPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TestRatingFunctionPriceItem

    maximum: Optional[TestRatingFunctionPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[TestRatingFunctionPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["test_rating_function"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    test_rating_function_config: Dict[str, object]


class FivetranExamplePriceBillableMetric(BaseModel):
    id: str


class FivetranExamplePriceItem(BaseModel):
    id: str

    name: str


class FivetranExamplePriceMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class FivetranExamplePriceMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class FivetranExamplePrice(BaseModel):
    id: str

    billable_metric: Optional[FivetranExamplePriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fivetran_example_config: Dict[str, object]

    fixed_price_quantity: Optional[float]

    item: FivetranExamplePriceItem

    maximum: Optional[FivetranExamplePriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[FivetranExamplePriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["fivetran_example"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]


class ThresholdTotalAmountPriceBillableMetric(BaseModel):
    id: str


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

    billable_metric: Optional[ThresholdTotalAmountPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: ThresholdTotalAmountPriceItem

    maximum: Optional[ThresholdTotalAmountPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[ThresholdTotalAmountPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    threshold_total_amount_config: Dict[str, object]


class TieredPackagePriceBillableMetric(BaseModel):
    id: str


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

    billable_metric: Optional[TieredPackagePriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredPackagePriceItem

    maximum: Optional[TieredPackagePriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[TieredPackagePriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_config: Dict[str, object]


class TieredWithMinimumPriceBillableMetric(BaseModel):
    id: str


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

    billable_metric: Optional[TieredWithMinimumPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredWithMinimumPriceItem

    maximum: Optional[TieredWithMinimumPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[TieredWithMinimumPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_minimum_config: Dict[str, object]


class PackageWithAllocationPriceBillableMetric(BaseModel):
    id: str


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

    billable_metric: Optional[PackageWithAllocationPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    discount: Optional[Discount]

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: PackageWithAllocationPriceItem

    maximum: Optional[PackageWithAllocationPriceMaximum]

    maximum_amount: Optional[str]

    minimum: Optional[PackageWithAllocationPriceMinimum]

    minimum_amount: Optional[str]

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    package_with_allocation_config: Dict[str, object]

    plan_phase_order: Optional[int]

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
    TestRatingFunctionPrice,
    FivetranExamplePrice,
    ThresholdTotalAmountPrice,
    TieredPackagePrice,
    TieredWithMinimumPrice,
    PackageWithAllocationPrice,
]
