# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel
from ..shared.pagination_metadata import PaginationMetadata

__all__ = ["UsageGetUsageResponse", "Data"]


class Data(BaseModel):
    """
    The LicenseUsage resource represents usage and remaining credits for a license over a date range.

    When grouped by 'day' only, license_id and external_license_id will be null as the data
    is aggregated across all licenses.
    """

    allocated_credits: float
    """The total credits allocated to this license for the period."""

    consumed_credits: float
    """The credits consumed by this license for the period."""

    end_date: date
    """The end date of the usage period."""

    license_type_id: str
    """The unique identifier for the license type."""

    pricing_unit: str
    """The pricing unit for the credits (e.g., 'credits')."""

    remaining_credits: float
    """The remaining credits available for this license (allocated - consumed)."""

    start_date: date
    """The start date of the usage period."""

    subscription_id: str
    """The unique identifier for the subscription."""

    allocation_eligible_credits: Optional[float] = None
    """
    Credits consumed while the license was active (eligible for individual
    allocation deduction).
    """

    external_license_id: Optional[str] = None
    """The external identifier for the license. Null when grouped by day only."""

    license_id: Optional[str] = None
    """The unique identifier for the license. Null when grouped by day only."""

    shared_pool_credits: Optional[float] = None
    """
    Credits consumed while the license was inactive (draws from shared pool, not
    individual allocation).
    """


class UsageGetUsageResponse(BaseModel):
    data: List[Data]

    pagination_metadata: PaginationMetadata
