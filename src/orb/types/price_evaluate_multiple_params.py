# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.new_floating_bps_price import NewFloatingBPSPrice
from .shared_params.new_floating_bulk_price import NewFloatingBulkPrice
from .shared_params.new_floating_unit_price import NewFloatingUnitPrice
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

__all__ = ["PriceEvaluateMultipleParams", "PriceEvaluation", "PriceEvaluationPrice"]


class PriceEvaluateMultipleParams(TypedDict, total=False):
    timeframe_end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The exclusive upper bound for event timestamps"""

    timeframe_start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The inclusive lower bound for event timestamps"""

    customer_id: Optional[str]
    """The ID of the customer to which this evaluation is scoped."""

    external_customer_id: Optional[str]
    """The external customer ID of the customer to which this evaluation is scoped."""

    price_evaluations: Iterable[PriceEvaluation]
    """List of prices to evaluate (max 100)"""


PriceEvaluationPrice: TypeAlias = Union[
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


class PriceEvaluation(TypedDict, total=False):
    external_price_id: Optional[str]
    """The external ID of a price to evaluate that exists in your Orb account."""

    filter: Optional[str]
    """
    A boolean
    [computed property](/extensibility/advanced-metrics#computed-properties) used to
    filter the underlying billable metric
    """

    grouping_keys: List[str]
    """
    Properties (or
    [computed properties](/extensibility/advanced-metrics#computed-properties)) used
    to group the underlying billable metric
    """

    price: Optional[PriceEvaluationPrice]
    """
    An inline price definition to evaluate, allowing you to test price
    configurations before adding them to Orb.
    """

    price_id: Optional[str]
    """The ID of a price to evaluate that exists in your Orb account."""
