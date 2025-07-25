# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConversionRateUnitConfig"]


class ConversionRateUnitConfig(TypedDict, total=False):
    unit_amount: Required[str]
    """Amount per unit of overage"""
