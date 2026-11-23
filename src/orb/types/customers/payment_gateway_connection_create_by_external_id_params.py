# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PaymentGatewayConnectionCreateByExternalIDParams"]


class PaymentGatewayConnectionCreateByExternalIDParams(TypedDict, total=False):
    payment_gateway_connection_id: Required[str]
    """The ID of the payment gateway connection to map the customer to."""

    is_default: bool
    """
    Whether Orb charges the customer for the billing entity's invoices through this
    mapping. The customer's first mapping for a billing entity is the default
    regardless.
    """

    provider_customer_id: Optional[str]
    """The ID of the customer in the external payment provider."""
