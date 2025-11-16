# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.new_floating_bulk_price import NewFloatingBulkPrice
from .shared_params.new_floating_unit_price import NewFloatingUnitPrice
from .shared_params.new_floating_matrix_price import NewFloatingMatrixPrice
from .shared_params.new_floating_tiered_price import NewFloatingTieredPrice
from .shared_params.new_floating_package_price import NewFloatingPackagePrice
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_floating_grouped_tiered_price import NewFloatingGroupedTieredPrice
from .shared_params.new_floating_tiered_package_price import NewFloatingTieredPackagePrice
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration
from .shared_params.new_floating_minimum_composite_price import NewFloatingMinimumCompositePrice
from .shared_params.new_floating_unit_with_percent_price import NewFloatingUnitWithPercentPrice
from .shared_params.new_floating_grouped_allocation_price import NewFloatingGroupedAllocationPrice
from .shared_params.new_floating_bulk_with_proration_price import NewFloatingBulkWithProrationPrice
from .shared_params.new_floating_tiered_with_minimum_price import NewFloatingTieredWithMinimumPrice
from .shared_params.new_floating_unit_with_proration_price import NewFloatingUnitWithProrationPrice
from .shared_params.new_floating_tiered_with_proration_price import NewFloatingTieredWithProrationPrice
from .shared_params.new_floating_grouped_tiered_package_price import NewFloatingGroupedTieredPackagePrice
from .shared_params.new_floating_matrix_with_allocation_price import NewFloatingMatrixWithAllocationPrice
from .shared_params.new_floating_threshold_total_amount_price import NewFloatingThresholdTotalAmountPrice
from .shared_params.new_floating_cumulative_grouped_bulk_price import NewFloatingCumulativeGroupedBulkPrice
from .shared_params.new_floating_package_with_allocation_price import NewFloatingPackageWithAllocationPrice
from .shared_params.new_floating_matrix_with_display_name_price import NewFloatingMatrixWithDisplayNamePrice
from .shared_params.new_floating_max_group_tiered_package_price import NewFloatingMaxGroupTieredPackagePrice
from .shared_params.new_floating_tiered_package_with_minimum_price import NewFloatingTieredPackageWithMinimumPrice
from .shared_params.new_floating_grouped_with_metered_minimum_price import NewFloatingGroupedWithMeteredMinimumPrice
from .shared_params.new_floating_grouped_with_prorated_minimum_price import NewFloatingGroupedWithProratedMinimumPrice
from .shared_params.new_floating_scalable_matrix_with_unit_pricing_price import (
    NewFloatingScalableMatrixWithUnitPricingPrice,
)
from .shared_params.new_floating_scalable_matrix_with_tiered_pricing_price import (
    NewFloatingScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "PriceEvaluateMultipleParams",
    "PriceEvaluation",
    "PriceEvaluationPrice",
    "PriceEvaluationPriceNewFloatingBulkWithFiltersPrice",
    "PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfig",
    "PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "PriceEvaluationPriceNewFloatingBulkWithFiltersPriceConversionRateConfig",
    "PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPrice",
    "PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPrice",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPriceConversionRateConfig",
    "PriceEvaluationPriceNewFloatingPercentCompositePrice",
    "PriceEvaluationPriceNewFloatingPercentCompositePricePercentConfig",
    "PriceEvaluationPriceNewFloatingPercentCompositePriceConversionRateConfig",
    "PriceEvaluationPriceNewFloatingEventOutputPrice",
    "PriceEvaluationPriceNewFloatingEventOutputPriceEventOutputConfig",
    "PriceEvaluationPriceNewFloatingEventOutputPriceConversionRateConfig",
]


class PriceEvaluateMultipleParams(TypedDict, total=False):
    timeframe_end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The exclusive upper bound for event timestamps"""

    timeframe_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The inclusive lower bound for event timestamps"""

    customer_id: Optional[str]
    """The ID of the customer to which this evaluation is scoped."""

    external_customer_id: Optional[str]
    """The external customer ID of the customer to which this evaluation is scoped."""

    price_evaluations: Iterable[PriceEvaluation]
    """List of prices to evaluate (max 100)"""


class PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    filters: Required[Iterable[PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


PriceEvaluationPriceNewFloatingBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceEvaluationPriceNewFloatingBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[PriceEvaluationPriceNewFloatingBulkWithFiltersPriceBulkWithFiltersConfig]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["bulk_with_filters"]]
    """The pricing model type"""

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

    conversion_rate_config: Optional[PriceEvaluationPriceNewFloatingBulkWithFiltersPriceConversionRateConfig]
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


class PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(
    TypedDict, total=False
):
    grouping_key: Required[str]
    """The event property used to group before applying thresholds"""

    maximum_charge: Required[str]
    """The maximum amount to charge each group"""

    minimum_charge: Required[str]
    """The minimum amount to charge each group, regardless of usage"""

    per_unit_rate: Required[str]
    """The base price charged per group"""


PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    grouped_with_min_max_thresholds_config: Required[
        PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
    ]
    """Configuration for grouped_with_min_max_thresholds pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_min_max_thresholds"]]
    """The pricing model type"""

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

    conversion_rate_config: Optional[
        PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPriceConversionRateConfig
    ]
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


class PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(
    TypedDict, total=False
):
    cumulative_allocation: Required[str]
    """The overall allocation across all groups"""

    group_allocation: Required[str]
    """The allocation per individual group"""

    grouping_key: Required[str]
    """The event property used to group usage before applying allocations"""

    unit_amount: Required[str]
    """The amount to charge for each unit outside of the allocation"""


PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["cumulative_grouped_allocation"]]
    """The pricing model type"""

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

    conversion_rate_config: Optional[
        PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPriceConversionRateConfig
    ]
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


class PriceEvaluationPriceNewFloatingPercentCompositePricePercentConfig(TypedDict, total=False):
    percent: Required[float]
    """What percent of the component subtotals to charge"""


PriceEvaluationPriceNewFloatingPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceEvaluationPriceNewFloatingPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[PriceEvaluationPriceNewFloatingPercentCompositePricePercentConfig]
    """Configuration for percent pricing"""

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

    conversion_rate_config: Optional[PriceEvaluationPriceNewFloatingPercentCompositePriceConversionRateConfig]
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


class PriceEvaluationPriceNewFloatingEventOutputPriceEventOutputConfig(TypedDict, total=False):
    unit_rating_key: Required[str]
    """The key in the event data to extract the unit rate from."""

    default_unit_rate: Optional[str]
    """
    If provided, this amount will be used as the unit rate when an event does not
    have a value for the `unit_rating_key`. If not provided, events missing a unit
    rate will be ignored.
    """

    grouping_key: Optional[str]
    """An optional key in the event data to group by (e.g., event ID).

    All events will also be grouped by their unit rate.
    """


PriceEvaluationPriceNewFloatingEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class PriceEvaluationPriceNewFloatingEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    event_output_config: Required[PriceEvaluationPriceNewFloatingEventOutputPriceEventOutputConfig]
    """Configuration for event_output pricing"""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["event_output"]]
    """The pricing model type"""

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

    conversion_rate_config: Optional[PriceEvaluationPriceNewFloatingEventOutputPriceConversionRateConfig]
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


PriceEvaluationPrice: TypeAlias = Union[
    NewFloatingUnitPrice,
    NewFloatingTieredPrice,
    NewFloatingBulkPrice,
    PriceEvaluationPriceNewFloatingBulkWithFiltersPrice,
    NewFloatingPackagePrice,
    NewFloatingMatrixPrice,
    NewFloatingThresholdTotalAmountPrice,
    NewFloatingTieredPackagePrice,
    NewFloatingTieredWithMinimumPrice,
    NewFloatingGroupedTieredPrice,
    NewFloatingTieredPackageWithMinimumPrice,
    NewFloatingPackageWithAllocationPrice,
    NewFloatingUnitWithPercentPrice,
    NewFloatingMatrixWithAllocationPrice,
    NewFloatingTieredWithProrationPrice,
    NewFloatingUnitWithProrationPrice,
    NewFloatingGroupedAllocationPrice,
    NewFloatingBulkWithProrationPrice,
    NewFloatingGroupedWithProratedMinimumPrice,
    NewFloatingGroupedWithMeteredMinimumPrice,
    PriceEvaluationPriceNewFloatingGroupedWithMinMaxThresholdsPrice,
    NewFloatingMatrixWithDisplayNamePrice,
    NewFloatingGroupedTieredPackagePrice,
    NewFloatingMaxGroupTieredPackagePrice,
    NewFloatingScalableMatrixWithUnitPricingPrice,
    NewFloatingScalableMatrixWithTieredPricingPrice,
    NewFloatingCumulativeGroupedBulkPrice,
    PriceEvaluationPriceNewFloatingCumulativeGroupedAllocationPrice,
    NewFloatingMinimumCompositePrice,
    PriceEvaluationPriceNewFloatingPercentCompositePrice,
    PriceEvaluationPriceNewFloatingEventOutputPrice,
]


class PriceEvaluation(TypedDict, total=False):
    external_price_id: Optional[str]
    """The external ID of a price to evaluate that exists in your Orb account."""

    filter: Optional[str]
    """
    A boolean
    [computed property](/extensibility/advanced-metrics#computed-properties) used to
    filter the underlying billable metric
    """

    grouping_keys: SequenceNotStr[str]
    """
    Properties (or
    [computed properties](/extensibility/advanced-metrics#computed-properties)) used
    to group the underlying billable metric
    """

    price: Optional[PriceEvaluationPrice]
    """New floating price request body params."""

    price_id: Optional[str]
    """The ID of a price to evaluate that exists in your Orb account."""
