# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .matrix_value import MatrixValue

__all__ = ["MatrixConfig"]


class MatrixConfig(BaseModel):
    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[MatrixValue]
    """Matrix values configuration"""
