# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.new_maximum import NewMaximum
from .shared_params.new_minimum import NewMinimum
from .shared_params.new_plan_bps_price import NewPlanBPSPrice
from .shared_params.new_usage_discount import NewUsageDiscount
from .shared_params.new_amount_discount import NewAmountDiscount
from .shared_params.new_plan_bulk_price import NewPlanBulkPrice
from .shared_params.new_plan_unit_price import NewPlanUnitPrice
from .shared_params.new_allocation_price import NewAllocationPrice
from .shared_params.new_plan_matrix_price import NewPlanMatrixPrice
from .shared_params.new_plan_tiered_price import NewPlanTieredPrice
from .shared_params.new_plan_package_price import NewPlanPackagePrice
from .shared_params.new_percentage_discount import NewPercentageDiscount
from .shared_params.new_plan_bulk_bps_price import NewPlanBulkBPSPrice
from .shared_params.new_plan_tiered_bps_price import NewPlanTieredBPSPrice
from .shared_params.new_plan_grouped_tiered_price import NewPlanGroupedTieredPrice
from .shared_params.new_plan_tiered_package_price import NewPlanTieredPackagePrice
from .shared_params.new_plan_unit_with_percent_price import NewPlanUnitWithPercentPrice
from .shared_params.new_plan_grouped_allocation_price import NewPlanGroupedAllocationPrice
from .shared_params.new_plan_bulk_with_proration_price import NewPlanBulkWithProrationPrice
from .shared_params.new_plan_tier_with_proration_price import NewPlanTierWithProrationPrice
from .shared_params.new_plan_tiered_with_minimum_price import NewPlanTieredWithMinimumPrice
from .shared_params.new_plan_unit_with_proration_price import NewPlanUnitWithProrationPrice
from .shared_params.new_plan_grouped_tiered_package_price import NewPlanGroupedTieredPackagePrice
from .shared_params.new_plan_matrix_with_allocation_price import NewPlanMatrixWithAllocationPrice
from .shared_params.new_plan_threshold_total_amount_price import NewPlanThresholdTotalAmountPrice
from .shared_params.new_plan_cumulative_grouped_bulk_price import NewPlanCumulativeGroupedBulkPrice
from .shared_params.new_plan_package_with_allocation_price import NewPlanPackageWithAllocationPrice
from .shared_params.new_plan_matrix_with_display_name_price import NewPlanMatrixWithDisplayNamePrice
from .shared_params.new_plan_max_group_tiered_package_price import NewPlanMaxGroupTieredPackagePrice
from .shared_params.new_plan_tiered_package_with_minimum_price import NewPlanTieredPackageWithMinimumPrice
from .shared_params.new_plan_grouped_with_metered_minimum_price import NewPlanGroupedWithMeteredMinimumPrice
from .shared_params.new_plan_grouped_with_prorated_minimum_price import NewPlanGroupedWithProratedMinimumPrice
from .shared_params.new_plan_scalable_matrix_with_unit_pricing_price import NewPlanScalableMatrixWithUnitPricingPrice
from .shared_params.new_plan_scalable_matrix_with_tiered_pricing_price import (
    NewPlanScalableMatrixWithTieredPricingPrice,
)

__all__ = [
    "BetaCreatePlanVersionParams",
    "AddAdjustment",
    "AddAdjustmentAdjustment",
    "AddPrice",
    "AddPricePrice",
    "RemoveAdjustment",
    "RemovePrice",
    "ReplaceAdjustment",
    "ReplaceAdjustmentAdjustment",
    "ReplacePrice",
    "ReplacePricePrice",
]


class BetaCreatePlanVersionParams(TypedDict, total=False):
    version: Required[int]
    """New version number."""

    add_adjustments: Optional[Iterable[AddAdjustment]]
    """Additional adjustments to be added to the plan."""

    add_prices: Optional[Iterable[AddPrice]]
    """Additional prices to be added to the plan."""

    remove_adjustments: Optional[Iterable[RemoveAdjustment]]
    """Adjustments to be removed from the plan."""

    remove_prices: Optional[Iterable[RemovePrice]]
    """Prices to be removed from the plan."""

    replace_adjustments: Optional[Iterable[ReplaceAdjustment]]
    """Adjustments to be replaced with additional adjustments on the plan."""

    replace_prices: Optional[Iterable[ReplacePrice]]
    """Prices to be replaced with additional prices on the plan."""

    set_as_default: Optional[bool]
    """Set this new plan version as the default"""


AddAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class AddAdjustment(TypedDict, total=False):
    adjustment: Required[AddAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this adjustment to."""


AddPricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanPackagePrice,
    NewPlanMatrixPrice,
    NewPlanTieredPrice,
    NewPlanTieredBPSPrice,
    NewPlanBPSPrice,
    NewPlanBulkBPSPrice,
    NewPlanBulkPrice,
    NewPlanThresholdTotalAmountPrice,
    NewPlanTieredPackagePrice,
    NewPlanTieredWithMinimumPrice,
    NewPlanUnitWithPercentPrice,
    NewPlanPackageWithAllocationPrice,
    NewPlanTierWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    NewPlanTieredPackageWithMinimumPrice,
    NewPlanMatrixWithAllocationPrice,
    NewPlanGroupedTieredPrice,
]


class AddPrice(TypedDict, total=False):
    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to add this price to."""

    price: Optional[AddPricePrice]
    """The price to add to the plan"""


class RemoveAdjustment(TypedDict, total=False):
    adjustment_id: Required[str]
    """The id of the adjustment to remove from on the plan."""

    plan_phase_order: Optional[int]
    """The phase to remove this adjustment from."""


class RemovePrice(TypedDict, total=False):
    price_id: Required[str]
    """The id of the price to remove from the plan."""

    plan_phase_order: Optional[int]
    """The phase to remove this price from."""


ReplaceAdjustmentAdjustment: TypeAlias = Union[
    NewPercentageDiscount, NewUsageDiscount, NewAmountDiscount, NewMinimum, NewMaximum
]


class ReplaceAdjustment(TypedDict, total=False):
    adjustment: Required[ReplaceAdjustmentAdjustment]
    """The definition of a new adjustment to create and add to the plan."""

    replaces_adjustment_id: Required[str]
    """The id of the adjustment on the plan to replace in the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this adjustment from."""


ReplacePricePrice: TypeAlias = Union[
    NewPlanUnitPrice,
    NewPlanPackagePrice,
    NewPlanMatrixPrice,
    NewPlanTieredPrice,
    NewPlanTieredBPSPrice,
    NewPlanBPSPrice,
    NewPlanBulkBPSPrice,
    NewPlanBulkPrice,
    NewPlanThresholdTotalAmountPrice,
    NewPlanTieredPackagePrice,
    NewPlanTieredWithMinimumPrice,
    NewPlanUnitWithPercentPrice,
    NewPlanPackageWithAllocationPrice,
    NewPlanTierWithProrationPrice,
    NewPlanUnitWithProrationPrice,
    NewPlanGroupedAllocationPrice,
    NewPlanGroupedWithProratedMinimumPrice,
    NewPlanGroupedWithMeteredMinimumPrice,
    NewPlanMatrixWithDisplayNamePrice,
    NewPlanBulkWithProrationPrice,
    NewPlanGroupedTieredPackagePrice,
    NewPlanMaxGroupTieredPackagePrice,
    NewPlanScalableMatrixWithUnitPricingPrice,
    NewPlanScalableMatrixWithTieredPricingPrice,
    NewPlanCumulativeGroupedBulkPrice,
    NewPlanTieredPackageWithMinimumPrice,
    NewPlanMatrixWithAllocationPrice,
    NewPlanGroupedTieredPrice,
]


class ReplacePrice(TypedDict, total=False):
    replaces_price_id: Required[str]
    """The id of the price on the plan to replace in the plan."""

    allocation_price: Optional[NewAllocationPrice]
    """The allocation price to add to the plan."""

    plan_phase_order: Optional[int]
    """The phase to replace this price from."""

    price: Optional[ReplacePricePrice]
    """The price to add to the plan"""
