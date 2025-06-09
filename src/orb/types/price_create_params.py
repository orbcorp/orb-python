# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.bps_config import BPSConfig
from .shared_params.bulk_config import BulkConfig
from .shared_params.unit_config import UnitConfig
from .shared_params.matrix_config import MatrixConfig
from .shared_params.tiered_config import TieredConfig
from .shared_params.package_config import PackageConfig
from .shared_params.bulk_bps_config import BulkBPSConfig
from .shared_params.tiered_bps_config import TieredBPSConfig
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.matrix_with_allocation_config import MatrixWithAllocationConfig
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "PriceCreateParams",
    "NewFloatingUnitPrice",
    "NewFloatingUnitPriceConversionRateConfig",
    "NewFloatingPackagePrice",
    "NewFloatingPackagePriceConversionRateConfig",
    "NewFloatingMatrixPrice",
    "NewFloatingMatrixPriceConversionRateConfig",
    "NewFloatingMatrixWithAllocationPrice",
    "NewFloatingMatrixWithAllocationPriceConversionRateConfig",
    "NewFloatingTieredPrice",
    "NewFloatingTieredPriceConversionRateConfig",
    "NewFloatingTieredBPSPrice",
    "NewFloatingTieredBPSPriceConversionRateConfig",
    "NewFloatingBPSPrice",
    "NewFloatingBPSPriceConversionRateConfig",
    "NewFloatingBulkBPSPrice",
    "NewFloatingBulkBPSPriceConversionRateConfig",
    "NewFloatingBulkPrice",
    "NewFloatingBulkPriceConversionRateConfig",
    "NewFloatingThresholdTotalAmountPrice",
    "NewFloatingThresholdTotalAmountPriceConversionRateConfig",
    "NewFloatingTieredPackagePrice",
    "NewFloatingTieredPackagePriceConversionRateConfig",
    "NewFloatingGroupedTieredPrice",
    "NewFloatingGroupedTieredPriceConversionRateConfig",
    "NewFloatingMaxGroupTieredPackagePrice",
    "NewFloatingMaxGroupTieredPackagePriceConversionRateConfig",
    "NewFloatingTieredWithMinimumPrice",
    "NewFloatingTieredWithMinimumPriceConversionRateConfig",
    "NewFloatingPackageWithAllocationPrice",
    "NewFloatingPackageWithAllocationPriceConversionRateConfig",
    "NewFloatingTieredPackageWithMinimumPrice",
    "NewFloatingTieredPackageWithMinimumPriceConversionRateConfig",
    "NewFloatingUnitWithPercentPrice",
    "NewFloatingUnitWithPercentPriceConversionRateConfig",
    "NewFloatingTieredWithProrationPrice",
    "NewFloatingTieredWithProrationPriceConversionRateConfig",
    "NewFloatingUnitWithProrationPrice",
    "NewFloatingUnitWithProrationPriceConversionRateConfig",
    "NewFloatingGroupedAllocationPrice",
    "NewFloatingGroupedAllocationPriceConversionRateConfig",
    "NewFloatingGroupedWithProratedMinimumPrice",
    "NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig",
    "NewFloatingGroupedWithMeteredMinimumPrice",
    "NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig",
    "NewFloatingMatrixWithDisplayNamePrice",
    "NewFloatingMatrixWithDisplayNamePriceConversionRateConfig",
    "NewFloatingBulkWithProrationPrice",
    "NewFloatingBulkWithProrationPriceConversionRateConfig",
    "NewFloatingGroupedTieredPackagePrice",
    "NewFloatingGroupedTieredPackagePriceConversionRateConfig",
    "NewFloatingScalableMatrixWithUnitPricingPrice",
    "NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig",
    "NewFloatingScalableMatrixWithTieredPricingPrice",
    "NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig",
    "NewFloatingCumulativeGroupedBulkPrice",
    "NewFloatingCumulativeGroupedBulkPriceConversionRateConfig",
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


NewFloatingUnitPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingPackagePriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingMatrixPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingMatrixWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingTieredPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingTieredBPSPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingBPSPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingBulkBPSPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingBulkPriceConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


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


NewFloatingThresholdTotalAmountPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingGroupedTieredPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingMaxGroupTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingTieredWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingPackageWithAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingTieredPackageWithMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingUnitWithPercentPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingUnitWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingGroupedWithProratedMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingGroupedWithMeteredMinimumPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingMatrixWithDisplayNamePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingBulkWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingGroupedTieredPackagePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingScalableMatrixWithUnitPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingScalableMatrixWithTieredPricingPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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


NewFloatingCumulativeGroupedBulkPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
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
