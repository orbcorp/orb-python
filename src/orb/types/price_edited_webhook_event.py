# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.price import Price

__all__ = ["PriceEditedWebhookEvent", "Properties", "PropertiesPreviousAttributes"]


class PropertiesPreviousAttributes(BaseModel):
    """
    metadata values are non-null on the wire (deleting a key removes it from storage); the
    Optional[str] values only exist on the new half of a metadata FieldChange.
    """

    metadata: Optional[Dict[str, str]] = None


class Properties(BaseModel):
    previous_attributes: PropertiesPreviousAttributes
    """
    metadata values are non-null on the wire (deleting a key removes it from
    storage); the Optional[str] values only exist on the new half of a metadata
    FieldChange.
    """


class PriceEditedWebhookEvent(BaseModel):
    """Issued when a price is edited."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    price: Price
    """
    The Price resource represents a price that can be billed on a subscription,
    resulting in a charge on an invoice in the form of an invoice line item. Prices
    take a quantity and determine an amount to bill.

    Orb supports a few different pricing models out of the box. Each of these models
    is serialized differently in a given Price object. The model_type field
    determines the key for the configuration object that is present.

    For more on the types of prices, see
    [the core concepts documentation](/core-concepts#plan-and-price)
    """

    properties: Properties

    type: Literal["price.edited"]
    """The event this payload describes."""
