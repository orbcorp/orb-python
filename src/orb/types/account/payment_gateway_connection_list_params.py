# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["PaymentGatewayConnectionListParams"]


class PaymentGatewayConnectionListParams(TypedDict, total=False):
    billing_entity_id: Optional[str]
    """Only return connections of this billing entity."""

    cursor: Optional[str]
    """Cursor for pagination.

    This can be populated by the `next_cursor` value returned from the initial
    request.
    """

    limit: int
    """The number of items to fetch. Defaults to 20."""

    provider_type: Optional[Literal["stripe", "adyen"]]
    """Only return connections of this payment provider."""
