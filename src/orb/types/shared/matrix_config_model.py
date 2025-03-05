# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .matrix_value_model import MatrixValueModel

__all__ = ["MatrixConfigModel"]


class MatrixConfigModel(BaseModel):
    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[MatrixValueModel]
    """Matrix values for specified matrix grouping keys"""
