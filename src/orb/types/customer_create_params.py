# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CustomerCreateParams",
    "AccountingSyncConfiguration",
    "AccountingSyncConfigurationAccountingProvider",
    "BillingAddress",
    "ReportingConfiguration",
    "ShippingAddress",
    "TaxID",
]


class CustomerCreateParams(TypedDict, total=False):
    email: Required[str]
    """A valid customer email, to be used for notifications.

    When Orb triggers payment through a payment gateway, this email will be used for
    any automatically issued receipts.
    """

    name: Required[str]
    """The full name of the customer"""

    accounting_sync_configuration: Optional[AccountingSyncConfiguration]

    additional_emails: Optional[List[str]]
    """Additional email addresses for this customer.

    If populated, these email addresses will be CC'd for customer communications.
    """

    auto_collection: Optional[bool]
    """
    Used to determine if invoices for this customer will automatically attempt to
    charge a saved payment method, if available. This parameter defaults to `True`
    when a payment provider is provided on customer creation.
    """

    billing_address: Optional[BillingAddress]

    currency: Optional[str]
    """An ISO 4217 currency string used for the customer's invoices and balance.

    If not set at creation time, will be set at subscription creation time.
    """

    email_delivery: Optional[bool]

    external_customer_id: Optional[str]
    """
    An optional user-defined ID for this customer resource, used throughout the
    system as an alias for this Customer. Use this field to identify a customer by
    an existing identifier in your system.
    """

    metadata: Optional[object]
    """
    User-specified key value pairs, often useful for referencing internal resources
    or IDs. Returned as-is in the customer resource.
    """

    payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
    """This is used for creating charges or invoices in an external system via Orb.

    When not in test mode, the connection must first be configured in the Orb
    webapp.
    """

    payment_provider_id: Optional[str]
    """The ID of this customer in an external payments solution, such as Stripe.

    This is used for creating charges or invoices in the external system via Orb.
    """

    reporting_configuration: Optional[ReportingConfiguration]

    shipping_address: Optional[ShippingAddress]

    tax_id: Optional[TaxID]

    timezone: Optional[str]
    """
    A timezone identifier from the IANA timezone database, such as
    `"America/Los_Angeles"`. This defaults to your account's timezone if not set.
    This cannot be changed after customer creation.
    """


class AccountingSyncConfigurationAccountingProvider(TypedDict, total=False):
    external_provider_id: Required[str]

    provider_type: Required[str]


class AccountingSyncConfiguration(TypedDict, total=False):
    accounting_providers: Optional[List[AccountingSyncConfigurationAccountingProvider]]

    excluded: Optional[bool]


class BillingAddress(TypedDict, total=False):
    city: Optional[str]

    country: Optional[str]

    line1: Optional[str]

    line2: Optional[str]

    postal_code: Optional[str]

    state: Optional[str]


class ReportingConfiguration(TypedDict, total=False):
    exempt: Required[bool]


class ShippingAddress(TypedDict, total=False):
    city: Optional[str]

    country: Optional[str]

    line1: Optional[str]

    line2: Optional[str]

    postal_code: Optional[str]

    state: Optional[str]


class TaxID(TypedDict, total=False):
    country: Required[str]

    type: Required[str]

    value: Required[str]
