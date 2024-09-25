# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .trial_discount import TrialDiscount
from .amount_discount import AmountDiscount
from .percentage_discount import PercentageDiscount

__all__ = ["InvoiceLevelDiscount"]

InvoiceLevelDiscount: TypeAlias = Annotated[
    Union[PercentageDiscount, AmountDiscount, TrialDiscount], PropertyInfo(discriminator="discount_type")
]
