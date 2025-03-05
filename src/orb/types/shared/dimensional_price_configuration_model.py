# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["DimensionalPriceConfigurationModel"]


class DimensionalPriceConfigurationModel(BaseModel):
    dimension_values: List[str]

    dimensional_price_group_id: str
