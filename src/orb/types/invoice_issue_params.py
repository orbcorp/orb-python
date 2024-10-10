# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InvoiceIssueParams"]


class InvoiceIssueParams(TypedDict, total=False):
    synchronous: bool
    """If true, the invoice will be issued synchronously.

    If false, the invoice will be issued asynchronously.
    """
