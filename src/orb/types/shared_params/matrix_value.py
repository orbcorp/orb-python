# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MatrixValue"]


class MatrixValue(TypedDict, total=False):
    dimension_values: Required[SequenceNotStr[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by"""

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""
