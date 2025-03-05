# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.subscription_model import SubscriptionModel
from .shared.pagination_metadata import PaginationMetadata

__all__ = ["Subscriptions"]


class Subscriptions(BaseModel):
    data: List[SubscriptionModel]

    pagination_metadata: PaginationMetadata
