# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .customer import Customer
from .shared.custom_expiration import CustomExpiration

__all__ = [
    "CustomerCreditLedgerIncrementedWebhookEvent",
    "Properties",
    "PropertiesBlock",
    "PropertiesBlockFilter",
    "PropertiesBlockCreditAllocation",
    "PropertiesBlockCreditAllocationFilter",
    "PropertiesBlockCreditCommitment",
    "PropertiesPricingUnit",
]


class PropertiesBlockFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PropertiesBlockCreditAllocationFilter(BaseModel):
    field: Literal["price_id", "item_id", "price_type", "currency", "pricing_unit_id"]
    """The property of the price to filter on."""

    operator: Literal["includes", "excludes"]
    """Should prices that match the filter be included or excluded."""

    values: List[str]
    """The IDs or values that match this filter."""


class PropertiesBlockCreditAllocation(BaseModel):
    """The credit allocation that funded a block.

    Extends the allocation resource
    serialized on prices with the catalog-item attribution of the funding price.
    """

    allows_rollover: bool

    currency: str

    custom_expiration: Optional[CustomExpiration] = None

    item_id: str
    """
    The ID of the catalog item this block was allocated from, derived from the
    allocation's price.
    """

    filters: Optional[List[PropertiesBlockCreditAllocationFilter]] = None

    license_type_id: Optional[str] = None


class PropertiesBlockCreditCommitment(BaseModel):
    """
    The subscription commitment whose true-up rolled forward into this credit block.
    Present only when `credit_block_source` is `commitment`.
    """

    id: str
    """The ID of the subscription commitment this block was rolled forward from."""

    subscription_id: Optional[str] = None
    """The subscription the commitment belongs to."""


class PropertiesBlock(BaseModel):
    """The Credit Block resource models prepaid credits within Orb."""

    id: str

    balance: str

    credit_block_source: Literal["allocation", "top_up", "commitment", "manual"]
    """
    How this credit block was created: `allocation` (a subscription's recurring
    credit allocation), `top_up` (an automatic balance-threshold top-up),
    `commitment` (a subscription commitment true-up rolled forward as credit), or
    `manual` (a manual credit ledger increment, including credits voided or expired
    off another block).
    """

    effective_date: Optional[datetime] = None

    expiry_date: Optional[datetime] = None

    filters: List[PropertiesBlockFilter]

    maximum_initial_balance: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    per_unit_cost_basis: Optional[str] = None

    status: Literal["active", "pending_payment"]

    credit_allocation: Optional[PropertiesBlockCreditAllocation] = None
    """The credit allocation that funded a block.

    Extends the allocation resource serialized on prices with the catalog-item
    attribution of the funding price.
    """

    credit_commitment: Optional[PropertiesBlockCreditCommitment] = None
    """
    The subscription commitment whose true-up rolled forward into this credit block.
    Present only when `credit_block_source` is `commitment`.
    """


class PropertiesPricingUnit(BaseModel):
    """A currency or custom credit unit, as embedded in webhook payloads."""

    id: str

    display_name: Optional[str] = None

    name: str

    symbol: Optional[str] = None


class Properties(BaseModel):
    block: PropertiesBlock
    """The Credit Block resource models prepaid credits within Orb."""

    pricing_unit: PropertiesPricingUnit
    """A currency or custom credit unit, as embedded in webhook payloads."""


class CustomerCreditLedgerIncrementedWebhookEvent(BaseModel):
    """Issued when a customer's credit ledger is incremented."""

    id: str
    """The ID of this webhook event."""

    created_at: datetime
    """The time at which this event was created, to the second."""

    customer: Customer
    """
    A customer is a buyer of your products, and the other party to the billing
    relationship.

    In Orb, customers are assigned system generated identifiers automatically, but
    it's often desirable to have these match existing identifiers in your system. To
    avoid having to denormalize Orb ID information, you can pass in an
    `external_customer_id` with your own identifier. See
    [Customer ID Aliases](/events-and-metrics/customer-aliases) for further
    information about how these aliases work in Orb.

    In addition to having an identifier in your system, a customer may exist in a
    payment provider solution like Stripe. Use the `payment_provider_id` and the
    `payment_provider` enum field to express this mapping.

    A customer also has a timezone (from the standard
    [IANA timezone database](https://www.iana.org/time-zones)), which defaults to
    your account's timezone. See [Timezone localization](/essentials/timezones) for
    information on what this timezone parameter influences within Orb.
    """

    properties: Properties

    type: Literal["customer.credit_ledger_incremented"]
    """The event this payload describes."""
