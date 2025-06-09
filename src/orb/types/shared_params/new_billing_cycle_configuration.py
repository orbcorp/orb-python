# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewBillingCycleConfiguration"]


class NewBillingCycleConfiguration(TypedDict, total=False):
    duration: Required[int]
    """The duration of the billing period."""

    duration_unit: Required[Literal["day", "month"]]
    """The unit of billing period duration."""
