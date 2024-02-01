# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .price import Price
from .shared import Discount
from .._models import BaseModel

__all__ = [
    "Plan",
    "BasePlan",
    "Maximum",
    "Minimum",
    "PlanPhase",
    "PlanPhaseMaximum",
    "PlanPhaseMinimum",
    "Product",
    "TrialConfig",
]


class BasePlan(BaseModel):
    id: Optional[str] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    name: Optional[str] = None


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


class PlanPhaseMaximum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this maximum amount applies to.

    For plan/plan phase maximums, this can be a subset of prices.
    """

    maximum_amount: str
    """Maximum amount applied"""


class PlanPhaseMinimum(BaseModel):
    applies_to_price_ids: List[str]
    """List of price_ids that this minimum amount applies to.

    For plan/plan phase minimums, this can be a subset of prices.
    """

    minimum_amount: str
    """Minimum amount applied"""


class PlanPhase(BaseModel):
    id: str

    description: Optional[str] = None

    discount: Optional[Discount] = None

    duration: Optional[int] = None
    """How many terms of length `duration_unit` this phase is active for.

    If null, this phase is evergreen and active indefinitely
    """

    duration_unit: Optional[Literal["daily", "monthly", "quarterly", "annual"]] = None

    maximum: Optional[PlanPhaseMaximum] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[PlanPhaseMinimum] = None

    minimum_amount: Optional[str] = None

    name: str

    order: int
    """Determines the ordering of the phase in a plan's lifecycle. 1 = first phase."""


class Product(BaseModel):
    id: str

    created_at: datetime

    name: str


class TrialConfig(BaseModel):
    trial_period: Optional[int] = None

    trial_period_unit: Literal["days"]


class Plan(BaseModel):
    id: str

    base_plan: Optional[BasePlan] = None

    base_plan_id: Optional[str] = None
    """
    The parent plan id if the given plan was created by overriding one or more of
    the parent's prices
    """

    created_at: datetime

    currency: str
    """
    An ISO 4217 currency string or custom pricing unit (`credits`) for this plan's
    prices.
    """

    default_invoice_memo: Optional[str] = None
    """
    The default memo text on the invoices corresponding to subscriptions on this
    plan. Note that each subscription may configure its own memo.
    """

    description: str

    discount: Optional[Discount] = None

    external_plan_id: Optional[str] = None
    """
    An optional user-defined ID for this plan resource, used throughout the system
    as an alias for this Plan. Use this field to identify a plan by an existing
    identifier in your system.
    """

    invoicing_currency: str
    """An ISO 4217 currency string for which this plan is billed in.

    Matches `currency` unless `currency` is a custom pricing unit.
    """

    maximum: Optional[Maximum] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[Minimum] = None

    minimum_amount: Optional[str] = None

    name: str

    net_terms: Optional[int] = None
    """Determines the difference between the invoice issue date and the due date.

    A value of "0" here signifies that invoices are due on issue, whereas a value of
    "30" means that the customer has a month to pay the invoice before its overdue.
    Note that individual subscriptions or invoices may set a different net terms
    configuration.
    """

    plan_phases: Optional[List[PlanPhase]] = None

    prices: List[Price]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    product: Product

    status: Literal["active", "archived", "draft"]

    trial_config: TrialConfig

    version: int
