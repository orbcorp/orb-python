# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewAvalaraTaxConfigurationParam"]


class NewAvalaraTaxConfigurationParam(TypedDict, total=False):
    tax_exempt: Required[bool]

    tax_provider: Required[Literal["avalara"]]

    tax_exemption_code: Optional[str]
