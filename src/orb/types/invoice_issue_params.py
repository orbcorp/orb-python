# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["InvoiceIssueParams"]


class InvoiceIssueParams(TypedDict, total=False):
    synchronous: bool
    """If true, the invoice will be issued synchronously.

    If false, the invoice will be issued asynchronously. The synchronous option is
    only available for invoices that have no usage fees. If the invoice is
    configured to sync to an external provider, a successful response from this
    endpoint guarantees the invoice is present in the provider.
    """
