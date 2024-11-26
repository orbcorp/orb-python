# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SubscriptionCreateParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddAdjustmentAdjustmentNewPercentageDiscount",
    "AddAdjustmentAdjustmentNewUsageDiscount",
    "AddAdjustmentAdjustmentNewAmountDiscount",
    "AddAdjustmentAdjustmentNewMinimum",
    "AddAdjustmentAdjustmentNewMaximum",
    "AddPrice",
    "AddPriceDiscount",
    "AddPricePrice",
    "AddPricePriceNewSubscriptionUnitPrice",
    "AddPricePriceNewSubscriptionUnitPriceUnitConfig",
    "AddPricePriceNewSubscriptionUnitPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackagePrice",
    "AddPricePriceNewSubscriptionPackagePricePackageConfig",
    "AddPricePriceNewSubscriptionPackagePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixPrice",
    "AddPricePriceNewSubscriptionMatrixPriceMatrixConfig",
    "AddPricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue",
    "AddPricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPrice",
    "AddPricePriceNewSubscriptionTieredPriceTieredConfig",
    "AddPricePriceNewSubscriptionTieredPriceTieredConfigTier",
    "AddPricePriceNewSubscriptionTieredPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredBpsPrice",
    "AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig",
    "AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier",
    "AddPricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBpsPrice",
    "AddPricePriceNewSubscriptionBpsPriceBpsConfig",
    "AddPricePriceNewSubscriptionBpsPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkBpsPrice",
    "AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig",
    "AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier",
    "AddPricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkPrice",
    "AddPricePriceNewSubscriptionBulkPriceBulkConfig",
    "AddPricePriceNewSubscriptionBulkPriceBulkConfigTier",
    "AddPricePriceNewSubscriptionBulkPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPrice",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPackagePrice",
    "AddPricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredWithMinimumPrice",
    "AddPricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithPercentPrice",
    "AddPricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackageWithAllocationPrice",
    "AddPricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTierWithProrationPrice",
    "AddPricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithProrationPrice",
    "AddPricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedAllocationPrice",
    "AddPricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPrice",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkWithProrationPrice",
    "AddPricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration",
    "BillingCycleAnchorConfiguration",
    "RemoveAdjustment",
    "RemovePrice",
    "ReplaceAdjustment",
    "ReplaceAdjustmentAdjustment",
    "ReplaceAdjustmentAdjustmentNewPercentageDiscount",
    "ReplaceAdjustmentAdjustmentNewUsageDiscount",
    "ReplaceAdjustmentAdjustmentNewAmountDiscount",
    "ReplaceAdjustmentAdjustmentNewMinimum",
    "ReplaceAdjustmentAdjustmentNewMaximum",
    "ReplacePrice",
    "ReplacePriceDiscount",
    "ReplacePricePrice",
    "ReplacePricePriceNewSubscriptionUnitPrice",
    "ReplacePricePriceNewSubscriptionUnitPriceUnitConfig",
    "ReplacePricePriceNewSubscriptionUnitPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackagePrice",
    "ReplacePricePriceNewSubscriptionPackagePricePackageConfig",
    "ReplacePricePriceNewSubscriptionPackagePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixPrice",
    "ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfig",
    "ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue",
    "ReplacePricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPrice",
    "ReplacePricePriceNewSubscriptionTieredPriceTieredConfig",
    "ReplacePricePriceNewSubscriptionTieredPriceTieredConfigTier",
    "ReplacePricePriceNewSubscriptionTieredPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredBpsPrice",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBpsPrice",
    "ReplacePricePriceNewSubscriptionBpsPriceBpsConfig",
    "ReplacePricePriceNewSubscriptionBpsPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkBpsPrice",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkPrice",
    "ReplacePricePriceNewSubscriptionBulkPriceBulkConfig",
    "ReplacePricePriceNewSubscriptionBulkPriceBulkConfigTier",
    "ReplacePricePriceNewSubscriptionBulkPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPrice",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackagePrice",
    "ReplacePricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPrice",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPrice",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPrice",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTierWithProrationPrice",
    "ReplacePricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPrice",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPrice",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPrice",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPrice",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration",
]


class SubscriptionCreateParams(TypedDict, total=False):
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

    align_billing_with_subscription_start_date: bool

    auto_collection: Optional[bool]
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. If not specified, this
    defaults to the behavior configured for this customer.
    """

    aws_region: Optional[str]

    billing_cycle_anchor_configuration: Optional[BillingCycleAnchorConfiguration]

    coupon_redemption_code: Optional[str]
    """Redemption code to be used for this subscription.

    If the coupon cannot be found by its redemption code, or cannot be redeemed, an
    error response will be returned and the subscription creation or plan change
    will not be scheduled.
    """

    credits_overage_rate: Optional[float]

    customer_id: Optional[str]

    default_invoice_memo: Optional[str]
    """Determines the default memo on this subscription's invoices.

    Note that if this is not provided, it is determined by the plan configuration.
    """

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    external_customer_id: Optional[str]

    external_marketplace: Optional[Literal["google", "aws", "azure"]]

    external_marketplace_reporting_id: Optional[str]

    external_plan_id: Optional[str]
    """
    The external_plan_id of the plan that the given subscription should be switched
    to. Note that either this property or `plan_id` must be specified.
    """

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](../guides/extensibility/advanced-metrics#computed-properties).
    If null, usage queries will not include any additional filter.
    """

    initial_phase_order: Optional[int]
    """The phase of the plan to start with"""

    invoicing_threshold: Optional[str]
    """
    When this subscription's accrued usage reaches this threshold, an invoice will
    be issued for the subscription. If not specified, invoices will only be issued
    at the end of the billing period.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
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
    """Specifies which version of the plan to subscribe to.

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

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    trial_duration_days: Optional[int]
    """The duration of the trial period in days.

    If not provided, this defaults to the value specified in the plan. If `0` is
    provided, the trial on the plan will be skipped.
    """


class AddAdjustmentAdjustmentNewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    percentage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    usage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewMinimum(TypedDict, total=False):
    adjustment_type: Required[Literal["minimum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    item_id: Required[str]
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    maximum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


AddAdjustmentAdjustment: TypeAlias = Union[
    AddAdjustmentAdjustmentNewPercentageDiscount,
    AddAdjustmentAdjustmentNewUsageDiscount,
    AddAdjustmentAdjustmentNewAmountDiscount,
    AddAdjustmentAdjustmentNewMinimum,
    AddAdjustmentAdjustmentNewMaximum,
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The end date of the adjustment interval.

    This is the date that the adjustment will stop affecting prices on the
    subscription. If null, the adjustment will start when the phase or subscription
    starts.
    """

    plan_phase_order: Optional[int]
    """The phase to add this adjustment to."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The start date of the adjustment interval.

    This is the date that the adjustment will start affecting prices on the
    subscription. If null, the adjustment will start when the phase or subscription
    starts.
    """


class AddPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class AddPricePriceNewSubscriptionUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""


class AddPricePriceNewSubscriptionUnitPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[AddPricePriceNewSubscriptionUnitPriceUnitConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionUnitPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Required[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class AddPricePriceNewSubscriptionPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[AddPricePriceNewSubscriptionPackagePricePackageConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class AddPricePriceNewSubscriptionMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[AddPricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""


class AddPricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    matrix_config: Required[AddPricePriceNewSubscriptionMatrixPriceMatrixConfig]

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class AddPricePriceNewSubscriptionTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewSubscriptionTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class AddPricePriceNewSubscriptionTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[AddPricePriceNewSubscriptionTieredPriceTieredConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class AddPricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class AddPricePriceNewSubscriptionBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBpsPrice(TypedDict, total=False):
    bps_config: Required[AddPricePriceNewSubscriptionBpsPriceBpsConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class AddPricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class AddPricePriceNewSubscriptionBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewSubscriptionBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class AddPricePriceNewSubscriptionBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBulkPrice(TypedDict, total=False):
    bulk_config: Required[AddPricePriceNewSubscriptionBulkPriceBulkConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBulkPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration]
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


class AddPricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTierWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_allocation_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
    ]
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


class AddPricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[Dict[str, object]]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration
    ]
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
    AddPricePriceNewSubscriptionUnitPrice,
    AddPricePriceNewSubscriptionPackagePrice,
    AddPricePriceNewSubscriptionMatrixPrice,
    AddPricePriceNewSubscriptionTieredPrice,
    AddPricePriceNewSubscriptionTieredBpsPrice,
    AddPricePriceNewSubscriptionBpsPrice,
    AddPricePriceNewSubscriptionBulkBpsPrice,
    AddPricePriceNewSubscriptionBulkPrice,
    AddPricePriceNewSubscriptionThresholdTotalAmountPrice,
    AddPricePriceNewSubscriptionTieredPackagePrice,
    AddPricePriceNewSubscriptionTieredWithMinimumPrice,
    AddPricePriceNewSubscriptionUnitWithPercentPrice,
    AddPricePriceNewSubscriptionPackageWithAllocationPrice,
    AddPricePriceNewSubscriptionTierWithProrationPrice,
    AddPricePriceNewSubscriptionUnitWithProrationPrice,
    AddPricePriceNewSubscriptionGroupedAllocationPrice,
    AddPricePriceNewSubscriptionGroupedWithProratedMinimumPrice,
    AddPricePriceNewSubscriptionBulkWithProrationPrice,
]


class AddPrice(TypedDict, total=False):
    discounts: Optional[Iterable[AddPriceDiscount]]
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
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription. If null,
    billing will start when the phase or subscription starts.
    """


class BillingCycleAnchorConfiguration(TypedDict, total=False):
    day: Required[int]
    """The day of the month on which the billing cycle is anchored.

    If the maximum number of days in a month is greater than this value, the last
    day of the month is the billing cycle day (e.g. billing_cycle_day=31 for April
    means the billing period begins on the 30th.
    """

    month: Optional[int]
    """The month on which the billing cycle is anchored (e.g.

    a quarterly price anchored in February would have cycles starting February, May,
    August, and November).
    """

    year: Optional[int]
    """The year on which the billing cycle is anchored (e.g.

    a 2 year billing cycle anchored on 2021 would have cycles starting on 2021,
    2023, 2025, etc.).
    """


class RemoveAdjustment(TypedDict, total=False):
    adjustment_id: Required[str]
    """The id of the adjustment to remove on the subscription."""


class RemovePrice(TypedDict, total=False):
    external_price_id: Optional[str]
    """The external price id of the price to remove on the subscription."""

    price_id: Optional[str]
    """The id of the price to remove on the subscription."""


class ReplaceAdjustmentAdjustmentNewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    percentage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    usage_discount: Required[float]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewMinimum(TypedDict, total=False):
    adjustment_type: Required[Literal["minimum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    item_id: Required[str]
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    applies_to_price_ids: Required[List[str]]
    """The set of price IDs to which this adjustment applies."""

    maximum_amount: Required[str]

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


ReplaceAdjustmentAdjustment: TypeAlias = Union[
    ReplaceAdjustmentAdjustmentNewPercentageDiscount,
    ReplaceAdjustmentAdjustmentNewUsageDiscount,
    ReplaceAdjustmentAdjustmentNewAmountDiscount,
    ReplaceAdjustmentAdjustmentNewMinimum,
    ReplaceAdjustmentAdjustmentNewMaximum,
]


class ReplaceAdjustment(TypedDict, total=False):
    adjustment: Required[ReplaceAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the subscription."""


class ReplacePriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class ReplacePricePriceNewSubscriptionUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""


class ReplacePricePriceNewSubscriptionUnitPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[ReplacePricePriceNewSubscriptionUnitPriceUnitConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionUnitPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Required[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class ReplacePricePriceNewSubscriptionPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[ReplacePricePriceNewSubscriptionPackagePricePackageConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""


class ReplacePricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    matrix_config: Required[ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfig]

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class ReplacePricePriceNewSubscriptionTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class ReplacePricePriceNewSubscriptionTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[ReplacePricePriceNewSubscriptionTieredPriceTieredConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionTieredPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class ReplacePricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class ReplacePricePriceNewSubscriptionBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBpsPrice(TypedDict, total=False):
    bps_config: Required[ReplacePricePriceNewSubscriptionBpsPriceBpsConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class ReplacePricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class ReplacePricePriceNewSubscriptionBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class ReplacePricePriceNewSubscriptionBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBulkPrice(TypedDict, total=False):
    bulk_config: Required[ReplacePricePriceNewSubscriptionBulkPriceBulkConfig]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionBulkPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration]
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


class ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTierWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_allocation_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: Required[Dict[str, object]]

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionBulkWithProrationPrice(TypedDict, total=False):
    bulk_with_proration_config: Required[Dict[str, object]]

    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration
    ]
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
    ReplacePricePriceNewSubscriptionUnitPrice,
    ReplacePricePriceNewSubscriptionPackagePrice,
    ReplacePricePriceNewSubscriptionMatrixPrice,
    ReplacePricePriceNewSubscriptionTieredPrice,
    ReplacePricePriceNewSubscriptionTieredBpsPrice,
    ReplacePricePriceNewSubscriptionBpsPrice,
    ReplacePricePriceNewSubscriptionBulkBpsPrice,
    ReplacePricePriceNewSubscriptionBulkPrice,
    ReplacePricePriceNewSubscriptionThresholdTotalAmountPrice,
    ReplacePricePriceNewSubscriptionTieredPackagePrice,
    ReplacePricePriceNewSubscriptionTieredWithMinimumPrice,
    ReplacePricePriceNewSubscriptionUnitWithPercentPrice,
    ReplacePricePriceNewSubscriptionPackageWithAllocationPrice,
    ReplacePricePriceNewSubscriptionTierWithProrationPrice,
    ReplacePricePriceNewSubscriptionUnitWithProrationPrice,
    ReplacePricePriceNewSubscriptionGroupedAllocationPrice,
    ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPrice,
    ReplacePricePriceNewSubscriptionBulkWithProrationPrice,
]


class ReplacePrice(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the subscription."""

    discounts: Optional[Iterable[ReplacePriceDiscount]]
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
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""
