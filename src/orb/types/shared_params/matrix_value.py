# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["MatrixValue"]


class MatrixValue(TypedDict, total=False):
    dimension_values: Required[List[Optional[str]]]
    """One or two matrix keys to filter usage to this Matrix value by.

    For example, ["region", "tier"] could be used to filter cloud usage by a cloud
    region and an instance tier.
    """

    unit_amount: Required[str]
    """Unit price for the specified dimension_values"""
