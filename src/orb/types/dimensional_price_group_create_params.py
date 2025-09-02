# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DimensionalPriceGroupCreateParams"]


class DimensionalPriceGroupCreateParams(TypedDict, total=False):
    billable_metric_id: Required[str]

    dimensions: Required[SequenceNotStr[str]]
    """The set of keys (in order) used to disambiguate prices in the group."""

    name: Required[str]

    external_dimensional_price_group_id: Optional[str]

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """
