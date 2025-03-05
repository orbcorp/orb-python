# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .aggregated_cost_model import AggregatedCostModel

__all__ = ["CustomerCostsModel"]


class CustomerCostsModel(BaseModel):
    data: List[AggregatedCostModel]
