# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PriceCreateParams",
    "NewFloatingUnitPrice",
    "NewFloatingUnitPriceUnitConfig",
    "NewFloatingPackagePrice",
    "NewFloatingPackagePricePackageConfig",
    "NewFloatingMatrixPrice",
    "NewFloatingMatrixPriceMatrixConfig",
    "NewFloatingMatrixPriceMatrixConfigMatrixValue",
    "NewFloatingTieredPrice",
    "NewFloatingTieredPriceTieredConfig",
    "NewFloatingTieredPriceTieredConfigTier",
    "NewFloatingTieredBpsPrice",
    "NewFloatingTieredBpsPriceTieredBpsConfig",
    "NewFloatingTieredBpsPriceTieredBpsConfigTier",
    "NewFloatingBpsPrice",
    "NewFloatingBpsPriceBpsConfig",
    "NewFloatingBulkBpsPrice",
    "NewFloatingBulkBpsPriceBulkBpsConfig",
    "NewFloatingBulkBpsPriceBulkBpsConfigTier",
    "NewFloatingBulkPrice",
    "NewFloatingBulkPriceBulkConfig",
    "NewFloatingBulkPriceBulkConfigTier",
    "NewFloatingThresholdTotalAmountPrice",
    "NewFloatingTieredPackagePrice",
    "NewFloatingTieredWithMinimumPrice",
    "NewFloatingPackageWithAllocationPrice",
]


class NewFloatingUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[NewFloatingUnitPriceUnitConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""

    scaling_factor: Optional[float]
    """Multiplier to scale rated quantity by"""


class NewFloatingPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[NewFloatingPackagePricePackageConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Optional[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class NewFloatingMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    matrix_config: Required[NewFloatingMatrixPriceMatrixConfig]

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""

    scaling_factor: Optional[float]
    """Optional multiplier to scale rated quantities by"""


class NewFloatingMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[NewFloatingMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""

    scaling_factor: Optional[float]
    """
    Default optional multiplier to scale rated quantities that fall into the default
    bucket by
    """


class NewFloatingTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[NewFloatingTieredPriceTieredConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class NewFloatingTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class NewFloatingTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[NewFloatingTieredBpsPriceTieredBpsConfig]

    billable_metric_id: Optional[str]
    """The id of the billable metric for the price.

    Only needed if the price is usage-based.
    """

    billed_in_advance: Optional[bool]
    """
    If the Price represents a fixed cost, the price will be billed in-advance if
    this is true, and in-arrears if this is false.
    """

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class NewFloatingTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class NewFloatingBpsPrice(TypedDict, total=False):
    bps_config: Required[NewFloatingBpsPriceBpsConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class NewFloatingBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[NewFloatingBulkBpsPriceBulkBpsConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class NewFloatingBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class NewFloatingBulkPrice(TypedDict, total=False):
    bulk_config: Required[NewFloatingBulkPriceBulkConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class NewFloatingBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[NewFloatingBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class NewFloatingThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


class NewFloatingPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

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

    external_price_id: Optional[str]
    """An alias for the price."""

    fixed_price_quantity: Optional[float]
    """
    If the Price represents a fixed cost, this represents the quantity of units
    applied.
    """

    invoice_grouping_key: Optional[str]
    """The property used to group this price on an invoice"""


PriceCreateParams = Union[
    NewFloatingUnitPrice,
    NewFloatingPackagePrice,
    NewFloatingMatrixPrice,
    NewFloatingTieredPrice,
    NewFloatingTieredBpsPrice,
    NewFloatingBpsPrice,
    NewFloatingBulkBpsPrice,
    NewFloatingBulkPrice,
    NewFloatingThresholdTotalAmountPrice,
    NewFloatingTieredPackagePrice,
    NewFloatingTieredWithMinimumPrice,
    NewFloatingPackageWithAllocationPrice,
]
