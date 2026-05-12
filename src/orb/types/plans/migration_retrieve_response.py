# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MigrationRetrieveResponse"]


class MigrationRetrieveResponse(BaseModel):
    id: str
    """Unique identifier for this plan version change."""

    effective_time: Union[date, datetime, Literal["end_of_term"], None] = None
    """When the migration takes effect.

    Can be a specific date/time, or 'end_of_term' when scheduled to be at the end of
    the current billing period.
    """

    plan_id: str
    """The ID of the plan being migrated."""

    status: Literal["not_started", "in_progress", "completed", "action_needed", "canceled"]
    """
    Current status of the migration: 'not_started', 'in_progress', 'completed',
    'action_needed', or 'canceled'.
    """
