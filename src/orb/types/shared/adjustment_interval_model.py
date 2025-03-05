# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .adjustment_model import AdjustmentModel

__all__ = ["AdjustmentIntervalModel"]


class AdjustmentIntervalModel(BaseModel):
    id: str

    adjustment: AdjustmentModel

    applies_to_price_interval_ids: List[str]
    """The price interval IDs that this adjustment applies to."""

    end_date: Optional[datetime] = None
    """The end date of the adjustment interval."""

    start_date: datetime
    """The start date of the adjustment interval."""
