# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from ..._models import BaseModel

__all__ = ["EvaluatePriceGroup"]


class EvaluatePriceGroup(BaseModel):
    amount: str
    """The price's output for the group"""

    grouping_values: List[Union[str, float, bool]]
    """The values for the group in the order specified by `grouping_keys`"""

    quantity: float
    """The price's usage quantity for the group"""
