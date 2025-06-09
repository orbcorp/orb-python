# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .new_billing_cycle_configuration import NewBillingCycleConfiguration
from .new_dimensional_price_configuration import NewDimensionalPriceConfiguration

__all__ = [
    "NewPlanGroupedWithProratedMinimumPrice",
    "ConversionRateConfig",
    "ConversionRateConfigUnitConversionRateConfig",
    "ConversionRateConfigUnitConversionRateConfigUnitConfig",
    "ConversionRateConfigTieredConversionRateConfig",
    "ConversionRateConfigTieredConversionRateConfigTieredConfig",
    "ConversionRateConfigTieredConversionRateConfigTieredConfigTier",
]


class ConversionRateConfigUnitConversionRateConfigUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""


class ConversionRateConfigUnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: ConversionRateConfigUnitConversionRateConfigUnitConfig


class ConversionRateConfigTieredConversionRateConfigTieredConfigTier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit of overage"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""


class ConversionRateConfigTieredConversionRateConfigTieredConfig(BaseModel):
    tiers: List[ConversionRateConfigTieredConversionRateConfigTieredConfigTier]
    """Tiers for rating based on total usage quantities into the specified tier"""


class ConversionRateConfigTieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: ConversionRateConfigTieredConversionRateConfigTieredConfig


ConversionRateConfig: TypeAlias = Annotated[
    Union[ConversionRateConfigUnitConversionRateConfig, ConversionRateConfigTieredConversionRateConfig, None],
    PropertyInfo(discriminator="conversion_rate_type"),
]


class NewPlanGroupedWithProratedMinimumPrice(BaseModel):
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

    billing_cycle_configuration: Optional[NewBillingCycleConfiguration] = None
    """
    For custom cadence: specifies the duration of the billing period in days or
    months.
    """

    conversion_rate: Optional[float] = None
    """The per unit conversion rate of the price currency to the invoicing currency."""

    conversion_rate_config: Optional[ConversionRateConfig] = None
    """The configuration for the rate of the price currency to the invoicing currency."""

    currency: Optional[str] = None
    """
    An ISO 4217 currency string, or custom pricing unit identifier, in which this
    price is billed.
    """

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
