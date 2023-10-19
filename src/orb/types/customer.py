# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "Customer",
    "BillingAddress",
    "ShippingAddress",
    "TaxID",
    "AccountingSyncConfiguration",
    "AccountingSyncConfigurationAccountingProvider",
    "ReportingConfiguration",
]


class BillingAddress(BaseModel):
    city: Optional[str]

    country: Optional[str]

    line1: Optional[str]

    line2: Optional[str]

    postal_code: Optional[str]

    state: Optional[str]


class ShippingAddress(BaseModel):
    city: Optional[str]

    country: Optional[str]

    line1: Optional[str]

    line2: Optional[str]

    postal_code: Optional[str]

    state: Optional[str]


class TaxID(BaseModel):
    country: str

    type: str

    value: str


class AccountingSyncConfigurationAccountingProvider(BaseModel):
    external_provider_id: Optional[str]

    provider_type: Literal["quickbooks", "netsuite"]


class AccountingSyncConfiguration(BaseModel):
    accounting_providers: List[AccountingSyncConfigurationAccountingProvider]

    excluded: bool


class ReportingConfiguration(BaseModel):
    exempt: bool


class Customer(BaseModel):
    id: str

    additional_emails: List[str]

    auto_collection: bool

    balance: str
    """The customer's current balance in their currency."""

    billing_address: Optional[BillingAddress]

    created_at: datetime

    currency: Optional[str]

    email: str
    """A valid customer email, to be used for notifications.

    When Orb triggers payment through a payment gateway, this email will be used for
    any automatically issued receipts.
    """

    email_delivery: bool

    external_customer_id: Optional[str]
    """
    An optional user-defined ID for this customer resource, used throughout the
    system as an alias for this Customer. Use this field to identify a customer by
    an existing identifier in your system.
    """

    metadata: Dict[str, str]

    name: str
    """The full name of the customer"""

    payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
    """This is used for creating charges or invoices in an external system via Orb.

    When not in test mode, the connection must first be configured in the Orb
    webapp.
    """

    payment_provider_id: Optional[str]
    """The ID of this customer in an external payments solution, such as Stripe.

    This is used for creating charges or invoices in the external system via Orb.
    """

    portal_url: Optional[str]

    shipping_address: Optional[ShippingAddress]

    tax_id: Optional[TaxID]

    timezone: str
    """
    A timezone identifier from the IANA timezone database, such as
    "America/Los_Angeles". This "defaults to your account's timezone if not set.
    This cannot be changed after customer creation.
    """

    accounting_sync_configuration: Optional[AccountingSyncConfiguration] = None

    reporting_configuration: Optional[ReportingConfiguration] = None
