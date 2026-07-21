# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MigrationCancelResponse"]


class MigrationCancelResponse(BaseModel):
    id: str
    """Unique identifier for this plan version change."""

    effective_time: Union[date, datetime, Literal["end_of_term", "end_of_invoice"], None] = None
    """When the migration takes effect.

    Can be a specific date/time, 'end_of_term' when scheduled to be at the end of
    the current billing period, or 'end_of_invoice' when scheduled to be at the
    start of the next invoice.
    """

    plan_id: str
    """The ID of the plan being migrated."""

    status: Literal["not_started", "in_progress", "completed", "action_needed", "canceled"]
    """
    Current status of the migration: 'not_started', 'in_progress', 'completed',
    'action_needed', or 'canceled'.
    """
