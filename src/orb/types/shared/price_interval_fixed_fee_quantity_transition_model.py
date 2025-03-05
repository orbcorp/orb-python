# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["PriceIntervalFixedFeeQuantityTransitionModel"]


class PriceIntervalFixedFeeQuantityTransitionModel(BaseModel):
    effective_date: datetime
    """The date that the fixed fee quantity transition should take effect."""

    quantity: int
    """The quantity of the fixed fee quantity transition."""
