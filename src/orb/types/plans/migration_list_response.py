# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MigrationListResponse"]


class MigrationListResponse(BaseModel):
    id: str

    effective_time: Union[date, datetime, Literal["end_of_term"], None] = None

    plan_id: str

    status: Literal["not_started", "in_progress", "completed", "action_needed", "canceled"]
