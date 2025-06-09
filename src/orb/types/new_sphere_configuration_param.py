# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewSphereConfigurationParam"]


class NewSphereConfigurationParam(TypedDict, total=False):
    tax_exempt: Required[bool]

    tax_provider: Required[Literal["sphere"]]
