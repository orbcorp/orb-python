# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LicenseRetrieveByExternalIDParams"]


class LicenseRetrieveByExternalIDParams(TypedDict, total=False):
    license_type_id: Required[str]
    """The ID of the license type to fetch the license for."""

    subscription_id: Required[str]
    """The ID of the subscription to fetch the license for."""
