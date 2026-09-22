# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .subscription import Subscription

__all__ = ["SubscriptionEditedWebhookEvent", "Properties", "PropertiesPreviousAttributes"]


class PropertiesPreviousAttributes(BaseModel):
    auto_collection: Optional[bool] = None

    auto_issuance: Optional[bool] = None

    default_invoice_memo: Optional[str] = None

    invoicing_threshold: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None

    net_terms: Optional[int] = None


class Properties(BaseModel):
    previous_attributes: PropertiesPreviousAttributes


class SubscriptionEditedWebhookEvent(BaseModel):
    """Issued when a subscription is updated."""

    id: str
    """The ID of this webhook event."""

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

    type: Literal["subscription.edited"]
    """The event this payload describes."""
