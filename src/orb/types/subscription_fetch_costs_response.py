# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.aggregated_cost_model import AggregatedCostModel

__all__ = ["SubscriptionFetchCostsResponse"]


class SubscriptionFetchCostsResponse(BaseModel):
    data: List[AggregatedCostModel]
