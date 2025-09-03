# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnitConfig"]


class UnitConfig(BaseModel):
    unit_amount: str
    """Rate per unit of usage"""

    scaling_factor: Optional[float] = None
    """Multiplier to scale rated quantity by"""
