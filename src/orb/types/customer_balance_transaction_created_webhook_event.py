# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .customer import Customer
from .shared.invoice_tiny import InvoiceTiny
from .shared.credit_note_tiny import CreditNoteTiny

__all__ = ["CustomerBalanceTransactionCreatedWebhookEvent", "Properties", "PropertiesBalanceTransaction"]


class PropertiesBalanceTransaction(BaseModel):
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
        "prepaid_commit_cancel",
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


class Properties(BaseModel):
    balance_transaction: PropertiesBalanceTransaction


class CustomerBalanceTransactionCreatedWebhookEvent(BaseModel):
    """Issued when a customer balance transaction is created."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    customer: Customer
    """
    A customer is a buyer of your products, and the other party to the billing
    relationship.

    In Orb, customers are assigned system generated identifiers automatically, but
    it's often desirable to have these match existing identifiers in your system. To
    avoid having to denormalize Orb ID information, you can pass in an
    `external_customer_id` with your own identifier. See
    [Customer ID Aliases](/events-and-metrics/customer-aliases) for further
    information about how these aliases work in Orb.

    In addition to having an identifier in your system, a customer may exist in a
    payment provider solution like Stripe. Use the `payment_provider_id` and the
    `payment_provider` enum field to express this mapping.

    A customer also has a timezone (from the standard
    [IANA timezone database](https://www.iana.org/time-zones)), which defaults to
    your account's timezone. See [Timezone localization](/essentials/timezones) for
    information on what this timezone parameter influences within Orb.
    """

    properties: Properties

    type: Literal["customer.balance_transaction_created"]
    """The event this payload describes."""
