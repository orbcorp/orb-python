# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .transform_price_filter import TransformPriceFilter

__all__ = ["AmountDiscountInterval"]


class AmountDiscountInterval(BaseModel):
    amount_discount: str
    """Only available if discount_type is `amount`."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["amount"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    filters: List[TransformPriceFilter]
    """The filters that determine which prices this discount interval applies to."""

    start_date: datetime
    """The start date of the discount interval."""
