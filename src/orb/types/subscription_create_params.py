# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .discount_override_param import DiscountOverrideParam
from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .new_subscription_bps_price_param import NewSubscriptionBPSPriceParam
from .shared_params.new_usage_discount import NewUsageDiscount
from .new_subscription_bulk_price_param import NewSubscriptionBulkPriceParam
from .new_subscription_unit_price_param import NewSubscriptionUnitPriceParam
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared_params.new_allocation_price import NewAllocationPrice
from .new_subscription_matrix_price_param import NewSubscriptionMatrixPriceParam
from .new_subscription_tiered_price_param import NewSubscriptionTieredPriceParam
from .new_subscription_package_price_param import NewSubscriptionPackagePriceParam
from .new_subscription_bulk_bps_price_param import NewSubscriptionBulkBPSPriceParam
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .new_subscription_tiered_bps_price_param import NewSubscriptionTieredBPSPriceParam
from .new_subscription_grouped_tiered_price_param import NewSubscriptionGroupedTieredPriceParam
from .new_subscription_tiered_package_price_param import NewSubscriptionTieredPackagePriceParam
from .new_subscription_unit_with_percent_price_param import NewSubscriptionUnitWithPercentPriceParam
from .new_subscription_grouped_allocation_price_param import NewSubscriptionGroupedAllocationPriceParam
from .new_subscription_bulk_with_proration_price_param import NewSubscriptionBulkWithProrationPriceParam
from .new_subscription_tier_with_proration_price_param import NewSubscriptionTierWithProrationPriceParam
from .new_subscription_tiered_with_minimum_price_param import NewSubscriptionTieredWithMinimumPriceParam
from .new_subscription_unit_with_proration_price_param import NewSubscriptionUnitWithProrationPriceParam
from .shared_params.billing_cycle_anchor_configuration import BillingCycleAnchorConfiguration
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
    "SubscriptionCreateParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddPrice",
    "AddPricePrice",
    "RemoveAdjustment",
    "RemovePrice",
    "ReplaceAdjustment",
    "ReplaceAdjustmentAdjustment",
    "ReplacePrice",
    "ReplacePricePrice",
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

    currency: Optional[str]
    """The currency to use for the subscription.

    If not specified, the invoicing currency for the plan will be used.
    """

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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    name: Optional[str]
    """The name to use for the subscription.

    If not specified, the plan name will be used.
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

    usage_customer_ids: Optional[List[str]]
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


AddPricePrice: TypeAlias = Union[
    NewSubscriptionUnitPriceParam,
    NewSubscriptionPackagePriceParam,
    NewSubscriptionMatrixPriceParam,
    NewSubscriptionTieredPriceParam,
    NewSubscriptionTieredBPSPriceParam,
    NewSubscriptionBPSPriceParam,
    NewSubscriptionBulkBPSPriceParam,
    NewSubscriptionBulkPriceParam,
    NewSubscriptionThresholdTotalAmountPriceParam,
    NewSubscriptionTieredPackagePriceParam,
    NewSubscriptionTieredWithMinimumPriceParam,
    NewSubscriptionUnitWithPercentPriceParam,
    NewSubscriptionPackageWithAllocationPriceParam,
    NewSubscriptionTierWithProrationPriceParam,
    NewSubscriptionUnitWithProrationPriceParam,
    NewSubscriptionGroupedAllocationPriceParam,
    NewSubscriptionGroupedWithProratedMinimumPriceParam,
    NewSubscriptionBulkWithProrationPriceParam,
    NewSubscriptionScalableMatrixWithUnitPricingPriceParam,
    NewSubscriptionScalableMatrixWithTieredPricingPriceParam,
    NewSubscriptionCumulativeGroupedBulkPriceParam,
    NewSubscriptionMaxGroupTieredPackagePriceParam,
    NewSubscriptionGroupedWithMeteredMinimumPriceParam,
    NewSubscriptionMatrixWithDisplayNamePriceParam,
    NewSubscriptionGroupedTieredPackagePriceParam,
    NewSubscriptionMatrixWithAllocationPriceParam,
    NewSubscriptionTieredPackageWithMinimumPriceParam,
    NewSubscriptionGroupedTieredPriceParam,
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
    """The definition of a new price to create and add to the subscription."""

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


ReplacePricePrice: TypeAlias = Union[
    NewSubscriptionUnitPriceParam,
    NewSubscriptionPackagePriceParam,
    NewSubscriptionMatrixPriceParam,
    NewSubscriptionTieredPriceParam,
    NewSubscriptionTieredBPSPriceParam,
    NewSubscriptionBPSPriceParam,
    NewSubscriptionBulkBPSPriceParam,
    NewSubscriptionBulkPriceParam,
    NewSubscriptionThresholdTotalAmountPriceParam,
    NewSubscriptionTieredPackagePriceParam,
    NewSubscriptionTieredWithMinimumPriceParam,
    NewSubscriptionUnitWithPercentPriceParam,
    NewSubscriptionPackageWithAllocationPriceParam,
    NewSubscriptionTierWithProrationPriceParam,
    NewSubscriptionUnitWithProrationPriceParam,
    NewSubscriptionGroupedAllocationPriceParam,
    NewSubscriptionGroupedWithProratedMinimumPriceParam,
    NewSubscriptionBulkWithProrationPriceParam,
    NewSubscriptionScalableMatrixWithUnitPricingPriceParam,
    NewSubscriptionScalableMatrixWithTieredPricingPriceParam,
    NewSubscriptionCumulativeGroupedBulkPriceParam,
    NewSubscriptionMaxGroupTieredPackagePriceParam,
    NewSubscriptionGroupedWithMeteredMinimumPriceParam,
    NewSubscriptionMatrixWithDisplayNamePriceParam,
    NewSubscriptionGroupedTieredPackagePriceParam,
    NewSubscriptionMatrixWithAllocationPriceParam,
    NewSubscriptionTieredPackageWithMinimumPriceParam,
    NewSubscriptionGroupedTieredPriceParam,
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
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""
