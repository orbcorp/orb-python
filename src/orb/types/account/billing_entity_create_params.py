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

    memo: Optional[str]
    """The memo printed on the entity's invoices."""


class TaxRegistration(TypedDict, total=False):
    code: Required[str]
    """The tax registration type, for example `DE VAT`."""

    value: Required[str]
    """The registration number."""

    applies_to: Optional[str]
    """The jurisdiction the registration applies to.

    If null, it applies to every customer.
    """
