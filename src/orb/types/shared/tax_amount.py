# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaxAmount"]


class TaxAmount(BaseModel):
    amount: str
    """The amount of additional tax incurred by this tax rate."""

    tax_rate_description: str
    """The human-readable description of the applied tax rate."""

    tax_rate_percentage: Optional[str] = None
    """The tax rate percentage, out of 100."""

    tax_reason: Optional[
        Literal[
            "taxed",
            "reverse_charge",
            "customer_exempt",
            "product_exempt",
            "not_registered",
            "zero_rated",
            "not_taxed_other",
        ]
    ] = None
    """Why this tax was or was not charged, such as reverse_charge or customer_exempt.

    Null on tax calculated before reasons were recorded.
    """
