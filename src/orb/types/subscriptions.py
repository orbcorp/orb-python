# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from .subscription import Subscription

from .shared.pagination_metadata import PaginationMetadata

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Subscriptions"]


class Subscriptions(BaseModel):
    data: List[Subscription]

    pagination_metadata: PaginationMetadata
