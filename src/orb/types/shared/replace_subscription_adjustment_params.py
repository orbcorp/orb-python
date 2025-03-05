# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel
from .new_adjustment_model import NewAdjustmentModel

__all__ = ["ReplaceSubscriptionAdjustmentParams"]


class ReplaceSubscriptionAdjustmentParams(BaseModel):
    adjustment: NewAdjustmentModel
    """The definition of a new adjustment to create and add to the subscription."""

    replaces_adjustment_id: str
    """The id of the adjustment on the plan to replace in the subscription."""
