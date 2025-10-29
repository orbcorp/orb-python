# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address import Address
from .shared.customer_tax_id import CustomerTaxID
from .shared.customer_minified import CustomerMinified

__all__ = [
    "Customer",
    "Hierarchy",
    "AccountingSyncConfiguration",
    "AccountingSyncConfigurationAccountingProvider",
    "ReportingConfiguration",
]


class Hierarchy(BaseModel):
    children: List[CustomerMinified]

    parent: Optional[CustomerMinified] = None


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

    auto_issuance: Optional[bool] = None
    """Whether invoices for this customer should be automatically issued.

    If true, invoices will be automatically issued. If false, invoices will require
    manual approval. If null, inherits the account-level setting.
    """

    balance: str
    """The customer's current balance in their currency."""

    billing_address: Optional[Address] = None

    created_at: datetime

    currency: Optional[str] = None

    email: str
    """A valid customer email, to be used for notifications.

    When Orb triggers payment through a payment gateway, this email will be used for
    any automatically issued receipts.
    """

    email_delivery: bool

    exempt_from_automated_tax: Optional[bool] = None

    external_customer_id: Optional[str] = None
    """
    An optional user-defined ID for this customer resource, used throughout the
    system as an alias for this Customer. Use this field to identify a customer by
    an existing identifier in your system.
    """

    hierarchy: Hierarchy
    """The hierarchical relationships for this customer."""

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

    shipping_address: Optional[Address] = None

    tax_id: Optional[CustomerTaxID] = None
    """
    Tax IDs are commonly required to be displayed on customer invoices, which are
    added to the headers of invoices.

    ### Supported Tax ID Countries and Types

    | Country                | Type         | Description                                                                                             |
    | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
    | Albania                | `al_tin`     | Albania Tax Identification Number                                                                       |
    | Andorra                | `ad_nrt`     | Andorran NRT Number                                                                                     |
    | Angola                 | `ao_tin`     | Angola Tax Identification Number                                                                        |
    | Argentina              | `ar_cuit`    | Argentinian Tax ID Number                                                                               |
    | Armenia                | `am_tin`     | Armenia Tax Identification Number                                                                       |
    | Aruba                  | `aw_tin`     | Aruba Tax Identification Number                                                                         |
    | Australia              | `au_abn`     | Australian Business Number (AU ABN)                                                                     |
    | Australia              | `au_arn`     | Australian Taxation Office Reference Number                                                             |
    | Austria                | `eu_vat`     | European VAT Number                                                                                     |
    | Azerbaijan             | `az_tin`     | Azerbaijan Tax Identification Number                                                                    |
    | Bahamas                | `bs_tin`     | Bahamas Tax Identification Number                                                                       |
    | Bahrain                | `bh_vat`     | Bahraini VAT Number                                                                                     |
    | Bangladesh             | `bd_bin`     | Bangladesh Business Identification Number                                                               |
    | Barbados               | `bb_tin`     | Barbados Tax Identification Number                                                                      |
    | Belarus                | `by_tin`     | Belarus TIN Number                                                                                      |
    | Belgium                | `eu_vat`     | European VAT Number                                                                                     |
    | Benin                  | `bj_ifu`     | Benin Tax Identification Number (Identifiant Fiscal Unique)                                             |
    | Bolivia                | `bo_tin`     | Bolivian Tax ID                                                                                         |
    | Bosnia and Herzegovina | `ba_tin`     | Bosnia and Herzegovina Tax Identification Number                                                        |
    | Brazil                 | `br_cnpj`    | Brazilian CNPJ Number                                                                                   |
    | Brazil                 | `br_cpf`     | Brazilian CPF Number                                                                                    |
    | Bulgaria               | `bg_uic`     | Bulgaria Unified Identification Code                                                                    |
    | Bulgaria               | `eu_vat`     | European VAT Number                                                                                     |
    | Burkina Faso           | `bf_ifu`     | Burkina Faso Tax Identification Number (Numéro d'Identifiant Fiscal Unique)                             |
    | Cambodia               | `kh_tin`     | Cambodia Tax Identification Number                                                                      |
    | Cameroon               | `cm_niu`     | Cameroon Tax Identification Number (Numéro d'Identifiant fiscal Unique)                                 |
    | Canada                 | `ca_bn`      | Canadian BN                                                                                             |
    | Canada                 | `ca_gst_hst` | Canadian GST/HST Number                                                                                 |
    | Canada                 | `ca_pst_bc`  | Canadian PST Number (British Columbia)                                                                  |
    | Canada                 | `ca_pst_mb`  | Canadian PST Number (Manitoba)                                                                          |
    | Canada                 | `ca_pst_sk`  | Canadian PST Number (Saskatchewan)                                                                      |
    | Canada                 | `ca_qst`     | Canadian QST Number (Québec)                                                                            |
    | Cape Verde             | `cv_nif`     | Cape Verde Tax Identification Number (Número de Identificação Fiscal)                                   |
    | Chile                  | `cl_tin`     | Chilean TIN                                                                                             |
    | China                  | `cn_tin`     | Chinese Tax ID                                                                                          |
    | Colombia               | `co_nit`     | Colombian NIT Number                                                                                    |
    | Congo-Kinshasa         | `cd_nif`     | Congo (DR) Tax Identification Number (Número de Identificação Fiscal)                                   |
    | Costa Rica             | `cr_tin`     | Costa Rican Tax ID                                                                                      |
    | Croatia                | `eu_vat`     | European VAT Number                                                                                     |
    | Croatia                | `hr_oib`     | Croatian Personal Identification Number (OIB)                                                           |
    | Cyprus                 | `eu_vat`     | European VAT Number                                                                                     |
    | Czech Republic         | `eu_vat`     | European VAT Number                                                                                     |
    | Denmark                | `eu_vat`     | European VAT Number                                                                                     |
    | Dominican Republic     | `do_rcn`     | Dominican RCN Number                                                                                    |
    | Ecuador                | `ec_ruc`     | Ecuadorian RUC Number                                                                                   |
    | Egypt                  | `eg_tin`     | Egyptian Tax Identification Number                                                                      |
    | El Salvador            | `sv_nit`     | El Salvadorian NIT Number                                                                               |
    | Estonia                | `eu_vat`     | European VAT Number                                                                                     |
    | Ethiopia               | `et_tin`     | Ethiopia Tax Identification Number                                                                      |
    | European Union         | `eu_oss_vat` | European One Stop Shop VAT Number for non-Union scheme                                                  |
    | Finland                | `eu_vat`     | European VAT Number                                                                                     |
    | France                 | `eu_vat`     | European VAT Number                                                                                     |
    | Georgia                | `ge_vat`     | Georgian VAT                                                                                            |
    | Germany                | `de_stn`     | German Tax Number (Steuernummer)                                                                        |
    | Germany                | `eu_vat`     | European VAT Number                                                                                     |
    | Greece                 | `eu_vat`     | European VAT Number                                                                                     |
    | Guinea                 | `gn_nif`     | Guinea Tax Identification Number (Número de Identificação Fiscal)                                       |
    | Hong Kong              | `hk_br`      | Hong Kong BR Number                                                                                     |
    | Hungary                | `eu_vat`     | European VAT Number                                                                                     |
    | Hungary                | `hu_tin`     | Hungary Tax Number (adószám)                                                                            |
    | Iceland                | `is_vat`     | Icelandic VAT                                                                                           |
    | India                  | `in_gst`     | Indian GST Number                                                                                       |
    | Indonesia              | `id_npwp`    | Indonesian NPWP Number                                                                                  |
    | Ireland                | `eu_vat`     | European VAT Number                                                                                     |
    | Israel                 | `il_vat`     | Israel VAT                                                                                              |
    | Italy                  | `eu_vat`     | European VAT Number                                                                                     |
    | Japan                  | `jp_cn`      | Japanese Corporate Number (_Hōjin Bangō_)                                                               |
    | Japan                  | `jp_rn`      | Japanese Registered Foreign Businesses' Registration Number (_Tōroku Kokugai Jigyōsha no Tōroku Bangō_) |
    | Japan                  | `jp_trn`     | Japanese Tax Registration Number (_Tōroku Bangō_)                                                       |
    | Kazakhstan             | `kz_bin`     | Kazakhstani Business Identification Number                                                              |
    | Kenya                  | `ke_pin`     | Kenya Revenue Authority Personal Identification Number                                                  |
    | Kyrgyzstan             | `kg_tin`     | Kyrgyzstan Tax Identification Number                                                                    |
    | Laos                   | `la_tin`     | Laos Tax Identification Number                                                                          |
    | Latvia                 | `eu_vat`     | European VAT Number                                                                                     |
    | Liechtenstein          | `li_uid`     | Liechtensteinian UID Number                                                                             |
    | Liechtenstein          | `li_vat`     | Liechtenstein VAT Number                                                                                |
    | Lithuania              | `eu_vat`     | European VAT Number                                                                                     |
    | Luxembourg             | `eu_vat`     | European VAT Number                                                                                     |
    | Malaysia               | `my_frp`     | Malaysian FRP Number                                                                                    |
    | Malaysia               | `my_itn`     | Malaysian ITN                                                                                           |
    | Malaysia               | `my_sst`     | Malaysian SST Number                                                                                    |
    | Malta                  | `eu_vat`     | European VAT Number                                                                                     |
    | Mauritania             | `mr_nif`     | Mauritania Tax Identification Number (Número de Identificação Fiscal)                                   |
    | Mexico                 | `mx_rfc`     | Mexican RFC Number                                                                                      |
    | Moldova                | `md_vat`     | Moldova VAT Number                                                                                      |
    | Montenegro             | `me_pib`     | Montenegro PIB Number                                                                                   |
    | Morocco                | `ma_vat`     | Morocco VAT Number                                                                                      |
    | Nepal                  | `np_pan`     | Nepal PAN Number                                                                                        |
    | Netherlands            | `eu_vat`     | European VAT Number                                                                                     |
    | New Zealand            | `nz_gst`     | New Zealand GST Number                                                                                  |
    | Nigeria                | `ng_tin`     | Nigerian Tax Identification Number                                                                      |
    | North Macedonia        | `mk_vat`     | North Macedonia VAT Number                                                                              |
    | Northern Ireland       | `eu_vat`     | Northern Ireland VAT Number                                                                             |
    | Norway                 | `no_vat`     | Norwegian VAT Number                                                                                    |
    | Norway                 | `no_voec`    | Norwegian VAT on e-commerce Number                                                                      |
    | Oman                   | `om_vat`     | Omani VAT Number                                                                                        |
    | Peru                   | `pe_ruc`     | Peruvian RUC Number                                                                                     |
    | Philippines            | `ph_tin`     | Philippines Tax Identification Number                                                                   |
    | Poland                 | `eu_vat`     | European VAT Number                                                                                     |
    | Portugal               | `eu_vat`     | European VAT Number                                                                                     |
    | Romania                | `eu_vat`     | European VAT Number                                                                                     |
    | Romania                | `ro_tin`     | Romanian Tax ID Number                                                                                  |
    | Russia                 | `ru_inn`     | Russian INN                                                                                             |
    | Russia                 | `ru_kpp`     | Russian KPP                                                                                             |
    | Saudi Arabia           | `sa_vat`     | Saudi Arabia VAT                                                                                        |
    | Senegal                | `sn_ninea`   | Senegal NINEA Number                                                                                    |
    | Serbia                 | `rs_pib`     | Serbian PIB Number                                                                                      |
    | Singapore              | `sg_gst`     | Singaporean GST                                                                                         |
    | Singapore              | `sg_uen`     | Singaporean UEN                                                                                         |
    | Slovakia               | `eu_vat`     | European VAT Number                                                                                     |
    | Slovenia               | `eu_vat`     | European VAT Number                                                                                     |
    | Slovenia               | `si_tin`     | Slovenia Tax Number (davčna številka)                                                                   |
    | South Africa           | `za_vat`     | South African VAT Number                                                                                |
    | South Korea            | `kr_brn`     | Korean BRN                                                                                              |
    | Spain                  | `es_cif`     | Spanish NIF Number (previously Spanish CIF Number)                                                      |
    | Spain                  | `eu_vat`     | European VAT Number                                                                                     |
    | Suriname               | `sr_fin`     | Suriname FIN Number                                                                                     |
    | Sweden                 | `eu_vat`     | European VAT Number                                                                                     |
    | Switzerland            | `ch_uid`     | Switzerland UID Number                                                                                  |
    | Switzerland            | `ch_vat`     | Switzerland VAT Number                                                                                  |
    | Taiwan                 | `tw_vat`     | Taiwanese VAT                                                                                           |
    | Tajikistan             | `tj_tin`     | Tajikistan Tax Identification Number                                                                    |
    | Tanzania               | `tz_vat`     | Tanzania VAT Number                                                                                     |
    | Thailand               | `th_vat`     | Thai VAT                                                                                                |
    | Turkey                 | `tr_tin`     | Turkish Tax Identification Number                                                                       |
    | Uganda                 | `ug_tin`     | Uganda Tax Identification Number                                                                        |
    | Ukraine                | `ua_vat`     | Ukrainian VAT                                                                                           |
    | United Arab Emirates   | `ae_trn`     | United Arab Emirates TRN                                                                                |
    | United Kingdom         | `gb_vat`     | United Kingdom VAT Number                                                                               |
    | United States          | `us_ein`     | United States EIN                                                                                       |
    | Uruguay                | `uy_ruc`     | Uruguayan RUC Number                                                                                    |
    | Uzbekistan             | `uz_tin`     | Uzbekistan TIN Number                                                                                   |
    | Uzbekistan             | `uz_vat`     | Uzbekistan VAT Number                                                                                   |
    | Venezuela              | `ve_rif`     | Venezuelan RIF Number                                                                                   |
    | Vietnam                | `vn_tin`     | Vietnamese Tax ID Number                                                                                |
    | Zambia                 | `zm_tin`     | Zambia Tax Identification Number                                                                        |
    | Zimbabwe               | `zw_tin`     | Zimbabwe Tax Identification Number                                                                      |
    """

    timezone: str
    """
    A timezone identifier from the IANA timezone database, such as
    "America/Los_Angeles". This "defaults to your account's timezone if not set.
    This cannot be changed after customer creation.
    """

    accounting_sync_configuration: Optional[AccountingSyncConfiguration] = None

    automatic_tax_enabled: Optional[bool] = None
    """Whether automatic tax calculation is enabled for this customer.

    This field is nullable for backwards compatibility but will always return a
    boolean value.
    """

    reporting_configuration: Optional[ReportingConfiguration] = None
