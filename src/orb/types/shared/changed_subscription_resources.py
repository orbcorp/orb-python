# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .price import Price
from .address import Address
from .invoice import Invoice
from .maximum import Maximum
from .minimum import Minimum
from ..._utils import PropertyInfo
from ..._models import BaseModel
from .tax_amount import TaxAmount
from .credit_note import CreditNote
from .invoice_tiny import InvoiceTiny
from .customer_tax_id import CustomerTaxID
from .credit_note_tiny import CreditNoteTiny
from .customer_minified import CustomerMinified
from .tier_sub_line_item import TierSubLineItem
from .other_sub_line_item import OtherSubLineItem
from .matrix_sub_line_item import MatrixSubLineItem
from .subscription_minified import SubscriptionMinified
from .invoice_level_discount import InvoiceLevelDiscount
from .monetary_maximum_adjustment import MonetaryMaximumAdjustment
from .monetary_minimum_adjustment import MonetaryMinimumAdjustment
from .monetary_usage_discount_adjustment import MonetaryUsageDiscountAdjustment
from .monetary_amount_discount_adjustment import MonetaryAmountDiscountAdjustment
from .monetary_percentage_discount_adjustment import MonetaryPercentageDiscountAdjustment

__all__ = [
    "ChangedSubscriptionResources",
    "CreatedInvoice",
    "CreatedInvoiceAutoCollection",
    "CreatedInvoiceCreditNote",
    "CreatedInvoiceCustomerBalanceTransaction",
    "CreatedInvoiceLineItem",
    "CreatedInvoiceLineItemAdjustment",
    "CreatedInvoiceLineItemSubLineItem",
    "CreatedInvoicePaymentAttempt",
]


class CreatedInvoiceAutoCollection(BaseModel):
    enabled: Optional[bool] = None
    """True only if auto-collection is enabled for this invoice."""

    next_attempt_at: Optional[datetime] = None
    """
    If the invoice is scheduled for auto-collection, this field will reflect when
    the next attempt will occur. If dunning has been exhausted, or auto-collection
    is not enabled for this invoice, this field will be `null`.
    """

    num_attempts: Optional[int] = None
    """Number of auto-collection payment attempts."""

    previously_attempted_at: Optional[datetime] = None
    """
    If Orb has ever attempted payment auto-collection for this invoice, this field
    will reflect when that attempt occurred. In conjunction with `next_attempt_at`,
    this can be used to tell whether the invoice is currently in dunning (that is,
    `previously_attempted_at` is non-null, and `next_attempt_time` is non-null), or
    if dunning has been exhausted (`previously_attempted_at` is non-null, but
    `next_attempt_time` is null).
    """


class CreatedInvoiceCreditNote(BaseModel):
    id: str

    credit_note_number: str

    memo: Optional[str] = None
    """An optional memo supplied on the credit note."""

    reason: str

    total: str

    type: str

    voided_at: Optional[datetime] = None
    """
    If the credit note has a status of `void`, this gives a timestamp when the
    credit note was voided.
    """


class CreatedInvoiceCustomerBalanceTransaction(BaseModel):
    id: str
    """A unique id for this transaction."""

    action: Literal[
        "applied_to_invoice",
        "manual_adjustment",
        "prorated_refund",
        "revert_prorated_refund",
        "return_from_voiding",
        "credit_note_applied",
        "credit_note_voided",
        "overpayment_refund",
        "external_payment",
        "small_invoice_carryover",
    ]

    amount: str
    """The value of the amount changed in the transaction."""

    created_at: datetime
    """The creation time of this transaction."""

    credit_note: Optional[CreditNoteTiny] = None

    description: Optional[str] = None
    """An optional description provided for manual customer balance adjustments."""

    ending_balance: str
    """
    The new value of the customer's balance prior to the transaction, in the
    customer's currency.
    """

    invoice: Optional[InvoiceTiny] = None

    starting_balance: str
    """
    The original value of the customer's balance prior to the transaction, in the
    customer's currency.
    """

    type: Literal["increment", "decrement"]


CreatedInvoiceLineItemAdjustment: TypeAlias = Annotated[
    Union[
        MonetaryUsageDiscountAdjustment,
        MonetaryAmountDiscountAdjustment,
        MonetaryPercentageDiscountAdjustment,
        MonetaryMinimumAdjustment,
        MonetaryMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]

CreatedInvoiceLineItemSubLineItem: TypeAlias = Annotated[
    Union[MatrixSubLineItem, TierSubLineItem, OtherSubLineItem], PropertyInfo(discriminator="type")
]


class CreatedInvoiceLineItem(BaseModel):
    id: str
    """A unique ID for this line item."""

    adjusted_subtotal: str
    """
    The line amount after any adjustments and before overage conversion, credits and
    partial invoicing.
    """

    adjustments: List[CreatedInvoiceLineItemAdjustment]
    """
    All adjustments applied to the line item in the order they were applied based on
    invoice calculations (ie. usage discounts -> amount discounts -> percentage
    discounts -> minimums -> maximums).
    """

    amount: str
    """
    The final amount for a line item after all adjustments and pre paid credits have
    been applied.
    """

    credits_applied: str
    """The number of prepaid credits applied."""

    end_date: datetime
    """The end date of the range of time applied for this line item's price."""

    filter: Optional[str] = None
    """An additional filter that was used to calculate the usage for this line item."""

    grouping: Optional[str] = None
    """
    [DEPRECATED] For configured prices that are split by a grouping key, this will
    be populated with the key and a value. The `amount` and `subtotal` will be the
    values for this particular grouping.
    """

    name: str
    """The name of the price associated with this line item."""

    partially_invoiced_amount: str
    """Any amount applied from a partial invoice"""

    price: Price
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    For more on the types of prices, see
    [the core concepts documentation](/core-concepts#plan-and-price)
    """

    quantity: float
    """Either the fixed fee quantity or the usage during the service period."""

    start_date: datetime
    """The start date of the range of time applied for this line item's price."""

    sub_line_items: List[CreatedInvoiceLineItemSubLineItem]
    """
    For complex pricing structures, the line item can be broken down further in
    `sub_line_items`.
    """

    subtotal: str
    """The line amount before any adjustments."""

    tax_amounts: List[TaxAmount]
    """An array of tax rates and their incurred tax amounts.

    Empty if no tax integration is configured.
    """

    usage_customer_ids: Optional[List[str]] = None
    """
    A list of customer ids that were used to calculate the usage for this line item.
    """


class CreatedInvoicePaymentAttempt(BaseModel):
    id: str
    """The ID of the payment attempt."""

    amount: str
    """The amount of the payment attempt."""

    created_at: datetime
    """The time at which the payment attempt was created."""

    payment_provider: Optional[Literal["stripe"]] = None
    """The payment provider that attempted to collect the payment."""

    payment_provider_id: Optional[str] = None
    """The ID of the payment attempt in the payment provider."""

    receipt_pdf: Optional[str] = None
    """URL to the downloadable PDF version of the receipt.

    This field will be `null` for payment attempts that did not succeed.
    """

    succeeded: bool
    """Whether the payment attempt succeeded."""


class CreatedInvoice(BaseModel):
    id: str

    amount_due: str
    """
    This is the final amount required to be charged to the customer and reflects the
    application of the customer balance to the `total` of the invoice.
    """

    auto_collection: CreatedInvoiceAutoCollection

    billing_address: Optional[Address] = None

    created_at: datetime
    """The creation time of the resource in Orb."""

    credit_notes: List[CreatedInvoiceCreditNote]
    """A list of credit notes associated with the invoice"""

    currency: str
    """An ISO 4217 currency string or `credits`"""

    customer: CustomerMinified

    customer_balance_transactions: List[CreatedInvoiceCustomerBalanceTransaction]

    customer_tax_id: Optional[CustomerTaxID] = None
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

    invoice_date: datetime
    """The scheduled date of the invoice"""

    invoice_number: str
    """Automatically generated invoice number to help track and reconcile invoices.

    Invoice numbers have a prefix such as `RFOBWG`. These can be sequential per
    account or customer.
    """

    invoice_pdf: Optional[str] = None
    """The link to download the PDF representation of the `Invoice`."""

    invoice_source: Literal["subscription", "partial", "one_off"]

    is_payable_now: bool
    """True if the invoice has only in-advance fixed fees and is payable now"""

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

    line_items: List[CreatedInvoiceLineItem]
    """The breakdown of prices in this invoice."""

    maximum: Optional[Maximum] = None

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

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    paid_at: Optional[datetime] = None
    """
    If the invoice has a status of `paid`, this gives a timestamp when the invoice
    was paid.
    """

    payment_attempts: List[CreatedInvoicePaymentAttempt]
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

    shipping_address: Optional[Address] = None

    status: Literal["issued", "paid", "synced", "void", "draft"]

    subscription: Optional[SubscriptionMinified] = None

    subtotal: str
    """The total before any discounts and minimums are applied."""

    sync_failed_at: Optional[datetime] = None
    """
    If the invoice failed to sync, this will be the last time an external invoicing
    provider sync was attempted. This field will always be `null` for invoices using
    Orb Invoicing.
    """

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


class ChangedSubscriptionResources(BaseModel):
    created_credit_notes: List[CreditNote]
    """The credit notes that were created as part of this operation."""

    created_invoices: List[CreatedInvoice]
    """The invoices that were created as part of this operation."""

    voided_credit_notes: List[CreditNote]
    """The credit notes that were voided as part of this operation."""

    voided_invoices: List[Invoice]
    """The invoices that were voided as part of this operation."""
