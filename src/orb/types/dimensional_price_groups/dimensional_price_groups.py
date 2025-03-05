# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..dimensional_price_group import DimensionalPriceGroup
from ..shared.pagination_metadata import PaginationMetadata

__all__ = ["DimensionalPriceGroups"]


class DimensionalPriceGroups(BaseModel):
    data: List[DimensionalPriceGroup]

    pagination_metadata: PaginationMetadata
