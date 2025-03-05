# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .discount import Discount
from ..._models import BaseModel
from .price_model import PriceModel
from .maximum_model import MaximumModel
from .minimum_model import MinimumModel
from .adjustment_model import AdjustmentModel
from .plan_minified_model import PlanMinifiedModel

__all__ = ["PlanModel", "PlanPhase", "Product", "TrialConfig"]


class PlanPhase(BaseModel):
    id: str

    description: Optional[str] = None

    discount: Optional[Discount] = None

    duration: Optional[int] = None
    """How many terms of length `duration_unit` this phase is active for.

    If null, this phase is evergreen and active indefinitely
    """

    duration_unit: Optional[Literal["daily", "monthly", "quarterly", "semi_annual", "annual"]] = None

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    minimum: Optional[MinimumModel] = None

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


class PlanModel(BaseModel):
    id: str

    adjustments: List[AdjustmentModel]
    """Adjustments for this plan.

    If the plan has phases, this includes adjustments across all phases of the plan.
    """

    base_plan: Optional[PlanMinifiedModel] = None

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

    maximum: Optional[MaximumModel] = None

    maximum_amount: Optional[str] = None

    metadata: Dict[str, str]
    """User specified key-value pairs for the resource.

    If not present, this defaults to an empty dictionary. Individual keys can be
    removed by setting the value to `null`, and the entire metadata mapping can be
    cleared by setting `metadata` to `null`.
    """

    minimum: Optional[MinimumModel] = None

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

    prices: List[PriceModel]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    product: Product

    status: Literal["active", "archived", "draft"]

    trial_config: TrialConfig

    version: int
