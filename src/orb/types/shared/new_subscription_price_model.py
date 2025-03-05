# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .bps_config_model import BpsConfigModel
from .bulk_config_model import BulkConfigModel
from .unit_config_model import UnitConfigModel
from .matrix_config_model import MatrixConfigModel
from .tiered_config_model import TieredConfigModel
from .package_config_model import PackageConfigModel
from .bulk_bps_config_model import BulkBpsConfigModel
from .tiered_bps_config_model import TieredBpsConfigModel
from .custom_rating_function_config_model import CustomRatingFunctionConfigModel
from .new_billing_cycle_configuration_model import NewBillingCycleConfigurationModel

__all__ = [
    "NewSubscriptionPriceModel",
    "NewSubscriptionUnitPrice",
    "NewSubscriptionPackagePrice",
    "NewSubscriptionMatrixPrice",
    "NewSubscriptionTieredPrice",
    "NewSubscriptionTieredBpsPrice",
    "NewSubscriptionBpsPrice",
    "NewSubscriptionBulkBpsPrice",
    "NewSubscriptionBulkPrice",
    "NewSubscriptionThresholdTotalAmountPrice",
    "NewSubscriptionTieredPackagePrice",
    "NewSubscriptionTieredWithMinimumPrice",
    "NewSubscriptionUnitWithPercentPrice",
    "NewSubscriptionPackageWithAllocationPrice",
    "NewSubscriptionTierWithProrationPrice",
    "NewSubscriptionUnitWithProrationPrice",
    "NewSubscriptionGroupedAllocationPrice",
    "NewSubscriptionGroupedWithProratedMinimumPrice",
    "NewSubscriptionBulkWithProrationPrice",
    "NewSubscriptionScalableMatrixWithUnitPricingPrice",
    "NewSubscriptionScalableMatrixWithTieredPricingPrice",
    "NewSubscriptionCumulativeGroupedBulkPrice",
    "NewSubscriptionMaxGroupTieredPackagePrice",
    "NewSubscriptionGroupedWithMeteredMinimumPrice",
    "NewSubscriptionMatrixWithDisplayNamePrice",
    "NewSubscriptionGroupedTieredPackagePrice",
]


class NewSubscriptionUnitPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["unit"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    unit_config: UnitConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["package"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    package_config: PackageConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionMatrixPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    matrix_config: MatrixConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionTieredPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_config: TieredConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionTieredBpsPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_bps"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_bps_config: TieredBpsConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionBpsPrice(BaseModel):
    bps_config: BpsConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionBulkBpsPrice(BaseModel):
    bulk_bps_config: BulkBpsConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionBulkPrice(BaseModel):
    bulk_config: BulkConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionThresholdTotalAmountPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["threshold_total_amount"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    threshold_total_amount_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionTieredPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_package"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_package_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionTieredWithMinimumPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_with_minimum"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_with_minimum_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionUnitWithPercentPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["unit_with_percent"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    unit_with_percent_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionPackageWithAllocationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["package_with_allocation"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    package_with_allocation_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionTierWithProrationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["tiered_with_proration"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    tiered_with_proration_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionUnitWithProrationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["unit_with_proration"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    unit_with_proration_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionGroupedAllocationPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_allocation_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionGroupedWithProratedMinimumPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_with_prorated_minimum_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionBulkWithProrationPrice(BaseModel):
    bulk_with_proration_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionScalableMatrixWithUnitPricingPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["scalable_matrix_with_unit_pricing"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    scalable_matrix_with_unit_pricing_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionScalableMatrixWithTieredPricingPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    price_model_type: Literal["scalable_matrix_with_tiered_pricing"] = FieldInfo(alias="model_type")

    name: str
    """The name of the price."""

    scalable_matrix_with_tiered_pricing_config: CustomRatingFunctionConfigModel

    billable_metric_id: Optional[str] = None
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool] = None
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionCumulativeGroupedBulkPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    cumulative_grouped_bulk_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionMaxGroupTieredPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    max_group_tiered_package_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionGroupedWithMeteredMinimumPrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_with_metered_minimum_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionMatrixWithDisplayNamePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    item_id: str
    """The id of the item the price will be associated with."""

    matrix_with_display_name_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


class NewSubscriptionGroupedTieredPackagePrice(BaseModel):
    cadence: Literal["annual", "semi_annual", "monthly", "quarterly", "one_time", "custom"]
    """The cadence to bill for this price on."""

    grouped_tiered_package_config: CustomRatingFunctionConfigModel

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

    billing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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

    invoicing_cycle_configuration: Optional[NewBillingCycleConfigurationModel] = None
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


NewSubscriptionPriceModel: TypeAlias = Annotated[
    Union[
        NewSubscriptionUnitPrice,
        NewSubscriptionPackagePrice,
        NewSubscriptionMatrixPrice,
        NewSubscriptionTieredPrice,
        NewSubscriptionTieredBpsPrice,
        NewSubscriptionBpsPrice,
        NewSubscriptionBulkBpsPrice,
        NewSubscriptionBulkPrice,
        NewSubscriptionThresholdTotalAmountPrice,
        NewSubscriptionTieredPackagePrice,
        NewSubscriptionTieredWithMinimumPrice,
        NewSubscriptionUnitWithPercentPrice,
        NewSubscriptionPackageWithAllocationPrice,
        NewSubscriptionTierWithProrationPrice,
        NewSubscriptionUnitWithProrationPrice,
        NewSubscriptionGroupedAllocationPrice,
        NewSubscriptionGroupedWithProratedMinimumPrice,
        NewSubscriptionBulkWithProrationPrice,
        NewSubscriptionScalableMatrixWithUnitPricingPrice,
        NewSubscriptionScalableMatrixWithTieredPricingPrice,
        NewSubscriptionCumulativeGroupedBulkPrice,
        NewSubscriptionMaxGroupTieredPackagePrice,
        NewSubscriptionGroupedWithMeteredMinimumPrice,
        NewSubscriptionMatrixWithDisplayNamePrice,
        NewSubscriptionGroupedTieredPackagePrice,
    ],
    PropertyInfo(discriminator="price_model_type"),
]
