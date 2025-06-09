# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BPSConfig"]


class BPSConfig(BaseModel):
    bps: float
    """Basis point take rate per event"""

    per_unit_maximum: Optional[str] = None
    """Optional currency amount maximum to cap spend per event"""
