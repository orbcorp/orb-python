# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RemoveSubscriptionPriceParams"]


class RemoveSubscriptionPriceParams(BaseModel):
    external_price_id: Optional[str] = None
    """The external price id of the price to remove on the subscription."""

    price_id: Optional[str] = None
    """The id of the price to remove on the subscription."""
