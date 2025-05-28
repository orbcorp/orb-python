# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BetaSetDefaultPlanVersionParams"]


class BetaSetDefaultPlanVersionParams(TypedDict, total=False):
    version: Required[int]
    """Plan version to set as the default."""
