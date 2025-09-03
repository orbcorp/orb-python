# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["Tier"]


class Tier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    unit_amount: Required[str]
    """Amount per unit"""

    last_unit: Optional[float]
    """Inclusive tier ending value.

    This value is null if and only if this is the last tier.
    """
