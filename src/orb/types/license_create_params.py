# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LicenseCreateParams"]


class LicenseCreateParams(TypedDict, total=False):
    external_license_id: Required[str]
    """The external identifier for the license."""

    license_type_id: Required[str]

    subscription_id: Required[str]

    end_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The end date of the license.

    If not provided, the license will remain active until deactivated.
    """

    start_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The start date of the license.

    If not provided, defaults to start of day today in the customer's timezone.
    """
