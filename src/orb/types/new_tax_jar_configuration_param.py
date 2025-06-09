# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewTaxJarConfigurationParam"]


class NewTaxJarConfigurationParam(TypedDict, total=False):
    tax_exempt: Required[bool]

    tax_provider: Required[Literal["taxjar"]]
