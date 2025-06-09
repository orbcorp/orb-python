# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .conversion_rate_tiered_config import ConversionRateTieredConfig

__all__ = ["TieredConversionRateConfig"]


class TieredConversionRateConfig(BaseModel):
    conversion_rate_type: Literal["tiered"]

    tiered_config: ConversionRateTieredConfig
