# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ReplaceSubscriptionPriceParams",
    "AllocationPrice",
    "Discount",
    "Price",
    "PriceNewSubscriptionUnitPrice",
    "PriceNewSubscriptionUnitPriceUnitConfig",
    "PriceNewSubscriptionUnitPriceBillingCycleConfiguration",
    "PriceNewSubscriptionUnitPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionPackagePrice",
    "PriceNewSubscriptionPackagePricePackageConfig",
    "PriceNewSubscriptionPackagePriceBillingCycleConfiguration",
    "PriceNewSubscriptionPackagePriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionMatrixPrice",
    "PriceNewSubscriptionMatrixPriceMatrixConfig",
    "PriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue",
    "PriceNewSubscriptionMatrixPriceBillingCycleConfiguration",
    "PriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionTieredPrice",
    "PriceNewSubscriptionTieredPriceTieredConfig",
    "PriceNewSubscriptionTieredPriceTieredConfigTier",
    "PriceNewSubscriptionTieredPriceBillingCycleConfiguration",
    "PriceNewSubscriptionTieredPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionTieredBpsPrice",
    "PriceNewSubscriptionTieredBpsPriceTieredBpsConfig",
    "PriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier",
    "PriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration",
    "PriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionBpsPrice",
    "PriceNewSubscriptionBpsPriceBpsConfig",
    "PriceNewSubscriptionBpsPriceBillingCycleConfiguration",
    "PriceNewSubscriptionBpsPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionBulkBpsPrice",
    "PriceNewSubscriptionBulkBpsPriceBulkBpsConfig",
    "PriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier",
    "PriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration",
    "PriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionBulkPrice",
    "PriceNewSubscriptionBulkPriceBulkConfig",
    "PriceNewSubscriptionBulkPriceBulkConfigTier",
    "PriceNewSubscriptionBulkPriceBillingCycleConfiguration",
    "PriceNewSubscriptionBulkPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionThresholdTotalAmountPrice",
    "PriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration",
    "PriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionTieredPackagePrice",
    "PriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration",
    "PriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionTieredWithMinimumPrice",
    "PriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration",
    "PriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionUnitWithPercentPrice",
    "PriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration",
    "PriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionPackageWithAllocationPrice",
    "PriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration",
    "PriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionTierWithProrationPrice",
    "PriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration",
    "PriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionUnitWithProrationPrice",
    "PriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration",
    "PriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionGroupedAllocationPrice",
    "PriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration",
    "PriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionGroupedWithProratedMinimumPrice",
    "PriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration",
    "PriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionBulkWithProrationPrice",
    "PriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration",
    "PriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionScalableMatrixWithUnitPricingPrice",
    "PriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration",
    "PriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionScalableMatrixWithTieredPricingPrice",
    "PriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration",
    "PriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionCumulativeGroupedBulkPrice",
    "PriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration",
    "PriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionMaxGroupTieredPackagePrice",
    "PriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration",
    "PriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionGroupedWithMeteredMinimumPrice",
    "PriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration",
    "PriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionMatrixWithDisplayNamePrice",
    "PriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration",
    "PriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration",
    "PriceNewSubscriptionGroupedTieredPackagePrice",
    "PriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration",
    "PriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration",
]


class AllocationPrice(BaseModel):
    amount: str
    """An amount of the currency to allocate to the customer at the specified cadence."""

    cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual", "custom"]
    """The cadence at which to allocate the amount to the customer."""

    currency: str
    """
    An ISO 4217 currency string or a custom pricing unit identifier in which to bill
    this price.
    """

    expires_at_end_of_cadence: bool
    """
    Whether the allocated amount should expire at the end of the cadence or roll
    over to the next period.
    """


class Discount(BaseModel):
    discount_type: Literal["percentage", "usage", "amount"]

    amount_discount: Optional[str] = None
    """Only available if discount_type is `amount`."""

    percentage_discount: Optional[float] = None
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    usage_discount: Optional[float] = None
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceNewSubscriptionUnitPriceUnitConfig(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""


class PriceNewSubscriptionUnitPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionUnitPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionUnitPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    unit_config: PriceNewSubscriptionUnitPriceUnitConfig

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionUnitPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionUnitPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionPackagePricePackageConfig(BaseModel):
    package_amount: str
    """A currency amount to rate usage by"""

    package_size: int
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class PriceNewSubscriptionPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    package_config: PriceNewSubscriptionPackagePricePackageConfig

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionPackagePriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionPackagePriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue(BaseModel):
    dimension_values: List[Optional[str]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: str
    """Unit price for the specified dimension_values"""


class PriceNewSubscriptionMatrixPriceMatrixConfig(BaseModel):
    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[PriceNewSubscriptionMatrixPriceMatrixConfigMatrixValue]
    """Matrix values for specified matrix grouping keys"""


class PriceNewSubscriptionMatrixPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionMatrixPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    matrix_config: PriceNewSubscriptionMatrixPriceMatrixConfig

    price_model_type: Literal["matrix"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionMatrixPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionMatrixPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionTieredPriceTieredConfigTier(BaseModel):
    first_unit: float
    """Inclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""

    last_unit: Optional[float] = None
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class PriceNewSubscriptionTieredPriceTieredConfig(BaseModel):
    tiers: List[PriceNewSubscriptionTieredPriceTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class PriceNewSubscriptionTieredPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_config: PriceNewSubscriptionTieredPriceTieredConfig

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionTieredPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionTieredPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier(BaseModel):
    bps: float
    """Per-event basis point rate"""

    minimum_amount: str
    """Inclusive tier starting value"""

    maximum_amount: Optional[str] = None
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str] = None
    """Per unit maximum to charge"""


class PriceNewSubscriptionTieredBpsPriceTieredBpsConfig(BaseModel):
    tiers: List[PriceNewSubscriptionTieredBpsPriceTieredBpsConfigTier]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class PriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredBpsPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_bps_config: PriceNewSubscriptionTieredBpsPriceTieredBpsConfig

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionTieredBpsPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionTieredBpsPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionBpsPriceBpsConfig(BaseModel):
    bps: float
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str] = None
    """Optional currency amount maximum to cap spend per event"""


class PriceNewSubscriptionBpsPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBpsPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBpsPrice(BaseModel):
    bps_config: PriceNewSubscriptionBpsPriceBpsConfig

    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["bps"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionBpsPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionBpsPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier(BaseModel):
    bps: float
    """Basis points to rate on"""

    maximum_amount: Optional[str] = None
    """Upper bound for tier"""

    per_unit_maximum: Optional[str] = None
    """The maximum amount to charge for any one event"""


class PriceNewSubscriptionBulkBpsPriceBulkBpsConfig(BaseModel):
    tiers: List[PriceNewSubscriptionBulkBpsPriceBulkBpsConfigTier]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class PriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBulkBpsPrice(BaseModel):
    bulk_bps_config: PriceNewSubscriptionBulkBpsPriceBulkBpsConfig

    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["bulk_bps"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionBulkBpsPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionBulkBpsPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionBulkPriceBulkConfigTier(BaseModel):
    unit_amount: str
    """Amount per unit"""

    maximum_units: Optional[float] = None
    """Upper bound for this tier"""


class PriceNewSubscriptionBulkPriceBulkConfig(BaseModel):
    tiers: List[PriceNewSubscriptionBulkPriceBulkConfigTier]
    """Bulk tiers for rating based on total usage volume"""


class PriceNewSubscriptionBulkPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBulkPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBulkPrice(BaseModel):
    bulk_config: PriceNewSubscriptionBulkPriceBulkConfig

    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["bulk"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionBulkPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionBulkPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionThresholdTotalAmountPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    threshold_total_amount_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionThresholdTotalAmountPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionThresholdTotalAmountPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_package_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionTieredPackagePriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionTieredPackagePriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTieredWithMinimumPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_with_minimum_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionTieredWithMinimumPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionTieredWithMinimumPriceInvoicingCycleConfiguration] = (
        None
    )
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionUnitWithPercentPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["unit_with_percent"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    unit_with_percent_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionUnitWithPercentPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionUnitWithPercentPriceInvoicingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionPackageWithAllocationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    package_with_allocation_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionPackageWithAllocationPriceBillingCycleConfiguration] = (
        None
    )
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionPackageWithAllocationPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionTierWithProrationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_with_proration"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_with_proration_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionTierWithProrationPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionTierWithProrationPriceInvoicingCycleConfiguration] = (
        None
    )
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionUnitWithProrationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["unit_with_proration"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    unit_with_proration_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionUnitWithProrationPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionUnitWithProrationPriceInvoicingCycleConfiguration] = (
        None
    )
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedAllocationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_allocation_config: Dict[str, object]

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["grouped_allocation"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionGroupedAllocationPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionGroupedAllocationPriceInvoicingCycleConfiguration] = (
        None
    )
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedWithProratedMinimumPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: Dict[str, object]

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["grouped_with_prorated_minimum"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[
        PriceNewSubscriptionGroupedWithProratedMinimumPriceBillingCycleConfiguration
    ] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionGroupedWithProratedMinimumPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionBulkWithProrationPrice(BaseModel):
    bulk_with_proration_config: Dict[str, object]

    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["bulk_with_proration"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionBulkWithProrationPriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[PriceNewSubscriptionBulkWithProrationPriceInvoicingCycleConfiguration] = (
        None
    )
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionScalableMatrixWithUnitPricingPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["scalable_matrix_with_unit_pricing"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    scalable_matrix_with_unit_pricing_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[
        PriceNewSubscriptionScalableMatrixWithUnitPricingPriceBillingCycleConfiguration
    ] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionScalableMatrixWithUnitPricingPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionScalableMatrixWithTieredPricingPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["scalable_matrix_with_tiered_pricing"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: Dict[str, object]

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[
        PriceNewSubscriptionScalableMatrixWithTieredPricingPriceBillingCycleConfiguration
    ] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionScalableMatrixWithTieredPricingPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionCumulativeGroupedBulkPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: Dict[str, object]

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["cumulative_grouped_bulk"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionCumulativeGroupedBulkPriceBillingCycleConfiguration] = (
        None
    )
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionCumulativeGroupedBulkPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionMaxGroupTieredPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    max_group_tiered_package_config: Dict[str, object]

    price_model_type: Literal["max_group_tiered_package"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionMaxGroupTieredPackagePriceBillingCycleConfiguration] = (
        None
    )
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionMaxGroupTieredPackagePriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedWithMeteredMinimumPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_with_metered_minimum_config: Dict[str, object]

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["grouped_with_metered_minimum"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[
        PriceNewSubscriptionGroupedWithMeteredMinimumPriceBillingCycleConfiguration
    ] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionGroupedWithMeteredMinimumPriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionMatrixWithDisplayNamePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    matrix_with_display_name_config: Dict[str, object]

    price_model_type: Literal["matrix_with_display_name"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionMatrixWithDisplayNamePriceBillingCycleConfiguration] = (
        None
    )
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionMatrixWithDisplayNamePriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


class PriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""


class PriceNewSubscriptionGroupedTieredPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_tiered_package_config: Dict[str, object]

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["grouped_tiered_package"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[PriceNewSubscriptionGroupedTieredPackagePriceBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[
        PriceNewSubscriptionGroupedTieredPackagePriceInvoicingCycleConfiguration
    ] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    reference_id: Optional[str] = None
    """
    A transient ID that can be used to reference this price when adding adjustments
    in the same API call.
    """


Price: TypeAlias = Annotated[
    Union[
        PriceNewSubscriptionUnitPrice,
        PriceNewSubscriptionPackagePrice,
        PriceNewSubscriptionMatrixPrice,
        PriceNewSubscriptionTieredPrice,
        PriceNewSubscriptionTieredBpsPrice,
        PriceNewSubscriptionBpsPrice,
        PriceNewSubscriptionBulkBpsPrice,
        PriceNewSubscriptionBulkPrice,
        PriceNewSubscriptionThresholdTotalAmountPrice,
        PriceNewSubscriptionTieredPackagePrice,
        PriceNewSubscriptionTieredWithMinimumPrice,
        PriceNewSubscriptionUnitWithPercentPrice,
        PriceNewSubscriptionPackageWithAllocationPrice,
        PriceNewSubscriptionTierWithProrationPrice,
        PriceNewSubscriptionUnitWithProrationPrice,
        PriceNewSubscriptionGroupedAllocationPrice,
        PriceNewSubscriptionGroupedWithProratedMinimumPrice,
        PriceNewSubscriptionBulkWithProrationPrice,
        PriceNewSubscriptionScalableMatrixWithUnitPricingPrice,
        PriceNewSubscriptionScalableMatrixWithTieredPricingPrice,
        PriceNewSubscriptionCumulativeGroupedBulkPrice,
        PriceNewSubscriptionMaxGroupTieredPackagePrice,
        PriceNewSubscriptionGroupedWithMeteredMinimumPrice,
        PriceNewSubscriptionMatrixWithDisplayNamePrice,
        PriceNewSubscriptionGroupedTieredPackagePrice,
        None,
    ],
    PropertyInfo(discriminator="price_model_type"),
]


class ReplaceSubscriptionPriceParams(BaseModel):
    replaces_price_id: str
    """The id of the price on the plan to replace in the subscription."""

    allocation_price: Optional[AllocationPrice] = None
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[List[Discount]] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's discounts for the replacement price.
    """

    external_price_id: Optional[str] = None
    """The external price id of the price to add to the subscription."""

    fixed_price_quantity: Optional[float] = None
    """The new quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's maximum amount for the replacement price.
    """

    minimum_amount: Optional[str] = None
    """[DEPRECATED] Use add_adjustments instead.

    The subscription's minimum amount for the replacement price.
    """

    price: Optional[Price] = None
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str] = None
    """The id of the price to add to the subscription."""
