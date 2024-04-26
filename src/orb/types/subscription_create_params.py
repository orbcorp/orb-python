# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SubscriptionCreateParams",
    "PriceOverride",
    "PriceOverrideOverrideUnitPrice",
    "PriceOverrideOverrideUnitPriceUnitConfig",
    "PriceOverrideOverrideUnitPriceDiscount",
    "PriceOverrideOverridePackagePrice",
    "PriceOverrideOverridePackagePricePackageConfig",
    "PriceOverrideOverridePackagePriceDiscount",
    "PriceOverrideOverrideMatrixPrice",
    "PriceOverrideOverrideMatrixPriceMatrixConfig",
    "PriceOverrideOverrideMatrixPriceMatrixConfigMatrixValue",
    "PriceOverrideOverrideMatrixPriceDiscount",
    "PriceOverrideOverrideTieredPrice",
    "PriceOverrideOverrideTieredPriceTieredConfig",
    "PriceOverrideOverrideTieredPriceTieredConfigTier",
    "PriceOverrideOverrideTieredPriceDiscount",
    "PriceOverrideOverrideTieredBpsPrice",
    "PriceOverrideOverrideTieredBpsPriceTieredBpsConfig",
    "PriceOverrideOverrideTieredBpsPriceTieredBpsConfigTier",
    "PriceOverrideOverrideTieredBpsPriceDiscount",
    "PriceOverrideOverrideBpsPrice",
    "PriceOverrideOverrideBpsPriceBpsConfig",
    "PriceOverrideOverrideBpsPriceDiscount",
    "PriceOverrideOverrideBulkBpsPrice",
    "PriceOverrideOverrideBulkBpsPriceBulkBpsConfig",
    "PriceOverrideOverrideBulkBpsPriceBulkBpsConfigTier",
    "PriceOverrideOverrideBulkBpsPriceDiscount",
    "PriceOverrideOverrideBulkPrice",
    "PriceOverrideOverrideBulkPriceBulkConfig",
    "PriceOverrideOverrideBulkPriceBulkConfigTier",
    "PriceOverrideOverrideBulkPriceDiscount",
    "PriceOverrideOverrideThresholdTotalAmountPrice",
    "PriceOverrideOverrideThresholdTotalAmountPriceDiscount",
    "PriceOverrideOverrideTieredPackagePrice",
    "PriceOverrideOverrideTieredPackagePriceDiscount",
    "PriceOverrideOverrideTieredWithMinimumPrice",
    "PriceOverrideOverrideTieredWithMinimumPriceDiscount",
    "PriceOverrideOverridePackageWithAllocationPrice",
    "PriceOverrideOverridePackageWithAllocationPriceDiscount",
    "PriceOverrideOverrideUnitWithPercentPrice",
    "PriceOverrideOverrideUnitWithPercentPriceDiscount",
]


class SubscriptionCreateParams(TypedDict, total=False):
    align_billing_with_subscription_start_date: bool

    auto_collection: Optional[bool]

    aws_region: Optional[str]

    coupon_redemption_code: Optional[str]

    credits_overage_rate: Optional[float]

    customer_id: Optional[str]

    default_invoice_memo: Optional[str]

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    external_customer_id: Optional[str]

    external_marketplace: Optional[Literal["google", "aws", "azure"]]

    external_marketplace_reporting_id: Optional[str]

    external_plan_id: Optional[str]
    """
    The external_plan_id of the plan that the given subscription should be switched
    to. Note that either this property or `plan_id` must be specified.
    """

    initial_phase_order: Optional[int]

    invoicing_threshold: Optional[str]

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    net_terms: Optional[int]

    per_credit_overage_amount: Optional[str]

    plan_id: Optional[str]
    """The plan that the given subscription should be switched to.

    Note that either this property or `external_plan_id` must be specified.
    """

    price_overrides: Optional[Iterable[PriceOverride]]
    """Optionally provide a list of overrides for prices on the plan"""

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]


class PriceOverrideOverrideUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""


class PriceOverrideOverrideUnitPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideUnitPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["unit"]]

    unit_config: Required[PriceOverrideOverrideUnitPriceUnitConfig]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideUnitPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverridePackagePricePackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Required[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """


class PriceOverrideOverridePackagePriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverridePackagePrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["package"]]

    package_config: Required[PriceOverrideOverridePackagePricePackageConfig]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverridePackagePriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideMatrixPriceMatrixConfigMatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class PriceOverrideOverrideMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[PriceOverrideOverrideMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""


class PriceOverrideOverrideMatrixPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideMatrixPrice(TypedDict, total=False):
    id: Required[str]

    matrix_config: Required[PriceOverrideOverrideMatrixPriceMatrixConfig]

    model_type: Required[Literal["matrix"]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideMatrixPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideTieredPriceTieredConfigTier(TypedDict, total=False):
    first_unit: Required[float]
    """Inclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Exclusive tier ending value. If null, this is treated as the last tier"""


class PriceOverrideOverrideTieredPriceTieredConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceOverrideOverrideTieredPriceTieredConfigTier]]
    """Tiers for rating based on total usage quantities into the specified tier"""


class PriceOverrideOverrideTieredPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideTieredPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["tiered"]]

    tiered_config: Required[PriceOverrideOverrideTieredPriceTieredConfig]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideTieredPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideTieredBpsPriceTieredBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Per-event basis point rate"""

    minimum_amount: Required[str]
    """Inclusive tier starting value"""

    maximum_amount: Optional[str]
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str]
    """Per unit maximum to charge"""


class PriceOverrideOverrideTieredBpsPriceTieredBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceOverrideOverrideTieredBpsPriceTieredBpsConfigTier]]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """


class PriceOverrideOverrideTieredBpsPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideTieredBpsPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["tiered_bps"]]

    tiered_bps_config: Required[PriceOverrideOverrideTieredBpsPriceTieredBpsConfig]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideTieredBpsPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideBpsPriceBpsConfig(TypedDict, total=False):
    bps: Required[float]
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str]
    """Optional currency amount maximum to cap spend per event"""


class PriceOverrideOverrideBpsPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideBpsPrice(TypedDict, total=False):
    id: Required[str]

    bps_config: Required[PriceOverrideOverrideBpsPriceBpsConfig]

    model_type: Required[Literal["bps"]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideBpsPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideBulkBpsPriceBulkBpsConfigTier(TypedDict, total=False):
    bps: Required[float]
    """Basis points to rate on"""

    maximum_amount: Optional[str]
    """Upper bound for tier"""

    per_unit_maximum: Optional[str]
    """The maximum amount to charge for any one event"""


class PriceOverrideOverrideBulkBpsPriceBulkBpsConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceOverrideOverrideBulkBpsPriceBulkBpsConfigTier]]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """


class PriceOverrideOverrideBulkBpsPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideBulkBpsPrice(TypedDict, total=False):
    id: Required[str]

    bulk_bps_config: Required[PriceOverrideOverrideBulkBpsPriceBulkBpsConfig]

    model_type: Required[Literal["bulk_bps"]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideBulkBpsPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideBulkPriceBulkConfigTier(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit"""

    maximum_units: Optional[float]
    """Upper bound for this tier"""


class PriceOverrideOverrideBulkPriceBulkConfig(TypedDict, total=False):
    tiers: Required[Iterable[PriceOverrideOverrideBulkPriceBulkConfigTier]]
    """Bulk tiers for rating based on total usage volume"""


class PriceOverrideOverrideBulkPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideBulkPrice(TypedDict, total=False):
    id: Required[str]

    bulk_config: Required[PriceOverrideOverrideBulkPriceBulkConfig]

    model_type: Required[Literal["bulk"]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideBulkPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideThresholdTotalAmountPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideThresholdTotalAmountPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["threshold_total_amount"]]

    threshold_total_amount_config: Required[Dict[str, object]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideThresholdTotalAmountPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideTieredPackagePriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideTieredPackagePrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["tiered_package"]]

    tiered_package_config: Required[Dict[str, object]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideTieredPackagePriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideTieredWithMinimumPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideTieredWithMinimumPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["tiered_with_minimum"]]

    tiered_with_minimum_config: Required[Dict[str, object]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideTieredWithMinimumPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverridePackageWithAllocationPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverridePackageWithAllocationPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["package_with_allocation"]]

    package_with_allocation_config: Required[Dict[str, object]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverridePackageWithAllocationPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideUnitWithPercentPriceDiscount(TypedDict, total=False):
    discount_type: Required[Literal["percentage", "trial", "usage", "amount"]]

    amount_discount: Optional[str]
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: Optional[List[str]]
    """List of price_ids that this discount applies to.

    For plan/plan phase discounts, this can be a subset of prices.
    """

    percentage_discount: Optional[float]
    """Only available if discount_type is `percentage`.

    This is a number between 0 and 1.
    """

    trial_amount_discount: Optional[str]
    """Only available if discount_type is `trial`"""

    usage_discount: Optional[float]
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


class PriceOverrideOverrideUnitWithPercentPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["unit_with_percent"]]

    unit_with_percent_config: Required[Dict[str, object]]

    conversion_rate: Optional[float]
    """The per unit conversion rate of the price currency to the invoicing currency."""

    currency: Optional[str]
    """The currency of the price.

    If not provided, the currency of the plan will be used.
    """

    discount: Optional[PriceOverrideOverrideUnitWithPercentPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


PriceOverride = Union[
    PriceOverrideOverrideUnitPrice,
    PriceOverrideOverridePackagePrice,
    PriceOverrideOverrideMatrixPrice,
    PriceOverrideOverrideTieredPrice,
    PriceOverrideOverrideTieredBpsPrice,
    PriceOverrideOverrideBpsPrice,
    PriceOverrideOverrideBulkBpsPrice,
    PriceOverrideOverrideBulkPrice,
    PriceOverrideOverrideThresholdTotalAmountPrice,
    PriceOverrideOverrideTieredPackagePrice,
    PriceOverrideOverrideTieredWithMinimumPrice,
    PriceOverrideOverridePackageWithAllocationPrice,
    PriceOverrideOverrideUnitWithPercentPrice,
]
