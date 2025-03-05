# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.pagination_metadata import PaginationMetadata
from ..shared.dimensional_price_group_model import DimensionalPriceGroupModel

__all__ = ["DimensionalPriceGroups"]


class DimensionalPriceGroups(BaseModel):
    data: List[DimensionalPriceGroupModel]

    pagination_metadata: PaginationMetadata
