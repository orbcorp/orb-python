# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["LicenseTypeRetrieveResponse"]


class LicenseTypeRetrieveResponse(BaseModel):
    """
    The LicenseType resource represents a type of license that can be assigned to users.
    License types are used during billing by grouping metrics on the configured grouping key.
    """

    id: str
    """The Orb-assigned unique identifier for the license type."""

    grouping_key: str
    """The key used for grouping licenses of this type.

    This is typically a user identifier field.
    """

    name: str
    """The name of the license type."""
