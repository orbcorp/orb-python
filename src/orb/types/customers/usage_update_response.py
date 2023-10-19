# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["UsageUpdateResponse"]


class UsageUpdateResponse(BaseModel):
    duplicate: List[str]
    """
    An array of strings, corresponding to idempotency_key's marked as duplicates
    (previously ingested)
    """

    ingested: List[str]
    """
    An array of strings, corresponding to idempotency_key's which were successfully
    ingested.
    """
