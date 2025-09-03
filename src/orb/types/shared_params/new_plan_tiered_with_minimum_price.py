# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .unit_conversion_rate_config import UnitConversionRateConfig
from .tiered_conversion_rate_config import TieredConversionRateConfig
from .new_billing_cycle_configuration import NewBillingCycleConfiguration
from .new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "NewPlanTieredWithMinimumPrice",
    "TieredWithMinimumConfig",
    "TieredWithMinimumConfigTier",
    "ConversionRateConfig",
]


class TieredWithMinimumConfigTier(TypedDict, total=False):
    minimum_amount: Required[str]
    """Minimum amount"""

    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Per unit amount"""


class TieredWithMinimumConfig(TypedDict, total=False):
    tiers: Required[Iterable[TieredWithMinimumConfigTier]]
    """Tiered pricing with a minimum amount dependent on the volume tier.

    Tiers are defined using exclusive lower bounds.
    """

    hide_zero_amount_tiers: bool
    """If true, tiers with an accrued amount of 0 will not be included in the rating."""

    prorate: bool
    """If true, the unit price will be prorated to the billing period"""


ConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewPlanTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["tiered_with_minimum"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    tiered_with_minimum_config: Required[TieredWithMinimumConfig]
    """Configuration for tiered_with_minimum pricing"""

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
