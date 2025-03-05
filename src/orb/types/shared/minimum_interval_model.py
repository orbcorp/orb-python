# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MinimumIntervalModel"]


class MinimumIntervalModel(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this minimum interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this minimum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the minimum interval."""

    minimum_amount: str
    """
    The minimum amount to charge in a given billing period for the price intervals
    this minimum applies to.
    """

    start_date: datetime
    """The start date of the minimum interval."""
