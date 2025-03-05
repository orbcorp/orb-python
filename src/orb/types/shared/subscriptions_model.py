# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .subscription_model import SubscriptionModel
from .pagination_metadata import PaginationMetadata

__all__ = ["SubscriptionsModel"]


class SubscriptionsModel(BaseModel):
    data: List[SubscriptionModel]

    pagination_metadata: PaginationMetadata
