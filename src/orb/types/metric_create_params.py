# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["MetricCreateParams"]


class MetricCreateParams(TypedDict, total=False):
    description: Required[Optional[str]]
    """A description of the metric."""

    item_id: Required[str]
    """The id of the item"""

    name: Required[str]
    """The name of the metric."""

    sql: Required[str]
    """A sql string defining the metric."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """
