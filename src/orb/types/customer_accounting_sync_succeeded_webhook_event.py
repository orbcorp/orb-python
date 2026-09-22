# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .customer import Customer

__all__ = ["CustomerAccountingSyncSucceededWebhookEvent", "AccountingSyncRecord", "Properties"]


class AccountingSyncRecord(BaseModel):
    id: str

    customer_id: str

    record_type: Literal[
        "customer",
        "invoice",
        "transaction",
        "customer_balance_transaction",
        "credit_note",
        "subscription",
        "sales_order",
        "block",
    ]

    error_details: Optional[Dict[str, object]] = None

    provider_customer_id: Optional[str] = None

    status: Optional[str] = None

    sync_action: Optional[str] = None


class Properties(BaseModel):
    connection_type: str


class CustomerAccountingSyncSucceededWebhookEvent(BaseModel):
    """Issued when a customer accounting sync succeeds."""

    id: str
    """The ID of this webhook event."""

    accounting_sync_record: AccountingSyncRecord

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

    type: Literal["customer.accounting_sync_succeeded"]
    """The event this payload describes."""
