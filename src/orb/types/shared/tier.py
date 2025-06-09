# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Tier"]


class Tier(BaseModel):
    first_unit: float
    """Exclusive tier starting value"""

    unit_amount: str
    """Amount per unit"""

    last_unit: Optional[float] = None
    """Inclusive tier ending value. If null, this is treated as the last tier"""
