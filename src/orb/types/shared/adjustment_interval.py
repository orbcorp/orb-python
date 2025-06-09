# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .plan_phase_maximum_adjustment import PlanPhaseMaximumAdjustment
from .plan_phase_minimum_adjustment import PlanPhaseMinimumAdjustment
from .plan_phase_usage_discount_adjustment import PlanPhaseUsageDiscountAdjustment
from .plan_phase_amount_discount_adjustment import PlanPhaseAmountDiscountAdjustment
from .plan_phase_percentage_discount_adjustment import PlanPhasePercentageDiscountAdjustment

__all__ = ["AdjustmentInterval", "Adjustment"]

Adjustment: TypeAlias = Annotated[
    Union[
        PlanPhaseUsageDiscountAdjustment,
        PlanPhaseAmountDiscountAdjustment,
        PlanPhasePercentageDiscountAdjustment,
        PlanPhaseMinimumAdjustment,
        PlanPhaseMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class AdjustmentInterval(BaseModel):
    id: str

    adjustment: Adjustment

    applies_to_price_interval_ids: List[str]
    """The price interval IDs that this adjustment applies to."""

    end_date: Optional[datetime] = None
    """The end date of the adjustment interval."""

    start_date: datetime
    """The start date of the adjustment interval."""
