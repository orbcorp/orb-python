# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.customers import (
    BalanceTransactionListResponse,
    BalanceTransactionCreateResponse,
    balance_transaction_list_params,
    balance_transaction_create_params,
)

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["BalanceTransactions", "AsyncBalanceTransactions"]


class BalanceTransactions(SyncAPIResource):
    with_raw_response: BalanceTransactionsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = BalanceTransactionsWithRawResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        amount: str,
        type: Literal["increment", "decrement"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BalanceTransactionCreateResponse:
        """
        Creates an immutable balance transaction that updates the customer's balance and
        returns back the newly created transaction.

        Args:
          description: An optional description that can be specified around this entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/customers/{customer_id}/balance_transactions",
            body=maybe_transform(
                {
                    "amount": amount,
                    "type": type,
                    "description": description,
                },
                balance_transaction_create_params.BalanceTransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BalanceTransactionCreateResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        operation_time_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        operation_time_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        operation_time_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        operation_time_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[BalanceTransactionListResponse]:
        """
        ## The customer balance

        The customer balance is an amount in the customer's currency, which Orb
        automatically applies to subsequent invoices. This balance can be adjusted
        manually via Orb's webapp on the customer details page. You can use this balance
        to provide a fixed mid-period credit to the customer. Commonly, this is done due
        to system downtime/SLA violation, or an adhoc adjustment discussed with the
        customer.

        If the balance is a positive value at the time of invoicing, it represents that
        the customer has credit that should be used to offset the amount due on the next
        issued invoice. In this case, Orb will automatically reduce the next invoice by
        the balance amount, and roll over any remaining balance if the invoice is fully
        discounted.

        If the balance is a negative value at the time of invoicing, Orb will increase
        the invoice's amount due with a positive adjustment, and reset the balance to 0.

        This endpoint retrieves all customer balance transactions in reverse
        chronological order for a single customer, providing a complete audit trail of
        all adjustments and invoice applications.

        ## Eligibility

        The customer balance can only be applied to invoices or adjusted manually if
        invoices are not synced to a separate invoicing provider. If a payment gateway
        such as Stripe is used, the balance will be applied to the invoice before
        forwarding payment to the gateway.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/customers/{customer_id}/balance_transactions",
            page=SyncPage[BalanceTransactionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "operation_time_gt": operation_time_gt,
                        "operation_time_gte": operation_time_gte,
                        "operation_time_lt": operation_time_lt,
                        "operation_time_lte": operation_time_lte,
                    },
                    balance_transaction_list_params.BalanceTransactionListParams,
                ),
            ),
            model=BalanceTransactionListResponse,
        )


class AsyncBalanceTransactions(AsyncAPIResource):
    with_raw_response: AsyncBalanceTransactionsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncBalanceTransactionsWithRawResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        amount: str,
        type: Literal["increment", "decrement"],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> BalanceTransactionCreateResponse:
        """
        Creates an immutable balance transaction that updates the customer's balance and
        returns back the newly created transaction.

        Args:
          description: An optional description that can be specified around this entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/customers/{customer_id}/balance_transactions",
            body=maybe_transform(
                {
                    "amount": amount,
                    "type": type,
                    "description": description,
                },
                balance_transaction_create_params.BalanceTransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BalanceTransactionCreateResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        operation_time_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        operation_time_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        operation_time_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        operation_time_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BalanceTransactionListResponse, AsyncPage[BalanceTransactionListResponse]]:
        """
        ## The customer balance

        The customer balance is an amount in the customer's currency, which Orb
        automatically applies to subsequent invoices. This balance can be adjusted
        manually via Orb's webapp on the customer details page. You can use this balance
        to provide a fixed mid-period credit to the customer. Commonly, this is done due
        to system downtime/SLA violation, or an adhoc adjustment discussed with the
        customer.

        If the balance is a positive value at the time of invoicing, it represents that
        the customer has credit that should be used to offset the amount due on the next
        issued invoice. In this case, Orb will automatically reduce the next invoice by
        the balance amount, and roll over any remaining balance if the invoice is fully
        discounted.

        If the balance is a negative value at the time of invoicing, Orb will increase
        the invoice's amount due with a positive adjustment, and reset the balance to 0.

        This endpoint retrieves all customer balance transactions in reverse
        chronological order for a single customer, providing a complete audit trail of
        all adjustments and invoice applications.

        ## Eligibility

        The customer balance can only be applied to invoices or adjusted manually if
        invoices are not synced to a separate invoicing provider. If a payment gateway
        such as Stripe is used, the balance will be applied to the invoice before
        forwarding payment to the gateway.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/customers/{customer_id}/balance_transactions",
            page=AsyncPage[BalanceTransactionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "operation_time_gt": operation_time_gt,
                        "operation_time_gte": operation_time_gte,
                        "operation_time_lt": operation_time_lt,
                        "operation_time_lte": operation_time_lte,
                    },
                    balance_transaction_list_params.BalanceTransactionListParams,
                ),
            ),
            model=BalanceTransactionListResponse,
        )


class BalanceTransactionsWithRawResponse:
    def __init__(self, balance_transactions: BalanceTransactions) -> None:
        self.create = to_raw_response_wrapper(
            balance_transactions.create,
        )
        self.list = to_raw_response_wrapper(
            balance_transactions.list,
        )


class AsyncBalanceTransactionsWithRawResponse:
    def __init__(self, balance_transactions: AsyncBalanceTransactions) -> None:
        self.create = async_to_raw_response_wrapper(
            balance_transactions.create,
        )
        self.list = async_to_raw_response_wrapper(
            balance_transactions.list,
        )
