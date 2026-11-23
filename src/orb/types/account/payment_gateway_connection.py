# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PaymentGatewayConnection"]


class PaymentGatewayConnection(BaseModel):
    """
    A payment gateway connection is one Stripe account or one Adyen merchant account that a billing entity collects
    payments through.
    """

    id: str
    """The Orb-assigned unique identifier for the payment gateway connection."""

    billing_entity_id: str
    """The ID of the billing entity that collects payments through this connection."""

    created_at: datetime
    """The time the connection was created."""

    external_account_id: Optional[str] = None
    """The ID of the account in the external payment provider."""

    is_default: bool
    """Whether this is the billing entity's default payment gateway connection."""

    provider_type: Literal["stripe", "adyen"]
    """The external payment provider of this connection."""
