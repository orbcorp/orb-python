# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PriceCreateParams", "Price", "Tier"]


class PriceCreateParams(TypedDict, total=False):
    cadence: Required[Literal["one_time", "monthly", "quarterly", "semi_annual", "annual"]]
    """Billing cadence for every price"""

    currency: Required[str]
    """An ISO 4217 currency string for every price."""

    item_id: Required[str]
    """The item for every price. Must be the group's billable metric item."""

    model_type: Required[Literal["unit", "tiered"]]

    prices: Required[Iterable[Price]]

    tiers: Optional[Iterable[Tier]]
    """Shared tier boundaries. Required for tiered prices and omitted for unit prices."""


class Price(TypedDict, total=False):
    amounts: Required[Iterable[float]]
    """One amount for a unit price.

    One amount per tier for a tiered price, in tier order.
    """

    dimension_values: Required[SequenceNotStr[str]]
    """Dimension values, in the group's dimension order."""

    name: Optional[str]
    """Price name. Defaults to the dimension values."""


class Tier(TypedDict, total=False):
    first_unit: Required[float]
    """Exclusive tier starting value"""

    last_unit: Optional[float]
    """Inclusive tier ending value. Null on the last tier."""
