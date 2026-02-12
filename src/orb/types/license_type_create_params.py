# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LicenseTypeCreateParams"]


class LicenseTypeCreateParams(TypedDict, total=False):
    grouping_key: Required[str]
    """The key used for grouping licenses of this type.

    This is typically a user identifier field.
    """

    name: Required[str]
    """The name of the license type."""
