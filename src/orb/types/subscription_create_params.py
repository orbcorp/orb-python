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
    "AddPriceAllocationPrice",
    "AddPriceAllocationPriceCustomExpiration",
    "AddPriceDiscount",
    "AddPricePrice",
    "AddPricePriceNewSubscriptionUnitPrice",
    "AddPricePriceNewSubscriptionUnitPriceUnitConfig",
    "AddPricePriceNewSubscriptionUnitPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackagePrice",
    "AddPricePriceNewSubscriptionPackagePricePackageConfig",
    "AddPricePriceNewSubscriptionPackagePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackagePriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixPrice",
    "AddPricePriceNewSubscriptionMatrixPriceMatrixConfig",
    "AddPricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue",
    "AddPricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPrice",
    "AddPricePriceNewSubscriptionTieredPriceTieredConfig",
    "AddPricePriceNewSubscriptionTieredPriceTieredConfigTier",
    "AddPricePriceNewSubscriptionTieredPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredBpsPrice",
    "AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig",
    "AddPricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier",
    "AddPricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredBpsPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBpsPrice",
    "AddPricePriceNewSubscriptionBpsPriceBpsConfig",
    "AddPricePriceNewSubscriptionBpsPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBpsPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkBpsPrice",
    "AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig",
    "AddPricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier",
    "AddPricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkBpsPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkPrice",
    "AddPricePriceNewSubscriptionBulkPriceBulkConfig",
    "AddPricePriceNewSubscriptionBulkPriceBulkConfigTier",
    "AddPricePriceNewSubscriptionBulkPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPrice",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPackagePrice",
    "AddPricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPackagePriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredWithMinimumPrice",
    "AddPricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredWithMinimumPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithPercentPrice",
    "AddPricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithPercentPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackageWithAllocationPrice",
    "AddPricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionPackageWithAllocationPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTierWithProrationPrice",
    "AddPricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTierWithProrationPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithProrationPrice",
    "AddPricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionUnitWithProrationPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedAllocationPrice",
    "AddPricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedAllocationPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPrice",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkWithProrationPrice",
    "AddPricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionBulkWithProrationPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPrice",
    "AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPrice",
    "AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionCumulativeGroupedBulkPrice",
    "AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionMaxGroupTieredPackagePrice",
    "AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPrice",
    "AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixWithDisplayNamePrice",
    "AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedTieredPackagePrice",
    "AddPricePriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedTieredPackagePriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixWithAllocationPrice",
    "AddPricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfig",
    "AddPricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue",
    "AddPricePriceNewSubscriptionMatrixWithAllocationPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionMatrixWithAllocationPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionMatrixWithAllocationPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPackageWithMinimumPrice",
    "AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceInvoicingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedTieredPrice",
    "AddPricePriceNewSubscriptionGroupedTieredPriceBillingCycleConfiguration",
    "AddPricePriceNewSubscriptionGroupedTieredPriceDimensionalPriceConfiguration",
    "AddPricePriceNewSubscriptionGroupedTieredPriceInvoicingCycleConfiguration",
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
    "ReplacePriceAllocationPrice",
    "ReplacePriceAllocationPriceCustomExpiration",
    "ReplacePriceDiscount",
    "ReplacePricePrice",
    "ReplacePricePriceNewSubscriptionUnitPrice",
    "ReplacePricePriceNewSubscriptionUnitPriceUnitConfig",
    "ReplacePricePriceNewSubscriptionUnitPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackagePrice",
    "ReplacePricePriceNewSubscriptionPackagePricePackageConfig",
    "ReplacePricePriceNewSubscriptionPackagePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackagePriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixPrice",
    "ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfig",
    "ReplacePricePriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue",
    "ReplacePricePriceNewSubscriptionMatrixPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPrice",
    "ReplacePricePriceNewSubscriptionTieredPriceTieredConfig",
    "ReplacePricePriceNewSubscriptionTieredPriceTieredConfigTier",
    "ReplacePricePriceNewSubscriptionTieredPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredBpsPrice",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfig",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBpsPrice",
    "ReplacePricePriceNewSubscriptionBpsPriceBpsConfig",
    "ReplacePricePriceNewSubscriptionBpsPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBpsPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionBpsPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkBpsPrice",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfig",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkPrice",
    "ReplacePricePriceNewSubscriptionBulkPriceBulkConfig",
    "ReplacePricePriceNewSubscriptionBulkPriceBulkConfigTier",
    "ReplacePricePriceNewSubscriptionBulkPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionBulkPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPrice",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackagePrice",
    "ReplacePricePriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackagePriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPrice",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPrice",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPrice",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTierWithProrationPrice",
    "ReplacePricePriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTierWithProrationPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPrice",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPrice",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPrice",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPrice",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPrice",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPrice",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPrice",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePrice",
    "ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPrice",
    "ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePrice",
    "ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedTieredPackagePrice",
    "ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixWithAllocationPrice",
    "ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfig",
    "ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue",
    "ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPrice",
    "ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceInvoicingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedTieredPrice",
    "ReplacePricePriceNewSubscriptionGroupedTieredPriceBillingCycleConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedTieredPriceDimensionalPriceConfiguration",
    "ReplacePricePriceNewSubscriptionGroupedTieredPriceInvoicingCycleConfiguration",
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


class AddAdjustmentAdjustmentNewPercentageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage_discount"]]

    percentage_discount: Required[float]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    usage_discount: Required[float]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewMinimum(TypedDict, total=False):
    adjustment_type: Required[Literal["minimum"]]

    item_id: Required[str]
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class AddAdjustmentAdjustmentNewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    maximum_amount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

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


class AddPriceAllocationPriceCustomExpiration(TypedDict, total=False):
    duration: Required[int]

    duration_unit: Required[Literal["day", "month"]]


class AddPriceAllocationPrice(TypedDict, total=False):
    amount: Required[str]
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Required[Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]]
    """The cadence at which to allocate the amount to the customer."""

    currency: Required[str]
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    custom_expiration: Optional[AddPriceAllocationPriceCustomExpiration]
    """The custom expiration for the allocation."""

    expires_at_end_of_cadence: Optional[bool]
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period. Set to null if using custom_expiration.
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


class AddPricePriceNewSubscriptionUnitPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionUnitPriceDimensionalPriceConfiguration]
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


class AddPricePriceNewSubscriptionPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionPackagePriceDimensionalPriceConfiguration]
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


class AddPricePriceNewSubscriptionMatrixPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionMatrixPriceDimensionalPriceConfiguration]
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
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class AddPricePriceNewSubscriptionTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[AddPricePriceNewSubscriptionTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class AddPricePriceNewSubscriptionTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionTieredPriceDimensionalPriceConfiguration]
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
    """Exclusive tier starting value"""

    maximum_amount: Optional[str]
    """Inclusive tier ending value"""

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


class AddPricePriceNewSubscriptionTieredBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionTieredBpsPriceDimensionalPriceConfiguration]
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


class AddPricePriceNewSubscriptionBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionBpsPriceDimensionalPriceConfiguration]
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


class AddPricePriceNewSubscriptionBulkBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionBulkBpsPriceDimensionalPriceConfiguration]
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


class AddPricePriceNewSubscriptionBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[AddPricePriceNewSubscriptionBulkPriceDimensionalPriceConfiguration]
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


class AddPricePriceNewSubscriptionThresholdTotalAmountPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionThresholdTotalAmountPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionTieredPackagePriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionTieredWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionTieredWithMinimumPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionUnitWithPercentPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionUnitWithPercentPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionPackageWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionPackageWithAllocationPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionTierWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTierWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionTierWithProrationPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionUnitWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionUnitWithProrationPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionGroupedAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedAllocationPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedWithProratedMinimumPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionBulkWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionBulkWithProrationPriceDimensionalPriceConfiguration
    ]
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


class AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[Dict[str, object]]

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedTieredPackagePriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue(
    TypedDict, total=False
):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class AddPricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfig(TypedDict, total=False):
    allocation: Required[float]
    """Allocation to be used to calculate the price"""

    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[
        Iterable[AddPricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue]
    ]
    """Matrix values for specified matrix grouping keys"""


class AddPricePriceNewSubscriptionMatrixWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionMatrixWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_allocation_config: Required[
        AddPricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfig
    ]

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionMatrixWithAllocationPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionMatrixWithAllocationPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionMatrixWithAllocationPriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        AddPricePriceNewSubscriptionTieredPackageWithMinimumPriceInvoicingCycleConfiguration
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


class AddPricePriceNewSubscriptionGroupedTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class AddPricePriceNewSubscriptionGroupedTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class AddPricePriceNewSubscriptionGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[AddPricePriceNewSubscriptionGroupedTieredPriceBillingCycleConfiguration]
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

    dimensional_price_configuration: Optional[
        AddPricePriceNewSubscriptionGroupedTieredPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[AddPricePriceNewSubscriptionGroupedTieredPriceInvoicingCycleConfiguration]
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
    AddPricePriceNewSubscriptionScalableMatrixWithUnitPricingPrice,
    AddPricePriceNewSubscriptionScalableMatrixWithTieredPricingPrice,
    AddPricePriceNewSubscriptionCumulativeGroupedBulkPrice,
    AddPricePriceNewSubscriptionMaxGroupTieredPackagePrice,
    AddPricePriceNewSubscriptionGroupedWithMeteredMinimumPrice,
    AddPricePriceNewSubscriptionMatrixWithDisplayNamePrice,
    AddPricePriceNewSubscriptionGroupedTieredPackagePrice,
    AddPricePriceNewSubscriptionMatrixWithAllocationPrice,
    AddPricePriceNewSubscriptionTieredPackageWithMinimumPrice,
    AddPricePriceNewSubscriptionGroupedTieredPrice,
]


class AddPrice(TypedDict, total=False):
    allocation_price: Optional[AddPriceAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

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

    percentage_discount: Required[float]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewUsageDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["usage_discount"]]

    usage_discount: Required[float]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewAmountDiscount(TypedDict, total=False):
    adjustment_type: Required[Literal["amount_discount"]]

    amount_discount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewMinimum(TypedDict, total=False):
    adjustment_type: Required[Literal["minimum"]]

    item_id: Required[str]
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

    is_invoice_level: bool
    """When false, this adjustment will be applied to a single price.

    Otherwise, it will be applied at the invoice level, possibly to multiple prices.
    """


class ReplaceAdjustmentAdjustmentNewMaximum(TypedDict, total=False):
    adjustment_type: Required[Literal["maximum"]]

    maximum_amount: Required[str]

    applies_to_price_ids: Optional[List[str]]
    """The set of price IDs to which this adjustment applies."""

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


class ReplacePriceAllocationPriceCustomExpiration(TypedDict, total=False):
    duration: Required[int]

    duration_unit: Required[Literal["day", "month"]]


class ReplacePriceAllocationPrice(TypedDict, total=False):
    amount: Required[str]
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Required[Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]]
    """The cadence at which to allocate the amount to the customer."""

    currency: Required[str]
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    custom_expiration: Optional[ReplacePriceAllocationPriceCustomExpiration]
    """The custom expiration for the allocation."""

    expires_at_end_of_cadence: Optional[bool]
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period. Set to null if using custom_expiration.
    """


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


class ReplacePricePriceNewSubscriptionUnitPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionUnitPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionUnitPriceDimensionalPriceConfiguration]
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


class ReplacePricePriceNewSubscriptionPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionPackagePriceDimensionalPriceConfiguration]
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


class ReplacePricePriceNewSubscriptionMatrixPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionMatrixPriceDimensionalPriceConfiguration]
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
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class ReplacePricePriceNewSubscriptionTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[ReplacePricePriceNewSubscriptionTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class ReplacePricePriceNewSubscriptionTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionTieredPriceDimensionalPriceConfiguration]
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
    """Exclusive tier starting value"""

    maximum_amount: Optional[str]
    """Inclusive tier ending value"""

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


class ReplacePricePriceNewSubscriptionTieredBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredBpsPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionBpsPriceDimensionalPriceConfiguration]
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


class ReplacePricePriceNewSubscriptionBulkBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionBulkBpsPriceDimensionalPriceConfiguration]
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


class ReplacePricePriceNewSubscriptionBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[ReplacePricePriceNewSubscriptionBulkPriceDimensionalPriceConfiguration]
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


class ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionThresholdTotalAmountPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredPackagePriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionTieredWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredWithMinimumPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionUnitWithPercentPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitWithPercentPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionUnitWithPercentPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionPackageWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionPackageWithAllocationPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionTierWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTierWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionTierWithProrationPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionUnitWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionUnitWithProrationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionUnitWithProrationPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionGroupedAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedAllocationPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedWithProratedMinimumPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionBulkWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionBulkWithProrationPriceDimensionalPriceConfiguration
    ]
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


class ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Required[Dict[str, object]]

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue(
    TypedDict, total=False
):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfig(TypedDict, total=False):
    allocation: Required[float]
    """Allocation to be used to calculate the price"""

    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[
        Iterable[ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue]
    ]
    """Matrix values for specified matrix grouping keys"""


class ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_allocation_config: Required[
        ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceMatrixWithAllocationConfig
    ]

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionMatrixWithAllocationPriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceDimensionalPriceConfiguration(
    TypedDict, total=False
):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceBillingCycleConfiguration
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPriceInvoicingCycleConfiguration
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


class ReplacePricePriceNewSubscriptionGroupedTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class ReplacePricePriceNewSubscriptionGroupedTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class ReplacePricePriceNewSubscriptionGroupedTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

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

    billing_cycle_configuration: Optional[ReplacePricePriceNewSubscriptionGroupedTieredPriceBillingCycleConfiguration]
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

    dimensional_price_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedTieredPriceDimensionalPriceConfiguration
    ]
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

    invoicing_cycle_configuration: Optional[
        ReplacePricePriceNewSubscriptionGroupedTieredPriceInvoicingCycleConfiguration
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
    ReplacePricePriceNewSubscriptionScalableMatrixWithUnitPricingPrice,
    ReplacePricePriceNewSubscriptionScalableMatrixWithTieredPricingPrice,
    ReplacePricePriceNewSubscriptionCumulativeGroupedBulkPrice,
    ReplacePricePriceNewSubscriptionMaxGroupTieredPackagePrice,
    ReplacePricePriceNewSubscriptionGroupedWithMeteredMinimumPrice,
    ReplacePricePriceNewSubscriptionMatrixWithDisplayNamePrice,
    ReplacePricePriceNewSubscriptionGroupedTieredPackagePrice,
    ReplacePricePriceNewSubscriptionMatrixWithAllocationPrice,
    ReplacePricePriceNewSubscriptionTieredPackageWithMinimumPrice,
    ReplacePricePriceNewSubscriptionGroupedTieredPrice,
]


class ReplacePrice(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the subscription."""

    allocation_price: Optional[ReplacePriceAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

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
