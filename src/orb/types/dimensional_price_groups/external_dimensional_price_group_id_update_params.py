# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExternalDimensionalPriceGroupIDUpdateParams"]


class ExternalDimensionalPriceGroupIDUpdateParams(TypedDict, total=False):
    body_external_dimensional_price_group_id: Annotated[
        Optional[str], PropertyInfo(alias="external_dimensional_price_group_id")
    ]
    """
    An optional user-defined ID for this dimensional price group resource, used
    throughout the system as an alias for this dimensional price group. Use this
    field to identify a dimensional price group by an existing identifier in your
    system.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """
