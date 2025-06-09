# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Threshold"]


class Threshold(BaseModel):
    value: float
    """The value at which an alert will fire.

    For credit balance alerts, the alert will fire at or below this value. For usage
    and cost alerts, the alert will fire at or above this value.
    """
