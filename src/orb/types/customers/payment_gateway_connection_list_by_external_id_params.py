# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PaymentGatewayConnectionListByExternalIDParams"]


class PaymentGatewayConnectionListByExternalIDParams(TypedDict, total=False):
    billing_entity_id: Optional[str]
    """Only return mappings to this billing entity's connections."""

    payment_gateway_connection_id: Optional[str]
    """Only return the mapping to this connection."""
