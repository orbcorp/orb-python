# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AddressInputParam"]


class AddressInputParam(TypedDict, total=False):
    country: Required[str]

    city: Optional[str]

    line1: Optional[str]

    line2: Optional[str]

    postal_code: Optional[str]

    state: Optional[str]
