# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentMethodDeletedWebhookEvent", "PaymentMethod"]


class PaymentMethod(BaseModel):
    """
    A payment method represents a customer's stored payment instrument held with an external payment
    provider (such as Adyen or Stripe).

    The serialization is intentionally minimal for now; provider-pulled details (e.g. card display
    metadata) will be added over time.
    """

    id: str
    """The Orb-assigned unique identifier for the payment method."""

    created_at: datetime
    """The time at which the payment method was created."""

    customer_id: str
    """The ID of the Orb customer this payment method is attached to."""

    default: bool
    """Whether this is the customer's default payment method."""

    external_payment_method_id: str
    """The identifier of this payment method in the external payment provider."""

    payment_method_type: Literal["card", "us_bank_account", "link", "amazon_pay", "crypto"]
    """The type of the underlying payment instrument, e.g.

    `card` or `us_bank_account`.
    """

    provider_type: Optional[str] = None
    """
    The external payment provider this method belongs to, derived from the linked
    payment gateway connection (e.g. `adyen` or `stripe`). Null if the connection
    has been removed.
    """


class PaymentMethodDeletedWebhookEvent(BaseModel):
    """Issued when a payment method is deleted."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    payment_method: PaymentMethod
    """
    A payment method represents a customer's stored payment instrument held with an
    external payment provider (such as Adyen or Stripe).

    The serialization is intentionally minimal for now; provider-pulled details
    (e.g. card display metadata) will be added over time.
    """

    properties: object

    type: Literal["payment_method.deleted"]
    """The event this payload describes."""
