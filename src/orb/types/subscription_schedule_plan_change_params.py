# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "SubscriptionSchedulePlanChangeParams",
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
    "PriceOverrideOverrideTestRatingFunctionPrice",
    "PriceOverrideOverrideTestRatingFunctionPriceDiscount",
    "PriceOverrideOverrideFivetranExamplePrice",
    "PriceOverrideOverrideFivetranExamplePriceDiscount",
    "PriceOverrideOverrideThresholdTotalAmountPrice",
    "PriceOverrideOverrideThresholdTotalAmountPriceDiscount",
    "PriceOverrideOverrideTieredPackagePrice",
    "PriceOverrideOverrideTieredPackagePriceDiscount",
    "PriceOverrideOverrideTieredWithMinimumPrice",
    "PriceOverrideOverrideTieredWithMinimumPriceDiscount",
    "PriceOverrideOverridePackageWithAllocationPrice",
    "PriceOverrideOverridePackageWithAllocationPriceDiscount",
]


class SubscriptionSchedulePlanChangeParams(TypedDict, total=False):
    change_option: Required[Literal["requested_date", "end_of_subscription_term", "immediate"]]

    align_billing_with_plan_change_date: Optional[bool]
    """[DEPRECATED] Use billing_cycle_alignment instead.

    Reset billing periods to be aligned with the plan change’s effective date.
    """

    billing_cycle_alignment: Optional[Literal["unchanged", "plan_change_date", "start_of_month"]]
    """
    Reset billing periods to be aligned with the plan change’s effective date or
    start of the month. Defaults to `unchanged` which keeps subscription's existing
    billing cycle alignment.
    """

    change_date: Optional[str]
    """The date that the plan change should take effect.

    This parameter can only be passed if the `change_option` is `requested_date`.
    """

    coupon_redemption_code: Optional[str]
    """Redemption code to be used for this subscription.

    If the coupon cannot be found by its redemption code, or cannot be redeemed, an
    error response will be returned and the plan change will not be scheduled.
    """

    credits_overage_rate: Optional[float]

    external_plan_id: Optional[str]
    """
    The external_plan_id of the plan that the given subscription should be switched
    to. Note that either this property or `plan_id` must be specified.
    """

    initial_phase_order: Optional[int]
    """The phase of the plan to start with"""

    invoicing_threshold: Optional[str]
    """
    When this subscription's accrued usage reaches this threshold, an invoice will
    be issued for the subscription. If not specified, invoices will only be issued
    at the end of the billing period.
    """

    per_credit_overage_amount: Optional[str]

    plan_id: Optional[str]
    """The plan that the given subscription should be switched to.

    Note that either this property or `external_plan_id` must be specified.
    """

    price_overrides: Optional[List[PriceOverride]]
    """Optionally provide a list of overrides for prices on the plan"""


class PriceOverrideOverrideUnitPriceUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""

    scaling_factor: Optional[float]
    """Multiplier to scale rated quantity by"""


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

    package_size: Optional[int]
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

    scaling_factor: Optional[float]
    """Optional multiplier to scale rated quantities by"""


class PriceOverrideOverrideMatrixPriceMatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[List[PriceOverrideOverrideMatrixPriceMatrixConfigMatrixValue]]
    """Matrix values for specified matrix grouping keys"""

    scaling_factor: Optional[float]
    """
    Default optional multiplier to scale rated quantities that fall into the default
    bucket by
    """


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
    tiers: Required[List[PriceOverrideOverrideTieredPriceTieredConfigTier]]
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
    tiers: Required[List[PriceOverrideOverrideTieredBpsPriceTieredBpsConfigTier]]
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
    tiers: Required[List[PriceOverrideOverrideBulkBpsPriceBulkBpsConfigTier]]
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
    tiers: Required[List[PriceOverrideOverrideBulkPriceBulkConfigTier]]
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

    discount: Optional[PriceOverrideOverrideBulkPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideTestRatingFunctionPriceDiscount(TypedDict, total=False):
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


class PriceOverrideOverrideTestRatingFunctionPrice(TypedDict, total=False):
    id: Required[str]

    model_type: Required[Literal["test_rating_function"]]

    test_rating_function_config: Required[Dict[str, object]]

    discount: Optional[PriceOverrideOverrideTestRatingFunctionPriceDiscount]
    """The subscription's override discount for the plan."""

    fixed_price_quantity: Optional[float]
    """The starting quantity of the price, if the price is a fixed price."""

    maximum_amount: Optional[str]
    """The subscription's override maximum amount for the plan."""

    minimum_amount: Optional[str]
    """The subscription's override minimum amount for the plan."""


class PriceOverrideOverrideFivetranExamplePriceDiscount(TypedDict, total=False):
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


class PriceOverrideOverrideFivetranExamplePrice(TypedDict, total=False):
    id: Required[str]

    fivetran_example_config: Required[Dict[str, object]]

    model_type: Required[Literal["fivetran_example"]]

    discount: Optional[PriceOverrideOverrideFivetranExamplePriceDiscount]
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

    discount: Optional[PriceOverrideOverridePackageWithAllocationPriceDiscount]
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
    PriceOverrideOverrideTestRatingFunctionPrice,
    PriceOverrideOverrideFivetranExamplePrice,
    PriceOverrideOverrideThresholdTotalAmountPrice,
    PriceOverrideOverrideTieredPackagePrice,
    PriceOverrideOverrideTieredWithMinimumPrice,
    PriceOverrideOverridePackageWithAllocationPrice,
]
