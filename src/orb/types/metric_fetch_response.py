# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional
from typing_extensions import Literal

from .item import Item
from .._models import BaseModel

__all__ = ["MetricFetchResponse"]


class MetricFetchResponse(BaseModel):
    id: str

    description: Optional[str]

    item: Item
    """The Item resource represents a sellable product or good.

    Items are associated with all line items, billable metrics, and prices and are
    used for defining external sync behavior for invoices and tax calculation
    purposes.
    """

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    name: str

    status: Literal["active", "draft", "archived"]
