# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BillingCycleConfigurationModel"]


class BillingCycleConfigurationModel(BaseModel):
    duration: int

    duration_unit: Literal["day", "month"]
