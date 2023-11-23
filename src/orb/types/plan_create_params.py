# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PlanCreateParams",
    "Price",
    "PriceNewPlanUnitPrice",
    "PriceNewPlanUnitPriceUnitConfig",
    "PriceNewPlanPackagePrice",
    "PriceNewPlanPackagePricePackageConfig",
    "PriceNewPlanMatrixPrice",
    "PriceNewPlanMatrixPriceMatrixConfig",
    "PriceNewPlanMatrixPriceMatrixConfigMatrixValue",
    "PriceNewPlanTieredPrice",
    "PriceNewPlanTieredPriceTieredConfig",
    "PriceNewPlanTieredPriceTieredConfigTier",
    "PriceNewPlanTieredBpsPrice",
    "PriceNewPlanTieredBpsPriceTieredBpsConfig",
    "PriceNewPlanTieredBpsPriceTieredBpsConfigTier",
    "PriceNewPlanBpsPrice",
    "PriceNewPlanBpsPriceBpsConfig",
    "PriceNewPlanBulkBpsPrice",
    "PriceNewPlanBulkBpsPriceBulkBpsConfig",
    "PriceNewPlanBulkBpsPriceBulkBpsConfigTier",
    "PriceNewPlanBulkPrice",
    "PriceNewPlanBulkPriceBulkConfig",
    "PriceNewPlanBulkPriceBulkConfigTier",
    "PriceNewPlanThresholdTotalAmountPrice",
    "PriceNewPlanTieredPackagePrice",
    "PriceNewPlanTieredWithMinimumPrice",
    "PriceNewPlanPackageWithAllocationPrice",
]


class PlanCreateParams(TypedDict, total=False):
    currency: Required[str]
    """
    An ISO 4217 currency string or custom pricing unit (`credits`) for this plan's
    prices.
    """

    name: Required[str]

    prices: Required[List[Price]]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    default_invoice_memo: Optional[str]
    """
    Free-form text which is available on the invoice PDF and the Orb invoice portal.
    """

    external_plan_id: Optional[str]

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    net_terms: Optional[int]
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0.
    """


class PriceNewPlanUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""

    scaling_factor: Optional[float]
    """Multiplier to scale rated quantity by"""


class PriceNewPlanUnitPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["unit"]]

    name: Required[str]
    """The name of the price."""

    unit_config: Required[PriceNewPlanUnitPriceUnitConfig]

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


class PriceNewPlanPackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Optional[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class PriceNewPlanPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["package"]]

    name: Required[str]
    """The name of the price."""

    package_config: Required[PriceNewPlanPackagePricePackageConfig]

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


class PriceNewPlanMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""

    scaling_factor: Optional[float]
    """Optional multiplier to scale rated quantities by"""


class PriceNewPlanMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[List[PriceNewPlanMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""

    scaling_factor: Optional[float]
    """
    Default optional multiplier to scale rated quantities that fall into the default
    bucket by
    """


class PriceNewPlanMatrixPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    matrix_config: Required[PriceNewPlanMatrixPriceMatrixConfig]

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


class PriceNewPlanTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class PriceNewPlanTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[List[PriceNewPlanTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class PriceNewPlanTieredPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered"]]

    name: Required[str]
    """The name of the price."""

    tiered_config: Required[PriceNewPlanTieredPriceTieredConfig]

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


class PriceNewPlanTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class PriceNewPlanTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[List[PriceNewPlanTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class PriceNewPlanTieredBpsPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

    item_id: Required[str]
    """The id of the item the plan will be associated with."""

    model_type: Required[Literal["tiered_bps"]]

    name: Required[str]
    """The name of the price."""

    tiered_bps_config: Required[PriceNewPlanTieredBpsPriceTieredBpsConfig]

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


class PriceNewPlanBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class PriceNewPlanBpsPrice(TypedDict, total=False):
    bps_config: Required[PriceNewPlanBpsPriceBpsConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


class PriceNewPlanBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class PriceNewPlanBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[List[PriceNewPlanBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class PriceNewPlanBulkBpsPrice(TypedDict, total=False):
    bulk_bps_config: Required[PriceNewPlanBulkBpsPriceBulkBpsConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


class PriceNewPlanBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class PriceNewPlanBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[List[PriceNewPlanBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class PriceNewPlanBulkPrice(TypedDict, total=False):
    bulk_config: Required[PriceNewPlanBulkPriceBulkConfig]

    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


class PriceNewPlanThresholdTotalAmountPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


class PriceNewPlanTieredPackagePrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


class PriceNewPlanTieredWithMinimumPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


class PriceNewPlanPackageWithAllocationPrice(TypedDict, total=False):
    cadence: Required[Literal["annual", "monthly", "quarterly", "one_time"]]
    """The cadence to bill for this price on."""

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


Price = Union[
    PriceNewPlanUnitPrice,
    PriceNewPlanPackagePrice,
    PriceNewPlanMatrixPrice,
    PriceNewPlanTieredPrice,
    PriceNewPlanTieredBpsPrice,
    PriceNewPlanBpsPrice,
    PriceNewPlanBulkBpsPrice,
    PriceNewPlanBulkPrice,
    PriceNewPlanThresholdTotalAmountPrice,
    PriceNewPlanTieredPackagePrice,
    PriceNewPlanTieredWithMinimumPrice,
    PriceNewPlanPackageWithAllocationPrice,
]
