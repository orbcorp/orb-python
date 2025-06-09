# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TaxAmount"]


class TaxAmount(BaseModel):
    amount: str
    """The amount of additional tax incurred by this tax rate."""

    tax_rate_description: str
    """The human-readable description of the applied tax rate."""

    tax_rate_percentage: Optional[str] = None
    """The tax rate percentage, out of 100."""
