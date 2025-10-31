# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, Optional, cast
from datetime import date, datetime
from typing_extensions import Literal, overload

import httpx

from .... import _legacy_response
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.customers.credits import (
    ledger_list_params,
    ledger_create_entry_params,
    ledger_list_by_external_id_params,
    ledger_create_entry_by_external_id_params,
)
from ....types.customers.credits.ledger_list_response import LedgerListResponse
from ....types.customers.credits.ledger_create_entry_response import LedgerCreateEntryResponse
from ....types.customers.credits.ledger_list_by_external_id_response import LedgerListByExternalIDResponse
from ....types.customers.credits.ledger_create_entry_by_external_id_response import (
    LedgerCreateEntryByExternalIDResponse,
)

__all__ = ["Ledger", "AsyncLedger"]


class Ledger(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LedgerWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return LedgerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LedgerWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return LedgerWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        entry_status: Optional[Literal["committed", "pending"]] | Omit = omit,
        entry_type: Optional[
            Literal[
                "increment",
                "decrement",
                "expiration_change",
                "credit_block_expiry",
                "void",
                "void_initiated",
                "amendment",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        minimum_amount: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[LedgerListResponse]:
        """
        The credits ledger provides _auditing_ functionality over Orb's credits system
        with a list of actions that have taken place to modify a customer's credit
        balance. This [paginated endpoint](/api-reference/pagination) lists these
        entries, starting from the most recent ledger entry.

        More details on using Orb's real-time credit feature are
        [here](/product-catalog/prepurchase).

        There are four major types of modifications to credit balance, detailed below.

        ## Increment

        Credits (which optionally expire on a future date) can be added via the API
        ([Add Ledger Entry](create-ledger-entry)). The ledger entry for such an action
        will always contain the total eligible starting and ending balance for the
        customer at the time the entry was added to the ledger.

        ## Decrement

        Deductions can occur as a result of an API call to create a ledger entry (see
        [Add Ledger Entry](create-ledger-entry)), or automatically as a result of
        incurring usage. Both ledger entries present the `decrement` entry type.

        As usage for a customer is reported into Orb, credits may be deducted according
        to the customer's plan configuration. An automated deduction of this type will
        result in a ledger entry, also with a starting and ending balance. In order to
        provide better tracing capabilities for automatic deductions, Orb always
        associates each automatic deduction with the `event_id` at the time of
        ingestion, used to pinpoint _why_ credit deduction took place and to ensure that
        credits are never deducted without an associated usage event.

        By default, Orb uses an algorithm that automatically deducts from the _soonest
        expiring credit block_ first in order to ensure that all credits are utilized
        appropriately. As an example, if trial credits with an expiration date of 2
        weeks from now are present for a customer, they will be used before any
        deductions take place from a non-expiring credit block.

        If there are multiple blocks with the same expiration date, Orb will deduct from
        the block with the _lower cost basis_ first (e.g. trial credits with a \\$$0 cost
        basis before paid credits with a \\$$5.00 cost basis).

        It's also possible for a single usage event's deduction to _span_ credit blocks.
        In this case, Orb will deduct from the next block, ending at the credit block
        which consists of unexpiring credits. Each of these deductions will lead to a
        _separate_ ledger entry, one per credit block that is deducted from. By default,
        the customer's total credit balance in Orb can be negative as a result of a
        decrement.

        ## Expiration change

        The expiry of credits can be changed as a result of the API (See
        [Add Ledger Entry](create-ledger-entry)). This will create a ledger entry that
        specifies the balance as well as the initial and target expiry dates.

        Note that for this entry type, `starting_balance` will equal `ending_balance`,
        and the `amount` represents the balance transferred. The credit block linked to
        the ledger entry is the source credit block from which there was an expiration
        change.

        ## Credits expiry

        When a set of credits expire on pre-set expiration date, the customer's balance
        automatically reflects this change and adds an entry to the ledger indicating
        this event. Note that credit expiry should always happen close to a date
        boundary in the customer's timezone.

        ## Void initiated

        Credit blocks can be voided via the API. The `amount` on this entry corresponds
        to the number of credits that were remaining in the block at time of void.
        `void_reason` will be populated if the void is created with a reason.

        ## Void

        When a set of credits is voided, the customer's balance automatically reflects
        this change and adds an entry to the ledger indicating this event.

        ## Amendment

        When credits are added to a customer's balance as a result of a correction, this
        entry will be added to the ledger to indicate the adjustment of credits.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/credits/ledger",
            page=SyncPage[LedgerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "currency": currency,
                        "cursor": cursor,
                        "entry_status": entry_status,
                        "entry_type": entry_type,
                        "limit": limit,
                        "minimum_amount": minimum_amount,
                    },
                    ledger_list_params.LedgerListParams,
                ),
            ),
            model=cast(Any, LedgerListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    @overload
    def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        entry_type: Literal["increment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[Iterable[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsFilter]]
        | Omit = omit,
        invoice_settings: Optional[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          effective_date: An ISO 8601 format date that denotes when this credit balance should become
              available for use.

          expiry_date: An ISO 8601 format date that denotes when this credit balance should expire.

          filters: Optional filter to specify which items this credit block applies to. If not
              specified, the block will apply to all items for the pricing unit.

          invoice_settings: Passing `invoice_settings` automatically generates an invoice for the newly
              added credits. If `invoice_settings` is passed, you must specify
              per_unit_cost_basis, as the calculation of the invoice total is done on that
              basis.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          per_unit_cost_basis: Can only be specified when entry_type=increment. How much, in the customer's
              currency, a customer paid for a single credit in this block

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        entry_type: Literal["decrement"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry(
        self,
        customer_id: str,
        *,
        entry_type: Literal["expiration_change"],
        target_expiry_date: Union[str, date],
        amount: Optional[float] | Omit = omit,
        block_id: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          target_expiry_date: A future date (specified in YYYY-MM-DD format) used for expiration change,
              denoting when credits transferred (as part of a partial block expiration) should
              expire.

          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block affected by an expiration_change, used to differentiate
              between multiple blocks with the same `expiry_date`.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          expiry_date: An ISO 8601 format date that identifies the origination credit block to expire

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["void"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block to void.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          void_reason: Can only be specified when `entry_type=void`. The reason for the void.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement or void operations.

          block_id: The ID of the block to reverse a decrement from.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["amount", "entry_type"], ["entry_type", "target_expiry_date"], ["amount", "block_id", "entry_type"])
    def create_entry(
        self,
        customer_id: str,
        *,
        amount: float | Optional[float] | Omit = omit,
        entry_type: Literal["increment"]
        | Literal["decrement"]
        | Literal["expiration_change"]
        | Literal["void"]
        | Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[Iterable[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsFilter]]
        | Omit = omit,
        invoice_settings: Optional[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        target_expiry_date: Union[str, date] | Omit = omit,
        block_id: Optional[str] | str | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return cast(
            LedgerCreateEntryResponse,
            self._post(
                f"/customers/{customer_id}/credits/ledger_entry",
                body=maybe_transform(
                    {
                        "amount": amount,
                        "entry_type": entry_type,
                        "currency": currency,
                        "description": description,
                        "effective_date": effective_date,
                        "expiry_date": expiry_date,
                        "filters": filters,
                        "invoice_settings": invoice_settings,
                        "metadata": metadata,
                        "per_unit_cost_basis": per_unit_cost_basis,
                        "target_expiry_date": target_expiry_date,
                        "block_id": block_id,
                        "void_reason": void_reason,
                    },
                    ledger_create_entry_params.LedgerCreateEntryParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, LedgerCreateEntryResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        entry_type: Literal["increment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[
            Iterable[ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsFilter]
        ]
        | Omit = omit,
        invoice_settings: Optional[
            ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings
        ]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          effective_date: An ISO 8601 format date that denotes when this credit balance should become
              available for use.

          expiry_date: An ISO 8601 format date that denotes when this credit balance should expire.

          filters: Optional filter to specify which items this credit block applies to. If not
              specified, the block will apply to all items for the pricing unit.

          invoice_settings: Passing `invoice_settings` automatically generates an invoice for the newly
              added credits. If `invoice_settings` is passed, you must specify
              per_unit_cost_basis, as the calculation of the invoice total is done on that
              basis.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          per_unit_cost_basis: Can only be specified when entry_type=increment. How much, in the customer's
              currency, a customer paid for a single credit in this block

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        entry_type: Literal["decrement"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        entry_type: Literal["expiration_change"],
        target_expiry_date: Union[str, date],
        amount: Optional[float] | Omit = omit,
        block_id: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          target_expiry_date: A future date (specified in YYYY-MM-DD format) used for expiration change,
              denoting when credits transferred (as part of a partial block expiration) should
              expire.

          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block affected by an expiration_change, used to differentiate
              between multiple blocks with the same `expiry_date`.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          expiry_date: An ISO 8601 format date that identifies the origination credit block to expire

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["void"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block to void.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          void_reason: Can only be specified when `entry_type=void`. The reason for the void.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement or void operations.

          block_id: The ID of the block to reverse a decrement from.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["amount", "entry_type"], ["entry_type", "target_expiry_date"], ["amount", "block_id", "entry_type"])
    def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float | Optional[float] | Omit = omit,
        entry_type: Literal["increment"]
        | Literal["decrement"]
        | Literal["expiration_change"]
        | Literal["void"]
        | Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[
            Iterable[ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsFilter]
        ]
        | Omit = omit,
        invoice_settings: Optional[
            ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings
        ]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        target_expiry_date: Union[str, date] | Omit = omit,
        block_id: Optional[str] | str | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return cast(
            LedgerCreateEntryByExternalIDResponse,
            self._post(
                f"/customers/external_customer_id/{external_customer_id}/credits/ledger_entry",
                body=maybe_transform(
                    {
                        "amount": amount,
                        "entry_type": entry_type,
                        "currency": currency,
                        "description": description,
                        "effective_date": effective_date,
                        "expiry_date": expiry_date,
                        "filters": filters,
                        "invoice_settings": invoice_settings,
                        "metadata": metadata,
                        "per_unit_cost_basis": per_unit_cost_basis,
                        "target_expiry_date": target_expiry_date,
                        "block_id": block_id,
                        "void_reason": void_reason,
                    },
                    ledger_create_entry_by_external_id_params.LedgerCreateEntryByExternalIDParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, LedgerCreateEntryByExternalIDResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        entry_status: Optional[Literal["committed", "pending"]] | Omit = omit,
        entry_type: Optional[
            Literal[
                "increment",
                "decrement",
                "expiration_change",
                "credit_block_expiry",
                "void",
                "void_initiated",
                "amendment",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        minimum_amount: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[LedgerListByExternalIDResponse]:
        """
        The credits ledger provides _auditing_ functionality over Orb's credits system
        with a list of actions that have taken place to modify a customer's credit
        balance. This [paginated endpoint](/api-reference/pagination) lists these
        entries, starting from the most recent ledger entry.

        More details on using Orb's real-time credit feature are
        [here](/product-catalog/prepurchase).

        There are four major types of modifications to credit balance, detailed below.

        ## Increment

        Credits (which optionally expire on a future date) can be added via the API
        ([Add Ledger Entry](create-ledger-entry)). The ledger entry for such an action
        will always contain the total eligible starting and ending balance for the
        customer at the time the entry was added to the ledger.

        ## Decrement

        Deductions can occur as a result of an API call to create a ledger entry (see
        [Add Ledger Entry](create-ledger-entry)), or automatically as a result of
        incurring usage. Both ledger entries present the `decrement` entry type.

        As usage for a customer is reported into Orb, credits may be deducted according
        to the customer's plan configuration. An automated deduction of this type will
        result in a ledger entry, also with a starting and ending balance. In order to
        provide better tracing capabilities for automatic deductions, Orb always
        associates each automatic deduction with the `event_id` at the time of
        ingestion, used to pinpoint _why_ credit deduction took place and to ensure that
        credits are never deducted without an associated usage event.

        By default, Orb uses an algorithm that automatically deducts from the _soonest
        expiring credit block_ first in order to ensure that all credits are utilized
        appropriately. As an example, if trial credits with an expiration date of 2
        weeks from now are present for a customer, they will be used before any
        deductions take place from a non-expiring credit block.

        If there are multiple blocks with the same expiration date, Orb will deduct from
        the block with the _lower cost basis_ first (e.g. trial credits with a \\$$0 cost
        basis before paid credits with a \\$$5.00 cost basis).

        It's also possible for a single usage event's deduction to _span_ credit blocks.
        In this case, Orb will deduct from the next block, ending at the credit block
        which consists of unexpiring credits. Each of these deductions will lead to a
        _separate_ ledger entry, one per credit block that is deducted from. By default,
        the customer's total credit balance in Orb can be negative as a result of a
        decrement.

        ## Expiration change

        The expiry of credits can be changed as a result of the API (See
        [Add Ledger Entry](create-ledger-entry)). This will create a ledger entry that
        specifies the balance as well as the initial and target expiry dates.

        Note that for this entry type, `starting_balance` will equal `ending_balance`,
        and the `amount` represents the balance transferred. The credit block linked to
        the ledger entry is the source credit block from which there was an expiration
        change.

        ## Credits expiry

        When a set of credits expire on pre-set expiration date, the customer's balance
        automatically reflects this change and adds an entry to the ledger indicating
        this event. Note that credit expiry should always happen close to a date
        boundary in the customer's timezone.

        ## Void initiated

        Credit blocks can be voided via the API. The `amount` on this entry corresponds
        to the number of credits that were remaining in the block at time of void.
        `void_reason` will be populated if the void is created with a reason.

        ## Void

        When a set of credits is voided, the customer's balance automatically reflects
        this change and adds an entry to the ledger indicating this event.

        ## Amendment

        When credits are added to a customer's balance as a result of a correction, this
        entry will be added to the ledger to indicate the adjustment of credits.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._get_api_list(
            f"/customers/external_customer_id/{external_customer_id}/credits/ledger",
            page=SyncPage[LedgerListByExternalIDResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "currency": currency,
                        "cursor": cursor,
                        "entry_status": entry_status,
                        "entry_type": entry_type,
                        "limit": limit,
                        "minimum_amount": minimum_amount,
                    },
                    ledger_list_by_external_id_params.LedgerListByExternalIDParams,
                ),
            ),
            model=cast(
                Any, LedgerListByExternalIDResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncLedger(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLedgerWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLedgerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLedgerWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncLedgerWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        entry_status: Optional[Literal["committed", "pending"]] | Omit = omit,
        entry_type: Optional[
            Literal[
                "increment",
                "decrement",
                "expiration_change",
                "credit_block_expiry",
                "void",
                "void_initiated",
                "amendment",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        minimum_amount: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LedgerListResponse, AsyncPage[LedgerListResponse]]:
        """
        The credits ledger provides _auditing_ functionality over Orb's credits system
        with a list of actions that have taken place to modify a customer's credit
        balance. This [paginated endpoint](/api-reference/pagination) lists these
        entries, starting from the most recent ledger entry.

        More details on using Orb's real-time credit feature are
        [here](/product-catalog/prepurchase).

        There are four major types of modifications to credit balance, detailed below.

        ## Increment

        Credits (which optionally expire on a future date) can be added via the API
        ([Add Ledger Entry](create-ledger-entry)). The ledger entry for such an action
        will always contain the total eligible starting and ending balance for the
        customer at the time the entry was added to the ledger.

        ## Decrement

        Deductions can occur as a result of an API call to create a ledger entry (see
        [Add Ledger Entry](create-ledger-entry)), or automatically as a result of
        incurring usage. Both ledger entries present the `decrement` entry type.

        As usage for a customer is reported into Orb, credits may be deducted according
        to the customer's plan configuration. An automated deduction of this type will
        result in a ledger entry, also with a starting and ending balance. In order to
        provide better tracing capabilities for automatic deductions, Orb always
        associates each automatic deduction with the `event_id` at the time of
        ingestion, used to pinpoint _why_ credit deduction took place and to ensure that
        credits are never deducted without an associated usage event.

        By default, Orb uses an algorithm that automatically deducts from the _soonest
        expiring credit block_ first in order to ensure that all credits are utilized
        appropriately. As an example, if trial credits with an expiration date of 2
        weeks from now are present for a customer, they will be used before any
        deductions take place from a non-expiring credit block.

        If there are multiple blocks with the same expiration date, Orb will deduct from
        the block with the _lower cost basis_ first (e.g. trial credits with a \\$$0 cost
        basis before paid credits with a \\$$5.00 cost basis).

        It's also possible for a single usage event's deduction to _span_ credit blocks.
        In this case, Orb will deduct from the next block, ending at the credit block
        which consists of unexpiring credits. Each of these deductions will lead to a
        _separate_ ledger entry, one per credit block that is deducted from. By default,
        the customer's total credit balance in Orb can be negative as a result of a
        decrement.

        ## Expiration change

        The expiry of credits can be changed as a result of the API (See
        [Add Ledger Entry](create-ledger-entry)). This will create a ledger entry that
        specifies the balance as well as the initial and target expiry dates.

        Note that for this entry type, `starting_balance` will equal `ending_balance`,
        and the `amount` represents the balance transferred. The credit block linked to
        the ledger entry is the source credit block from which there was an expiration
        change.

        ## Credits expiry

        When a set of credits expire on pre-set expiration date, the customer's balance
        automatically reflects this change and adds an entry to the ledger indicating
        this event. Note that credit expiry should always happen close to a date
        boundary in the customer's timezone.

        ## Void initiated

        Credit blocks can be voided via the API. The `amount` on this entry corresponds
        to the number of credits that were remaining in the block at time of void.
        `void_reason` will be populated if the void is created with a reason.

        ## Void

        When a set of credits is voided, the customer's balance automatically reflects
        this change and adds an entry to the ledger indicating this event.

        ## Amendment

        When credits are added to a customer's balance as a result of a correction, this
        entry will be added to the ledger to indicate the adjustment of credits.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/credits/ledger",
            page=AsyncPage[LedgerListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "currency": currency,
                        "cursor": cursor,
                        "entry_status": entry_status,
                        "entry_type": entry_type,
                        "limit": limit,
                        "minimum_amount": minimum_amount,
                    },
                    ledger_list_params.LedgerListParams,
                ),
            ),
            model=cast(Any, LedgerListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    @overload
    async def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        entry_type: Literal["increment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[Iterable[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsFilter]]
        | Omit = omit,
        invoice_settings: Optional[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          effective_date: An ISO 8601 format date that denotes when this credit balance should become
              available for use.

          expiry_date: An ISO 8601 format date that denotes when this credit balance should expire.

          filters: Optional filter to specify which items this credit block applies to. If not
              specified, the block will apply to all items for the pricing unit.

          invoice_settings: Passing `invoice_settings` automatically generates an invoice for the newly
              added credits. If `invoice_settings` is passed, you must specify
              per_unit_cost_basis, as the calculation of the invoice total is done on that
              basis.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          per_unit_cost_basis: Can only be specified when entry_type=increment. How much, in the customer's
              currency, a customer paid for a single credit in this block

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        entry_type: Literal["decrement"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry(
        self,
        customer_id: str,
        *,
        entry_type: Literal["expiration_change"],
        target_expiry_date: Union[str, date],
        amount: Optional[float] | Omit = omit,
        block_id: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          target_expiry_date: A future date (specified in YYYY-MM-DD format) used for expiration change,
              denoting when credits transferred (as part of a partial block expiration) should
              expire.

          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block affected by an expiration_change, used to differentiate
              between multiple blocks with the same `expiry_date`.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          expiry_date: An ISO 8601 format date that identifies the origination credit block to expire

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["void"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block to void.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          void_reason: Can only be specified when `entry_type=void`. The reason for the void.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry(
        self,
        customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement or void operations.

          block_id: The ID of the block to reverse a decrement from.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["amount", "entry_type"], ["entry_type", "target_expiry_date"], ["amount", "block_id", "entry_type"])
    async def create_entry(
        self,
        customer_id: str,
        *,
        amount: float | Optional[float] | Omit = omit,
        entry_type: Literal["increment"]
        | Literal["decrement"]
        | Literal["expiration_change"]
        | Literal["void"]
        | Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[Iterable[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsFilter]]
        | Omit = omit,
        invoice_settings: Optional[ledger_create_entry_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        target_expiry_date: Union[str, date] | Omit = omit,
        block_id: Optional[str] | str | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryResponse:
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return cast(
            LedgerCreateEntryResponse,
            await self._post(
                f"/customers/{customer_id}/credits/ledger_entry",
                body=await async_maybe_transform(
                    {
                        "amount": amount,
                        "entry_type": entry_type,
                        "currency": currency,
                        "description": description,
                        "effective_date": effective_date,
                        "expiry_date": expiry_date,
                        "filters": filters,
                        "invoice_settings": invoice_settings,
                        "metadata": metadata,
                        "per_unit_cost_basis": per_unit_cost_basis,
                        "target_expiry_date": target_expiry_date,
                        "block_id": block_id,
                        "void_reason": void_reason,
                    },
                    ledger_create_entry_params.LedgerCreateEntryParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, LedgerCreateEntryResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        entry_type: Literal["increment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[
            Iterable[ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsFilter]
        ]
        | Omit = omit,
        invoice_settings: Optional[
            ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings
        ]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          effective_date: An ISO 8601 format date that denotes when this credit balance should become
              available for use.

          expiry_date: An ISO 8601 format date that denotes when this credit balance should expire.

          filters: Optional filter to specify which items this credit block applies to. If not
              specified, the block will apply to all items for the pricing unit.

          invoice_settings: Passing `invoice_settings` automatically generates an invoice for the newly
              added credits. If `invoice_settings` is passed, you must specify
              per_unit_cost_basis, as the calculation of the invoice total is done on that
              basis.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          per_unit_cost_basis: Can only be specified when entry_type=increment. How much, in the customer's
              currency, a customer paid for a single credit in this block

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        entry_type: Literal["decrement"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        entry_type: Literal["expiration_change"],
        target_expiry_date: Union[str, date],
        amount: Optional[float] | Omit = omit,
        block_id: Optional[str] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          target_expiry_date: A future date (specified in YYYY-MM-DD format) used for expiration change,
              denoting when credits transferred (as part of a partial block expiration) should
              expire.

          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block affected by an expiration_change, used to differentiate
              between multiple blocks with the same `expiry_date`.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          expiry_date: An ISO 8601 format date that identifies the origination credit block to expire

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["void"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement, void, or undo operations.

          block_id: The ID of the block to void.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          void_reason: Can only be specified when `entry_type=void`. The reason for the void.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float,
        block_id: str,
        entry_type: Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        """
        This endpoint allows you to create a new ledger entry for a specified customer's
        balance. This can be used to increment balance, deduct credits, and change the
        expiry date of existing credits.

        ## Effects of adding a ledger entry

        1. After calling this endpoint, [Fetch Credit Balance](fetch-customer-credits)
           will return a credit block that represents the changes (i.e. balance changes
           or transfers).
        2. A ledger entry will be added to the credits ledger for this customer, and
           therefore returned in the
           [View Credits Ledger](fetch-customer-credits-ledger) response as well as
           serialized in the response to this request. In the case of deductions without
           a specified block, multiple ledger entries may be created if the deduction
           spans credit blocks.
        3. If `invoice_settings` is specified, an invoice will be created that reflects
           the cost of the credits (based on `amount` and `per_unit_cost_basis`).

        ## Adding credits

        Adding credits is done by creating an entry of type `increment`. This requires
        the caller to specify a number of credits as well as an optional expiry date in
        `YYYY-MM-DD` format. Orb also recommends specifying a description to assist with
        auditing. When adding credits, the caller can also specify a cost basis
        per-credit, to indicate how much in USD a customer paid for a single credit in a
        block. This can later be used for revenue recognition.

        The following snippet illustrates a sample request body to increment credits
        which will expire in January of 2022.

        ```json
        {
          "entry_type": "increment",
          "amount": 100,
          "expiry_date": "2022-12-28",
          "per_unit_cost_basis": "0.20",
          "description": "Purchased 100 credits"
        }
        ```

        Note that by default, Orb will always first increment any _negative_ balance in
        existing blocks before adding the remaining amount to the desired credit block.

        ### Invoicing for credits

        By default, Orb manipulates the credit ledger but does not charge for credits.
        However, if you pass `invoice_settings` in the body of this request, Orb will
        also generate a one-off invoice for the customer for the credits pre-purchase.
        Note that you _must_ provide the `per_unit_cost_basis`, since the total charges
        on the invoice are calculated by multiplying the cost basis with the number of
        credit units added.

        ## Deducting Credits

        Orb allows you to deduct credits from a customer by creating an entry of type
        `decrement`. Orb matches the algorithm for automatic deductions for determining
        which credit blocks to decrement from. In the case that the deduction leads to
        multiple ledger entries, the response from this endpoint will be the final
        deduction. Orb also optionally allows specifying a description to assist with
        auditing.

        The following snippet illustrates a sample request body to decrement credits.

        ```json
        {
          "entry_type": "decrement",
          "amount": 20,
          "description": "Removing excess credits"
        }
        ```

        ## Changing credits expiry

        If you'd like to change when existing credits expire, you should create a ledger
        entry of type `expiration_change`. For this entry, the required parameter
        `expiry_date` identifies the _originating_ block, and the required parameter
        `target_expiry_date` identifies when the transferred credits should now expire.
        A new credit block will be created with expiry date `target_expiry_date`, with
        the same cost basis data as the original credit block, if present.

        Note that the balance of the block with the given `expiry_date` must be at least
        equal to the desired transfer amount determined by the `amount` parameter.

        The following snippet illustrates a sample request body to extend the expiration
        date of credits by one year:

        ```json
        {
          "entry_type": "expiration_change",
          "amount": 10,
          "expiry_date": "2022-12-28",
          "block_id": "UiUhFWeLHPrBY4Ad",
          "target_expiry_date": "2023-12-28",
          "description": "Extending credit validity"
        }
        ```

        ## Voiding credits

        If you'd like to void a credit block, create a ledger entry of type `void`. For
        this entry, `block_id` is required to identify the block, and `amount` indicates
        how many credits to void, up to the block's initial balance. Pass in a
        `void_reason` of `refund` if the void is due to a refund.

        ## Amendment

        If you'd like to undo a decrement on a credit block, create a ledger entry of
        type `amendment`. For this entry, `block_id` is required to identify the block
        that was originally decremented from, and `amount` indicates how many credits to
        return to the customer, up to the block's initial balance.

        Args:
          amount: The number of credits to effect. Note that this is required for increment,
              decrement or void operations.

          block_id: The ID of the block to reverse a decrement from.

          currency: The currency or custom pricing unit to use for this ledger entry. If this is a
              real-world currency, it must match the customer's invoicing currency.

          description: Optional metadata that can be specified when adding ledger results via the API.
              For example, this can be used to note an increment refers to trial credits, or
              for noting corrections as a result of an incident, etc.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(["amount", "entry_type"], ["entry_type", "target_expiry_date"], ["amount", "block_id", "entry_type"])
    async def create_entry_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: float | Optional[float] | Omit = omit,
        entry_type: Literal["increment"]
        | Literal["decrement"]
        | Literal["expiration_change"]
        | Literal["void"]
        | Literal["amendment"],
        currency: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        effective_date: Union[str, datetime, None] | Omit = omit,
        expiry_date: Union[str, datetime, None] | Omit = omit,
        filters: Optional[
            Iterable[ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsFilter]
        ]
        | Omit = omit,
        invoice_settings: Optional[
            ledger_create_entry_by_external_id_params.AddIncrementCreditLedgerEntryRequestParamsInvoiceSettings
        ]
        | Omit = omit,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        per_unit_cost_basis: Optional[str] | Omit = omit,
        target_expiry_date: Union[str, date] | Omit = omit,
        block_id: Optional[str] | str | Omit = omit,
        void_reason: Optional[Literal["refund"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LedgerCreateEntryByExternalIDResponse:
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return cast(
            LedgerCreateEntryByExternalIDResponse,
            await self._post(
                f"/customers/external_customer_id/{external_customer_id}/credits/ledger_entry",
                body=await async_maybe_transform(
                    {
                        "amount": amount,
                        "entry_type": entry_type,
                        "currency": currency,
                        "description": description,
                        "effective_date": effective_date,
                        "expiry_date": expiry_date,
                        "filters": filters,
                        "invoice_settings": invoice_settings,
                        "metadata": metadata,
                        "per_unit_cost_basis": per_unit_cost_basis,
                        "target_expiry_date": target_expiry_date,
                        "block_id": block_id,
                        "void_reason": void_reason,
                    },
                    ledger_create_entry_by_external_id_params.LedgerCreateEntryByExternalIDParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, LedgerCreateEntryByExternalIDResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        currency: Optional[str] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        entry_status: Optional[Literal["committed", "pending"]] | Omit = omit,
        entry_type: Optional[
            Literal[
                "increment",
                "decrement",
                "expiration_change",
                "credit_block_expiry",
                "void",
                "void_initiated",
                "amendment",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        minimum_amount: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LedgerListByExternalIDResponse, AsyncPage[LedgerListByExternalIDResponse]]:
        """
        The credits ledger provides _auditing_ functionality over Orb's credits system
        with a list of actions that have taken place to modify a customer's credit
        balance. This [paginated endpoint](/api-reference/pagination) lists these
        entries, starting from the most recent ledger entry.

        More details on using Orb's real-time credit feature are
        [here](/product-catalog/prepurchase).

        There are four major types of modifications to credit balance, detailed below.

        ## Increment

        Credits (which optionally expire on a future date) can be added via the API
        ([Add Ledger Entry](create-ledger-entry)). The ledger entry for such an action
        will always contain the total eligible starting and ending balance for the
        customer at the time the entry was added to the ledger.

        ## Decrement

        Deductions can occur as a result of an API call to create a ledger entry (see
        [Add Ledger Entry](create-ledger-entry)), or automatically as a result of
        incurring usage. Both ledger entries present the `decrement` entry type.

        As usage for a customer is reported into Orb, credits may be deducted according
        to the customer's plan configuration. An automated deduction of this type will
        result in a ledger entry, also with a starting and ending balance. In order to
        provide better tracing capabilities for automatic deductions, Orb always
        associates each automatic deduction with the `event_id` at the time of
        ingestion, used to pinpoint _why_ credit deduction took place and to ensure that
        credits are never deducted without an associated usage event.

        By default, Orb uses an algorithm that automatically deducts from the _soonest
        expiring credit block_ first in order to ensure that all credits are utilized
        appropriately. As an example, if trial credits with an expiration date of 2
        weeks from now are present for a customer, they will be used before any
        deductions take place from a non-expiring credit block.

        If there are multiple blocks with the same expiration date, Orb will deduct from
        the block with the _lower cost basis_ first (e.g. trial credits with a \\$$0 cost
        basis before paid credits with a \\$$5.00 cost basis).

        It's also possible for a single usage event's deduction to _span_ credit blocks.
        In this case, Orb will deduct from the next block, ending at the credit block
        which consists of unexpiring credits. Each of these deductions will lead to a
        _separate_ ledger entry, one per credit block that is deducted from. By default,
        the customer's total credit balance in Orb can be negative as a result of a
        decrement.

        ## Expiration change

        The expiry of credits can be changed as a result of the API (See
        [Add Ledger Entry](create-ledger-entry)). This will create a ledger entry that
        specifies the balance as well as the initial and target expiry dates.

        Note that for this entry type, `starting_balance` will equal `ending_balance`,
        and the `amount` represents the balance transferred. The credit block linked to
        the ledger entry is the source credit block from which there was an expiration
        change.

        ## Credits expiry

        When a set of credits expire on pre-set expiration date, the customer's balance
        automatically reflects this change and adds an entry to the ledger indicating
        this event. Note that credit expiry should always happen close to a date
        boundary in the customer's timezone.

        ## Void initiated

        Credit blocks can be voided via the API. The `amount` on this entry corresponds
        to the number of credits that were remaining in the block at time of void.
        `void_reason` will be populated if the void is created with a reason.

        ## Void

        When a set of credits is voided, the customer's balance automatically reflects
        this change and adds an entry to the ledger indicating this event.

        ## Amendment

        When credits are added to a customer's balance as a result of a correction, this
        entry will be added to the ledger to indicate the adjustment of credits.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._get_api_list(
            f"/customers/external_customer_id/{external_customer_id}/credits/ledger",
            page=AsyncPage[LedgerListByExternalIDResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "currency": currency,
                        "cursor": cursor,
                        "entry_status": entry_status,
                        "entry_type": entry_type,
                        "limit": limit,
                        "minimum_amount": minimum_amount,
                    },
                    ledger_list_by_external_id_params.LedgerListByExternalIDParams,
                ),
            ),
            model=cast(
                Any, LedgerListByExternalIDResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class LedgerWithRawResponse:
    def __init__(self, ledger: Ledger) -> None:
        self._ledger = ledger

        self.list = _legacy_response.to_raw_response_wrapper(
            ledger.list,
        )
        self.create_entry = _legacy_response.to_raw_response_wrapper(
            ledger.create_entry,
        )
        self.create_entry_by_external_id = _legacy_response.to_raw_response_wrapper(
            ledger.create_entry_by_external_id,
        )
        self.list_by_external_id = _legacy_response.to_raw_response_wrapper(
            ledger.list_by_external_id,
        )


class AsyncLedgerWithRawResponse:
    def __init__(self, ledger: AsyncLedger) -> None:
        self._ledger = ledger

        self.list = _legacy_response.async_to_raw_response_wrapper(
            ledger.list,
        )
        self.create_entry = _legacy_response.async_to_raw_response_wrapper(
            ledger.create_entry,
        )
        self.create_entry_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            ledger.create_entry_by_external_id,
        )
        self.list_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            ledger.list_by_external_id,
        )


class LedgerWithStreamingResponse:
    def __init__(self, ledger: Ledger) -> None:
        self._ledger = ledger

        self.list = to_streamed_response_wrapper(
            ledger.list,
        )
        self.create_entry = to_streamed_response_wrapper(
            ledger.create_entry,
        )
        self.create_entry_by_external_id = to_streamed_response_wrapper(
            ledger.create_entry_by_external_id,
        )
        self.list_by_external_id = to_streamed_response_wrapper(
            ledger.list_by_external_id,
        )


class AsyncLedgerWithStreamingResponse:
    def __init__(self, ledger: AsyncLedger) -> None:
        self._ledger = ledger

        self.list = async_to_streamed_response_wrapper(
            ledger.list,
        )
        self.create_entry = async_to_streamed_response_wrapper(
            ledger.create_entry,
        )
        self.create_entry_by_external_id = async_to_streamed_response_wrapper(
            ledger.create_entry_by_external_id,
        )
        self.list_by_external_id = async_to_streamed_response_wrapper(
            ledger.list_by_external_id,
        )
