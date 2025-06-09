# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SubLineItemMatrixConfig"]


class SubLineItemMatrixConfig(BaseModel):
    dimension_values: List[Optional[str]]
    """The ordered dimension values for this line item."""
