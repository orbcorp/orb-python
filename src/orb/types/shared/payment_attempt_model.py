# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PaymentAttemptModel"]


class PaymentAttemptModel(BaseModel):
    id: str
    """The ID of the payment attempt."""

    amount: str
    """The amount of the payment attempt."""

    created_at: datetime
    """The time at which the payment attempt was created."""

    payment_provider: Optional[Literal["stripe"]] = None
    """The payment provider that attempted to collect the payment."""

    payment_provider_id: Optional[str] = None
    """The ID of the payment attempt in the payment provider."""

    succeeded: bool
    """Whether the payment attempt succeeded."""
