# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomerPaymentGatewayConnection"]


class CustomerPaymentGatewayConnection(BaseModel):
    """A customer's mapping to one payment gateway connection."""

    billing_entity_id: str
    """The ID of the billing entity that collects payments through the connection."""

    created_at: datetime
    """The time the mapping was created."""

    external_account_id: Optional[str] = None
    """The ID of the account in the external payment provider."""

    is_default: bool
    """
    Whether Orb charges the customer for that billing entity's invoices through this
    mapping. On the default billing entity, it is the mapping the customer's
    `payment_provider_id` reflects.
    """

    payment_gateway_connection_id: str
    """The ID of the payment gateway connection the customer is mapped to."""

    provider_customer_id: Optional[str] = None
    """
    The ID of the customer in the external payment provider, or null if none is set.
    """

    provider_type: Literal["stripe", "adyen"]
    """The external payment provider of the connection."""
