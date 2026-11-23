# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..address_input_param import AddressInputParam

__all__ = ["BillingEntityCreateParams", "InvoiceSettings", "TaxRegistration"]


class BillingEntityCreateParams(TypedDict, total=False):
    address: Required[AddressInputParam]
    """The address printed on invoices."""

    legal_name: Required[str]
    """The legal name printed on invoices."""

    name: Required[str]
    """An internal name for the billing entity."""

    external_billing_entity_id: Optional[str]
    """An optional user-defined ID for this billing entity, unique within the account.

    This cannot be changed after creation.
    """

    invoice_settings: Optional[InvoiceSettings]
    """Settings that override the account's for this billing entity."""

    tax_registrations: Iterable[TaxRegistration]


class InvoiceSettings(TypedDict, total=False):
    """Settings that override the account's for this billing entity."""

    auto_collection: Optional[bool]
    """Whether Orb charges the customer's payment method automatically."""

    automatic_tax_enabled: Optional[bool]
    """Whether Orb calculates tax through the tax provider."""

    email_delivery: Optional[bool]
    """Whether Orb emails invoices to customers."""

    manual_issuance: Optional[bool]
    """Whether invoices stay in draft until issued by hand."""

    memo: Optional[str]
    """The memo printed on the entity's invoices."""

    net_terms: Optional[int]
    """
    The number of days until payment is due, counting the start date as day 1, so
    net 30 from October 1 is due October 30. The account's
    [due date calculation method](/invoicing/payments#configuring-net-terms-and-collection-behavior)
    sets whether the start date is the invoice date or the issuance date.
    """


class TaxRegistration(TypedDict, total=False):
    code: Required[str]
    """The tax registration type, for example `DE VAT`."""

    value: Required[str]
    """The registration number."""

    applies_to: Optional[str]
    """The jurisdiction the registration applies to.

    If null, it applies to every customer.
    """
