# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.address import Address

__all__ = ["BillingEntity", "InvoiceSettings", "PaymentGatewayConnection", "TaxRegistration"]


class InvoiceSettings(BaseModel):
    """The billing entity's own invoice settings.

    Each null field inherits the account's setting.
    """

    memo: Optional[str] = None
    """The memo printed on the entity's invoices."""


class PaymentGatewayConnection(BaseModel):
    is_default: bool
    """Whether this is the billing entity's default payment gateway connection."""

    payment_gateway_connection_id: str
    """The ID of the billing entity's payment gateway connection."""

    payment_provider_type: Literal["stripe", "adyen"]
    """The connection's payment provider."""


class TaxRegistration(BaseModel):
    applies_to: Optional[str] = None
    """The jurisdiction the registration applies to.

    If null, it applies to every customer.
    """

    code: str
    """The tax registration type, for example `DE VAT`."""

    value: str
    """The registration number."""


class BillingEntity(BaseModel):
    """
    A billing entity is a legal entity an account invoices from, with its own legal name, address and tax
    registrations.
    """

    id: str
    """The Orb-assigned unique identifier for the billing entity."""

    address: Optional[Address] = None
    """The address printed on invoices."""

    created_at: datetime
    """The time the billing entity was created."""

    default_payment_gateway_connection_id: Optional[str] = None
    """
    The ID of the connection Orb charges when the customer is not mapped to any of
    the billing entity's connections.
    """

    external_billing_entity_id: Optional[str] = None
    """An optional user-defined ID for this billing entity, unique within the account.

    This cannot be changed after creation.
    """

    invoice_settings: InvoiceSettings
    """The billing entity's own invoice settings.

    Each null field inherits the account's setting.
    """

    is_default: bool
    """Whether this is the account's default billing entity."""

    legal_name: str
    """The legal name printed on invoices."""

    name: str
    """An internal name for the billing entity."""

    payment_gateway_connections: List[PaymentGatewayConnection]
    """The payment gateway connections the billing entity collects payments through."""

    status: Literal["active", "archived"]

    tax_registrations: List[TaxRegistration]
