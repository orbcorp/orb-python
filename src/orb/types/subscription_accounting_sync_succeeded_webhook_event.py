# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionAccountingSyncSucceededWebhookEvent", "AccountingSyncRecord", "Properties"]


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

    subscription_id: Optional[str] = None

    sync_action: Optional[str] = None


class Properties(BaseModel):
    connection_type: str


class SubscriptionAccountingSyncSucceededWebhookEvent(BaseModel):
    """Issued when a subscription accounting sync succeeds."""

    id: str
    """The ID of this webhook event."""

    accounting_sync_record: AccountingSyncRecord

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    subscription: Subscription
    """
    A [subscription](/core-concepts#subscription) represents the purchase of a plan
    by a customer.

    By default, subscriptions begin on the day that they're created and renew
    automatically for each billing cycle at the cadence that's configured in the
    plan definition.

    Subscriptions also default to **beginning of month alignment**, which means the
    first invoice issued for the subscription will have pro-rated charges between
    the `start_date` and the first of the following month. Subsequent billing
    periods will always start and end on a month boundary (e.g. subsequent month
    starts for monthly billing).

    Depending on the plan configuration, any _flat_ recurring fees will be billed
    either at the beginning (in-advance) or end (in-arrears) of each billing cycle.
    Plans default to **in-advance billing**. Usage-based fees are billed in arrears
    as usage is accumulated. In the normal course of events, you can expect an
    invoice to contain usage-based charges for the previous period, and a recurring
    fee for the following period.
    """

    type: Literal["subscription.accounting_sync_succeeded"]
    """The event this payload describes."""
