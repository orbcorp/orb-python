# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .unit_conversion_rate_config import UnitConversionRateConfig
from .tiered_conversion_rate_config import TieredConversionRateConfig
from .new_billing_cycle_configuration import NewBillingCycleConfiguration
from .new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "NewFloatingTieredWithProrationPrice",
    "TieredWithProrationConfig",
    "TieredWithProrationConfigTier",
    "ConversionRateConfig",
]


class TieredWithProrationConfigTier(BaseModel):
    tier_lower_bound: str
    """Inclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""


class TieredWithProrationConfig(BaseModel):
    tiers: List[TieredWithProrationConfigTier]
    """
    Tiers for rating based on total usage quantities into the specified tier with
    proration
    """


ConversionRateConfig: TypeAlias = Annotated[
    Union[UnitConversionRateConfig, TieredConversionRateConfig], PropertyInfo(discriminator="conversion_rate_type")
]


class NewFloatingTieredWithProrationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    currency: str
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_with_proration"] = FieldInfo(alias="model_type")
    """The pricing model type"""

    name: str
    """The name of the price."""

    tiered_with_proration_config: TieredWithProrationConfig
    """Configuration for tiered_with_proration pricing"""

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[ConversionRateConfig] = None
    """The configuration for the rate of the price currency to the invoicing currency."""

    dimensional_price_configuration: Optional[NewDimensionalPriceConfiguration] = None
    """For dimensional price: specifies a price group and dimension values"""

    external_price_id: Optional[str] = None
    """An alias for the price."""

    fixed_price_quantity: Optional[float] = None
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str] = None
    """The property used to group this price on an invoice"""

    invoicing_cycle_configuration: Optional[NewBillingCycleConfiguration] = None
    """Within each billing cycle, specifies the cadence at which invoices are produced.

    If unspecified, a single invoice is produced per billing cycle.
    """

    metadata: Optional[Dict[str, Optional[str]]] = None
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """
