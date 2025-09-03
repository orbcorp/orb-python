# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MatrixWithAllocationConfig", "MatrixValue"]


class MatrixValue(BaseModel):
    dimension_values: List[Optional[str]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: str
    """Unit price for the specified dimension_values"""


class MatrixWithAllocationConfig(BaseModel):
    allocation: str
    """Usage allocation"""

    default_unit_amount: str
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: List[Optional[str]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: List[MatrixValue]
    """Matrix values configuration"""
