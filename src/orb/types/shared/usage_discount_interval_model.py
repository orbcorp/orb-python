# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UsageDiscountIntervalModel"]


class UsageDiscountIntervalModel(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this discount interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["usage"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    start_date: datetime
    """The start date of the discount interval."""

    usage_discount: float
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """
