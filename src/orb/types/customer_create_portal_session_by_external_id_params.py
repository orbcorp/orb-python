# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomerCreatePortalSessionByExternalIDParams"]


class CustomerCreatePortalSessionByExternalIDParams(TypedDict, total=False):
    expires_in_minutes: int
    """Duration in minutes until the portal session expires.

    Defaults to 60. Maximum 180.
    """

    invalidate_existing: bool
    """
    When true (default), creating this session soft-deletes any other active portal
    sessions for the customer. Set to false to allow concurrent sessions — useful
    when minting portal links for multiple authenticated end-users at once. The
    customer's permanent portal link (if any) is never invalidated by this.
    """
