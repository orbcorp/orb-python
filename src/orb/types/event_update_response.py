# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["EventUpdateResponse"]


class EventUpdateResponse(BaseModel):
    amended: str
    """event_id of the amended event, if successfully ingested"""
