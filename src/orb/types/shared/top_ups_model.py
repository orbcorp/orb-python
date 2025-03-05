# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .top_up_model import TopUpModel
from .pagination_metadata import PaginationMetadata

__all__ = ["TopUpsModel"]


class TopUpsModel(BaseModel):
    data: List[TopUpModel]

    pagination_metadata: PaginationMetadata
