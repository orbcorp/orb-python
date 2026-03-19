# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoicePayParams"]


class InvoicePayParams(TypedDict, total=False):
    shared_payment_token_id: Required[str]
    """The ID of a shared payment token granted by an agent to use for this payment."""
