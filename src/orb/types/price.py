# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .invoice_discount import InvoiceDiscount

__all__ = [
    "Price",
    "UnitPrice",
    "UnitPriceBillableMetric",
    "UnitPriceItem",
    "UnitPriceUnitConfig",
    "UnitPriceMaximum",
    "UnitPriceMinimum",
    "PackagePrice",
    "PackagePriceBillableMetric",
    "PackagePriceItem",
    "PackagePricePackageConfig",
    "PackagePriceMaximum",
    "PackagePriceMinimum",
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
    "TieredPriceTieredConfig",
    "TieredPriceTieredConfigTier",
    "TieredPriceMaximum",
    "TieredPriceMinimum",
    "TieredBpsPrice",
    "TieredBpsPriceBillableMetric",
    "TieredBpsPriceItem",
    "TieredBpsPriceTieredBpsConfig",
    "TieredBpsPriceTieredBpsConfigTier",
    "TieredBpsPriceMaximum",
    "TieredBpsPriceMinimum",
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


class UnitPriceUnitConfig(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""

    scaling_factor: Optional[float] = None
    """Multiplier to scale rated quantity by"""


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


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[UnitPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: UnitPriceItem

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    unit_config: UnitPriceUnitConfig

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[UnitPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[UnitPriceMinimum] = None

    minimum_amount: Optional[str] = None


class PackagePriceBillableMetric(BaseModel):
    id: str


class PackagePriceItem(BaseModel):
    id: str

    name: str


class PackagePricePackageConfig(BaseModel):
    package_amount: str
    """A currency amount to rate usage by"""

    package_size: Optional[int] = None
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


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


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[PackagePriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: PackagePriceItem

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str

    package_config: PackagePricePackageConfig

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[PackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[PackagePriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: MatrixPriceItem

    matrix_config: MatrixPriceMatrixConfig

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[MatrixPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[MatrixPriceMinimum] = None

    minimum_amount: Optional[str] = None


class TieredPriceBillableMetric(BaseModel):
    id: str


class TieredPriceItem(BaseModel):
    id: str

    name: str


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


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredPriceItem

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_config: TieredPriceTieredConfig

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[TieredPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredPriceMinimum] = None

    minimum_amount: Optional[str] = None


class TieredBpsPriceBillableMetric(BaseModel):
    id: str


class TieredBpsPriceItem(BaseModel):
    id: str

    name: str


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


class TieredBpsPrice(BaseModel):
    id: str

    billable_metric: Optional[TieredBpsPriceBillableMetric]

    cadence: Literal["one_time", "monthly", "quarterly", "annual"]

    created_at: datetime

    currency: str

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredBpsPriceItem

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_bps_config: TieredBpsPriceTieredBpsConfig

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[TieredBpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredBpsPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: BpsPriceItem

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[BpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[BpsPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: BulkBpsPriceItem

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[BulkBpsPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[BulkBpsPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: BulkPriceItem

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[BulkPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[BulkPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TestRatingFunctionPriceItem

    price_model_type: Literal["test_rating_function"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    test_rating_function_config: Dict[str, object]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[TestRatingFunctionPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TestRatingFunctionPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fivetran_example_config: Dict[str, object]

    fixed_price_quantity: Optional[float]

    item: FivetranExamplePriceItem

    price_model_type: Literal["fivetran_example"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[FivetranExamplePriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[FivetranExamplePriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: ThresholdTotalAmountPriceItem

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    threshold_total_amount_config: Dict[str, object]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[ThresholdTotalAmountPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[ThresholdTotalAmountPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredPackagePriceItem

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_config: Dict[str, object]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[TieredPackagePriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredPackagePriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: TieredWithMinimumPriceItem

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_minimum_config: Dict[str, object]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[TieredWithMinimumPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[TieredWithMinimumPriceMinimum] = None

    minimum_amount: Optional[str] = None


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

    external_price_id: Optional[str]

    fixed_price_quantity: Optional[float]

    item: PackageWithAllocationPriceItem

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str

    package_with_allocation_config: Dict[str, object]

    plan_phase_order: Optional[int]

    price_type: Literal["usage_price", "fixed_price"]

    discount: Optional[InvoiceDiscount] = None

    maximum: Optional[PackageWithAllocationPriceMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[PackageWithAllocationPriceMinimum] = None

    minimum_amount: Optional[str] = None


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
