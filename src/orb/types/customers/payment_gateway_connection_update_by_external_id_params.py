# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentGatewayConnectionUpdateByExternalIDParams"]


class PaymentGatewayConnectionUpdateByExternalIDParams(TypedDict, total=False):
    external_customer_id: Required[str]

    is_default: Optional[Literal[True]]
    """
    Only `true` is accepted: it makes this the customer's default mapping for the
    connection's billing entity. Omit it to keep the current default. To move the
    default, set it on another mapping.
    """

    provider_customer_id: Optional[str]
    """The ID of the customer in the external payment provider.

    Omit it to keep the current one; `null` clears it, and Orb creates a Stripe
    customer at the next payment through this connection.
    """
