# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.price import Price

__all__ = ["PriceCreateResponse"]


class PriceCreateResponse(BaseModel):
    data: List[Price]
    """The prices created by this request, in request order."""
