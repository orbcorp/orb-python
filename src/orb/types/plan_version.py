# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.price import Price
from .plan_version_phase import PlanVersionPhase
from .shared.plan_phase_maximum_adjustment import PlanPhaseMaximumAdjustment
from .shared.plan_phase_minimum_adjustment import PlanPhaseMinimumAdjustment
from .shared.plan_phase_usage_discount_adjustment import PlanPhaseUsageDiscountAdjustment
from .shared.plan_phase_amount_discount_adjustment import PlanPhaseAmountDiscountAdjustment
from .shared.plan_phase_percentage_discount_adjustment import PlanPhasePercentageDiscountAdjustment

__all__ = ["PlanVersion", "Adjustment"]

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


class PlanVersion(BaseModel):
    adjustments: List[Adjustment]
    """Adjustments for this plan.

    If the plan has phases, this includes adjustments across all phases of the plan.
    """

    created_at: datetime

    plan_phases: Optional[List[PlanVersionPhase]] = None

    prices: List[Price]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    version: int
