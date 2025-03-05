# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["AllocationModel"]


class AllocationModel(BaseModel):
    allows_rollover: bool

    currency: str
