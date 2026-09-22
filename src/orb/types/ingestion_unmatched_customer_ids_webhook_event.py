# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IngestionUnmatchedCustomerIDsWebhookEvent", "Properties"]


class Properties(BaseModel):
    external_customer_ids: List[str]


class IngestionUnmatchedCustomerIDsWebhookEvent(BaseModel):
    """Issued when ingestion events reference unmatched customer IDs."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    properties: Properties

    type: Literal["ingestion.unmatched_customer_ids"]
    """The event this payload describes."""
