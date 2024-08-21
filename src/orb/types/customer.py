# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    city: Optional[str] = None

    country: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None


class ShippingAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None


class TaxID(BaseModel):
    country: Literal[
        "AD",
        "AE",
        "AR",
        "AT",
        "AU",
        "BE",
        "BG",
        "BH",
        "BO",
        "BR",
        "CA",
        "CH",
        "CL",
        "CN",
        "CO",
        "CR",
        "CY",
        "CZ",
        "DE",
        "DK",
        "EE",
        "DO",
        "EC",
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
        "KZ",
        "LI",
        "LT",
        "LU",
        "LV",
        "MT",
        "MX",
        "MY",
        "NG",
        "NL",
        "NO",
        "NZ",
        "OM",
        "PE",
        "PH",
        "PL",
        "PT",
        "RO",
        "RS",
        "RU",
        "SA",
        "SE",
        "SG",
        "SI",
        "SK",
        "SV",
        "TH",
        "TR",
        "TW",
        "UA",
        "US",
        "UY",
        "VE",
        "VN",
        "ZA",
    ]

    type: Literal[
        "ad_nrt",
        "ae_trn",
        "ar_cuit",
        "eu_vat",
        "au_abn",
        "au_arn",
        "bg_uic",
        "bh_vat",
        "bo_tin",
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
        "cn_tin",
        "co_nit",
        "cr_tin",
        "do_rcn",
        "ec_ruc",
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
        "kz_bin",
        "li_uid",
        "mx_rfc",
        "my_frp",
        "my_itn",
        "my_sst",
        "ng_tin",
        "no_vat",
        "no_voec",
        "nz_gst",
        "om_vat",
        "pe_ruc",
        "ph_tin",
        "ro_tin",
        "rs_pib",
        "ru_inn",
        "ru_kpp",
        "sa_vat",
        "sg_gst",
        "sg_uen",
        "si_tin",
        "sv_nit",
        "th_vat",
        "tr_tin",
        "tw_vat",
        "ua_vat",
        "us_ein",
        "uy_ruc",
        "ve_rif",
        "vn_tin",
        "za_vat",
    ]

    value: str


class AccountingSyncConfigurationAccountingProvider(BaseModel):
    external_provider_id: Optional[str] = None

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

    billing_address: Optional[BillingAddress] = None

    created_at: datetime

    currency: Optional[str] = None

    email: str
    """A valid customer email, to be used for notifications.

    When Orb triggers payment through a payment gateway, this email will be used for
    any automatically issued receipts.
    """

    email_delivery: bool

    external_customer_id: Optional[str] = None
    """
    An optional user-defined ID for this customer resource, used throughout the
    system as an alias for this Customer. Use this field to identify a customer by
    an existing identifier in your system.
    """

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    name: str
    """The full name of the customer"""

    payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]] = None
    """This is used for creating charges or invoices in an external system via Orb.

    When not in test mode, the connection must first be configured in the Orb
    webapp.
    """

    payment_provider_id: Optional[str] = None
    """The ID of this customer in an external payments solution, such as Stripe.

    This is used for creating charges or invoices in the external system via Orb.
    """

    portal_url: Optional[str] = None

    shipping_address: Optional[ShippingAddress] = None

    tax_id: Optional[TaxID] = None
    """
    Tax IDs are commonly required to be displayed on customer invoices, which are
    added to the headers of invoices.

    ### Supported Tax ID Countries and Types

    | Country              | Type         | Description                                                                                             |
    | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
    | Andorra              | `ad_nrt`     | Andorran NRT Number                                                                                     |
    | Argentina            | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
    | Australia            | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
    | Australia            | `au_arn`     | Australian Taxation Office Reference Number                                                             |
    | Austria              | `eu_vat`     | European VAT Number                                                                                     |
    | Bahrain              | `bh_vat`     | Bahraini VAT Number                                                                                     |
    | Belgium              | `eu_vat`     | European VAT Number                                                                                     |
    | Bolivia              | `bo_tin`     | Bolivian Tax ID                                                                                         |
    | Brazil               | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
    | Brazil               | `br_cpf`     | Brazilian CPF Number                                                                                    |
    | Bulgaria             | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
    | Bulgaria             | `eu_vat`     | European VAT Number                                                                                     |
    | Canada               | `ca_bn`      | Canadian BN                                                                                             |
    | Canada               | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
    | Canada               | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
    | Canada               | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
    | Canada               | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
    | Canada               | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
    | Chile                | `cl_tin`     | Chilean TIN                                                                                             |
    | China                | `cn_tin`     | Chinese Tax ID                                                                                          |
    | Colombia             | `co_nit`     | Colombian NIT Number                                                                                    |
    | Costa Rica           | `cr_tin`     | Costa Rican Tax ID                                                                                      |
    | Croatia              | `eu_vat`     | European VAT Number                                                                                     |
    | Cyprus               | `eu_vat`     | European VAT Number                                                                                     |
    | Czech Republic       | `eu_vat`     | European VAT Number                                                                                     |
    | Denmark              | `eu_vat`     | European VAT Number                                                                                     |
    | Dominican Republic   | `do_rcn`     | Dominican RCN Number                                                                                    |
    | Ecuador              | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
    | Egypt                | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
    | El Salvador          | `sv_nit`     | El Salvadorian NIT Number                                                                               |
    | Estonia              | `eu_vat`     | European VAT Number                                                                                     |
    | EU                   | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
    | Finland              | `eu_vat`     | European VAT Number                                                                                     |
    | France               | `eu_vat`     | European VAT Number                                                                                     |
    | Georgia              | `ge_vat`     | Georgian VAT                                                                                            |
    | Germany              | `eu_vat`     | European VAT Number                                                                                     |
    | Greece               | `eu_vat`     | European VAT Number                                                                                     |
    | Hong Kong            | `hk_br`      | Hong Kong BR Number                                                                                     |
    | Hungary              | `eu_vat`     | European VAT Number                                                                                     |
    | Hungary              | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
    | Iceland              | `is_vat`     | Icelandic VAT                                                                                           |
    | India                | `in_gst`     | Indian GST Number                                                                                       |
    | Indonesia            | `id_npwp`    | Indonesian NPWP Number                                                                                  |
    | Ireland              | `eu_vat`     | European VAT Number                                                                                     |
    | Israel               | `il_vat`     | Israel VAT                                                                                              |
    | Italy                | `eu_vat`     | European VAT Number                                                                                     |
    | Japan                | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
    | Japan                | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
    | Japan                | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
    | Kazakhstan           | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
    | Kenya                | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
    | Latvia               | `eu_vat`     | European VAT Number                                                                                     |
    | Liechtenstein        | `li_uid`     | Liechtensteinian UID Number                                                                             |
    | Lithuania            | `eu_vat`     | European VAT Number                                                                                     |
    | Luxembourg           | `eu_vat`     | European VAT Number                                                                                     |
    | Malaysia             | `my_frp`     | Malaysian FRP Number                                                                                    |
    | Malaysia             | `my_itn`     | Malaysian ITN                                                                                           |
    | Malaysia             | `my_sst`     | Malaysian SST Number                                                                                    |
    | Malta                | `eu_vat `    | European VAT Number                                                                                     |
    | Mexico               | `mx_rfc`     | Mexican RFC Number                                                                                      |
    | Netherlands          | `eu_vat`     | European VAT Number                                                                                     |
    | New Zealand          | `nz_gst`     | New Zealand GST Number                                                                                  |
    | Nigeria              | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
    | Norway               | `no_vat`     | Norwegian VAT Number                                                                                    |
    | Norway               | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
    | Oman                 | `om_vat`     | Omani VAT Number                                                                                        |
    | Peru                 | `pe_ruc`     | Peruvian RUC Number                                                                                     |
    | Philippines          | `ph_tin `    | Philippines Tax Identification Number                                                                   |
    | Poland               | `eu_vat`     | European VAT Number                                                                                     |
    | Portugal             | `eu_vat`     | European VAT Number                                                                                     |
    | Romania              | `eu_vat`     | European VAT Number                                                                                     |
    | Romania              | `ro_tin`     | Romanian Tax ID Number                                                                                  |
    | Russia               | `ru_inn`     | Russian INN                                                                                             |
    | Russia               | `ru_kpp`     | Russian KPP                                                                                             |
    | Saudi Arabia         | `sa_vat`     | Saudi Arabia VAT                                                                                        |
    | Serbia               | `rs_pib`     | Serbian PIB Number                                                                                      |
    | Singapore            | `sg_gst`     | Singaporean GST                                                                                         |
    | Singapore            | `sg_uen`     | Singaporean UEN                                                                                         |
    | Slovakia             | `eu_vat`     | European VAT Number                                                                                     |
    | Slovenia             | `eu_vat`     | European VAT Number                                                                                     |
    | Slovenia             | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
    | South Africa         | `za_vat`     | South African VAT Number                                                                                |
    | South Korea          | `kr_brn`     | Korean BRN                                                                                              |
    | Spain                | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
    | Spain                | `eu_vat`     | European VAT Number                                                                                     |
    | Sweden               | `eu_vat`     | European VAT Number                                                                                     |
    | Switzerland          | `ch_vat`     | Switzerland VAT Number                                                                                  |
    | Taiwan               | `tw_vat`     | Taiwanese VAT                                                                                           |
    | Thailand             | `th_vat`     | Thai VAT                                                                                                |
    | Turkey               | `tr_tin`     | Turkish Tax Identification Number                                                                       |
    | Ukraine              | `ua_vat`     | Ukrainian VAT                                                                                           |
    | United Arab Emirates | `ae_trn`     | United Arab Emirates TRN                                                                                |
    | United Kingdom       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
    | United Kingdom       | `gb_vat`     | United Kingdom VAT Number                                                                               |
    | United States        | `us_ein`     | United States EIN                                                                                       |
    | Uruguay              | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
    | Venezuela            | `ve_rif`     | Venezuelan RIF Number                                                                                   |
    | Vietnam              | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
    """

    timezone: str
    """
    A timezone identifier from the IANA timezone database, such as
    "America/Los_Angeles". This "defaults to your account's timezone if not set.
    This cannot be changed after customer creation.
    """

    accounting_sync_configuration: Optional[AccountingSyncConfiguration] = None

    reporting_configuration: Optional[ReportingConfiguration] = None
