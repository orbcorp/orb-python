# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .conversion_rate_unit_config import ConversionRateUnitConfig

__all__ = ["UnitConversionRateConfig"]


class UnitConversionRateConfig(TypedDict, total=False):
    conversion_rate_type: Required[Literal["unit"]]

    unit_config: Required[ConversionRateUnitConfig]
