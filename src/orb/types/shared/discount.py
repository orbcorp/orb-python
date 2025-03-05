# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .trial_discount import TrialDiscount
from .usage_discount import UsageDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["Discount"]

Discount: TypeAlias = Annotated[
    Union[PercentageDiscount, TrialDiscount, UsageDiscount, AmountDiscount], PropertyInfo(discriminator="discount_type")
]
