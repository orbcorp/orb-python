# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .subscription import Subscription
from .shared.pagination_metadata import PaginationMetadata

__all__ = ["Subscriptions"]


class Subscriptions(BaseModel):
    data: List[Subscription]

    pagination_metadata: PaginationMetadata
