# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .shared import PaginationMetadata
from .._models import BaseModel
from .subscription import Subscription

__all__ = ["Subscriptions"]


class Subscriptions(BaseModel):
    data: List[Subscription]

    pagination_metadata: PaginationMetadata
