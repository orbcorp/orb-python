# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NewBillingCycleConfiguration"]


class NewBillingCycleConfiguration(BaseModel):
    duration: int
    """The duration of the billing period."""

    duration_unit: Literal["day", "month"]
    """The unit of billing period duration."""
