# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .matrix_value import MatrixValue

__all__ = ["MatrixConfig"]


class MatrixConfig(TypedDict, total=False):
    default_unit_amount: Required[str]
    """Default per unit rate for any usage not bucketed into a specified matrix_value"""

    dimensions: Required[SequenceNotStr[Optional[str]]]
    """One or two event property values to evaluate matrix groups by"""

    matrix_values: Required[Iterable[MatrixValue]]
    """Matrix values configuration"""
