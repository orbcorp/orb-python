# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TopUpInvoiceSettings"]


class TopUpInvoiceSettings(BaseModel):
    auto_collection: bool
    """
    Whether the credits purchase invoice should auto collect with the customer's
    saved payment method.
    """

    net_terms: int
    """
    The number of days until the invoice is due, counting the start date as day 1,
    so net 30 from October 1 is due October 30. The account's
    [due date calculation method](/invoicing/payments#configuring-net-terms-and-collection-behavior)
    sets whether the start date is the invoice date or the issuance date. If you
    intend the invoice to be due on issue, set this to 0.
    """

    memo: Optional[str] = None
    """An optional memo to display on the invoice."""

    require_successful_payment: Optional[bool] = None
    """
    When true, credit blocks created by this top-up will require that the
    corresponding invoice is paid before they are drawn down from. If any topup
    block is pending payment, further automatic top-ups will be paused until the
    invoice is paid or voided.
    """
