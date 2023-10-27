# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from .item import Item
from .._models import BaseModel

__all__ = ["MetricListResponse"]


class MetricListResponse(BaseModel):
    id: str

    description: Optional[str]

    item: Item
    """The Item resource represents a sellable product or good.

    Items are associated with all line items, billable metrics, and prices and are
    used for defining external sync behavior for invoices and tax calculation
    purposes.
    """

    metadata: Dict[str, str]

    name: str

    status: Literal["active", "draft", "archived"]
