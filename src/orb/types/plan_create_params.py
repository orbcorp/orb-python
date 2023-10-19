# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PlanCreateParams"]


class PlanCreateParams(TypedDict, total=False):
    currency: Required[str]
    """
    An ISO 4217 currency string or custom pricing unit (`credits`) for this plan's
    prices.
    """

    name: Required[str]

    prices: Required[List[object]]
    """Prices for this plan.

    If the plan has phases, this includes prices across all phases of the plan.
    """

    default_invoice_memo: Optional[str]
    """
    Free-form text which is available on the invoice PDF and the Orb invoice portal.
    """

    external_plan_id: Optional[str]

    metadata: Optional[object]

    net_terms: Optional[int]
    """
    The net terms determines the difference between the invoice date and the issue
    date for the invoice. If you intend the invoice to be due on issue, set this
    to 0.
    """
