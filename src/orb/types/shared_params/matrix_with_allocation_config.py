# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, TypedDict

from .matrix_value import MatrixValue

__all__ = ["MatrixWithAllocationConfig"]


class MatrixWithAllocationConfig(TypedDict, total=False):
    allocation: Required[float]
    """Allocation to be used to calculate the price"""

    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[List[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[MatrixValue]]
    """Matrix values for specified matrix grouping keys"""
