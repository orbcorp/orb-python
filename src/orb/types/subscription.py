# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .plan import Plan
from .price import Price
from .._models import BaseModel
from .customer import Customer

__all__ = [
    "Subscription",
    "DiscountInterval",
    "DiscountIntervalAmountDiscountInterval",
    "DiscountIntervalPercentageDiscountInterval",
    "DiscountIntervalUsageDiscountInterval",
    "FixedFeeQuantitySchedule",
    "MaximumInterval",
    "MinimumInterval",
    "PriceInterval",
    "PriceIntervalFixedFeeQuantityTransition",
    "RedeemedCoupon",
    "TrialInfo",
]


class DiscountIntervalAmountDiscountInterval(BaseModel):
    amount_discount: str
    """Only available if discount_type is `amount`."""

    applies_to_price_ids: List[str]
    """The price ids that this discount interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["amount"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    start_date: datetime
    """The start date of the discount interval."""


class DiscountIntervalPercentageDiscountInterval(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this discount interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["percentage"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    percentage_discount: float
    """
    Only available if discount_type is `percentage`.This is a number between 0
    and 1.
    """

    start_date: datetime
    """The start date of the discount interval."""


class DiscountIntervalUsageDiscountInterval(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this discount interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this discount interval applies to."""

    discount_type: Literal["usage"]

    end_date: Optional[datetime] = None
    """The end date of the discount interval."""

    start_date: datetime
    """The start date of the discount interval."""

    usage_discount: float
    """Only available if discount_type is `usage`.

    Number of usage units that this discount is for
    """


DiscountInterval = Union[
    DiscountIntervalAmountDiscountInterval,
    DiscountIntervalPercentageDiscountInterval,
    DiscountIntervalUsageDiscountInterval,
]


class FixedFeeQuantitySchedule(BaseModel):
    end_date: Optional[datetime] = None

    price_id: str

    quantity: float

    start_date: datetime


class MaximumInterval(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this maximum interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this maximum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the maximum interval."""

    maximum_amount: str
    """
    The maximum amount to charge in a given billing period for the price intervals
    this transform applies to.
    """

    start_date: datetime
    """The start date of the maximum interval."""


class MinimumInterval(BaseModel):
    applies_to_price_ids: List[str]
    """The price ids that this minimum interval applies to."""

    applies_to_price_interval_ids: List[str]
    """The price interval ids that this minimum interval applies to."""

    end_date: Optional[datetime] = None
    """The end date of the minimum interval."""

    minimum_amount: str
    """
    The minimum amount to charge in a given billing period for the price intervals
    this minimum applies to.
    """

    start_date: datetime
    """The start date of the minimum interval."""


class PriceIntervalFixedFeeQuantityTransition(BaseModel):
    effective_date: datetime

    price_id: str

    quantity: int


class PriceInterval(BaseModel):
    id: str

    billing_cycle_day: int
    """The day of the month that Orb bills for this price"""

    current_billing_period_end_date: Optional[datetime] = None
    """The end of the current billing period.

    This is an exclusive timestamp, such that the instant returned is exactly the
    end of the billing period. Set to null if this price interval is not currently
    active.
    """

    current_billing_period_start_date: Optional[datetime] = None
    """The start date of the current billing period.

    This is an inclusive timestamp; the instant returned is exactly the beginning of
    the billing period. Set to null if this price interval is not currently active.
    """

    end_date: Optional[datetime] = None
    """The end date of the price interval.

    This is the date that Orb stops billing for this price.
    """

    fixed_fee_quantity_transitions: Optional[List[PriceIntervalFixedFeeQuantityTransition]] = None
    """The fixed fee quantity transitions for this price interval.

    This is only relevant for fixed fees.
    """

    price: Price
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

    ## Fixed fees

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

    start_date: datetime
    """The start date of the price interval.

    This is the date that Orb starts billing for this price.
    """


class RedeemedCoupon(BaseModel):
    coupon_id: str

    end_date: Optional[datetime] = None

    start_date: datetime


class TrialInfo(BaseModel):
    end_date: Optional[datetime] = None


class Subscription(BaseModel):
    id: str

    active_plan_phase_order: Optional[int] = None
    """
    The current plan phase that is active, only if the subscription's plan has
    phases.
    """

    auto_collection: Optional[bool] = None
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. This property defaults to
    the plan's behavior.
    """

    billing_cycle_day: int
    """The day of the month on which the billing cycle is anchored.

    If the maximum number of days in a month is greater than this value, the last
    day of the month is the billing cycle day (e.g. billing_cycle_day=31 for April
    means the billing period begins on the 30th.
    """

    created_at: datetime

    current_billing_period_end_date: Optional[datetime] = None
    """The end of the current billing period.

    This is an exclusive timestamp, such that the instant returned is not part of
    the billing period. Set to null for subscriptions that are not currently active.
    """

    current_billing_period_start_date: Optional[datetime] = None
    """The start date of the current billing period.

    This is an inclusive timestamp; the instant returned is exactly the beginning of
    the billing period. Set to null if the subscription is not currently active.
    """

    customer: Customer
    """
    A customer is a buyer of your products, and the other party to the billing
    relationship.

    In Orb, customers are assigned system generated identifiers automatically, but
    it's often desirable to have these match existing identifiers in your system. To
    avoid having to denormalize Orb ID information, you can pass in an
    `external_customer_id` with your own identifier. See
    [Customer ID Aliases](../guides/events-and-metrics/customer-aliases) for further
    information about how these aliases work in Orb.

    In addition to having an identifier in your system, a customer may exist in a
    payment provider solution like Stripe. Use the `payment_provider_id` and the
    `payment_provider` enum field to express this mapping.

    A customer also has a timezone (from the standard
    [IANA timezone database](https://www.iana.org/time-zones)), which defaults to
    your account's timezone. See
    [Timezone localization](../guides/product-catalog/timezones.md) for information
    on what this timezone parameter influences within Orb.
    """

    default_invoice_memo: Optional[str] = None
    """Determines the default memo on this subscriptions' invoices.

    Note that if this is not provided, it is determined by the plan configuration.
    """

    discount_intervals: List[DiscountInterval]
    """The discount intervals for this subscription."""

    end_date: Optional[datetime] = None
    """The date Orb stops billing for this subscription."""

    fixed_fee_quantity_schedule: List[FixedFeeQuantitySchedule]

    invoicing_threshold: Optional[str] = None

    maximum_intervals: List[MaximumInterval]
    """The maximum intervals for this subscription."""

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum_intervals: List[MinimumInterval]
    """The minimum intervals for this subscription."""

    net_terms: int
    """
    Determines the difference between the invoice issue date for subscription
    invoices as the date that they are due. A value of `0` here represents that the
    invoice is due on issue, whereas a value of `30` represents that the customer
    has a month to pay the invoice.
    """

    plan: Plan
    """
    The [Plan](../guides/core-concepts.mdx#plan-and-price) resource represents a
    plan that can be subscribed to by a customer. Plans define the billing behavior
    of the subscription. You can see more about how to configure prices in the
    [Price resource](/reference/price).
    """

    price_intervals: List[PriceInterval]
    """The price intervals for this subscription."""

    redeemed_coupon: Optional[RedeemedCoupon] = None

    start_date: datetime
    """The date Orb starts billing for this subscription."""

    status: Literal["active", "ended", "upcoming"]

    trial_info: TrialInfo
