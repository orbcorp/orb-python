# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TieredBpsConfigModel", "Tier"]


class Tier(BaseModel):
    bps: float
    """Per-event basis point rate"""

    minimum_amount: str
    """Inclusive tier starting value"""

    maximum_amount: Optional[str] = None
    """Exclusive tier ending value"""

    per_unit_maximum: Optional[str] = None
    """Per unit maximum to charge"""


class TieredBpsConfigModel(BaseModel):
    tiers: List[Tier]
    """
    Tiers for a Graduated BPS pricing model, where usage is bucketed into specified
    tiers
    """
