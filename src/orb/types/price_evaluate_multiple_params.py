# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PriceEvaluateMultipleParams",
    "Event",
    "PriceEvaluation",
    "PriceEvaluationPrice",
    "PriceEvaluationPriceNewFloatingUnitPrice",
    "PriceEvaluationPriceNewFloatingUnitPriceUnitConfig",
    "PriceEvaluationPriceNewFloatingUnitPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingUnitPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingUnitPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingPackagePrice",
    "PriceEvaluationPriceNewFloatingPackagePricePackageConfig",
    "PriceEvaluationPriceNewFloatingPackagePriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingPackagePriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingPackagePriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixPrice",
    "PriceEvaluationPriceNewFloatingMatrixPriceMatrixConfig",
    "PriceEvaluationPriceNewFloatingMatrixPriceMatrixConfigMatrixValue",
    "PriceEvaluationPriceNewFloatingMatrixPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixWithAllocationPrice",
    "PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig",
    "PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue",
    "PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPrice",
    "PriceEvaluationPriceNewFloatingTieredPriceTieredConfig",
    "PriceEvaluationPriceNewFloatingTieredPriceTieredConfigTier",
    "PriceEvaluationPriceNewFloatingTieredPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredBpsPrice",
    "PriceEvaluationPriceNewFloatingTieredBpsPriceTieredBpsConfig",
    "PriceEvaluationPriceNewFloatingTieredBpsPriceTieredBpsConfigTier",
    "PriceEvaluationPriceNewFloatingTieredBpsPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredBpsPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingTieredBpsPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBpsPrice",
    "PriceEvaluationPriceNewFloatingBpsPriceBpsConfig",
    "PriceEvaluationPriceNewFloatingBpsPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBpsPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingBpsPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBulkBpsPrice",
    "PriceEvaluationPriceNewFloatingBulkBpsPriceBulkBpsConfig",
    "PriceEvaluationPriceNewFloatingBulkBpsPriceBulkBpsConfigTier",
    "PriceEvaluationPriceNewFloatingBulkBpsPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBulkBpsPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingBulkBpsPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBulkPrice",
    "PriceEvaluationPriceNewFloatingBulkPriceBulkConfig",
    "PriceEvaluationPriceNewFloatingBulkPriceBulkConfigTier",
    "PriceEvaluationPriceNewFloatingBulkPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBulkPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingBulkPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingThresholdTotalAmountPrice",
    "PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPackagePrice",
    "PriceEvaluationPriceNewFloatingTieredPackagePriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPackagePriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPackagePriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedTieredPrice",
    "PriceEvaluationPriceNewFloatingGroupedTieredPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedTieredPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedTieredPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePrice",
    "PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredWithMinimumPrice",
    "PriceEvaluationPriceNewFloatingTieredWithMinimumPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingPackageWithAllocationPrice",
    "PriceEvaluationPriceNewFloatingPackageWithAllocationPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPrice",
    "PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingUnitWithPercentPrice",
    "PriceEvaluationPriceNewFloatingUnitWithPercentPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingUnitWithPercentPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingUnitWithPercentPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredWithProrationPrice",
    "PriceEvaluationPriceNewFloatingTieredWithProrationPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingTieredWithProrationPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingTieredWithProrationPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingUnitWithProrationPrice",
    "PriceEvaluationPriceNewFloatingUnitWithProrationPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingUnitWithProrationPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingUnitWithProrationPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedAllocationPrice",
    "PriceEvaluationPriceNewFloatingGroupedAllocationPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedAllocationPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedAllocationPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPrice",
    "PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPrice",
    "PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePrice",
    "PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBulkWithProrationPrice",
    "PriceEvaluationPriceNewFloatingBulkWithProrationPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingBulkWithProrationPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingBulkWithProrationPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedTieredPackagePrice",
    "PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPrice",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPrice",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPrice",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration",
    "PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration",
]


class PriceEvaluateMultipleParams(TypedDict, total=False):
    timeframe_end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The exclusive upper bound for event timestamps"""

    timeframe_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The inclusive lower bound for event timestamps"""

    customer_id: Optional[str]
    """The ID of the customer to which this evaluation is scoped."""

    events: Optional[Iterable[Event]]
    """Optional list of preview events to use instead of actual usage data (max 500)"""

    external_customer_id: Optional[str]
    """The external customer ID of the customer to which this evaluation is scoped."""

    price_evaluations: Iterable[PriceEvaluation]
    """List of prices to evaluate (max 100)"""


class Event(TypedDict, total=False):
    event_name: Required[str]
    """A name to meaningfully identify the action or event type."""

    properties: Required[Dict[str, object]]
    """A dictionary of custom properties.

    Values in this dictionary must be numeric, boolean, or strings. Nested
    dictionaries are disallowed.
    """

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """An ISO 8601 format date with no timezone offset (i.e.

    UTC). This should represent the time that usage was recorded, and is
    particularly important to attribute usage to a given billing period.
    """

    customer_id: Optional[str]
    """The Orb Customer identifier"""

    external_customer_id: Optional[str]
    """
    An alias for the Orb customer, whose mapping is specified when creating the
    customer
    """


class PriceEvaluationPriceNewFloatingUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""


class PriceEvaluationPriceNewFloatingUnitPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingUnitPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingUnitPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[PriceEvaluationPriceNewFloatingUnitPriceUnitConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingUnitPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingUnitPriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingUnitPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Required[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class PriceEvaluationPriceNewFloatingPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[PriceEvaluationPriceNewFloatingPackagePricePackageConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingPackagePriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingPackagePriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class PriceEvaluationPriceNewFloatingMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[PriceEvaluationPriceNewFloatingMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""


class PriceEvaluationPriceNewFloatingMatrixPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMatrixPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingMatrixPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_config: Required[PriceEvaluationPriceNewFloatingMatrixPriceMatrixConfig]

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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingMatrixPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingMatrixPriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingMatrixPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue(
    TypedDict, total=False
):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig(TypedDict, total=False):
    allocation: Required[float]
    """Allocation to be used to calculate the price"""

    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[
        Iterable[PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfigMatrixValue]
    ]
    """Matrix values for specified matrix grouping keys"""


class PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMatrixWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    matrix_with_allocation_config: Required[
        PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceMatrixWithAllocationConfig
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
        PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingMatrixWithAllocationPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class PriceEvaluationPriceNewFloatingTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceEvaluationPriceNewFloatingTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class PriceEvaluationPriceNewFloatingTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[PriceEvaluationPriceNewFloatingTieredPriceTieredConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingTieredPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingTieredPriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingTieredPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Exclusive tier starting value"""

    maximum_amount: Optional[str]
    """Inclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class PriceEvaluationPriceNewFloatingTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceEvaluationPriceNewFloatingTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class PriceEvaluationPriceNewFloatingTieredBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingTieredBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[PriceEvaluationPriceNewFloatingTieredBpsPriceTieredBpsConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingTieredBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredBpsPriceDimensionalPriceConfiguration
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingTieredBpsPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class PriceEvaluationPriceNewFloatingBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBpsPrice(TypedDict, total=False):
    bps_config: Required[PriceEvaluationPriceNewFloatingBpsPriceBpsConfig]

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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingBpsPriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingBpsPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class PriceEvaluationPriceNewFloatingBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceEvaluationPriceNewFloatingBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class PriceEvaluationPriceNewFloatingBulkBpsPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBulkBpsPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingBulkBpsPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[PriceEvaluationPriceNewFloatingBulkBpsPriceBulkBpsConfig]

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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingBulkBpsPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingBulkBpsPriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingBulkBpsPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class PriceEvaluationPriceNewFloatingBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceEvaluationPriceNewFloatingBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class PriceEvaluationPriceNewFloatingBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBulkPrice(TypedDict, total=False):
    bulk_config: Required[PriceEvaluationPriceNewFloatingBulkPriceBulkConfig]

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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingBulkPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[PriceEvaluationPriceNewFloatingBulkPriceDimensionalPriceConfiguration]
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

    invoicing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingBulkPriceInvoicingCycleConfiguration]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingThresholdTotalAmountPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingThresholdTotalAmountPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredPackagePrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingTieredPackagePriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredPackagePriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingTieredPackagePriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingGroupedTieredPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedTieredPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingGroupedTieredPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedTieredPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingGroupedTieredPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedTieredPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingGroupedTieredPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingTieredWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredWithMinimumPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredWithMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredWithMinimumPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingTieredWithMinimumPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingPackageWithAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingPackageWithAllocationPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingPackageWithAllocationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingPackageWithAllocationPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingPackageWithAllocationPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingUnitWithPercentPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingUnitWithPercentPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingUnitWithPercentPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingUnitWithPercentPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[PriceEvaluationPriceNewFloatingUnitWithPercentPriceBillingCycleConfiguration]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingUnitWithPercentPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingUnitWithPercentPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingTieredWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingTieredWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingTieredWithProrationPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredWithProrationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingTieredWithProrationPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingTieredWithProrationPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingUnitWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingUnitWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingUnitWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingUnitWithProrationPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingUnitWithProrationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingUnitWithProrationPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingUnitWithProrationPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingGroupedAllocationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedAllocationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingGroupedAllocationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedAllocationPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedAllocationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedAllocationPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingGroupedAllocationPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration(
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


class PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration(
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


class PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingBulkWithProrationPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBulkWithProrationPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingBulkWithProrationPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingBulkWithProrationPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingBulkWithProrationPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingBulkWithProrationPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingBulkWithProrationPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingGroupedTieredPackagePrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingGroupedTieredPackagePriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration(
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


class PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration(
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


class PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration(
    TypedDict, total=False
):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


class PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration(TypedDict, total=False):
    dimension_values: Required[List[str]]
    """
    The list of dimension values matching (in order) the dimensions of the price
    group
    """

    dimensional_price_group_id: Optional[str]
    """The id of the dimensional price group to include this price in"""

    external_dimensional_price_group_id: Optional[str]
    """The external id of the dimensional price group to include this price in"""


class PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""


class PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPrice(TypedDict, total=False):
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

    billing_cycle_configuration: Optional[
        PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceBillingCycleConfiguration
    ]
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[
        PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceDimensionalPriceConfiguration
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
        PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPriceInvoicingCycleConfiguration
    ]
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """


PriceEvaluationPrice: TypeAlias = Union[
    PriceEvaluationPriceNewFloatingUnitPrice,
    PriceEvaluationPriceNewFloatingPackagePrice,
    PriceEvaluationPriceNewFloatingMatrixPrice,
    PriceEvaluationPriceNewFloatingMatrixWithAllocationPrice,
    PriceEvaluationPriceNewFloatingTieredPrice,
    PriceEvaluationPriceNewFloatingTieredBpsPrice,
    PriceEvaluationPriceNewFloatingBpsPrice,
    PriceEvaluationPriceNewFloatingBulkBpsPrice,
    PriceEvaluationPriceNewFloatingBulkPrice,
    PriceEvaluationPriceNewFloatingThresholdTotalAmountPrice,
    PriceEvaluationPriceNewFloatingTieredPackagePrice,
    PriceEvaluationPriceNewFloatingGroupedTieredPrice,
    PriceEvaluationPriceNewFloatingMaxGroupTieredPackagePrice,
    PriceEvaluationPriceNewFloatingTieredWithMinimumPrice,
    PriceEvaluationPriceNewFloatingPackageWithAllocationPrice,
    PriceEvaluationPriceNewFloatingTieredPackageWithMinimumPrice,
    PriceEvaluationPriceNewFloatingUnitWithPercentPrice,
    PriceEvaluationPriceNewFloatingTieredWithProrationPrice,
    PriceEvaluationPriceNewFloatingUnitWithProrationPrice,
    PriceEvaluationPriceNewFloatingGroupedAllocationPrice,
    PriceEvaluationPriceNewFloatingGroupedWithProratedMinimumPrice,
    PriceEvaluationPriceNewFloatingGroupedWithMeteredMinimumPrice,
    PriceEvaluationPriceNewFloatingMatrixWithDisplayNamePrice,
    PriceEvaluationPriceNewFloatingBulkWithProrationPrice,
    PriceEvaluationPriceNewFloatingGroupedTieredPackagePrice,
    PriceEvaluationPriceNewFloatingScalableMatrixWithUnitPricingPrice,
    PriceEvaluationPriceNewFloatingScalableMatrixWithTieredPricingPrice,
    PriceEvaluationPriceNewFloatingCumulativeGroupedBulkPrice,
]


class PriceEvaluation(TypedDict, total=False):
    filter: Optional[str]
    """
    A boolean
    [computed property](/extensibility/advanced-metrics#computed-properties) used to
    filter the underlying billable metric
    """

    grouping_keys: List[str]
    """
    Properties (or
    [computed properties](/extensibility/advanced-metrics#computed-properties)) used
    to group the underlying billable metric
    """

    price: Optional[PriceEvaluationPrice]
    """
    An inline price definition to evaluate, allowing you to test price
    configurations before adding them to Orb.
    """

    price_id: Optional[str]
    """The ID of a price to evaluate that exists in your Orb account."""
