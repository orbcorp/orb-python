# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from .address_input_param import AddressInputParam
from .shared_params.customer_tax_id import CustomerTaxID
from .new_sphere_configuration_param import NewSphereConfigurationParam
from .customer_hierarchy_config_param import CustomerHierarchyConfigParam
from .new_tax_jar_configuration_param import NewTaxJarConfigurationParam
from .new_reporting_configuration_param import NewReportingConfigurationParam
from .new_avalara_tax_configuration_param import NewAvalaraTaxConfigurationParam
from .new_accounting_sync_configuration_param import NewAccountingSyncConfigurationParam

__all__ = ["CustomerUpdateByExternalIDParams", "TaxConfiguration"]


class CustomerUpdateByExternalIDParams(TypedDict, total=False):
    accounting_sync_configuration: Optional[NewAccountingSyncConfigurationParam]

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

    billing_address: Optional[AddressInputParam]

    currency: Optional[str]
    """An ISO 4217 currency string used for the customer's invoices and balance.

    If not set at creation time, will be set at subscription creation time.
    """

    email: Optional[str]
    """A valid customer email, to be used for invoicing and notifications."""

    email_delivery: Optional[bool]

    external_customer_id: Optional[str]
    """The external customer ID.

    This can only be set if empty and the customer has no past or current
    subscriptions.
    """

    hierarchy: Optional[CustomerHierarchyConfigParam]
    """The hierarchical relationships for this customer."""

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    name: Optional[str]
    """The full name of the customer"""

    payment_provider: Optional[Literal["quickbooks", "bill.com", "stripe_charge", "stripe_invoice", "netsuite"]]
    """This is used for creating charges or invoices in an external system via Orb.

    When not in test mode:

    - the connection must first be configured in the Orb webapp.
    - if the provider is an invoicing provider (`stripe_invoice`, `quickbooks`,
      `bill.com`, `netsuite`), any product mappings must first be configured with
      the Orb team.
    """

    payment_provider_id: Optional[str]
    """The ID of this customer in an external payments solution, such as Stripe.

    This is used for creating charges or invoices in the external system via Orb.
    """

    reporting_configuration: Optional[NewReportingConfigurationParam]

    shipping_address: Optional[AddressInputParam]

    tax_configuration: Optional[TaxConfiguration]

    tax_id: Optional[CustomerTaxID]
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


TaxConfiguration: TypeAlias = Union[
    NewAvalaraTaxConfigurationParam, NewTaxJarConfigurationParam, NewSphereConfigurationParam
]
