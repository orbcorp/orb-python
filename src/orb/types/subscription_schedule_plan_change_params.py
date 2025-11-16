# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .discount_override_param import DiscountOverrideParam
from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.new_usage_discount import NewUsageDiscount
from .new_subscription_bulk_price_param import NewSubscriptionBulkPriceParam
from .new_subscription_unit_price_param import NewSubscriptionUnitPriceParam
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared_params.new_allocation_price import NewAllocationPrice
from .new_subscription_matrix_price_param import NewSubscriptionMatrixPriceParam
from .new_subscription_tiered_price_param import NewSubscriptionTieredPriceParam
from .new_subscription_package_price_param import NewSubscriptionPackagePriceParam
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .new_subscription_grouped_tiered_price_param import NewSubscriptionGroupedTieredPriceParam
from .new_subscription_tiered_package_price_param import NewSubscriptionTieredPackagePriceParam
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .new_subscription_minimum_composite_price_param import NewSubscriptionMinimumCompositePriceParam
from .new_subscription_unit_with_percent_price_param import NewSubscriptionUnitWithPercentPriceParam
from .new_subscription_grouped_allocation_price_param import NewSubscriptionGroupedAllocationPriceParam
from .new_subscription_bulk_with_proration_price_param import NewSubscriptionBulkWithProrationPriceParam
from .new_subscription_tiered_with_minimum_price_param import NewSubscriptionTieredWithMinimumPriceParam
from .new_subscription_unit_with_proration_price_param import NewSubscriptionUnitWithProrationPriceParam
from .shared_params.billing_cycle_anchor_configuration import BillingCycleAnchorConfiguration
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration
from .new_subscription_grouped_tiered_package_price_param import NewSubscriptionGroupedTieredPackagePriceParam
from .new_subscription_matrix_with_allocation_price_param import NewSubscriptionMatrixWithAllocationPriceParam
from .new_subscription_threshold_total_amount_price_param import NewSubscriptionThresholdTotalAmountPriceParam
from .new_subscription_cumulative_grouped_bulk_price_param import NewSubscriptionCumulativeGroupedBulkPriceParam
from .new_subscription_package_with_allocation_price_param import NewSubscriptionPackageWithAllocationPriceParam
from .new_subscription_matrix_with_display_name_price_param import NewSubscriptionMatrixWithDisplayNamePriceParam
from .new_subscription_max_group_tiered_package_price_param import NewSubscriptionMaxGroupTieredPackagePriceParam
from .new_subscription_tiered_package_with_minimum_price_param import NewSubscriptionTieredPackageWithMinimumPriceParam
from .new_subscription_grouped_with_metered_minimum_price_param import (
    NewSubscriptionGroupedWithMeteredMinimumPriceParam,
)
from .new_subscription_grouped_with_prorated_minimum_price_param import (
    NewSubscriptionGroupedWithProratedMinimumPriceParam,
)
from .new_subscription_scalable_matrix_with_unit_pricing_price_param import (
    NewSubscriptionScalableMatrixWithUnitPricingPriceParam,
)
from .new_subscription_scalable_matrix_with_tiered_pricing_price_param import (
    NewSubscriptionScalableMatrixWithTieredPricingPriceParam,
)

__all__ = [
    "SubscriptionSchedulePlanChangeParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddPrice",
    "AddPricePrice",
    "AddPricePriceNewSubscriptionBulkWithFiltersPrice",
    "AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfig",
    "AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "AddPricePriceNewSubscriptionBulkWithFiltersPriceConversionRateConfig",
    "AddPricePriceNewSubscriptionTieredWithProrationPrice",
    "AddPricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfig",
    "AddPricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfigTier",
    "AddPricePriceNewSubscriptionTieredWithProrationPriceConversionRateConfig",
    "AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPrice",
    "AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "AddPricePriceNewSubscriptionCumulativeGroupedAllocationPrice",
    "AddPricePriceNewSubscriptionCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "AddPricePriceNewSubscriptionCumulativeGroupedAllocationPriceConversionRateConfig",
    "AddPricePriceNewSubscriptionPercentCompositePrice",
    "AddPricePriceNewSubscriptionPercentCompositePricePercentConfig",
    "AddPricePriceNewSubscriptionPercentCompositePriceConversionRateConfig",
    "AddPricePriceNewSubscriptionEventOutputPrice",
    "AddPricePriceNewSubscriptionEventOutputPriceEventOutputConfig",
    "AddPricePriceNewSubscriptionEventOutputPriceConversionRateConfig",
    "RemoveAdjustment",
    "RemovePrice",
    "ReplaceAdjustment",
    "ReplaceAdjustmentAdjustment",
    "ReplacePrice",
    "ReplacePricePrice",
    "ReplacePricePriceNewSubscriptionBulkWithFiltersPrice",
    "ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfig",
    "ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigFilter",
    "ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigTier",
    "ReplacePricePriceNewSubscriptionBulkWithFiltersPriceConversionRateConfig",
    "ReplacePricePriceNewSubscriptionTieredWithProrationPrice",
    "ReplacePricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfig",
    "ReplacePricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfigTier",
    "ReplacePricePriceNewSubscriptionTieredWithProrationPriceConversionRateConfig",
    "ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPrice",
    "ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig",
    "ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceConversionRateConfig",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPrice",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPriceConversionRateConfig",
    "ReplacePricePriceNewSubscriptionPercentCompositePrice",
    "ReplacePricePriceNewSubscriptionPercentCompositePricePercentConfig",
    "ReplacePricePriceNewSubscriptionPercentCompositePriceConversionRateConfig",
    "ReplacePricePriceNewSubscriptionEventOutputPrice",
    "ReplacePricePriceNewSubscriptionEventOutputPriceEventOutputConfig",
    "ReplacePricePriceNewSubscriptionEventOutputPriceConversionRateConfig",
]


class SubscriptionSchedulePlanChangeParams(TypedDict, total=False):
    change_option: Required[Literal["requested_date", "end_of_subscription_term", "immediate"]]

    add_adjustments: Optional[Iterable[AddAdjustment]]
    """Additional adjustments to be added to the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    add_prices: Optional[Iterable[AddPrice]]
    """Additional prices to be added to the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    align_billing_with_plan_change_date: Optional[bool]
    """[DEPRECATED] Use billing_cycle_alignment instead.

    Reset billing periods to be aligned with the plan change's effective date.
    """

    auto_collection: Optional[bool]
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. If not specified, this
    defaults to the behavior configured for this customer.
    """

    billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]]
    """
    Reset billing periods to be aligned with the plan change's effective date or
    start of the month. Defaults to `unchanged` which keeps subscription's existing
    billing cycle alignment.
    """

    billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration]

    change_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The date that the plan change should take effect.

    This parameter can only be passed if the `change_option` is `requested_date`. If
    a date with no time is passed, the plan change will happen at midnight in the
    customer's timezone.
    """

    coupon_redemption_code: Optional[str]
    """Redemption code to be used for this subscription.

    If the coupon cannot be found by its redemption code, or cannot be redeemed, an
    error response will be returned and the subscription creation or plan change
    will not be scheduled.
    """

    credits_overage_rate: Optional[float]

    default_invoice_memo: Optional[str]
    """Determines the default memo on this subscription's invoices.

    Note that if this is not provided, it is determined by the plan configuration.
    """

    external_plan_id: Optional[str]
    """
    The external_plan_id of the plan that the given subscription should be switched
    to. Note that either this property or `plan_id` must be specified.
    """

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](/extensibility/advanced-metrics#computed-properties). If
    null, usage queries will not include any additional filter.
    """

    initial_phase_order: Optional[int]
    """The phase of the plan to start with"""

    invoicing_threshold: Optional[str]
    """
    When this subscription's accrued usage reaches this threshold, an invoice will
    be issued for the subscription. If not specified, invoices will only be issued
    at the end of the billing period.
    """

    net_terms: Optional[int]
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0. If not provided, this defaults to the value specified in the plan.
    """

    per_credit_overage_amount: Optional[float]

    plan_id: Optional[str]
    """The plan that the given subscription should be switched to.

    Note that either this property or `external_plan_id` must be specified.
    """

    plan_version_number: Optional[int]
    """Specifies which version of the plan to change to.

    If null, the default version will be used.
    """

    price_overrides: Optional[Iterable[object]]
    """Optionally provide a list of overrides for prices on the plan"""

    remove_adjustments: Optional[Iterable[RemoveAdjustment]]
    """Plan adjustments to be removed from the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    remove_prices: Optional[Iterable[RemovePrice]]
    """Plan prices to be removed from the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    replace_adjustments: Optional[Iterable[ReplaceAdjustment]]
    """Plan adjustments to be replaced with additional adjustments on the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    replace_prices: Optional[Iterable[ReplacePrice]]
    """Plan prices to be replaced with additional prices on the subscription.

    (Only available for accounts that have migrated off of legacy subscription
    overrides)
    """

    trial_duration_days: Optional[int]
    """The duration of the trial period in days.

    If not provided, this defaults to the value specified in the plan. If `0` is
    provided, the trial on the plan will be skipped.
    """

    usage_customer_ids: Optional[SequenceNotStr[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


AddAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The end date of the adjustment interval.

    This is the date that the adjustment will stop affecting prices on the
    subscription.
    """

    plan_phase_order: Optional[int]
    """The phase to add this adjustment to."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The start date of the adjustment interval.

    This is the date that the adjustment will start affecting prices on the
    subscription. If null, the adjustment will start when the phase or subscription
    starts.
    """


class AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    filters: Required[Iterable[AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


AddPricePriceNewSubscriptionBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewSubscriptionBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[AddPricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfig]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    conversion_rate_config: Optional[AddPricePriceNewSubscriptionBulkWithFiltersPriceConversionRateConfig]
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


class AddPricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class AddPricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfigTier]]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


AddPricePriceNewSubscriptionTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewSubscriptionTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[
        AddPricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfig
    ]
    """Configuration for tiered_with_proration pricing"""

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

    conversion_rate_config: Optional[AddPricePriceNewSubscriptionTieredWithProrationPriceConversionRateConfig]
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


class AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(
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


AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
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

    conversion_rate_config: Optional[AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceConversionRateConfig]
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


class AddPricePriceNewSubscriptionCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(
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


AddPricePriceNewSubscriptionCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewSubscriptionCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        AddPricePriceNewSubscriptionCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

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

    conversion_rate_config: Optional[AddPricePriceNewSubscriptionCumulativeGroupedAllocationPriceConversionRateConfig]
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


class AddPricePriceNewSubscriptionPercentCompositePricePercentConfig(TypedDict, total=False):
    percent: Required[float]
    """What percent of the component subtotals to charge"""


AddPricePriceNewSubscriptionPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewSubscriptionPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[AddPricePriceNewSubscriptionPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[AddPricePriceNewSubscriptionPercentCompositePriceConversionRateConfig]
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


class AddPricePriceNewSubscriptionEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


AddPricePriceNewSubscriptionEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class AddPricePriceNewSubscriptionEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[AddPricePriceNewSubscriptionEventOutputPriceEventOutputConfig]
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

    conversion_rate_config: Optional[AddPricePriceNewSubscriptionEventOutputPriceConversionRateConfig]
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
    NewSubscriptionUnitPriceParam,
    NewSubscriptionTieredPriceParam,
    NewSubscriptionBulkPriceParam,
    AddPricePriceNewSubscriptionBulkWithFiltersPrice,
    NewSubscriptionPackagePriceParam,
    NewSubscriptionMatrixPriceParam,
    NewSubscriptionThresholdTotalAmountPriceParam,
    NewSubscriptionTieredPackagePriceParam,
    NewSubscriptionTieredWithMinimumPriceParam,
    NewSubscriptionGroupedTieredPriceParam,
    NewSubscriptionTieredPackageWithMinimumPriceParam,
    NewSubscriptionPackageWithAllocationPriceParam,
    NewSubscriptionUnitWithPercentPriceParam,
    NewSubscriptionMatrixWithAllocationPriceParam,
    AddPricePriceNewSubscriptionTieredWithProrationPrice,
    NewSubscriptionUnitWithProrationPriceParam,
    NewSubscriptionGroupedAllocationPriceParam,
    NewSubscriptionBulkWithProrationPriceParam,
    NewSubscriptionGroupedWithProratedMinimumPriceParam,
    NewSubscriptionGroupedWithMeteredMinimumPriceParam,
    AddPricePriceNewSubscriptionGroupedWithMinMaxThresholdsPrice,
    NewSubscriptionMatrixWithDisplayNamePriceParam,
    NewSubscriptionGroupedTieredPackagePriceParam,
    NewSubscriptionMaxGroupTieredPackagePriceParam,
    NewSubscriptionScalableMatrixWithUnitPricingPriceParam,
    NewSubscriptionScalableMatrixWithTieredPricingPriceParam,
    NewSubscriptionCumulativeGroupedBulkPriceParam,
    AddPricePriceNewSubscriptionCumulativeGroupedAllocationPrice,
    NewSubscriptionMinimumCompositePriceParam,
    AddPricePriceNewSubscriptionPercentCompositePrice,
    AddPricePriceNewSubscriptionEventOutputPrice,
]


class AddPrice(TypedDict, total=False):
    allocation_price: Optional[NewAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[Iterable[DiscountOverrideParam]]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for this price.
    """

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The end date of the price interval.

    This is the date that the price will stop billing on the subscription. If null,
    billing will end when the phase or subscription ends.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    maximum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for this price.
    """

    minimum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for this price.
    """

    plan_phase_order: Optional[int]
    """The phase to add this price to."""

    price: Optional[AddPricePrice]
    """New subscription price request body params."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription. If null,
    billing will start when the phase or subscription starts.
    """


class RemoveAdjustment(TypedDict, total=False):
    adjustment_id: Required[str]
    """The id of the adjustment to remove on the subscription."""


class RemovePrice(TypedDict, total=False):
    external_price_id: Optional[str]
    """The external price id of the price to remove on the subscription."""

    price_id: Optional[str]
    """The id of the price to remove on the subscription."""


ReplaceAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class ReplaceAdjustment(TypedDict, total=False):
    adjustment: Required[ReplaceAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the subscription."""


class ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigFilter(TypedDict, total=False):
    property_key: Required[str]
    """Event property key to filter on"""

    property_value: Required[str]
    """Event property value to match"""


class ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    tier_lower_bound: Optional[str]
    """The lower bound for this tier"""


class ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfig(TypedDict, total=False):
    filters: Required[Iterable[ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigFilter]]
    """Property filters to apply (all must match)"""

    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


ReplacePricePriceNewSubscriptionBulkWithFiltersPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewSubscriptionBulkWithFiltersPrice(TypedDict, total=False):
    bulk_with_filters_config: Required[ReplacePricePriceNewSubscriptionBulkWithFiltersPriceBulkWithFiltersConfig]
    """Configuration for bulk_with_filters pricing"""

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    conversion_rate_config: Optional[ReplacePricePriceNewSubscriptionBulkWithFiltersPriceConversionRateConfig]
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


class ReplacePricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""


class ReplacePricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfigTier]]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


ReplacePricePriceNewSubscriptionTieredWithProrationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewSubscriptionTieredWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_proration"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_proration_config: Required[
        ReplacePricePriceNewSubscriptionTieredWithProrationPriceTieredWithProrationConfig
    ]
    """Configuration for tiered_with_proration pricing"""

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

    conversion_rate_config: Optional[ReplacePricePriceNewSubscriptionTieredWithProrationPriceConversionRateConfig]
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


class ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig(
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


ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_min_max_thresholds_config: Required[
        ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceGroupedWithMinMaxThresholdsConfig
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
        ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPriceConversionRateConfig
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


class ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig(
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


ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_allocation_config: Required[
        ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPriceCumulativeGroupedAllocationConfig
    ]
    """Configuration for cumulative_grouped_allocation pricing"""

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
        ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPriceConversionRateConfig
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


class ReplacePricePriceNewSubscriptionPercentCompositePricePercentConfig(TypedDict, total=False):
    percent: Required[float]
    """What percent of the component subtotals to charge"""


ReplacePricePriceNewSubscriptionPercentCompositePriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewSubscriptionPercentCompositePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["percent"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    percent_config: Required[ReplacePricePriceNewSubscriptionPercentCompositePricePercentConfig]
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

    conversion_rate_config: Optional[ReplacePricePriceNewSubscriptionPercentCompositePriceConversionRateConfig]
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


class ReplacePricePriceNewSubscriptionEventOutputPriceEventOutputConfig(TypedDict, total=False):
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


ReplacePricePriceNewSubscriptionEventOutputPriceConversionRateConfig: TypeAlias = Union[
    UnitConversionRateConfig, TieredConversionRateConfig
]


class ReplacePricePriceNewSubscriptionEventOutputPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    event_output_config: Required[ReplacePricePriceNewSubscriptionEventOutputPriceEventOutputConfig]
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

    conversion_rate_config: Optional[ReplacePricePriceNewSubscriptionEventOutputPriceConversionRateConfig]
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
    NewSubscriptionUnitPriceParam,
    NewSubscriptionTieredPriceParam,
    NewSubscriptionBulkPriceParam,
    ReplacePricePriceNewSubscriptionBulkWithFiltersPrice,
    NewSubscriptionPackagePriceParam,
    NewSubscriptionMatrixPriceParam,
    NewSubscriptionThresholdTotalAmountPriceParam,
    NewSubscriptionTieredPackagePriceParam,
    NewSubscriptionTieredWithMinimumPriceParam,
    NewSubscriptionGroupedTieredPriceParam,
    NewSubscriptionTieredPackageWithMinimumPriceParam,
    NewSubscriptionPackageWithAllocationPriceParam,
    NewSubscriptionUnitWithPercentPriceParam,
    NewSubscriptionMatrixWithAllocationPriceParam,
    ReplacePricePriceNewSubscriptionTieredWithProrationPrice,
    NewSubscriptionUnitWithProrationPriceParam,
    NewSubscriptionGroupedAllocationPriceParam,
    NewSubscriptionBulkWithProrationPriceParam,
    NewSubscriptionGroupedWithProratedMinimumPriceParam,
    NewSubscriptionGroupedWithMeteredMinimumPriceParam,
    ReplacePricePriceNewSubscriptionGroupedWithMinMaxThresholdsPrice,
    NewSubscriptionMatrixWithDisplayNamePriceParam,
    NewSubscriptionGroupedTieredPackagePriceParam,
    NewSubscriptionMaxGroupTieredPackagePriceParam,
    NewSubscriptionScalableMatrixWithUnitPricingPriceParam,
    NewSubscriptionScalableMatrixWithTieredPricingPriceParam,
    NewSubscriptionCumulativeGroupedBulkPriceParam,
    ReplacePricePriceNewSubscriptionCumulativeGroupedAllocationPrice,
    NewSubscriptionMinimumCompositePriceParam,
    ReplacePricePriceNewSubscriptionPercentCompositePrice,
    ReplacePricePriceNewSubscriptionEventOutputPrice,
]


class ReplacePrice(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the subscription."""

    allocation_price: Optional[NewAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[Iterable[DiscountOverrideParam]]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for the replacement price.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    fixed_price_quantity: Optional[float]
    """The new quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for the replacement price.
    """

    minimum_amount: Optional[str]
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for the replacement price.
    """

    price: Optional[ReplacePricePrice]
    """New subscription price request body params."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""
