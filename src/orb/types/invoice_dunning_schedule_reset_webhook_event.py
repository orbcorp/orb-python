# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.invoice import Invoice

__all__ = [
    "InvoiceDunningScheduleResetWebhookEvent",
    "Properties",
    "PropertiesDunningSchedule",
    "PropertiesPreviousSchedule",
]


class PropertiesDunningSchedule(BaseModel):
    """
    The schedule shape `DunningScheduleV2.external_serialization()` produces, which is narrower
    than the schedule's api resource.
    """

    completion_time: Optional[datetime] = None

    created_at: Optional[datetime] = None

    invoice_id: str

    modified_at: Optional[datetime] = None

    start_time: Optional[datetime] = None

    status: Optional[str] = None


class PropertiesPreviousSchedule(BaseModel):
    """
    The schedule shape `DunningScheduleV2.external_serialization()` produces, which is narrower
    than the schedule's api resource.
    """

    completion_time: Optional[datetime] = None

    created_at: Optional[datetime] = None

    invoice_id: str

    modified_at: Optional[datetime] = None

    start_time: Optional[datetime] = None

    status: Optional[str] = None


class Properties(BaseModel):
    dunning_schedule: PropertiesDunningSchedule
    """
    The schedule shape `DunningScheduleV2.external_serialization()` produces, which
    is narrower than the schedule's api resource.
    """

    previous_schedule: PropertiesPreviousSchedule
    """
    The schedule shape `DunningScheduleV2.external_serialization()` produces, which
    is narrower than the schedule's api resource.
    """


class InvoiceDunningScheduleResetWebhookEvent(BaseModel):
    """Issued when a dunning schedule is reset."""

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

    type: Literal["invoice.dunning_schedule_reset"]
    """The event this payload describes."""
