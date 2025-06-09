# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.bps_config import BPSConfig
from .shared_params.bulk_config import BulkConfig
from .shared_params.unit_config import UnitConfig
from .shared_params.matrix_config import MatrixConfig
from .shared_params.tiered_config import TieredConfig
from .shared_params.package_config import PackageConfig
from .shared_params.bulk_bps_config import BulkBPSConfig
from .shared_params.tiered_bps_config import TieredBPSConfig
from .shared_params.matrix_with_allocation_config import MatrixWithAllocationConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "PriceCreateParams",
    "NewFloatingUnitPrice",
    "NewFloatingUnitPriceConversionRateConfig",
    "NewFloatingUnitPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingUnitPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingPackagePrice",
    "NewFloatingPackagePriceConversionRateConfig",
    "NewFloatingPackagePriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingMatrixPrice",
    "NewFloatingMatrixPriceConversionRateConfig",
    "NewFloatingMatrixPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingMatrixPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingMatrixWithAllocationPrice",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfig",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingTieredPrice",
    "NewFloatingTieredPriceConversionRateConfig",
    "NewFloatingTieredPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingTieredBPSPrice",
    "NewFloatingTieredBPSPriceConversionRateConfig",
    "NewFloatingTieredBPSPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingTieredBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingBPSPrice",
    "NewFloatingBPSPriceConversionRateConfig",
    "NewFloatingBPSPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingBulkBPSPrice",
    "NewFloatingBulkBPSPriceConversionRateConfig",
    "NewFloatingBulkBPSPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingBulkBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingBulkPrice",
    "NewFloatingBulkPriceConversionRateConfig",
    "NewFloatingBulkPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingThresholdTotalAmountPrice",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfig",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingTieredPackagePrice",
    "NewFloatingTieredPackagePriceConversionRateConfig",
    "NewFloatingTieredPackagePriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingGroupedTieredPrice",
    "NewFloatingGroupedTieredPriceConversionRateConfig",
    "NewFloatingGroupedTieredPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingGroupedTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingMaxGroupTieredPackagePrice",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfig",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingTieredWithMinimumPrice",
    "NewFloatingTieredWithMinimumPriceConversionRateConfig",
    "NewFloatingTieredWithMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingTieredWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingPackageWithAllocationPrice",
    "NewFloatingPackageWithAllocationPriceConversionRateConfig",
    "NewFloatingPackageWithAllocationPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingPackageWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingTieredPackageWithMinimumPrice",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfig",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingUnitWithPercentPrice",
    "NewFloatingUnitWithPercentPriceConversionRateConfig",
    "NewFloatingUnitWithPercentPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingUnitWithPercentPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingTieredWithProrationPrice",
    "NewFloatingTieredWithProrationPriceConversionRateConfig",
    "NewFloatingTieredWithProrationPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingTieredWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingUnitWithProrationPrice",
    "NewFloatingUnitWithProrationPriceConversionRateConfig",
    "NewFloatingUnitWithProrationPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingUnitWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingGroupedAllocationPrice",
    "NewFloatingGroupedAllocationPriceConversionRateConfig",
    "NewFloatingGroupedAllocationPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingGroupedAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingGroupedWithProratedMinimumPrice",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingGroupedWithMeteredMinimumPrice",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingMatrixWithDisplayNamePrice",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfig",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingBulkWithProrationPrice",
    "NewFloatingBulkWithProrationPriceConversionRateConfig",
    "NewFloatingBulkWithProrationPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingBulkWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingGroupedTieredPackagePrice",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfig",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingScalableMatrixWithUnitPricingPrice",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingScalableMatrixWithTieredPricingPrice",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
    "NewFloatingCumulativeGroupedBulkPrice",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfig",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfig",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfig",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier",
]


class NewFloatingUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[UnitConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingUnitPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingUnitPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingUnitPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingUnitPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingUnitPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingUnitPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingUnitPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[PackageConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingPackagePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingPackagePriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingPackagePriceConversionRateConfig: TypeAlias = Union[
    NewFloatingPackagePriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingPackagePriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_config: Required[MatrixConfig]

    model_type: Required[Literal["matrix"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingMatrixPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMatrixPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingMatrixPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingMatrixPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingMatrixPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingMatrixPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingMatrixPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_allocation_config: Required[MatrixWithAllocationConfig]

    model_type: Required[Literal["matrix_with_allocation"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingMatrixWithAllocationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingMatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingMatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingMatrixWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingMatrixWithAllocationPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingMatrixWithAllocationPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[TieredConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingTieredPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingTieredPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingTieredPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingTieredPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingTieredPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingTieredBPSPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[TieredBPSConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingTieredBPSPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingTieredBPSPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingTieredBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingTieredBPSPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingTieredBPSPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingTieredBPSPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingBPSPrice(TypedDict, total=False):
    bps_config: Required[BPSConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bps"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingBPSPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingBPSPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingBPSPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingBPSPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingBPSPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingBulkBPSPrice(TypedDict, total=False):
    bulk_bps_config: Required[BulkBPSConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk_bps"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingBulkBPSPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingBulkBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingBulkBPSPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingBulkBPSPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingBulkBPSPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingBulkBPSPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingBulkBPSPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingBulkPrice(TypedDict, total=False):
    bulk_config: Required[BulkConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingBulkPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingBulkPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingBulkPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingBulkPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingBulkPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["threshold_total_amount"]]

    name: Required[str]
    """The name of the price."""

    threshold_total_amount_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingThresholdTotalAmountPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingThresholdTotalAmountPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingThresholdTotalAmountPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_package"]]

    name: Required[str]
    """The name of the price."""

    tiered_package_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingTieredPackagePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingTieredPackagePriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[
        Iterable[NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    NewFloatingTieredPackagePriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingTieredPackagePriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_tiered_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_tiered"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingGroupedTieredPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingGroupedTieredPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingGroupedTieredPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[
        Iterable[NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingGroupedTieredPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingGroupedTieredPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingGroupedTieredPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    max_group_tiered_package_config: Required[Dict[str, object]]

    model_type: Required[Literal["max_group_tiered_package"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingMaxGroupTieredPackagePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingMaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingMaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingMaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    NewFloatingMaxGroupTieredPackagePriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingMaxGroupTieredPackagePriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_minimum"]]

    name: Required[str]
    """The name of the price."""

    tiered_with_minimum_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingTieredWithMinimumPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingTieredWithMinimumPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingTieredWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingTieredWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingTieredWithMinimumPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingTieredWithMinimumPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["package_with_allocation"]]

    name: Required[str]
    """The name of the price."""

    package_with_allocation_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingPackageWithAllocationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingPackageWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingPackageWithAllocationPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingPackageWithAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingPackageWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingPackageWithAllocationPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingPackageWithAllocationPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_package_with_minimum"]]

    name: Required[str]
    """The name of the price."""

    tiered_package_with_minimum_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingTieredPackageWithMinimumPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingTieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[
        NewFloatingTieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig
    ]


class NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingTieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingTieredPackageWithMinimumPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingTieredPackageWithMinimumPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit_with_percent"]]

    name: Required[str]
    """The name of the price."""

    unit_with_percent_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingUnitWithPercentPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingUnitWithPercentPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingUnitWithPercentPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingUnitWithPercentPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfig(TypedDict, total=False):
    tiers: Required[
        Iterable[NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingUnitWithPercentPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingUnitWithPercentPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingUnitWithPercentPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingTieredWithProrationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingTieredWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingTieredWithProrationPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingTieredWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingTieredWithProrationPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingTieredWithProrationPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit_with_proration"]]

    name: Required[str]
    """The name of the price."""

    unit_with_proration_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingUnitWithProrationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingUnitWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingUnitWithProrationPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingUnitWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingUnitWithProrationPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingUnitWithProrationPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingUnitWithProrationPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_allocation_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_allocation"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingGroupedAllocationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingGroupedAllocationPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingGroupedAllocationPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingGroupedAllocationPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingGroupedAllocationPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_prorated_minimum_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_prorated_minimum"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[
        NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig
    ]


class NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[
            NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier
        ]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingGroupedWithProratedMinimumPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_metered_minimum_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_metered_minimum"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[
        NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfigUnitConfig
    ]


class NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[
            NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier
        ]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_display_name_config: Required[Dict[str, object]]

    model_type: Required[Literal["matrix_with_display_name"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingMatrixWithDisplayNamePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingMatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingMatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingMatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingMatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Union[
    NewFloatingMatrixWithDisplayNamePriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingMatrixWithDisplayNamePriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[Dict[str, object]]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk_with_proration"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingBulkWithProrationPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingBulkWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingBulkWithProrationPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingBulkWithProrationPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfigTieredConfig]


NewFloatingBulkWithProrationPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingBulkWithProrationPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingBulkWithProrationPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_tiered_package_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_tiered_package"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingGroupedTieredPackagePriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingGroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingGroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingGroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingGroupedTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    NewFloatingGroupedTieredPackagePriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingGroupedTieredPackagePriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_unit_pricing"]]

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_unit_pricing_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[
        NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig
    ]


class NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[
            NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier
        ]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfig(
    TypedDict, total=False
):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_tiered_pricing"]]

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: Required[Dict[str, object]]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfig(
    TypedDict, total=False
):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[
        NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfigUnitConfig
    ]


class NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[
            NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier
        ]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfig(
    TypedDict, total=False
):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfigTieredConversionRateConfig,
]


class NewFloatingCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[Dict[str, object]]

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["cumulative_grouped_bulk"]]

    name: Required[str]
    """The name of the price."""

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[NewFloatingCumulativeGroupedBulkPriceConversionRateConfig]
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration]
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class NewFloatingCumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig(
    TypedDict, total=False
):
    unit_amount: Required[str]
    """Amount per unit of overage"""


class NewFloatingCumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[NewFloatingCumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfigUnitConfig]


class NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier(
    TypedDict, total=False
):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit of overage"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig(
    TypedDict, total=False
):
    tiers: Required[
        Iterable[NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    ]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[
        NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfigTieredConfig
    ]


NewFloatingCumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Union[
    NewFloatingCumulativeGroupedBulkPriceConversionRateConfigUnitConversionRateConfig,
    NewFloatingCumulativeGroupedBulkPriceConversionRateConfigTieredConversionRateConfig,
]

PriceCreateParams: TypeAlias = Union[
    NewFloatingUnitPrice,
    NewFloatingPackagePrice,
    NewFloatingMatrixPrice,
    NewFloatingMatrixWithAllocationPrice,
    NewFloatingTieredPrice,
    NewFloatingTieredBPSPrice,
    NewFloatingBPSPrice,
    NewFloatingBulkBPSPrice,
    NewFloatingBulkPrice,
    NewFloatingThresholdTotalAmountPrice,
    NewFloatingTieredPackagePrice,
    NewFloatingGroupedTieredPrice,
    NewFloatingMaxGroupTieredPackagePrice,
    NewFloatingTieredWithMinimumPrice,
    NewFloatingPackageWithAllocationPrice,
    NewFloatingTieredPackageWithMinimumPrice,
    NewFloatingUnitWithPercentPrice,
    NewFloatingTieredWithProrationPrice,
    NewFloatingUnitWithProrationPrice,
    NewFloatingGroupedAllocationPrice,
    NewFloatingGroupedWithProratedMinimumPrice,
    NewFloatingGroupedWithMeteredMinimumPrice,
    NewFloatingMatrixWithDisplayNamePrice,
    NewFloatingBulkWithProrationPrice,
    NewFloatingGroupedTieredPackagePrice,
    NewFloatingScalableMatrixWithUnitPricingPrice,
    NewFloatingScalableMatrixWithTieredPricingPrice,
    NewFloatingCumulativeGroupedBulkPrice,
]
