# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EventDeprecateResponse"]


class EventDeprecateResponse(BaseModel):
    deprecated: str
    """event_id of the deprecated event, if successfully updated"""
