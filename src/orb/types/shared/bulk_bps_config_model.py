# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BulkBpsConfigModel", "Tier"]


class Tier(BaseModel):
    bps: float
    """Basis points to rate on"""

    maximum_amount: Optional[str] = None
    """Upper bound for tier"""

    per_unit_maximum: Optional[str] = None
    """The maximum amount to charge for any one event"""


class BulkBpsConfigModel(BaseModel):
    tiers: List[Tier]
    """
    Tiers for a bulk BPS pricing model where all usage is aggregated to a single
    tier based on total volume
    """
