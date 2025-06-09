# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomExpiration"]


class CustomExpiration(TypedDict, total=False):
    duration: Required[int]

    duration_unit: Required[Literal["day", "month"]]
