# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PlanVersionPhase"]


class PlanVersionPhase(BaseModel):
    id: str

    description: Optional[str] = None

    duration: Optional[int] = None
    """How many terms of length `duration_unit` this phase is active for.

    If null, this phase is evergreen and active indefinitely
    """

    duration_unit: Optional[Literal["daily", "monthly", "quarterly", "semi_annual", "annual"]] = None

    name: str

    order: int
    """Determines the ordering of the phase in a plan's lifecycle. 1 = first phase."""
