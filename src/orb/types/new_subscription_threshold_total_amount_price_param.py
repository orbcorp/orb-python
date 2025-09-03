# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.unit_conversion_rate_config import UnitConversionRateConfig
from .shared_params.tiered_conversion_rate_config import TieredConversionRateConfig
from .shared_params.new_billing_cycle_configuration import NewBillingCycleConfiguration
from .shared_params.new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "NewSubscriptionThresholdTotalAmountPriceParam",
    "ThresholdTotalAmountConfig",
    "ThresholdTotalAmountConfigConsumptionTable",
    "ConversionRateConfig",
]


class ThresholdTotalAmountConfigConsumptionTable(TypedDict, total=False):
    threshold: Required[str]
    """Quantity threshold"""

    total_amount: Required[str]
    """Total amount for this threshold"""


class ThresholdTotalAmountConfig(TypedDict, total=False):
    consumption_table: Required[Iterable[ThresholdTotalAmountConfigConsumptionTable]]
    """
    When the quantity consumed passes a provided threshold, the configured total
    will be charged
    """

    prorate: Optional[bool]
    """If true, the unit price will be prorated to the billing period"""


ConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewSubscriptionThresholdTotalAmountPriceParam(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["threshold_total_amount"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    threshold_total_amount_config: Required[ThresholdTotalAmountConfig]
    """Configuration for threshold_total_amount pricing"""

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

    conversion_rate_config: Optional[ConversionRateConfig]
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
