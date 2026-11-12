# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MigrationCreateParams"]


class MigrationCreateParams(TypedDict, total=False):
    effective_time: Required[
        Literal["immediately", "requested_date", "start_of_term", "end_of_term", "start_of_invoice", "end_of_invoice"]
    ]
    """
    When the migration takes effect: 'immediately', 'requested_date' on
    `effective_date`, 'start_of_term' or 'end_of_term' for the start or end of each
    subscription's current billing period, or 'start_of_invoice' or 'end_of_invoice'
    for the start of its current or next invoice.
    """

    target_plan_version_number: Required[int]
    """The plan version to migrate subscriptions to. It can't be a draft version."""

    allow_invoice_credit_or_void: bool
    """
    When false, a subscription whose migration would void an issued invoice or
    create a credit note fails instead.
    """

    can_defer_billing: bool
    """
    When true, an in-arrears price the migration ends mid-cycle bills its final line
    item on the next scheduled invoice instead of on its end date.
    """

    effective_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The date the migration takes effect, at midnight in each customer's timezone.

    Required when `effective_time` is `requested_date`, and not allowed otherwise.
    """

    excluded_subscription_ids: Optional[SequenceNotStr[str]]
    """Leave these subscriptions out.

    Can't be combined with `included_subscription_ids`.
    """

    external_plan_id: Optional[str]
    """The external ID of the plan whose subscriptions to migrate."""

    in_trial: Optional[bool]
    """
    `true` migrates only subscriptions in a trial, `false` only subscriptions not in
    a trial.
    """

    included_subscription_ids: Optional[SequenceNotStr[str]]
    """Migrate only these subscriptions. When set, the filters below are ignored."""

    plan_id: Optional[str]
    """The plan whose subscriptions to migrate.

    Exactly one of `plan_id` and `external_plan_id` is required.
    """

    plan_version_numbers: Optional[Iterable[int]]
    """Migrate only subscriptions currently on these plan versions."""

    reason: Optional[str]
    """Why the migration was created."""

    statuses: List[Literal["active", "upcoming"]]
    """Migrate subscriptions with these statuses. Defaults to active subscriptions."""
