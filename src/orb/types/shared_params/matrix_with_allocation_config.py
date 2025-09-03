# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MatrixWithAllocationConfig", "MatrixValue"]


class MatrixValue(TypedDict, total=False):
    dimension_values: Required[SequenceNotStr[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""


class MatrixWithAllocationConfig(TypedDict, total=False):
    allocation: Required[str]
    """Usage allocation"""

    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[SequenceNotStr[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[MatrixValue]]
    """Matrix values configuration"""
