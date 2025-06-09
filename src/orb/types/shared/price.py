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
    "UnitPriceConversionRateConfig",
    "UnitPriceConversionRateConfigUnitConversionRateConfig",
    "UnitPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "UnitPriceConversionRateConfigTieredConversionRateConfig",
    "UnitPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "UnitPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "PackagePrice",
    "PackagePriceConversionRateConfig",
    "PackagePriceConversionRateConfigUnitConversionRateConfig",
    "PackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "PackagePriceConversionRateConfigTieredConversionRateConfig",
    "PackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "PackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "MatrixPrice",
    "MatrixPriceConversionRateConfig",
    "MatrixPriceConversionRateConfigUnitConversionRateConfig",
    "MatrixPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "MatrixPriceConversionRateConfigTieredConversionRateConfig",
    "MatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "MatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "TieredPrice",
    "TieredPriceConversionRateConfig",
    "TieredPriceConversionRateConfigUnitConversionRateConfig",
    "TieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "TieredPriceConversionRateConfigTieredConversionRateConfig",
    "TieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "TieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "TieredBPSPrice",
    "TieredBPSPriceConversionRateConfig",
    "TieredBPSPriceConversionRateConfigUnitConversionRateConfig",
    "TieredBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "TieredBPSPriceConversionRateConfigTieredConversionRateConfig",
    "TieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "TieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "BPSPrice",
    "BPSPriceConversionRateConfig",
    "BPSPriceConversionRateConfigUnitConversionRateConfig",
    "BPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "BPSPriceConversionRateConfigTieredConversionRateConfig",
    "BPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "BPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "BulkBPSPrice",
    "BulkBPSPriceConversionRateConfig",
    "BulkBPSPriceConversionRateConfigUnitConversionRateConfig",
    "BulkBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "BulkBPSPriceConversionRateConfigTieredConversionRateConfig",
    "BulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "BulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "BulkPrice",
    "BulkPriceConversionRateConfig",
    "BulkPriceConversionRateConfigUnitConversionRateConfig",
    "BulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "BulkPriceConversionRateConfigTieredConversionRateConfig",
    "BulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "BulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "ThresholdTotalAmountPrice",
    "ThresholdTotalAmountPriceConversionRateConfig",
    "ThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfig",
    "ThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfig",
    "ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "TieredPackagePrice",
    "TieredPackagePriceConversionRateConfig",
    "TieredPackagePriceConversionRateConfigUnitConversionRateConfig",
    "TieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "TieredPackagePriceConversionRateConfigTieredConversionRateConfig",
    "TieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "TieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "GroupedTieredPrice",
    "GroupedTieredPriceConversionRateConfig",
    "GroupedTieredPriceConversionRateConfigUnitConversionRateConfig",
    "GroupedTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "GroupedTieredPriceConversionRateConfigTieredConversionRateConfig",
    "GroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "GroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "TieredWithMinimumPrice",
    "TieredWithMinimumPriceConversionRateConfig",
    "TieredWithMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "TieredWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "TieredPackageWithMinimumPrice",
    "TieredPackageWithMinimumPriceConversionRateConfig",
    "TieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "TieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "PackageWithAllocationPrice",
    "PackageWithAllocationPriceConversionRateConfig",
    "PackageWithAllocationPriceConversionRateConfigUnitConversionRateConfig",
    "PackageWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfig",
    "PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "UnitWithPercentPrice",
    "UnitWithPercentPriceConversionRateConfig",
    "UnitWithPercentPriceConversionRateConfigUnitConversionRateConfig",
    "UnitWithPercentPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "UnitWithPercentPriceConversionRateConfigTieredConversionRateConfig",
    "UnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "UnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "MatrixWithAllocationPrice",
    "MatrixWithAllocationPriceConversionRateConfig",
    "MatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfig",
    "MatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfig",
    "MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "TieredWithProrationPrice",
    "TieredWithProrationPriceConversionRateConfig",
    "TieredWithProrationPriceConversionRateConfigUnitConversionRateConfig",
    "TieredWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "TieredWithProrationPriceConversionRateConfigTieredConversionRateConfig",
    "TieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "TieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "UnitWithProrationPrice",
    "UnitWithProrationPriceConversionRateConfig",
    "UnitWithProrationPriceConversionRateConfigUnitConversionRateConfig",
    "UnitWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "UnitWithProrationPriceConversionRateConfigTieredConversionRateConfig",
    "UnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "UnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "GroupedAllocationPrice",
    "GroupedAllocationPriceConversionRateConfig",
    "GroupedAllocationPriceConversionRateConfigUnitConversionRateConfig",
    "GroupedAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "GroupedAllocationPriceConversionRateConfigTieredConversionRateConfig",
    "GroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "GroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "GroupedWithProratedMinimumPrice",
    "GroupedWithProratedMinimumPriceConversionRateConfig",
    "GroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "GroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "GroupedWithMeteredMinimumPrice",
    "GroupedWithMeteredMinimumPriceConversionRateConfig",
    "GroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "GroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "MatrixWithDisplayNamePrice",
    "MatrixWithDisplayNamePriceConversionRateConfig",
    "MatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfig",
    "MatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfig",
    "MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "BulkWithProrationPrice",
    "BulkWithProrationPriceConversionRateConfig",
    "BulkWithProrationPriceConversionRateConfigUnitConversionRateConfig",
    "BulkWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "BulkWithProrationPriceConversionRateConfigTieredConversionRateConfig",
    "BulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "BulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "GroupedTieredPackagePrice",
    "GroupedTieredPackagePriceConversionRateConfig",
    "GroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfig",
    "GroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfig",
    "GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "MaxGroupTieredPackagePrice",
    "MaxGroupTieredPackagePriceConversionRateConfig",
    "MaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfig",
    "MaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfig",
    "MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "ScalableMatrixWithUnitPricingPrice",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfig",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfig",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "ScalableMatrixWithTieredPricingPrice",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfig",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfig",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "CumulativeGroupedBulkPrice",
    "CumulativeGroupedBulkPriceConversionRateConfig",
    "CumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfig",
    "CumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfig",
    "CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
]


class UnitPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class UnitPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: UnitPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class UnitPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class UnitPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[UnitPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class UnitPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: UnitPriceConversionRateConfigTieredConversionRateConfigTieredConfig


UnitPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        UnitPriceConversionRateConfigUnitConversionRateConfig,
        UnitPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class UnitPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_config: UnitConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class PackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class PackagePriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: PackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig


class PackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class PackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[PackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class PackagePriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: PackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig


PackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        PackagePriceConversionRateConfigUnitConversionRateConfig,
        PackagePriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class PackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    package_config: PackageConfig

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class MatrixPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class MatrixPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: MatrixPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class MatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class MatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[MatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class MatrixPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: MatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfig


MatrixPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        MatrixPriceConversionRateConfigUnitConversionRateConfig,
        MatrixPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class MatrixPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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


class TieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class TieredPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: TieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class TieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[TieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: TieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig


TieredPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        TieredPriceConversionRateConfigUnitConversionRateConfig,
        TieredPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class TieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_config: TieredConfig

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class TieredBPSPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: TieredBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class TieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[TieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredBPSPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: TieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig


TieredBPSPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        TieredBPSPriceConversionRateConfigUnitConversionRateConfig,
        TieredBPSPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class TieredBPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[TieredBPSPriceConversionRateConfig] = None

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


class BPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class BPSPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: BPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class BPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class BPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[BPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class BPSPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: BPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig


BPSPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        BPSPriceConversionRateConfigUnitConversionRateConfig,
        BPSPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class BPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bps_config: BPSConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BPSPriceConversionRateConfig] = None

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


class BulkBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class BulkBPSPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: BulkBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class BulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class BulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[BulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class BulkBPSPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: BulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig


BulkBPSPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        BulkBPSPriceConversionRateConfigUnitConversionRateConfig,
        BulkBPSPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class BulkBPSPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_bps_config: BulkBPSConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[BulkBPSPriceConversionRateConfig] = None

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


class BulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class BulkPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: BulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class BulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class BulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[BulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class BulkPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: BulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig


BulkPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        BulkPriceConversionRateConfigUnitConversionRateConfig,
        BulkPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class BulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_config: BulkConfig

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class ThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class ThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: ThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfig


ThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        ThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfig,
        ThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class ThresholdTotalAmountPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    threshold_total_amount_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class TieredPackagePriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: TieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig


class TieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[TieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredPackagePriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: TieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig


TieredPackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        TieredPackagePriceConversionRateConfigUnitConversionRateConfig,
        TieredPackagePriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class TieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class GroupedTieredPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: GroupedTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class GroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class GroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[GroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class GroupedTieredPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: GroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig


GroupedTieredPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        GroupedTieredPriceConversionRateConfigUnitConversionRateConfig,
        GroupedTieredPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class GroupedTieredPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPriceConversionRateConfig] = None

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


class TieredWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class TieredWithMinimumPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: TieredWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig


TieredWithMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        TieredWithMinimumPriceConversionRateConfigUnitConversionRateConfig,
        TieredWithMinimumPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class TieredWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class TieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class TieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: TieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig


TieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        TieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfig,
        TieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class TieredPackageWithMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_package_with_minimum_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class PackageWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class PackageWithAllocationPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: PackageWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig


PackageWithAllocationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        PackageWithAllocationPriceConversionRateConfigUnitConversionRateConfig,
        PackageWithAllocationPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class PackageWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    package_with_allocation_config: Dict[str, object]

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class UnitWithPercentPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class UnitWithPercentPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: UnitWithPercentPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class UnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class UnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[UnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class UnitWithPercentPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: UnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfig


UnitWithPercentPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        UnitWithPercentPriceConversionRateConfigUnitConversionRateConfig,
        UnitWithPercentPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class UnitWithPercentPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_percent_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class MatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class MatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: MatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig


MatrixWithAllocationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        MatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfig,
        MatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class MatrixWithAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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


class TieredWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class TieredWithProrationPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: TieredWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class TieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class TieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[TieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class TieredWithProrationPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: TieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig


TieredWithProrationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        TieredWithProrationPriceConversionRateConfigUnitConversionRateConfig,
        TieredWithProrationPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class TieredWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    tiered_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class UnitWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class UnitWithProrationPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: UnitWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class UnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class UnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[UnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class UnitWithProrationPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: UnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig


UnitWithProrationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        UnitWithProrationPriceConversionRateConfigUnitConversionRateConfig,
        UnitWithProrationPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class UnitWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    unit_with_proration_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class GroupedAllocationPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: GroupedAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class GroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class GroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[GroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class GroupedAllocationPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: GroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig


GroupedAllocationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        GroupedAllocationPriceConversionRateConfigUnitConversionRateConfig,
        GroupedAllocationPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class GroupedAllocationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedAllocationPriceConversionRateConfig] = None

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


class GroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class GroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: GroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig


GroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        GroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfig,
        GroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class GroupedWithProratedMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithProratedMinimumPriceConversionRateConfig] = None

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


class GroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class GroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: GroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig


GroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        GroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfig,
        GroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class GroupedWithMeteredMinimumPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedWithMeteredMinimumPriceConversionRateConfig] = None

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


class MatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class MatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: MatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfigUnitConfig


class MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfig


MatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        MatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfig,
        MatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class MatrixWithDisplayNamePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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


class BulkWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class BulkWithProrationPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: BulkWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class BulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class BulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[BulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class BulkWithProrationPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: BulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig


BulkWithProrationPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        BulkWithProrationPriceConversionRateConfigUnitConversionRateConfig,
        BulkWithProrationPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class BulkWithProrationPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    bulk_with_proration_config: Dict[str, object]

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class GroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class GroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: GroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig


class GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig


GroupedTieredPackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        GroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfig,
        GroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class GroupedTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[GroupedTieredPackagePriceConversionRateConfig] = None

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


class MaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class MaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: MaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig


class MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig


MaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        MaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfig,
        MaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class MaxGroupTieredPackagePrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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


class ScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class ScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: ScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig


ScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        ScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfig,
        ScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class ScalableMatrixWithUnitPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    scalable_matrix_with_unit_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class ScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class ScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: ScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig


ScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        ScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfig,
        ScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class ScalableMatrixWithTieredPricingPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

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

    name: str

    plan_phase_order: Optional[int] = None

    price_type: Literal["usage_price", "fixed_price"]

    scalable_matrix_with_tiered_pricing_config: Dict[str, object]

    dimensional_price_configuration: Optional[DimensionalPriceConfiguration] = None


class CumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class CumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: CumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig


class CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig


CumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Annotated[
    Union[
        CumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfig,
        CumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfig,
        None,
    ],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class CumulativeGroupedBulkPrice(BaseModel):
    id: str

    billable_metric: Optional[BillableMetricTiny] = None

    billing_cycle_configuration: BillingCycleConfiguration

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]

    conversion_rate: Optional[float] = None

    conversion_rate_config: Optional[CumulativeGroupedBulkPriceConversionRateConfig] = None

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
