# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.customer_minified import CustomerMinified

__all__ = ["MigrationSubscription"]


class MigrationSubscription(BaseModel):
    customer: CustomerMinified

    effective_date: Optional[datetime] = None
    """When the subscription is migrated to the target plan version.

    Null unless the status is 'scheduled' or 'completed'.
    """

    failure_reason: Optional[str] = None
    """Why the subscription could not be migrated. Null unless the status is 'failed'."""

    status: Literal["scheduling", "scheduled", "completed", "skipped", "failed"]
    """
    The subscription's status in the migration: 'scheduling' until the migration has
    processed it, 'scheduled' when it will be migrated to the target version at
    `effective_date`, 'completed' once it has been migrated, 'skipped' when the
    migration left it unchanged, or 'failed' when it could not be migrated (see
    `failure_reason`).
    """

    subscription_id: str
    """The ID of the subscription."""
