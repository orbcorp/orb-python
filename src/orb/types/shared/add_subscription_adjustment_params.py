# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .new_adjustment_model import NewAdjustmentModel

__all__ = ["AddSubscriptionAdjustmentParams"]


class AddSubscriptionAdjustmentParams(BaseModel):
    adjustment: NewAdjustmentModel
    """The definition of a new adjustment to create and add to the subscription."""

    end_date: Optional[datetime] = None
    """The end date of the adjustment interval.

    This is the date that the adjustment will stop affecting prices on the
    subscription.
    """

    plan_phase_order: Optional[int] = None
    """The phase to add this adjustment to."""

    start_date: Optional[datetime] = None
    """The start date of the adjustment interval.

    This is the date that the adjustment will start affecting prices on the
    subscription. If null, the adjustment will start when the phase or subscription
    starts.
    """
