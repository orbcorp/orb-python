# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["EventIngestResponse", "ValidationFailed"]


class ValidationFailed(BaseModel):
    idempotency_key: str
    """The passed idempotency_key corresponding to the validation_errors"""

    validation_errors: List[str]
    """
    An array of strings corresponding to validation failures for this
    idempotency_key.
    """


class EventIngestResponse(BaseModel):
    validation_failed: List[ValidationFailed]
    """Contains all failing validation events.

    In the case of a 200, this array will always be empty. This field will always be
    present.
    """
