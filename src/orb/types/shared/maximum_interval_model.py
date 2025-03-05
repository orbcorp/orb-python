# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MaximumIntervalModel"]


class MaximumIntervalModel(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this maximum interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this maximum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the maximum interval."""

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the price intervals
    this transform applies to.
    """

    start_date: datetime
    """The start date of the maximum interval."""
