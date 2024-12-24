# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["DimensionalPriceGroup"]


class DimensionalPriceGroup(BaseModel):
    id: str

    billable_metric_id: str
    """The billable metric associated with this dimensional price group.

    All prices associated with this dimensional price group will be computed using
    this billable metric.
    """

    dimensions: List[str]
    """The dimensions that this dimensional price group is defined over"""

    external_dimensional_price_group_id: Optional[str] = None
    """An alias for the dimensional price group"""

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    name: str
    """The name of the dimensional price group"""
