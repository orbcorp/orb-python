# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TierConfig"]


class TierConfig(BaseModel):
    first_unit: float

    last_unit: Optional[float] = None

    unit_amount: str
