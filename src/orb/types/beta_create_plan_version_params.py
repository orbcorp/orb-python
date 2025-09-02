# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.new_usage_discount import NewUsageDiscount
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared_params.new_plan_bulk_price import NewPlanBulkPrice
from .shared_params.new_plan_unit_price import NewPlanUnitPrice
from .shared_params.new_allocation_price import NewAllocationPrice
from .shared_params.new_plan_matrix_price import NewPlanMatrixPrice
from .shared_params.new_plan_tiered_price import NewPlanTieredPrice
from .shared_params.new_plan_package_price import NewPlanPackagePrice
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.new_plan_grouped_tiered_price import NewPlanGroupedTieredPrice
from .shared_params.new_plan_tiered_package_price import NewPlanTieredPackagePrice
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_plan_unit_with_percent_price import NewPlanUnitWithPercentPrice
from .shared_params.new_plan_grouped_allocation_price import NewPlanGroupedAllocationPrice
from .shared_params.new_plan_bulk_with_proration_price import NewPlanBulkWithProrationPrice
from .shared_params.new_plan_tier_with_proration_price import NewPlanTierWithProrationPrice
from .shared_params.new_plan_tiered_with_minimum_price import NewPlanTieredWithMinimumPrice
from .shared_params.new_plan_unit_with_proration_price import NewPlanUnitWithProrationPrice
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration
from .shared_params.new_plan_grouped_tiered_package_price import NewPlanGroupedTieredPackagePrice
from .shared_params.new_plan_matrix_with_allocation_price import NewPlanMatrixWithAllocationPrice
from .shared_params.new_plan_threshold_total_amount_price import NewPlanThresholdTotalAmountPrice
from .shared_params.new_plan_cumulative_grouped_bulk_price import NewPlanCumulativeGroupedBulkPrice
from .shared_params.new_plan_package_with_allocation_price import NewPlanPackageWithAllocationPrice
from .shared_params.new_plan_matrix_with_display_name_price import NewPlanMatrixWithDisplayNamePrice
from .shared_params.new_plan_max_group_tiered_package_price import NewPlanMaxGroupTieredPackagePrice
from .shared_params.new_plan_tiered_package_with_minimum_price import NewPlanTieredPackageWithMinimumPrice
from .shared_params.new_plan_grouped_with_metered_minimum_price import NewPlanGroupedWithMeteredMinimumPrice
from .shared_params.new_plan_grouped_with_prorated_minimum_price import NewPlanGroupedWithProratedMinimumPrice
from .shared_params.new_plan_scalable_matrix_with_unit_pricing_price import NewPlanScalableMatrixWithUnitPricingPrice
from .shared_params.new_plan_scalable_matrix_with_tiered_pricing_price import (
    NewPlanScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "BetaCreatePlanVersionParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddPrice",
    "AddPricePrice",
    "AddPricePriceNewPlanGroupedWithMinMaxThresholdsPrice",
    "AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent154",
    "AddPricePriceNewPlanMinimumCompositePrice",
    "AddPricePriceNewPlanMinimumCompositePriceMinimumConfig",
    "AddPricePriceNewPlanMinimumCompositePriceUnnamedTypeWithobjectParent155",
    "RemoveAdjustment",
    "RemovePrice",
    "ReplaceAdjustment",
    "ReplaceAdjustmentAdjustment",
    "ReplacePrice",
    "ReplacePricePrice",
    "ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPrice",
    "ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent156",
    "ReplacePricePriceNewPlanMinimumCompositePrice",
    "ReplacePricePriceNewPlanMinimumCompositePriceMinimumConfig",
    "ReplacePricePriceNewPlanMinimumCompositePriceUnnamedTypeWithobjectParent157",
]


class BetaCreatePlanVersionParams(TypedDict, total=False):
    version: Required[int]
    """New version number."""

    add_adjustments: Optional[Iterable[AddAdjustment]]
    """Additional adjustments to be added to the plan."""

    add_prices: Optional[Iterable[AddPrice]]
    """Additional prices to be added to the plan."""

    remove_adjustments: Optional[Iterable[RemoveAdjustment]]
    """Adjustments to be removed from the plan."""

    remove_prices: Optional[Iterable[RemovePrice]]
    """Prices to be removed from the plan."""

    replace_adjustments: Optional[Iterable[ReplaceAdjustment]]
    """Adjustments to be replaced with additional adjustments on the plan."""

    replace_prices: Optional[Iterable[ReplacePrice]]
    """Prices to be replaced with additional prices on the plan."""

    set_as_default: Optional[bool]
    """Set this new plan version as the default"""


AddAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this adjustment to."""


AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent154: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_min_max_thresholds"]]

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

    conversion_rate_config: Optional[AddPricePriceNewPlanGroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent154]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class AddPricePriceNewPlanMinimumCompositePriceMinimumConfig(TypedDict, total=False):
    minimum_amount: Required[str]
    """The minimum amount to apply"""

    prorated: Optional[bool]
    """
    By default, subtotals from minimum composite prices are prorated based on the
    service period. Set to false to disable proration.
    """


AddPricePriceNewPlanMinimumCompositePriceUnnamedTypeWithobjectParent155: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewPlanMinimumCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    minimum_config: Required[AddPricePriceNewPlanMinimumCompositePriceMinimumConfig]

    model_type: Required[Literal["minimum"]]

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

    conversion_rate_config: Optional[AddPricePriceNewPlanMinimumCompositePriceUnnamedTypeWithobjectParent155]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


AddPricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanPackagePrice,
    NewPlanMatrixPrice,
    NewPlanTieredPrice,
    NewPlanBulkPrice,
    NewPlanThresholdTotalAmountPrice,
    NewPlanTieredPackagePrice,
    NewPlanTieredWithMinimumPrice,
    NewPlanUnitWithPercentPrice,
    NewPlanPackageWithAllocationPrice,
    NewPlanTierWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    AddPricePriceNewPlanGroupedWithMinMaxThresholdsPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    NewPlanTieredPackageWithMinimumPrice,
    NewPlanMatrixWithAllocationPrice,
    NewPlanGroupedTieredPrice,
    AddPricePriceNewPlanMinimumCompositePrice,
]


class AddPrice(TypedDict, total=False):
    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this price to."""

    price: Optional[AddPricePrice]
    """The price to add to the plan"""


class RemoveAdjustment(TypedDict, total=False):
    adjustment_id: Required[str]
    """The id of the adjustment to remove from on the plan."""

    plan_phase_order: Optional[int]
    """The phase to remove this adjustment from."""


class RemovePrice(TypedDict, total=False):
    price_id: Required[str]
    """The id of the price to remove from the plan."""

    plan_phase_order: Optional[int]
    """The phase to remove this price from."""


ReplaceAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class ReplaceAdjustment(TypedDict, total=False):
    adjustment: Required[ReplaceAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this adjustment from."""


ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent156: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["grouped_with_min_max_thresholds"]]

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
        ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPriceUnnamedTypeWithobjectParent156
    ]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class ReplacePricePriceNewPlanMinimumCompositePriceMinimumConfig(TypedDict, total=False):
    minimum_amount: Required[str]
    """The minimum amount to apply"""

    prorated: Optional[bool]
    """
    By default, subtotals from minimum composite prices are prorated based on the
    service period. Set to false to disable proration.
    """


ReplacePricePriceNewPlanMinimumCompositePriceUnnamedTypeWithobjectParent157: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewPlanMinimumCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    minimum_config: Required[ReplacePricePriceNewPlanMinimumCompositePriceMinimumConfig]

    model_type: Required[Literal["minimum"]]

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

    conversion_rate_config: Optional[ReplacePricePriceNewPlanMinimumCompositePriceUnnamedTypeWithobjectParent157]
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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

    reference_id: Optional[str]
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


ReplacePricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanPackagePrice,
    NewPlanMatrixPrice,
    NewPlanTieredPrice,
    NewPlanBulkPrice,
    NewPlanThresholdTotalAmountPrice,
    NewPlanTieredPackagePrice,
    NewPlanTieredWithMinimumPrice,
    NewPlanUnitWithPercentPrice,
    NewPlanPackageWithAllocationPrice,
    NewPlanTierWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    ReplacePricePriceNewPlanGroupedWithMinMaxThresholdsPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    NewPlanTieredPackageWithMinimumPrice,
    NewPlanMatrixWithAllocationPrice,
    NewPlanGroupedTieredPrice,
    ReplacePricePriceNewPlanMinimumCompositePrice,
]


class ReplacePrice(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the plan."""

    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this price from."""

    price: Optional[ReplacePricePrice]
    """The price to add to the plan"""
