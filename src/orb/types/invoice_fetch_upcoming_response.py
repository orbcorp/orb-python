# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.address_model import AddressModel
from .shared.maximum_model import MaximumModel
from .shared.minimum_model import MinimumModel
from .shared.auto_collection_model import AutoCollectionModel
from .shared.customer_tax_id_model import CustomerTaxIDModel
from .shared.payment_attempt_model import PaymentAttemptModel
from .shared.invoice_level_discount import InvoiceLevelDiscount
from .shared.customer_minified_model import CustomerMinifiedModel
from .shared.invoice_line_item_model import InvoiceLineItemModel
from .shared.credit_note_summary_model import CreditNoteSummaryModel
from .shared.subscription_minified_model import SubscriptionMinifiedModel
from .shared.customer_balance_transaction_model import CustomerBalanceTransactionModel

__all__ = ["InvoiceFetchUpcomingResponse"]


class InvoiceFetchUpcomingResponse(BaseModel):
    id: str

    amount_due: str
    """
    This is the final amount required to be charged to the customer and reflects the
    application of the customer balance to the `total` of the invoice.
    """

    auto_collection: AutoCollectionModel

    billing_address: Optional[AddressModel] = None

    created_at: datetime
    """The creation time of the resource in Orb."""

    credit_notes: List[CreditNoteSummaryModel]
    """A list of credit notes associated with the invoice"""

    currency: str
    """An ISO 4217 currency string or `credits`"""

    customer: CustomerMinifiedModel

    customer_balance_transactions: List[CustomerBalanceTransactionModel]

    customer_tax_id: Optional[CustomerTaxIDModel] = None
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

    discount: object
    """This field is deprecated in favor of `discounts`.

    If a `discounts` list is provided, the first discount in the list will be
    returned. If the list is empty, `None` will be returned.
    """

    discounts: List[InvoiceLevelDiscount]

    due_date: Optional[datetime] = None
    """When the invoice payment is due.

    The due date is null if the invoice is not yet finalized.
    """

    eligible_to_issue_at: Optional[datetime] = None
    """
    If the invoice has a status of `draft`, this will be the time that the invoice
    will be eligible to be issued, otherwise it will be `null`. If `auto-issue` is
    true, the invoice will automatically begin issuing at this time.
    """

    hosted_invoice_url: Optional[str] = None
    """A URL for the customer-facing invoice portal.

    This URL expires 30 days after the invoice's due date, or 60 days after being
    re-generated through the UI.
    """

    invoice_number: str
    """Automatically generated invoice number to help track and reconcile invoices.

    Invoice numbers have a prefix such as `RFOBWG`. These can be sequential per
    account or customer.
    """

    invoice_pdf: Optional[str] = None
    """The link to download the PDF representation of the `Invoice`."""

    invoice_source: Literal["subscription", "partial", "one_off"]

    issue_failed_at: Optional[datetime] = None
    """
    If the invoice failed to issue, this will be the last time it failed to issue
    (even if it is now in a different state.)
    """

    issued_at: Optional[datetime] = None
    """
    If the invoice has been issued, this will be the time it transitioned to
    `issued` (even if it is now in a different state.)
    """

    line_items: List[InvoiceLineItemModel]
    """The breakdown of prices in this invoice."""

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    memo: Optional[str] = None
    """
    Free-form text which is available on the invoice PDF and the Orb invoice portal.
    """

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

    minimum_amount: Optional[str] = None

    paid_at: Optional[datetime] = None
    """
    If the invoice has a status of `paid`, this gives a timestamp when the invoice
    was paid.
    """

    payment_attempts: List[PaymentAttemptModel]
    """A list of payment attempts associated with the invoice"""

    payment_failed_at: Optional[datetime] = None
    """
    If payment was attempted on this invoice but failed, this will be the time of
    the most recent attempt.
    """

    payment_started_at: Optional[datetime] = None
    """
    If payment was attempted on this invoice, this will be the start time of the
    most recent attempt. This field is especially useful for delayed-notification
    payment mechanisms (like bank transfers), where payment can take 3 days or more.
    """

    scheduled_issue_at: Optional[datetime] = None
    """
    If the invoice is in draft, this timestamp will reflect when the invoice is
    scheduled to be issued.
    """

    shipping_address: Optional[AddressModel] = None

    status: Literal["issued", "paid", "synced", "void", "draft"]

    subscription: Optional[SubscriptionMinifiedModel] = None

    subtotal: str
    """The total before any discounts and minimums are applied."""

    sync_failed_at: Optional[datetime] = None
    """
    If the invoice failed to sync, this will be the last time an external invoicing
    provider sync was attempted. This field will always be `null` for invoices using
    Orb Invoicing.
    """

    target_date: datetime
    """The scheduled date of the invoice"""

    total: str
    """The total after any minimums and discounts have been applied."""

    voided_at: Optional[datetime] = None
    """
    If the invoice has a status of `void`, this gives a timestamp when the invoice
    was voided.
    """

    will_auto_issue: bool
    """
    This is true if the invoice will be automatically issued in the future, and
    false otherwise.
    """
