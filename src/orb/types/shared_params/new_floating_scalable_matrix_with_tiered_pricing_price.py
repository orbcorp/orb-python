# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .unit_conversion_rate_config import UnitConversionRateConfig
from .tiered_conversion_rate_config import TieredConversionRateConfig
from .new_billing_cycle_configuration import NewBillingCycleConfiguration
from .new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "NewFloatingScalableMatrixWithTieredPricingPrice",
    "ScalableMatrixWithTieredPricingConfig",
    "ScalableMatrixWithTieredPricingConfigMatrixScalingFactor",
    "ScalableMatrixWithTieredPricingConfigTier",
    "ConversionRateConfig",
]


class ScalableMatrixWithTieredPricingConfigMatrixScalingFactor(TypedDict, total=False):
    first_dimension_value: Required[str]
    """First dimension value"""

    scaling_factor: Required[str]
    """Scaling factor"""

    second_dimension_value: Optional[str]
    """Second dimension value (optional)"""


class ScalableMatrixWithTieredPricingConfigTier(TypedDict, total=False):
    tier_lower_bound: Required[str]
    """Tier lower bound"""

    unit_amount: Required[str]
    """Per unit amount"""


class ScalableMatrixWithTieredPricingConfig(TypedDict, total=False):
    first_dimension: Required[str]
    """Used for the scalable matrix first dimension"""

    matrix_scaling_factors: Required[Iterable[ScalableMatrixWithTieredPricingConfigMatrixScalingFactor]]
    """Apply a scaling factor to each dimension"""

    tiers: Required[Iterable[ScalableMatrixWithTieredPricingConfigTier]]
    """Tier pricing structure"""

    second_dimension: Optional[str]
    """Used for the scalable matrix second dimension (optional)"""


ConversionRateConfig: TypeAlias = Union[UnitConversionRateConfig, TieredConversionRateConfig]


class NewFloatingScalableMatrixWithTieredPricingPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the price will be associated with."""

    model_type: Required[Literal["scalable_matrix_with_tiered_pricing"]]
    """The pricing model type"""

    name: Required[str]
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: Required[ScalableMatrixWithTieredPricingConfig]
    """Configuration for scalable_matrix_with_tiered_pricing pricing"""

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
