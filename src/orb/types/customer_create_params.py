# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
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

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
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
    """
    Tax IDs are commonly required to be displayed on customer invoices, which are
    added to the headers of invoices.

    ### Supported Tax ID Countries and Types

    | Country              | Type         | Description                                                                                             |
    | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
    | Andorra              | `ad_nrt`     | Andorran NRT number                                                                                     |
    | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
    | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
    | Austria              | `eu_vat`     | European VAT number                                                                                     |
    | Belgium              | `eu_vat`     | European VAT number                                                                                     |
    | Brazil               | `br_cnpj`    | Brazilian CNPJ number                                                                                   |
    | Brazil               | `br_cpf`     | Brazilian CPF number                                                                                    |
    | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
    | Bulgaria             | `eu_vat`     | European VAT number                                                                                     |
    | Canada               | `ca_bn`      | Canadian BN                                                                                             |
    | Canada               | `ca_gst_hst` | Canadian GST/HST number                                                                                 |
    | Canada               | `ca_pst_bc`  | Canadian PST number (British Columbia)                                                                  |
    | Canada               | `ca_pst_mb`  | Canadian PST number (Manitoba)                                                                          |
    | Canada               | `ca_pst_sk`  | Canadian PST number (Saskatchewan)                                                                      |
    | Canada               | `ca_qst`     | Canadian QST number (Québec)                                                                            |
    | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
    | Croatia              | `eu_vat`     | European VAT number                                                                                     |
    | Cyprus               | `eu_vat`     | European VAT number                                                                                     |
    | Czech Republic       | `eu_vat`     | European VAT number                                                                                     |
    | Denmark              | `eu_vat`     | European VAT number                                                                                     |
    | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
    | Estonia              | `eu_vat`     | European VAT number                                                                                     |
    | EU                   | `eu_oss_vat` | European One Stop Shop VAT number for non-Union scheme                                                  |
    | Finland              | `eu_vat`     | European VAT number                                                                                     |
    | France               | `eu_vat`     | European VAT number                                                                                     |
    | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
    | Germany              | `eu_vat`     | European VAT number                                                                                     |
    | Greece               | `eu_vat`     | European VAT number                                                                                     |
    | Hong Kong            | `hk_br`      | Hong Kong BR number                                                                                     |
    | Hungary              | `eu_vat`     | European VAT number                                                                                     |
    | Hungary              | `hu_tin`     | Hungary tax number (adószám)                                                                            |
    | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
    | India                | `in_gst`     | Indian GST number                                                                                       |
    | Indonesia            | `id_npwp`    | Indonesian NPWP number                                                                                  |
    | Ireland              | `eu_vat`     | European VAT number                                                                                     |
    | Israel               | `il_vat`     | Israel VAT                                                                                              |
    | Italy                | `eu_vat`     | European VAT number                                                                                     |
    | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
    | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
    | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
    | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
    | Latvia               | `eu_vat`     | European VAT number                                                                                     |
    | Liechtenstein        | `li_uid`     | Liechtensteinian UID number                                                                             |
    | Lithuania            | `eu_vat`     | European VAT number                                                                                     |
    | Luxembourg           | `eu_vat`     | European VAT number                                                                                     |
    | Malaysia             | `my_frp`     | Malaysian FRP number                                                                                    |
    | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
    | Malaysia             | `my_sst`     | Malaysian SST number                                                                                    |
    | Malta                | `eu_vat `    | European VAT number                                                                                     |
    | Mexico               | `mx_rfc`     | Mexican RFC number                                                                                      |
    | Netherlands          | `eu_vat`     | European VAT number                                                                                     |
    | New Zealand          | `nz_gst`     | New Zealand GST number                                                                                  |
    | Norway               | `no_vat`     | Norwegian VAT number                                                                                    |
    | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
    | Poland               | `eu_vat`     | European VAT number                                                                                     |
    | Portugal             | `eu_vat`     | European VAT number                                                                                     |
    | Romania              | `eu_vat`     | European VAT number                                                                                     |
    | Russia               | `ru_inn`     | Russian INN                                                                                             |
    | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
    | Saudi Arabia         | `sg_gst`     | Singaporean GST                                                                                         |
    | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
    | Slovakia             | `eu_vat`     | European VAT number                                                                                     |
    | Slovenia             | `eu_vat`     | European VAT number                                                                                     |
    | Slovenia             | `si_tin`     | Slovenia tax number (davčna številka)                                                                   |
    | South Africa         | `za_vat`     | South African VAT number                                                                                |
    | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
    | Spain                | `es_cif`     | Spanish NIF number (previously Spanish CIF number)                                                      |
    | Spain                | `eu_vat`     | European VAT number                                                                                     |
    | Sweden               | `eu_vat`     | European VAT number                                                                                     |
    | Switzerland          | `ch_vat`     | Switzerland VAT number                                                                                  |
    | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
    | Thailand             | `th_vat`     | Thai VAT                                                                                                |
    | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
    | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
    | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
    | United Kingdom       | `eu_vat`     | Northern Ireland VAT number                                                                             |
    | United Kingdom       | `gb_vat`     | United Kingdom VAT number                                                                               |
    | United States        | `us_ein`     | United States EIN                                                                                       |
    """

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
    accounting_providers: Optional[Iterable[AccountingSyncConfigurationAccountingProvider]]

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
    country: Required[
        Literal[
            "AD",
            "AE",
            "AT",
            "AU",
            "BE",
            "BG",
            "BR",
            "CA",
            "CH",
            "CL",
            "CY",
            "CZ",
            "DE",
            "DK",
            "EE",
            "EG",
            "ES",
            "EU",
            "FI",
            "FR",
            "GB",
            "GE",
            "GR",
            "HK",
            "HR",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JP",
            "KE",
            "KR",
            "LI",
            "LT",
            "LU",
            "LV",
            "MT",
            "MX",
            "MY",
            "NL",
            "NO",
            "NZ",
            "PH",
            "PL",
            "PT",
            "RO",
            "RU",
            "SA",
            "SE",
            "SG",
            "SI",
            "SK",
            "TH",
            "TR",
            "TW",
            "UA",
            "US",
            "ZA",
        ]
    ]

    type: Required[
        Literal[
            "ad_nrt",
            "ae_trn",
            "eu_vat",
            "au_abn",
            "au_arn",
            "bg_uic",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "nz_gst",
            "ph_tin",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "us_ein",
            "za_vat",
        ]
    ]

    value: Required[str]
