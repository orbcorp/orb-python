# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .price import Price
from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.discount import Discount
from .shared.invoice_level_discount import InvoiceLevelDiscount

__all__ = [
    "Invoice",
    "AutoCollection",
    "BillingAddress",
    "CreditNote",
    "Customer",
    "CustomerBalanceTransaction",
    "CustomerBalanceTransactionCreditNote",
    "CustomerBalanceTransactionInvoice",
    "CustomerTaxID",
    "LineItem",
    "LineItemAdjustment",
    "LineItemAdjustmentMonetaryUsageDiscountAdjustment",
    "LineItemAdjustmentMonetaryUsageDiscountAdjustmentFilter",
    "LineItemAdjustmentMonetaryAmountDiscountAdjustment",
    "LineItemAdjustmentMonetaryAmountDiscountAdjustmentFilter",
    "LineItemAdjustmentMonetaryPercentageDiscountAdjustment",
    "LineItemAdjustmentMonetaryPercentageDiscountAdjustmentFilter",
    "LineItemAdjustmentMonetaryMinimumAdjustment",
    "LineItemAdjustmentMonetaryMinimumAdjustmentFilter",
    "LineItemAdjustmentMonetaryMaximumAdjustment",
    "LineItemAdjustmentMonetaryMaximumAdjustmentFilter",
    "LineItemMaximum",
    "LineItemMaximumFilter",
    "LineItemMinimum",
    "LineItemMinimumFilter",
    "LineItemSubLineItem",
    "LineItemSubLineItemMatrixSubLineItem",
    "LineItemSubLineItemMatrixSubLineItemGrouping",
    "LineItemSubLineItemMatrixSubLineItemMatrixConfig",
    "LineItemSubLineItemTierSubLineItem",
    "LineItemSubLineItemTierSubLineItemGrouping",
    "LineItemSubLineItemTierSubLineItemTierConfig",
    "LineItemSubLineItemOtherSubLineItem",
    "LineItemSubLineItemOtherSubLineItemGrouping",
    "LineItemTaxAmount",
    "Maximum",
    "MaximumFilter",
    "Minimum",
    "MinimumFilter",
    "PaymentAttempt",
    "ShippingAddress",
    "Subscription",
]


class AutoCollection(BaseModel):
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


class BillingAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None


class CreditNote(BaseModel):
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


class Customer(BaseModel):
    id: str

    external_customer_id: Optional[str] = None


class CustomerBalanceTransactionCreditNote(BaseModel):
    id: str
    """The id of the Credit note"""


class CustomerBalanceTransactionInvoice(BaseModel):
    id: str
    """The Invoice id"""


class CustomerBalanceTransaction(BaseModel):
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
    ]

    amount: str
    """The value of the amount changed in the transaction."""

    created_at: datetime
    """The creation time of this transaction."""

    credit_note: Optional[CustomerBalanceTransactionCreditNote] = None

    description: Optional[str] = None
    """An optional description provided for manual customer balance adjustments."""

    ending_balance: str
    """
    The new value of the customer's balance prior to the transaction, in the
    customer's currency.
    """

    invoice: Optional[CustomerBalanceTransactionInvoice] = None

    starting_balance: str
    """
    The original value of the customer's balance prior to the transaction, in the
    customer's currency.
    """

    type: Literal["increment", "decrement"]


class CustomerTaxID(BaseModel):
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


class LineItemAdjustmentMonetaryUsageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemAdjustmentMonetaryUsageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["usage_discount"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[LineItemAdjustmentMonetaryUsageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""

    usage_discount: float
    """
    The number of usage units by which to discount the price this adjustment applies
    to in a given billing period.
    """


class LineItemAdjustmentMonetaryAmountDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemAdjustmentMonetaryAmountDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["amount_discount"]

    amount: str
    """The value applied by an adjustment."""

    amount_discount: str
    """
    The amount by which to discount the prices this adjustment applies to in a given
    billing period.
    """

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[LineItemAdjustmentMonetaryAmountDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


class LineItemAdjustmentMonetaryPercentageDiscountAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemAdjustmentMonetaryPercentageDiscountAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["percentage_discount"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[LineItemAdjustmentMonetaryPercentageDiscountAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    percentage_discount: float
    """
    The percentage (as a value between 0 and 1) by which to discount the price
    intervals this adjustment applies to in a given billing period.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


class LineItemAdjustmentMonetaryMinimumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemAdjustmentMonetaryMinimumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["minimum"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[LineItemAdjustmentMonetaryMinimumAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    item_id: str
    """The item ID that revenue from this minimum will be attributed to."""

    minimum_amount: str
    """
    The minimum amount to charge in a given billing period for the prices this
    adjustment applies to.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


class LineItemAdjustmentMonetaryMaximumAdjustmentFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemAdjustmentMonetaryMaximumAdjustment(BaseModel):
    id: str

    adjustment_type: Literal["maximum"]

    amount: str
    """The value applied by an adjustment."""

    applies_to_price_ids: List[str]
    """The price IDs that this adjustment applies to."""

    filters: List[LineItemAdjustmentMonetaryMaximumAdjustmentFilter]
    """The filters that determine which prices to apply this adjustment to."""

    is_invoice_level: bool
    """
    True for adjustments that apply to an entire invocice, false for adjustments
    that apply to only one price.
    """

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the prices this
    adjustment applies to.
    """

    reason: Optional[str] = None
    """The reason for the adjustment."""


LineItemAdjustment: TypeAlias = Annotated[
    Union[
        LineItemAdjustmentMonetaryUsageDiscountAdjustment,
        LineItemAdjustmentMonetaryAmountDiscountAdjustment,
        LineItemAdjustmentMonetaryPercentageDiscountAdjustment,
        LineItemAdjustmentMonetaryMinimumAdjustment,
        LineItemAdjustmentMonetaryMaximumAdjustment,
    ],
    PropertyInfo(discriminator="adjustment_type"),
]


class LineItemMaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[LineItemMaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class LineItemMinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class LineItemMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[LineItemMinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class LineItemSubLineItemMatrixSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class LineItemSubLineItemMatrixSubLineItemMatrixConfig(BaseModel):
    dimension_values: List[Optional[str]]
    """The ordered dimension values for this line item."""


class LineItemSubLineItemMatrixSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[LineItemSubLineItemMatrixSubLineItemGrouping] = None

    matrix_config: LineItemSubLineItemMatrixSubLineItemMatrixConfig

    name: str

    quantity: float

    type: Literal["matrix"]


class LineItemSubLineItemTierSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class LineItemSubLineItemTierSubLineItemTierConfig(BaseModel):
    first_unit: float

    last_unit: Optional[float] = None

    unit_amount: str


class LineItemSubLineItemTierSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[LineItemSubLineItemTierSubLineItemGrouping] = None

    name: str

    quantity: float

    tier_config: LineItemSubLineItemTierSubLineItemTierConfig

    type: Literal["tier"]


class LineItemSubLineItemOtherSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class LineItemSubLineItemOtherSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[LineItemSubLineItemOtherSubLineItemGrouping] = None

    name: str

    quantity: float

    type: Literal["'null'"]


LineItemSubLineItem: TypeAlias = Annotated[
    Union[
        LineItemSubLineItemMatrixSubLineItem, LineItemSubLineItemTierSubLineItem, LineItemSubLineItemOtherSubLineItem
    ],
    PropertyInfo(discriminator="type"),
]


class LineItemTaxAmount(BaseModel):
    amount: str
    """The amount of additional tax incurred by this tax rate."""

    tax_rate_description: str
    """The human-readable description of the applied tax rate."""

    tax_rate_percentage: Optional[str] = None
    """The tax rate percentage, out of 100."""


class LineItem(BaseModel):
    id: str
    """A unique ID for this line item."""

    adjusted_subtotal: str
    """
    The line amount after any adjustments and before overage conversion, credits and
    partial invoicing.
    """

    adjustments: List[LineItemAdjustment]
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

    discount: Optional[Discount] = None

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

    maximum: Optional[LineItemMaximum] = None
    """This field is deprecated in favor of `adjustments`."""

    maximum_amount: Optional[str] = None
    """This field is deprecated in favor of `adjustments`."""

    minimum: Optional[LineItemMinimum] = None
    """This field is deprecated in favor of `adjustments`."""

    minimum_amount: Optional[str] = None
    """This field is deprecated in favor of `adjustments`."""

    name: str
    """The name of the price associated with this line item."""

    partially_invoiced_amount: str
    """Any amount applied from a partial invoice"""

    price: Optional[Price] = None
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

    sub_line_items: List[LineItemSubLineItem]
    """
    For complex pricing structures, the line item can be broken down further in
    `sub_line_items`.
    """

    subtotal: str
    """The line amount before before any adjustments."""

    tax_amounts: List[LineItemTaxAmount]
    """An array of tax rates and their incurred tax amounts.

    Empty if no tax integration is configured.
    """

    usage_customer_ids: Optional[List[str]] = None
    """
    A list of customer ids that were used to calculate the usage for this line item.
    """


class MaximumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Maximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    filters: List[MaximumFilter]
    """The filters that determine which prices to apply this maximum to."""

    maximum_amount: str
    """Maximum amount applied"""


class MinimumFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class Minimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    filters: List[MinimumFilter]
    """The filters that determine which prices to apply this minimum to."""

    minimum_amount: str
    """Minimum amount applied"""


class PaymentAttempt(BaseModel):
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

    succeeded: bool
    """Whether the payment attempt succeeded."""


class ShippingAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None


class Subscription(BaseModel):
    id: str


class Invoice(BaseModel):
    id: str

    amount_due: str
    """
    This is the final amount required to be charged to the customer and reflects the
    application of the customer balance to the `total` of the invoice.
    """

    auto_collection: AutoCollection

    billing_address: Optional[BillingAddress] = None

    created_at: datetime
    """The creation time of the resource in Orb."""

    credit_notes: List[CreditNote]
    """A list of credit notes associated with the invoice"""

    currency: str
    """An ISO 4217 currency string or `credits`"""

    customer: Customer

    customer_balance_transactions: List[CustomerBalanceTransaction]

    customer_tax_id: Optional[CustomerTaxID] = None
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

    line_items: List[LineItem]
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

    payment_attempts: List[PaymentAttempt]
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

    shipping_address: Optional[ShippingAddress] = None

    status: Literal["issued", "paid", "synced", "void", "draft"]

    subscription: Optional[Subscription] = None

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
