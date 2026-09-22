# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "InvoiceAutomationScheduleStepExecutedWebhookEvent",
    "Invoice",
    "Properties",
    "PropertiesAction",
    "PropertiesActionSendEmailActionEntry",
    "PropertiesActionRetryPaymentActionEntry",
]


class Invoice(BaseModel):
    """
    The invoice fields a consumer needs to run their own notification flows without a
    follow-up API call, mirroring the variables Orb's own automation emails render against.
    """

    id: str

    amount_due: str

    currency: str

    customer_id: str

    customer_name: str

    due_date: Optional[date] = None

    external_customer_id: Optional[str] = None

    hosted_invoice_url: Optional[str] = None

    invoice_date: datetime

    invoice_number: str

    issued_at: Optional[datetime] = None

    memo: Optional[str] = None

    payment_method_last_four_digits: Optional[str] = None

    status: str

    subscription_id: Optional[str] = None


class PropertiesActionSendEmailActionEntry(BaseModel):
    recipient: Optional[str] = None

    sent: bool

    action_type: Optional[Literal["send_email"]] = None


class PropertiesActionRetryPaymentActionEntry(BaseModel):
    amount_attempted: Optional[str] = None

    currency: Optional[str] = None

    failure_reason: Optional[str] = None

    outcome: Literal["succeeded", "failed", "skipped"]

    payment_provider: Optional[str] = None

    payment_provider_transaction_id: Optional[str] = None

    payment_transaction_record_id: Optional[str] = None

    action_type: Optional[Literal["retry_payment"]] = None


PropertiesAction: TypeAlias = Annotated[
    Union[PropertiesActionSendEmailActionEntry, PropertiesActionRetryPaymentActionEntry],
    PropertyInfo(discriminator="action_type"),
]


class Properties(BaseModel):
    actions: List[PropertiesAction]

    automation_schedule_template_id: Optional[str] = None

    automation_schedule_template_name: Optional[str] = None

    executed_at: datetime

    label: str

    scheduled_at: datetime

    step_id: str


class InvoiceAutomationScheduleStepExecutedWebhookEvent(BaseModel):
    """Issued when a collections-automation schedule step is executed for an invoice."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    invoice: Invoice
    """
    The invoice fields a consumer needs to run their own notification flows without
    a follow-up API call, mirroring the variables Orb's own automation emails render
    against.
    """

    properties: Properties

    type: Literal["invoice.automation_schedule_step_executed"]
    """The event this payload describes."""
