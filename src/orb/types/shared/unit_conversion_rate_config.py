# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .conversion_rate_unit_config import ConversionRateUnitConfig

__all__ = ["UnitConversionRateConfig"]


class UnitConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["unit"]

    unit_config: ConversionRateUnitConfig
