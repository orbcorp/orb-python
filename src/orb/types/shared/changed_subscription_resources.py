# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .invoice import Invoice
from ..._models import BaseModel
from .credit_note import CreditNote

__all__ = ["ChangedSubscriptionResources"]


class ChangedSubscriptionResources(BaseModel):
    created_credit_notes: List[CreditNote]
    """The credit notes that were created as part of this operation."""

    created_invoices: List[Invoice]
    """The invoices that were created as part of this operation."""

    voided_credit_notes: List[CreditNote]
    """The credit notes that were voided as part of this operation."""

    voided_invoices: List[Invoice]
    """The invoices that were voided as part of this operation."""
