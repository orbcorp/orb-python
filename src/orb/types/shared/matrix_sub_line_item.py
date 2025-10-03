# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .sub_line_item_grouping import SubLineItemGrouping
from .sub_line_item_matrix_config import SubLineItemMatrixConfig

__all__ = ["MatrixSubLineItem"]


class MatrixSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemGrouping] = None

    matrix_config: SubLineItemMatrixConfig

    name: str

    quantity: float

    type: Literal["matrix"]

    scaled_quantity: Optional[float] = None
    """The scaled quantity for this line item for specific pricing structures"""
