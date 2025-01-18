# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .price import Price
from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.discount import Discount

__all__ = [
    "InvoiceLineItemCreateResponse",
    "Maximum",
    "Minimum",
    "SubLineItem",
    "SubLineItemMatrixSubLineItem",
    "SubLineItemMatrixSubLineItemGrouping",
    "SubLineItemMatrixSubLineItemMatrixConfig",
    "SubLineItemTierSubLineItem",
    "SubLineItemTierSubLineItemGrouping",
    "SubLineItemTierSubLineItemTierConfig",
    "SubLineItemOtherSubLineItem",
    "SubLineItemOtherSubLineItemGrouping",
    "TaxAmount",
]


class Maximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class Minimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class SubLineItemMatrixSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class SubLineItemMatrixSubLineItemMatrixConfig(BaseModel):
    dimension_values: List[Optional[str]]
    """The ordered dimension values for this line item."""


class SubLineItemMatrixSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemMatrixSubLineItemGrouping] = None

    matrix_config: SubLineItemMatrixSubLineItemMatrixConfig

    name: str

    quantity: float

    type: Literal["matrix"]


class SubLineItemTierSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class SubLineItemTierSubLineItemTierConfig(BaseModel):
    first_unit: float

    last_unit: Optional[float] = None

    unit_amount: str


class SubLineItemTierSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemTierSubLineItemGrouping] = None

    name: str

    quantity: float

    tier_config: SubLineItemTierSubLineItemTierConfig

    type: Literal["tier"]


class SubLineItemOtherSubLineItemGrouping(BaseModel):
    key: str

    value: Optional[str] = None
    """No value indicates the default group"""


class SubLineItemOtherSubLineItem(BaseModel):
    amount: str
    """The total amount for this sub line item."""

    grouping: Optional[SubLineItemOtherSubLineItemGrouping] = None

    name: str

    quantity: float

    type: Literal["'null'"]


SubLineItem: TypeAlias = Annotated[
    Union[SubLineItemMatrixSubLineItem, SubLineItemTierSubLineItem, SubLineItemOtherSubLineItem],
    PropertyInfo(discriminator="type"),
]


class TaxAmount(BaseModel):
    amount: str
    """The amount of additional tax incurred by this tax rate."""

    tax_rate_description: str
    """The human-readable description of the applied tax rate."""

    tax_rate_percentage: Optional[str] = None
    """The tax rate percentage, out of 100."""


class InvoiceLineItemCreateResponse(BaseModel):
    id: str
    """A unique ID for this line item."""

    amount: str
    """The final amount after any discounts or minimums."""

    discount: Optional[Discount] = None

    end_date: datetime
    """The end date of the range of time applied for this line item's price."""

    grouping: Optional[str] = None
    """
    [DEPRECATED] For configured prices that are split by a grouping key, this will
    be populated with the key and a value. The `amount` and `subtotal` will be the
    values for this particular grouping.
    """

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    name: str
    """The name of the price associated with this line item."""

    price: Optional[Price] = None
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

    quantity: float

    start_date: datetime
    """The start date of the range of time applied for this line item's price."""

    sub_line_items: List[SubLineItem]
    """
    For complex pricing structures, the line item can be broken down further in
    `sub_line_items`.
    """

    subtotal: str
    """The line amount before any line item-specific discounts or minimums."""

    tax_amounts: List[TaxAmount]
    """An array of tax rates and their incurred tax amounts.

    Empty if no tax integration is configured.
    """
