# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PaginationMetadataModel"]


class PaginationMetadataModel(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None
