# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PaginationMetadata"]


class PaginationMetadata(BaseModel):
    has_more: bool

    next_cursor: Optional[str] = None
