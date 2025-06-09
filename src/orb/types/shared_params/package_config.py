# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PackageConfig"]


class PackageConfig(TypedDict, total=False):
    package_amount: Required[str]
    """A currency amount to rate usage by"""

    package_size: Required[int]
    """An integer amount to represent package size.

    For example, 1000 here would divide usage by 1000 before multiplying by
    package_amount in rating
    """
