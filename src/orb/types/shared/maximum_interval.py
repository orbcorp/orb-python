# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["MaximumInterval"]


class MaximumInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this maximum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the maximum interval."""

    filters: List[TransformPriceFilter]
    """The filters that determine which prices this maximum interval applies to."""

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the price intervals
    this transform applies to.
    """

    start_date: datetime
    """The start date of the maximum interval."""
