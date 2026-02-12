# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UsageGetUsageParams"]


class UsageGetUsageParams(TypedDict, total=False):
    cursor: Optional[str]
    """Pagination cursor from a previous request."""

    end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """End date for the usage period (YYYY-MM-DD).

    Defaults to end of current billing period.
    """

    group_by: Optional[SequenceNotStr[str]]
    """How to group the results.

    Valid values: 'license', 'day'. Can be combined (e.g., 'license,day').
    """

    limit: int
    """Maximum number of rows in the response data (default 20, max 100)."""

    start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Start date for the usage period (YYYY-MM-DD).

    Defaults to start of current billing period.
    """
