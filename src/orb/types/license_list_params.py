# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LicenseListParams"]


class LicenseListParams(TypedDict, total=False):
    subscription_id: Required[str]

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    external_license_id: Optional[str]

    license_type_id: Optional[str]

    limit: int
    """The number of items to fetch. Defaults to 20."""

    status: Optional[Literal["active", "inactive"]]
