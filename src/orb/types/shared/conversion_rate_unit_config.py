# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ConversionRateUnitConfig"]


class ConversionRateUnitConfig(BaseModel):
    unit_amount: str
    """Amount per unit of overage"""
