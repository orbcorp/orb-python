# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubLineItemGroupingModel"]


class SubLineItemGroupingModel(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""
