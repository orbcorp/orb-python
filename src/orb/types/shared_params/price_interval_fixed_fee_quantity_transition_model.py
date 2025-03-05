# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PriceIntervalFixedFeeQuantityTransitionModel"]


class PriceIntervalFixedFeeQuantityTransitionModel(TypedDict, total=False):
    effective_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date that the fixed fee quantity transition should take effect."""

    quantity: Required[int]
    """The quantity of the fixed fee quantity transition."""
