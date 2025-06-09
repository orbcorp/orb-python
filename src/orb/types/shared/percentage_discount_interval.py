# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["PercentageDiscountInterval"]


class PercentageDiscountInterval(BaseModel):
    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["percentage"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    filters: List[TransformPriceFilter]
    """The filters that determine which prices this discount interval applies to."""

    percentage_discount: float
    """
    Only available if discount_type is `percentage`.This is a number between 0
    and 1.
    """

    start_date: datetime
    """The start date of the discount interval."""
