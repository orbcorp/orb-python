# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = [
    "InvoiceDunningScheduleCreatedWebhookEvent",
    "Properties",
    "PropertiesDunningSchedule",
    "PropertiesDunningStep",
]


class PropertiesDunningSchedule(BaseModel):
    completion_time: Optional[datetime] = None

    created_at: Optional[datetime] = None

    invoice_id: str

    modified_at: Optional[datetime] = None

    start_time: Optional[datetime] = None

    status: str


class PropertiesDunningStep(BaseModel):
    actions: List[str]

    created_at: Optional[datetime] = None

    execution_time: Optional[datetime] = None

    manually_triggered_at: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    status: str

    step_number: Optional[int] = None

    timestamp: Optional[datetime] = None


class Properties(BaseModel):
    dunning_schedule: PropertiesDunningSchedule

    dunning_steps: List[PropertiesDunningStep]

    source: str


class InvoiceDunningScheduleCreatedWebhookEvent(BaseModel):
    """Issued when a dunning schedule is created for an invoice."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    invoice: Invoice
    """
    An [`Invoice`](/core-concepts#invoice) is a fundamental billing entity,
    representing the request for payment for a single subscription. This includes a
    set of line items, which correspond to prices in the subscription's plan and can
    represent fixed recurring fees or usage-based fees. They are generated at the
    end of a billing period, or as the result of an action, such as a cancellation.
    """

    properties: Properties

    type: Literal["invoice.dunning_schedule_created"]
    """The event this payload describes."""
