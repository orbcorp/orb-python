# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DraftPublishParams"]


class DraftPublishParams(TypedDict, total=False):
    set_as_default: bool
    """Also make the new version the plan's default."""
