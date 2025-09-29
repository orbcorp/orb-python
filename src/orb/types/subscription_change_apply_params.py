# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SubscriptionChangeApplyParams"]


class SubscriptionChangeApplyParams(TypedDict, total=False):
    description: Optional[str]
    """Description to apply to the balance transaction representing this credit."""

    mark_as_paid: Optional[bool]
    """Mark all pending invoices that are payable as paid.

    If amount is also provided, mark as paid and credit the difference to the
    customer's balance.
    """

    previously_collected_amount: Optional[str]
    """Amount already collected to apply to the customer's balance.

    If mark_as_paid is also provided, credit the difference to the customer's
    balance.
    """
