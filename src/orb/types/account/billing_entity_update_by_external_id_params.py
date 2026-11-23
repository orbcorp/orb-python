# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..address_input_param import AddressInputParam

__all__ = ["BillingEntityUpdateByExternalIDParams", "InvoiceSettings", "PaymentGatewayConnection", "TaxRegistration"]


class BillingEntityUpdateByExternalIDParams(TypedDict, total=False):
    address: Optional[AddressInputParam]
    """Replaces the whole address. Omit it to keep the current one."""

    default_payment_gateway_connection_id: Optional[str]
    """
    The ID of the connection Orb charges when the customer is not mapped to any of
    the billing entity's connections. Required when `payment_gateway_connections`
    has more than one entry.
    """

    invoice_settings: Optional[InvoiceSettings]
    """The invoice settings to change.

    Omitted fields keep their value; null clears a field so it inherits the
    account's setting.
    """

    legal_name: Optional[str]
    """The legal name printed on invoices."""

    name: Optional[str]
    """An internal name for the billing entity."""

    payment_gateway_connections: Optional[Iterable[PaymentGatewayConnection]]
    """
    The full set of payment gateway connections the billing entity collects payments
    through. Omit it to keep the current ones. Naming another billing entity's
    connection gives this billing entity a connection of its own through the same
    Stripe account or Adyen merchant account.
    """

    tax_registrations: Optional[Iterable[TaxRegistration]]
    """The full list of registrations. Omit it to keep the current ones."""


class InvoiceSettings(TypedDict, total=False):
    """The invoice settings to change.

    Omitted fields keep their value; null clears a field so it inherits the account's setting.
    """

    memo: Optional[str]
    """The memo printed on the entity's invoices."""


class PaymentGatewayConnection(TypedDict, total=False):
    payment_gateway_connection_id: Required[str]
    """The ID of a payment gateway connection of the account."""

    payment_provider_type: Required[Literal["stripe", "adyen"]]
    """The connection's payment provider."""


class TaxRegistration(TypedDict, total=False):
    code: Required[str]
    """The tax registration type, for example `DE VAT`."""

    value: Required[str]
    """The registration number."""

    applies_to: Optional[str]
    """The jurisdiction the registration applies to.

    If null, it applies to every customer.
    """
