# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["NewTaxJarConfigurationParam"]


class NewTaxJarConfigurationParam(TypedDict, total=False):
    tax_exempt: Required[bool]

    tax_provider: Required[Literal["taxjar"]]

    automatic_tax_enabled: Optional[bool]
    """Whether to automatically calculate tax for this customer.

    When null, inherits from account-level setting. When true or false, overrides
    the account setting.
    """
