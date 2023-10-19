# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SubscriptionPriceIntervalsParams",
    "Add",
    "AddDiscount",
    "AddDiscountAmountDiscountCreationParams",
    "AddDiscountPercentageDiscountCreationParams",
    "AddDiscountUsageDiscountCreationParams",
    "AddFixedFeeQuantityTransition",
    "AddPrice",
    "AddPriceNewUnitPrice",
    "AddPriceNewUnitPriceUnitConfig",
    "AddPriceNewPackagePrice",
    "AddPriceNewPackagePricePackageConfig",
    "AddPriceNewMatrixPrice",
    "AddPriceNewMatrixPriceMatrixConfig",
    "AddPriceNewMatrixPriceMatrixConfigMatrixValue",
    "AddPriceNewTieredPrice",
    "AddPriceNewTieredPriceTieredConfig",
    "AddPriceNewTieredPriceTieredConfigTier",
    "AddPriceNewTieredBpsPrice",
    "AddPriceNewTieredBpsPriceTieredBpsConfig",
    "AddPriceNewTieredBpsPriceTieredBpsConfigTier",
    "AddPriceNewBpsPrice",
    "AddPriceNewBpsPriceBpsConfig",
    "AddPriceNewBulkBpsPrice",
    "AddPriceNewBulkBpsPriceBulkBpsConfig",
    "AddPriceNewBulkBpsPriceBulkBpsConfigTier",
    "AddPriceNewBulkPrice",
    "AddPriceNewBulkPriceBulkConfig",
    "AddPriceNewBulkPriceBulkConfigTier",
    "AddPriceNewThresholdTotalAmountPrice",
    "AddPriceNewTieredPackagePrice",
    "AddPriceNewTieredWithMinimumPrice",
    "AddPriceNewPackageWithAllocationPrice",
    "Edit",
    "EditFixedFeeQuantityTransition",
]


class SubscriptionPriceIntervalsParams(TypedDict, total=False):
    add: List[Add]
    """A list of price intervals to add to the subscription."""

    edit: List[Edit]
    """A list of price intervals to edit on the subscription."""


class AddDiscountAmountDiscountCreationParams(TypedDict, total=False):
    amount_discount: Required[float]
    """Only available if discount_type is `amount`."""

    discount_type: Required[Literal["amount"]]


class AddDiscountPercentageDiscountCreationParams(TypedDict, total=False):
    discount_type: Required[Literal["percentage"]]

    percentage_discount: Required[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """


class AddDiscountUsageDiscountCreationParams(TypedDict, total=False):
    discount_type: Required[Literal["usage"]]

    usage_discount: Required[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for.
    """


AddDiscount = Union[
    AddDiscountAmountDiscountCreationParams,
    AddDiscountPercentageDiscountCreationParams,
    AddDiscountUsageDiscountCreationParams,
]


class AddFixedFeeQuantityTransition(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""


class AddPriceNewUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""

    scaling_factor: Optional[float]
    """Multiplier to scale rated quantity by"""


class AddPriceNewUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[AddPriceNewUnitPriceUnitConfig]

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


class AddPriceNewPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Optional[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class AddPriceNewPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[AddPriceNewPackagePricePackageConfig]

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


class AddPriceNewMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""

    scaling_factor: Optional[float]
    """Optional multiplier to scale rated quantities by"""


class AddPriceNewMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[List[AddPriceNewMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""

    scaling_factor: Optional[float]
    """
    Default optional multiplier to scale rated quantities that fall into the default
    bucket by
    """


class AddPriceNewMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    matrix_config: Required[AddPriceNewMatrixPriceMatrixConfig]

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


class AddPriceNewTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class AddPriceNewTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[List[AddPriceNewTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class AddPriceNewTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[AddPriceNewTieredPriceTieredConfig]

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


class AddPriceNewTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class AddPriceNewTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[List[AddPriceNewTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class AddPriceNewTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
    """The cadence to bill for this price on."""

    currency: Required[str]
    """An ISO 4217 currency string for which this price is billed in."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[AddPriceNewTieredBpsPriceTieredBpsConfig]

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


class AddPriceNewBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class AddPriceNewBpsPrice(TypedDict, total=False):
    bps_config: Required[AddPriceNewBpsPriceBpsConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


class AddPriceNewBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class AddPriceNewBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[List[AddPriceNewBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class AddPriceNewBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[AddPriceNewBulkBpsPriceBulkBpsConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


class AddPriceNewBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class AddPriceNewBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[List[AddPriceNewBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class AddPriceNewBulkPrice(TypedDict, total=False):
    bulk_config: Required[AddPriceNewBulkPriceBulkConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


class AddPriceNewThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


class AddPriceNewTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


class AddPriceNewTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


class AddPriceNewPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly"]]
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


AddPrice = Union[
    AddPriceNewUnitPrice,
    AddPriceNewPackagePrice,
    AddPriceNewMatrixPrice,
    AddPriceNewTieredPrice,
    AddPriceNewTieredBpsPrice,
    AddPriceNewBpsPrice,
    AddPriceNewBulkBpsPrice,
    AddPriceNewBulkPrice,
    AddPriceNewThresholdTotalAmountPrice,
    AddPriceNewTieredPackagePrice,
    AddPriceNewTieredWithMinimumPrice,
    AddPriceNewPackageWithAllocationPrice,
]


class Add(TypedDict, total=False):
    start_date: Required[
        Annotated[Union[Union[str, datetime], Literal["start_of_term", "end_of_term"]], PropertyInfo(format="iso8601")]
    ]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription.
    """

    discounts: Optional[List[AddDiscount]]
    """A list of discounts to initialize on the price interval."""

    end_date: Annotated[
        Union[Union[str, datetime], Literal["start_of_term", "end_of_term"], None], PropertyInfo(format="iso8601")
    ]
    """The end date of the price interval.

    This is the date that the price will stop billing on the subscription.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    fixed_fee_quantity_transitions: Optional[List[AddFixedFeeQuantityTransition]]
    """A list of fixed fee quantity transitions to initialize on the price interval."""

    maximum_amount: Optional[float]
    """
    The maximum amount that will be billed for this price interval for a given
    billing period.
    """

    minimum_amount: Optional[float]
    """
    The minimum amount that will be billed for this price interval for a given
    billing period.
    """

    price: AddPrice
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""


class EditFixedFeeQuantityTransition(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""


class Edit(TypedDict, total=False):
    price_interval_id: Required[str]
    """The id of the price interval to edit."""

    end_date: Annotated[
        Union[Union[str, datetime], Literal["start_of_term", "end_of_term"], None], PropertyInfo(format="iso8601")
    ]
    """The updated end date of this price interval.

    If not specified, the start date will not be updated.
    """

    fixed_fee_quantity_transitions: Optional[List[EditFixedFeeQuantityTransition]]
    """A list of fixed fee quantity transitions to use for this price interval.

    Note that this list will overwrite all existing fixed fee quantity transitions
    on the price interval.
    """

    start_date: Annotated[
        Union[Union[str, datetime], Literal["start_of_term", "end_of_term"], None], PropertyInfo(format="iso8601")
    ]
    """The updated start date of this price interval.

    If not specified, the start date will not be updated.
    """
