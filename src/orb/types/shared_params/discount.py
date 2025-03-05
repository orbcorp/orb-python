# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .trial_discount import TrialDiscount
from .usage_discount import UsageDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["Discount"]

Discount: TypeAlias = Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount]
