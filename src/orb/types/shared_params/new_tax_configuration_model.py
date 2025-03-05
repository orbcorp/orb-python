# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["NewTaxConfigurationModel", "NewAvalaraTaxConfiguration", "NewTaxJarConfiguration"]


class NewAvalaraTaxConfiguration(TypedDict, total=False):
    tax_exempt: Required[bool]

    tax_provider: Required[Literal["avalara"]]

    tax_exemption_code: Optional[str]


class NewTaxJarConfiguration(TypedDict, total=False):
    tax_exempt: Required[bool]

    tax_provider: Required[Literal["taxjar"]]


NewTaxConfigurationModel: TypeAlias = Union[NewAvalaraTaxConfiguration, NewTaxJarConfiguration]
