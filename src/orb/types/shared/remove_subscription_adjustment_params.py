# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["RemoveSubscriptionAdjustmentParams"]


class RemoveSubscriptionAdjustmentParams(BaseModel):
    adjustment_id: str
    """The id of the adjustment to remove on the subscription."""
