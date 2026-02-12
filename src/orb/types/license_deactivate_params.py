# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LicenseDeactivateParams"]


class LicenseDeactivateParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The date to deactivate the license.

    If not provided, defaults to end of day today in the customer's timezone.
    """
