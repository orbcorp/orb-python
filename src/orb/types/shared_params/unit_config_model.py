# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UnitConfigModel"]


class UnitConfigModel(TypedDict, total=False):
    unit_amount: Required[str]
    """Rate per unit of usage"""
