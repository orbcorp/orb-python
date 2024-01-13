# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .price import Price
from .shared import Discount
from .._models import BaseModel

__all__ = [
    "InvoiceFetchUpcomingResponse",
    "AutoCollection",
    "BillingAddress",
    "CreditNote",
    "Customer",
    "CustomerBalanceTransaction",
    "CustomerBalanceTransactionCreditNote",
    "CustomerBalanceTransactionInvoice",
    "CustomerTaxID",
    "LineItem",
    "LineItemMaximum",
    "LineItemMinimum",
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
    "Minimum",
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

    type: Literal[
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

    value: str


class LineItemMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class LineItemMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

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


LineItemSubLineItem = Union[
    LineItemSubLineItemMatrixSubLineItem, LineItemSubLineItemTierSubLineItem, LineItemSubLineItemOtherSubLineItem
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

    amount: str
    """The final amount after any discounts or minimums."""

    discount: Optional[Discount] = None

    end_date: datetime
    """The end date of the range of time applied for this line item's price."""

    grouping: Optional[str] = None
    """
    [DEPRECATED] For configured prices that are split by a grouping key, this will
    be populated with the key and a value. The `amount` and `subtotal` will be the
    values for this particular grouping.
    """

    maximum: Optional[LineItemMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[LineItemMinimum] = None

    minimum_amount: Optional[str] = None

    name: str
    """The name of the price associated with this line item."""

    price: Optional[Price] = None
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    ## Unit pricing

    With unit pricing, each unit costs a fixed amount.

    ```json
    {
        ...
        "model_type": "unit",
        "unit_config": {
            "unit_amount": "0.50"
        }
        ...
    }
    ```

    ## Tiered pricing

    In tiered pricing, the cost of a given unit depends on the tier range that it
    falls into, where each tier range is defined by an upper and lower bound. For
    example, the first ten units may cost $0.50 each and all units thereafter may
    cost $0.10 each.

    ```json
    {
        ...
        "model_type": "tiered",
        "tiered_config": {
            "tiers": [
                {
                    "first_unit": 1,
                    "last_unit": 10,
                    "unit_amount": "0.50"
                },
                {
                    "first_unit": 11,
                    "last_unit": null,
                    "unit_amount": "0.10"
                }
            ]
        }
        ...
    ```

    ## Bulk pricing

    Bulk pricing applies when the number of units determine the cost of all units.
    For example, if you've bought less than 10 units, they may each be $0.50 for a
    total of $5.00. Once you've bought more than 10 units, all units may now be
    priced at $0.40 (i.e. 101 units total would be $40.40).

    ```json
    {
        ...
        "model_type": "bulk",
        "bulk_config": {
            "tiers": [
                {
                    "maximum_units": 10,
                    "unit_amount": "0.50"
                },
                {
                    "maximum_units": 1000,
                    "unit_amount": "0.40"
                }
            ]
        }
        ...
    }
    ```

    ## Package pricing

    Package pricing defines the size or granularity of a unit for billing purposes.
    For example, if the package size is set to 5, then 4 units will be billed as 5
    and 6 units will be billed at 10.

    ```json
    {
        ...
        "model_type": "package",
        "package_config": {
            "package_amount": "0.80",
            "package_size": 10
        }
        ...
    }
    ```

    ## BPS pricing

    BPS pricing specifies a per-event (e.g. per-payment) rate in one hundredth of a
    percent (the number of basis points to charge), as well as a cap per event to
    assess. For example, this would allow you to assess a fee of 0.25% on every
    payment you process, with a maximum charge of $25 per payment.

    ```json
    {
        ...
        "model_type": "bps",
        "bps_config": {
           "bps": 125,
           "per_unit_maximum": "11.00"
        }
        ...
     }
    ```

    ## Bulk BPS pricing

    Bulk BPS pricing specifies BPS parameters in a tiered manner, dependent on the
    total quantity across all events. Similar to bulk pricing, the BPS parameters of
    a given event depends on the tier range that the billing period falls into. Each
    tier range is defined by an upper bound. For example, after $1.5M of payment
    volume is reached, each individual payment may have a lower cap or a smaller
    take-rate.

    ```json
        ...
        "model_type": "bulk_bps",
        "bulk_bps_config": {
            "tiers": [
               {
                    "maximum_amount": "1000000.00",
                    "bps": 125,
                    "per_unit_maximum": "19.00"
               },
              {
                    "maximum_amount": null,
                    "bps": 115,
                    "per_unit_maximum": "4.00"
                }
            ]
        }
        ...
    }
    ```

    ## Tiered BPS pricing

    Tiered BPS pricing specifies BPS parameters in a graduated manner, where an
    event's applicable parameter is a function of its marginal addition to the
    period total. Similar to tiered pricing, the BPS parameters of a given event
    depends on the tier range that it falls into, where each tier range is defined
    by an upper and lower bound. For example, the first few payments may have a 0.8
    BPS take-rate and all payments after a specific volume may incur a take-rate of
    0.5 BPS each.

    ```json
        ...
        "model_type": "tiered_bps",
        "tiered_bps_config": {
            "tiers": [
               {
                    "minimum_amount": "0",
                    "maximum_amount": "1000000.00",
                    "bps": 125,
                    "per_unit_maximum": "19.00"
               },
              {
                    "minimum_amount": "1000000.00",
                    "maximum_amount": null,
                    "bps": 115,
                    "per_unit_maximum": "4.00"
                }
            ]
        }
        ...
    }
    ```

    ## Matrix pricing

    Matrix pricing defines a set of unit prices in a one or two-dimensional matrix.
    `dimensions` defines the two event property values evaluated in this pricing
    model. In a one-dimensional matrix, the second value is `null`. Every
    configuration has a list of `matrix_values` which give the unit prices for
    specified property values. In a one-dimensional matrix, the matrix values will
    have `dimension_values` where the second value of the pair is null. If an event
    does not match any of the dimension values in the matrix, it will resort to the
    `default_unit_amount`.

    ```json
    {
        "model_type": "matrix"
        "matrix_config": {
            "default_unit_amount": "3.00",
            "dimensions": [
                "cluster_name",
                "region"
            ],
            "matrix_values": [
                {
                    "dimension_values": [
                        "alpha",
                        "west"
                    ],
                    "unit_amount": "2.00"
                },
                ...
            ]
        }
    }
    ```

    ### Fixed fees

    Fixed fees are prices that are applied independent of usage quantities, and
    follow unit pricing. They also have an additional parameter
    `fixed_price_quantity`. If the Price represents a fixed cost, this represents
    the quantity of units applied.

    ```json
    {
        ...
        "id": "price_id",
        "model_type": "unit",
        "unit_config": {
           "unit_amount": "2.00"
        },
        "fixed_price_quantity": 3.0
        ...
    }
    ```
    """

    quantity: float

    start_date: datetime
    """The start date of the range of time applied for this line item's price."""

    sub_line_items: List[LineItemSubLineItem]
    """
    For complex pricing structures, the line item can be broken down further in
    `sub_line_items`.
    """

    subtotal: str
    """The line amount before any line item-specific discounts or minimums."""

    tax_amounts: List[LineItemTaxAmount]
    """An array of tax rates and their incurred tax amounts.

    Empty if no tax integration is configured.
    """


class Maximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class Minimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class ShippingAddress(BaseModel):
    city: Optional[str] = None

    country: Optional[str] = None

    line1: Optional[str] = None

    line2: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None


class Subscription(BaseModel):
    id: str


class InvoiceFetchUpcomingResponse(BaseModel):
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

    discount: Optional[Discount] = None

    discounts: List[Discount]

    due_date: datetime
    """When the invoice payment is due."""

    eligible_to_issue_at: Optional[datetime] = None
    """
    If the invoice has a status of `draft`, this will be the time that the invoice
    will be eligible to be issued, otherwise it will be `null`. If `auto-issue` is
    true, the invoice will automatically begin issuing at this time.
    """

    hosted_invoice_url: Optional[str] = None
    """A URL for the invoice portal."""

    invoice_number: str
    """Automatically generated invoice number to help track and reconcile invoices.

    Invoice numbers have a prefix such as `RFOBWG`. These can be sequential per
    account or customer.
    """

    invoice_pdf: Optional[str] = None
    """The link to download the PDF representation of the `Invoice`."""

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
