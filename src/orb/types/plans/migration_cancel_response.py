# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MigrationCancelResponse"]


class MigrationCancelResponse(BaseModel):
    """A migration moves a plan's subscriptions onto one of the plan's versions.

    Each subscription is migrated
    asynchronously, either immediately or at a scheduled time, and the migration reports its overall status as it
    progresses.
    """

    id: str
    """Unique identifier for this plan version change."""

    effective_time: Union[
        date, datetime, Literal["start_of_term", "end_of_term", "start_of_invoice", "end_of_invoice"], None
    ] = None
    """When the migration takes effect.

    Can be a specific date/time, 'start_of_term' or 'end_of_term' when scheduled to
    be at the start or end of the current billing period, or 'start_of_invoice' or
    'end_of_invoice' when scheduled to be at the start of the current or next
    invoice.
    """

    ended_at: Optional[datetime] = None
    """
    When the migration completed or was canceled, or null if it is still in
    progress.
    """

    plan_id: str
    """The ID of the plan being migrated."""

    started_at: Optional[datetime] = None
    """When Orb began migrating the plan's subscriptions.

    Null if the migration has not begun, or was canceled before it began.
    """

    status: Literal["not_started", "in_progress", "completed", "action_needed", "canceled"]
    """
    Current status of the migration: 'not_started', 'in_progress', 'completed',
    'action_needed', or 'canceled'.
    """

    target_plan_version_number: int
    """The plan version subscriptions are migrated to."""
