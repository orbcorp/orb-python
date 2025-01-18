# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .evaluate_price_group import EvaluatePriceGroup

__all__ = ["PriceEvaluateResponse"]


class PriceEvaluateResponse(BaseModel):
    data: List[EvaluatePriceGroup]
