# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["Subscriptions", "PaginationMetadata"]


class PaginationMetadata(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None


class Subscriptions(BaseModel):
    data: List[Subscription]

    pagination_metadata: PaginationMetadata
