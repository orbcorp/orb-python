# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.new_usage_discount import NewUsageDiscount
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared.billing_cycle_relative_date import BillingCycleRelativeDate
from .shared_params.new_allocation_price import NewAllocationPrice
from .shared_params.new_floating_bps_price import NewFloatingBPSPrice
from .shared_params.new_floating_bulk_price import NewFloatingBulkPrice
from .shared_params.new_floating_unit_price import NewFloatingUnitPrice
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .shared_params.new_floating_matrix_price import NewFloatingMatrixPrice
from .shared_params.new_floating_tiered_price import NewFloatingTieredPrice
from .shared_params.new_floating_package_price import NewFloatingPackagePrice
from .shared_params.new_floating_bulk_bps_price import NewFloatingBulkBPSPrice
from .shared_params.new_floating_tiered_bps_price import NewFloatingTieredBPSPrice
from .shared_params.new_floating_grouped_tiered_price import NewFloatingGroupedTieredPrice
from .shared_params.new_floating_tiered_package_price import NewFloatingTieredPackagePrice
from .shared_params.new_floating_unit_with_percent_price import NewFloatingUnitWithPercentPrice
from .shared_params.new_floating_grouped_allocation_price import NewFloatingGroupedAllocationPrice
from .shared_params.new_floating_bulk_with_proration_price import NewFloatingBulkWithProrationPrice
from .shared_params.new_floating_tiered_with_minimum_price import NewFloatingTieredWithMinimumPrice
from .shared_params.new_floating_unit_with_proration_price import NewFloatingUnitWithProrationPrice
from .shared_params.new_floating_tiered_with_proration_price import NewFloatingTieredWithProrationPrice
from .shared_params.new_floating_grouped_tiered_package_price import NewFloatingGroupedTieredPackagePrice
from .shared_params.new_floating_matrix_with_allocation_price import NewFloatingMatrixWithAllocationPrice
from .shared_params.new_floating_threshold_total_amount_price import NewFloatingThresholdTotalAmountPrice
from .shared_params.new_floating_cumulative_grouped_bulk_price import NewFloatingCumulativeGroupedBulkPrice
from .shared_params.new_floating_package_with_allocation_price import NewFloatingPackageWithAllocationPrice
from .shared_params.new_floating_matrix_with_display_name_price import NewFloatingMatrixWithDisplayNamePrice
from .shared_params.new_floating_max_group_tiered_package_price import NewFloatingMaxGroupTieredPackagePrice
from .shared_params.new_floating_tiered_package_with_minimum_price import NewFloatingTieredPackageWithMinimumPrice
from .shared_params.new_floating_grouped_with_metered_minimum_price import NewFloatingGroupedWithMeteredMinimumPrice
from .shared_params.new_floating_grouped_with_prorated_minimum_price import NewFloatingGroupedWithProratedMinimumPrice
from .shared_params.new_floating_scalable_matrix_with_unit_pricing_price import (
    NewFloatingScalableMatrixWithUnitPricingPrice,
)
from .shared_params.new_floating_scalable_matrix_with_tiered_pricing_price import (
    NewFloatingScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "SubscriptionPriceIntervalsParams",
    "Add",
    "AddDiscount",
    "AddDiscountAmountDiscountCreationParams",
    "AddDiscountPercentageDiscountCreationParams",
    "AddDiscountUsageDiscountCreationParams",
    "AddFixedFeeQuantityTransition",
    "AddPrice",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "Edit",
    "EditFixedFeeQuantityTransition",
    "EditAdjustment",
]


class SubscriptionPriceIntervalsParams(TypedDict, total=False):
    add: Iterable[Add]
    """A list of price intervals to add to the subscription."""

    add_adjustments: Iterable[AddAdjustment]
    """A list of adjustments to add to the subscription."""

    allow_invoice_credit_or_void: Optional[bool]
    """
    If false, this request will fail if it would void an issued invoice or create a
    credit note. Consider using this as a safety mechanism if you do not expect
    existing invoices to be changed.
    """

    edit: Iterable[Edit]
    """A list of price intervals to edit on the subscription."""

    edit_adjustments: Iterable[EditAdjustment]
    """A list of adjustments to edit on the subscription."""


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


AddDiscount: TypeAlias = Union[
    AddDiscountAmountDiscountCreationParams,
    AddDiscountPercentageDiscountCreationParams,
    AddDiscountUsageDiscountCreationParams,
]


class AddFixedFeeQuantityTransition(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""


AddPrice: TypeAlias = Union[
    NewFloatingUnitPrice,
    NewFloatingPackagePrice,
    NewFloatingMatrixPrice,
    NewFloatingMatrixWithAllocationPrice,
    NewFloatingTieredPrice,
    NewFloatingTieredBPSPrice,
    NewFloatingBPSPrice,
    NewFloatingBulkBPSPrice,
    NewFloatingBulkPrice,
    NewFloatingThresholdTotalAmountPrice,
    NewFloatingTieredPackagePrice,
    NewFloatingGroupedTieredPrice,
    NewFloatingMaxGroupTieredPackagePrice,
    NewFloatingTieredWithMinimumPrice,
    NewFloatingPackageWithAllocationPrice,
    NewFloatingTieredPackageWithMinimumPrice,
    NewFloatingUnitWithPercentPrice,
    NewFloatingTieredWithProrationPrice,
    NewFloatingUnitWithProrationPrice,
    NewFloatingGroupedAllocationPrice,
    NewFloatingGroupedWithProratedMinimumPrice,
    NewFloatingGroupedWithMeteredMinimumPrice,
    NewFloatingMatrixWithDisplayNamePrice,
    NewFloatingBulkWithProrationPrice,
    NewFloatingGroupedTieredPackagePrice,
    NewFloatingScalableMatrixWithUnitPricingPrice,
    NewFloatingScalableMatrixWithTieredPricingPrice,
    NewFloatingCumulativeGroupedBulkPrice,
]


class Add(TypedDict, total=False):
    start_date: Required[
        Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    ]
    """The start date of the price interval.

    This is the date that the price will start billing on the subscription.
    """

    allocation_price: Optional[NewAllocationPrice]
    """The definition of a new allocation price to create and add to the subscription."""

    discounts: Optional[Iterable[AddDiscount]]
    """A list of discounts to initialize on the price interval."""

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The end date of the price interval.

    This is the date that the price will stop billing on the subscription.
    """

    external_price_id: Optional[str]
    """The external price id of the price to add to the subscription."""

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](/extensibility/advanced-metrics#computed-properties). If
    null, usage queries will not include any additional filter.
    """

    fixed_fee_quantity_transitions: Optional[Iterable[AddFixedFeeQuantityTransition]]
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

    price: Optional[AddPrice]
    """The definition of a new price to create and add to the subscription."""

    price_id: Optional[str]
    """The id of the price to add to the subscription."""

    usage_customer_ids: Optional[List[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


AddAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the subscription."""

    start_date: Required[
        Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    ]
    """The start date of the adjustment interval.

    This is the date that the adjustment will start affecting prices on the
    subscription. The adjustment will apply to invoice dates that overlap with this
    `start_date`. This `start_date` is treated as inclusive for in-advance prices,
    and exclusive for in-arrears prices.
    """

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The end date of the adjustment interval.

    This is the date that the adjustment will stop affecting prices on the
    subscription. The adjustment will apply to invoice dates that overlap with this
    `end_date`.This `end_date` is treated as exclusive for in-advance prices, and
    inclusive for in-arrears prices.
    """


class EditFixedFeeQuantityTransition(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""


class Edit(TypedDict, total=False):
    price_interval_id: Required[str]
    """The id of the price interval to edit."""

    billing_cycle_day: Optional[int]
    """The updated billing cycle day for this price interval.

    If not specified, the billing cycle day will not be updated. Note that
    overlapping price intervals must have the same billing cycle day.
    """

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The updated end date of this price interval.

    If not specified, the end date will not be updated.
    """

    filter: Optional[str]
    """An additional filter to apply to usage queries.

    This filter must be expressed as a boolean
    [computed property](/extensibility/advanced-metrics#computed-properties). If
    null, usage queries will not include any additional filter.
    """

    fixed_fee_quantity_transitions: Optional[Iterable[EditFixedFeeQuantityTransition]]
    """A list of fixed fee quantity transitions to use for this price interval.

    Note that this list will overwrite all existing fixed fee quantity transitions
    on the price interval.
    """

    start_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    """The updated start date of this price interval.

    If not specified, the start date will not be updated.
    """

    usage_customer_ids: Optional[List[str]]
    """
    A list of customer IDs whose usage events will be aggregated and billed under
    this subscription. By default, a subscription only considers usage events
    associated with its attached customer's customer_id. When usage_customer_ids is
    provided, the subscription includes usage events from the specified customers
    only. Provided usage_customer_ids must be either the customer for this
    subscription itself, or any of that customer's children.
    """


class EditAdjustment(TypedDict, total=False):
    adjustment_interval_id: Required[str]
    """The id of the adjustment interval to edit."""

    end_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate, None], PropertyInfo(format="iso8601")]
    """The updated end date of this adjustment interval.

    If not specified, the end date will not be updated.
    """

    start_date: Annotated[Union[Union[str, datetime], BillingCycleRelativeDate], PropertyInfo(format="iso8601")]
    """The updated start date of this adjustment interval.

    If not specified, the start date will not be updated.
    """
