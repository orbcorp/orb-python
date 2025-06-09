# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .conversion_rate_tiered_config import ConversionRateTieredConfig

__all__ = ["TieredConversionRateConfig"]


class TieredConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["tiered"]]

    tiered_config: Required[ConversionRateTieredConfig]
