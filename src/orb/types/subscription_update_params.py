# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["SubscriptionUpdateParams"]


class SubscriptionUpdateParams(TypedDict, total=False):
    auto_collection: Optional[bool]
    """
    Determines whether issued invoices for this subscription will automatically be
    charged with the saved payment method on the due date. This property defaults to
    the plan's behavior.
    """

    auto_issuance: Optional[bool]
    """Used to determine if invoices for this subscription will be automatically
    issued.

    If true, invoices will be automatically issued. If false, invoices will require
    manual approval. If `null` is specified, this defaults to the behavior
    configured for this customer.
    """

    default_invoice_memo: Optional[str]
    """Determines the default memo on this subscription's invoices.

    Note that if this is not provided, it is determined by the plan configuration.
    """

    invoicing_threshold: Optional[str]
    """
    When this subscription's accrued usage reaches this threshold, an invoice will
    be issued for the subscription. If not specified, invoices will only be issued
    at the end of the billing period.
    """

    metadata: Optional[Dict[str, Optional[str]]]
    """User-specified key/value pairs for the resource.

    Individual keys can be removed by setting the value to `null`, and the entire
    metadata mapping can be cleared by setting `metadata` to `null`.
    """

    net_terms: Optional[int]
    """
    The number of days until subscription invoices are due, counting the start date
    set by the account's
    [due date calculation method](/invoicing/payments#configuring-net-terms-and-collection-behavior)
    as day 1. A value of `0` here represents that the invoice is due on issue,
    whereas a value of `30` represents that the customer has a month to pay the
    invoice.
    """
