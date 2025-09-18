# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.customers import balance_transaction_list_params, balance_transaction_create_params
from ...types.customers.balance_transaction_list_response import BalanceTransactionListResponse
from ...types.customers.balance_transaction_create_response import BalanceTransactionCreateResponse

__all__ = ["BalanceTransactions", "AsyncBalanceTransactions"]


class BalanceTransactions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalanceTransactionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return BalanceTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalanceTransactionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return BalanceTransactionsWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        amount: str,
        type: Literal["increment", "decrement"],
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        operation_time_gt: Union[str, datetime, None] | Omit = omit,
        operation_time_gte: Union[str, datetime, None] | Omit = omit,
        operation_time_lt: Union[str, datetime, None] | Omit = omit,
        operation_time_lte: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

        Args:
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
    @cached_property
    def with_raw_response(self) -> AsyncBalanceTransactionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalanceTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalanceTransactionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncBalanceTransactionsWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        amount: str,
        type: Literal["increment", "decrement"],
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/customers/{customer_id}/balance_transactions",
            body=await async_maybe_transform(
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
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        operation_time_gt: Union[str, datetime, None] | Omit = omit,
        operation_time_gte: Union[str, datetime, None] | Omit = omit,
        operation_time_lt: Union[str, datetime, None] | Omit = omit,
        operation_time_lte: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

        Args:
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
        self._balance_transactions = balance_transactions

        self.create = _legacy_response.to_raw_response_wrapper(
            balance_transactions.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            balance_transactions.list,
        )


class AsyncBalanceTransactionsWithRawResponse:
    def __init__(self, balance_transactions: AsyncBalanceTransactions) -> None:
        self._balance_transactions = balance_transactions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            balance_transactions.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            balance_transactions.list,
        )


class BalanceTransactionsWithStreamingResponse:
    def __init__(self, balance_transactions: BalanceTransactions) -> None:
        self._balance_transactions = balance_transactions

        self.create = to_streamed_response_wrapper(
            balance_transactions.create,
        )
        self.list = to_streamed_response_wrapper(
            balance_transactions.list,
        )


class AsyncBalanceTransactionsWithStreamingResponse:
    def __init__(self, balance_transactions: AsyncBalanceTransactions) -> None:
        self._balance_transactions = balance_transactions

        self.create = async_to_streamed_response_wrapper(
            balance_transactions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            balance_transactions.list,
        )
