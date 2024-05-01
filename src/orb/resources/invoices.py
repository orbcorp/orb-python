# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    invoice_list_params,
    invoice_create_params,
    invoice_mark_paid_params,
    invoice_fetch_upcoming_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.invoice import Invoice
from ..types.invoice_fetch_upcoming_response import InvoiceFetchUpcomingResponse

__all__ = ["Invoices", "AsyncInvoices"]


class Invoices(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesWithRawResponse:
        return InvoicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesWithStreamingResponse:
        return InvoicesWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: str,
        invoice_date: Union[str, datetime],
        line_items: Iterable[invoice_create_params.LineItem],
        net_terms: int,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        memo: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        will_auto_issue: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        This endpoint is used to create a one-off invoice for a customer.

        Args:
          currency: An ISO 4217 currency string. Must be the same as the customer's currency if it
              is set.

          invoice_date: Optional invoice date to set. Must be in the past, if not set, `invoice_date` is
              set to the current time in the customer's timezone.

          net_terms: Determines the difference between the invoice issue date for subscription
              invoices as the date that they are due. A value of '0' here represents that the
              invoice is due on issue, whereas a value of 30 represents that the customer has
              30 days to pay the invoice.

          customer_id: The id of the `Customer` to create this invoice for. One of `customer_id` and
              `external_customer_id` are required.

          external_customer_id: The `external_customer_id` of the `Customer` to create this invoice for. One of
              `customer_id` and `external_customer_id` are required.

          memo: An optional memo to attach to the invoice.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          will_auto_issue: When true, this invoice will automatically be issued upon creation. When false,
              the resulting invoice will require manual review to issue. Defaulted to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/invoices",
            body=maybe_transform(
                {
                    "currency": currency,
                    "invoice_date": invoice_date,
                    "line_items": line_items,
                    "net_terms": net_terms,
                    "customer_id": customer_id,
                    "external_customer_id": external_customer_id,
                    "memo": memo,
                    "metadata": metadata,
                    "will_auto_issue": will_auto_issue,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        amount: Optional[str] | NotGiven = NOT_GIVEN,
        amount_gt: Optional[str] | NotGiven = NOT_GIVEN,
        amount_lt: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        date_type: Optional[Literal["due_date", "invoice_date"]] | NotGiven = NOT_GIVEN,
        due_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        due_date_window: Optional[str] | NotGiven = NOT_GIVEN,
        due_date_gt: Union[str, date, None] | NotGiven = NOT_GIVEN,
        due_date_lt: Union[str, date, None] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        invoice_date_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        invoice_date_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        invoice_date_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        invoice_date_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        is_recurring: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Optional[List[Literal["draft", "issued", "paid", "synced", "void"]]] | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Invoice]:
        """
        This endpoint returns a list of all [`Invoice`](../guides/concepts#invoice)s for
        an account in a list format.

        The list of invoices is ordered starting from the most recently issued invoice
        date. The response also includes
        [`pagination_metadata`](../reference/pagination), which lets the caller retrieve
        the next page of results if they exist.

        By default, this only returns invoices that are `issued`, `paid`, or `synced`.

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
            "/invoices",
            page=SyncPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "amount": amount,
                        "amount_gt": amount_gt,
                        "amount_lt": amount_lt,
                        "cursor": cursor,
                        "customer_id": customer_id,
                        "date_type": date_type,
                        "due_date": due_date,
                        "due_date_window": due_date_window,
                        "due_date_gt": due_date_gt,
                        "due_date_lt": due_date_lt,
                        "external_customer_id": external_customer_id,
                        "invoice_date_gt": invoice_date_gt,
                        "invoice_date_gte": invoice_date_gte,
                        "invoice_date_lt": invoice_date_lt,
                        "invoice_date_lte": invoice_date_lte,
                        "is_recurring": is_recurring,
                        "limit": limit,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    def fetch(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invoice:
        """
        This endpoint is used to fetch an [`Invoice`](../guides/concepts#invoice) given
        an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get(
            f"/invoices/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    def fetch_upcoming(
        self,
        *,
        subscription_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceFetchUpcomingResponse:
        """
        This endpoint can be used to fetch the upcoming
        [invoice](../guides/concepts#invoice) for the current billing period given a
        subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/invoices/upcoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"subscription_id": subscription_id}, invoice_fetch_upcoming_params.InvoiceFetchUpcomingParams
                ),
            ),
            cast_to=InvoiceFetchUpcomingResponse,
        )

    def issue(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """This endpoint allows an eligible invoice to be issued manually.

        This is only
        possible with invoices where status is `draft`, `will_auto_issue` is false, and
        an `eligible_to_issue_at` is a time in the past. Issuing an invoice could
        possibly trigger side effects, some of which could be customer-visible (e.g.
        sending emails, auto-collecting payment, syncing the invoice to external
        providers, etc).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            f"/invoices/{invoice_id}/issue",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def mark_paid(
        self,
        invoice_id: str,
        *,
        payment_received_date: Union[str, date],
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """This endpoint allows an invoice's status to be set the `paid` status.

        This can
        only be done to invoices that are in the `issued` status.

        Args:
          payment_received_date: A date string to specify the date of the payment.

          external_id: An optional external ID to associate with the payment.

          notes: An optional note to associate with the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            f"/invoices/{invoice_id}/mark_paid",
            body=maybe_transform(
                {
                    "payment_received_date": payment_received_date,
                    "external_id": external_id,
                    "notes": notes,
                },
                invoice_mark_paid_params.InvoiceMarkPaidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def void(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """This endpoint allows an invoice's status to be set the `void` status.

        This can
        only be done to invoices that are in the `issued` status.

        If the associated invoice has used the customer balance to change the amount
        due, the customer balance operation will be reverted. For example, if the
        invoice used $10 of customer balance, that amount will be added back to the
        customer balance upon voiding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._post(
            f"/invoices/{invoice_id}/void",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )


class AsyncInvoices(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesWithRawResponse:
        return AsyncInvoicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesWithStreamingResponse:
        return AsyncInvoicesWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: str,
        invoice_date: Union[str, datetime],
        line_items: Iterable[invoice_create_params.LineItem],
        net_terms: int,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        memo: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        will_auto_issue: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """
        This endpoint is used to create a one-off invoice for a customer.

        Args:
          currency: An ISO 4217 currency string. Must be the same as the customer's currency if it
              is set.

          invoice_date: Optional invoice date to set. Must be in the past, if not set, `invoice_date` is
              set to the current time in the customer's timezone.

          net_terms: Determines the difference between the invoice issue date for subscription
              invoices as the date that they are due. A value of '0' here represents that the
              invoice is due on issue, whereas a value of 30 represents that the customer has
              30 days to pay the invoice.

          customer_id: The id of the `Customer` to create this invoice for. One of `customer_id` and
              `external_customer_id` are required.

          external_customer_id: The `external_customer_id` of the `Customer` to create this invoice for. One of
              `customer_id` and `external_customer_id` are required.

          memo: An optional memo to attach to the invoice.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          will_auto_issue: When true, this invoice will automatically be issued upon creation. When false,
              the resulting invoice will require manual review to issue. Defaulted to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/invoices",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "invoice_date": invoice_date,
                    "line_items": line_items,
                    "net_terms": net_terms,
                    "customer_id": customer_id,
                    "external_customer_id": external_customer_id,
                    "memo": memo,
                    "metadata": metadata,
                    "will_auto_issue": will_auto_issue,
                },
                invoice_create_params.InvoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    def list(
        self,
        *,
        amount: Optional[str] | NotGiven = NOT_GIVEN,
        amount_gt: Optional[str] | NotGiven = NOT_GIVEN,
        amount_lt: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        date_type: Optional[Literal["due_date", "invoice_date"]] | NotGiven = NOT_GIVEN,
        due_date: Union[str, date, None] | NotGiven = NOT_GIVEN,
        due_date_window: Optional[str] | NotGiven = NOT_GIVEN,
        due_date_gt: Union[str, date, None] | NotGiven = NOT_GIVEN,
        due_date_lt: Union[str, date, None] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        invoice_date_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        invoice_date_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        invoice_date_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        invoice_date_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        is_recurring: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Optional[List[Literal["draft", "issued", "paid", "synced", "void"]]] | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Invoice, AsyncPage[Invoice]]:
        """
        This endpoint returns a list of all [`Invoice`](../guides/concepts#invoice)s for
        an account in a list format.

        The list of invoices is ordered starting from the most recently issued invoice
        date. The response also includes
        [`pagination_metadata`](../reference/pagination), which lets the caller retrieve
        the next page of results if they exist.

        By default, this only returns invoices that are `issued`, `paid`, or `synced`.

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
            "/invoices",
            page=AsyncPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "amount": amount,
                        "amount_gt": amount_gt,
                        "amount_lt": amount_lt,
                        "cursor": cursor,
                        "customer_id": customer_id,
                        "date_type": date_type,
                        "due_date": due_date,
                        "due_date_window": due_date_window,
                        "due_date_gt": due_date_gt,
                        "due_date_lt": due_date_lt,
                        "external_customer_id": external_customer_id,
                        "invoice_date_gt": invoice_date_gt,
                        "invoice_date_gte": invoice_date_gte,
                        "invoice_date_lt": invoice_date_lt,
                        "invoice_date_lte": invoice_date_lte,
                        "is_recurring": is_recurring,
                        "limit": limit,
                        "status": status,
                        "subscription_id": subscription_id,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    async def fetch(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Invoice:
        """
        This endpoint is used to fetch an [`Invoice`](../guides/concepts#invoice) given
        an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._get(
            f"/invoices/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Invoice,
        )

    async def fetch_upcoming(
        self,
        *,
        subscription_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceFetchUpcomingResponse:
        """
        This endpoint can be used to fetch the upcoming
        [invoice](../guides/concepts#invoice) for the current billing period given a
        subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/invoices/upcoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"subscription_id": subscription_id}, invoice_fetch_upcoming_params.InvoiceFetchUpcomingParams
                ),
            ),
            cast_to=InvoiceFetchUpcomingResponse,
        )

    async def issue(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """This endpoint allows an eligible invoice to be issued manually.

        This is only
        possible with invoices where status is `draft`, `will_auto_issue` is false, and
        an `eligible_to_issue_at` is a time in the past. Issuing an invoice could
        possibly trigger side effects, some of which could be customer-visible (e.g.
        sending emails, auto-collecting payment, syncing the invoice to external
        providers, etc).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            f"/invoices/{invoice_id}/issue",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    async def mark_paid(
        self,
        invoice_id: str,
        *,
        payment_received_date: Union[str, date],
        external_id: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """This endpoint allows an invoice's status to be set the `paid` status.

        This can
        only be done to invoices that are in the `issued` status.

        Args:
          payment_received_date: A date string to specify the date of the payment.

          external_id: An optional external ID to associate with the payment.

          notes: An optional note to associate with the payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            f"/invoices/{invoice_id}/mark_paid",
            body=await async_maybe_transform(
                {
                    "payment_received_date": payment_received_date,
                    "external_id": external_id,
                    "notes": notes,
                },
                invoice_mark_paid_params.InvoiceMarkPaidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )

    async def void(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Invoice:
        """This endpoint allows an invoice's status to be set the `void` status.

        This can
        only be done to invoices that are in the `issued` status.

        If the associated invoice has used the customer balance to change the amount
        due, the customer balance operation will be reverted. For example, if the
        invoice used $10 of customer balance, that amount will be added back to the
        customer balance upon voiding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._post(
            f"/invoices/{invoice_id}/void",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Invoice,
        )


class InvoicesWithRawResponse:
    def __init__(self, invoices: Invoices) -> None:
        self._invoices = invoices

        self.create = _legacy_response.to_raw_response_wrapper(
            invoices.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            invoices.list,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            invoices.fetch,
        )
        self.fetch_upcoming = _legacy_response.to_raw_response_wrapper(
            invoices.fetch_upcoming,
        )
        self.issue = _legacy_response.to_raw_response_wrapper(
            invoices.issue,
        )
        self.mark_paid = _legacy_response.to_raw_response_wrapper(
            invoices.mark_paid,
        )
        self.void = _legacy_response.to_raw_response_wrapper(
            invoices.void,
        )


class AsyncInvoicesWithRawResponse:
    def __init__(self, invoices: AsyncInvoices) -> None:
        self._invoices = invoices

        self.create = _legacy_response.async_to_raw_response_wrapper(
            invoices.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            invoices.list,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            invoices.fetch,
        )
        self.fetch_upcoming = _legacy_response.async_to_raw_response_wrapper(
            invoices.fetch_upcoming,
        )
        self.issue = _legacy_response.async_to_raw_response_wrapper(
            invoices.issue,
        )
        self.mark_paid = _legacy_response.async_to_raw_response_wrapper(
            invoices.mark_paid,
        )
        self.void = _legacy_response.async_to_raw_response_wrapper(
            invoices.void,
        )


class InvoicesWithStreamingResponse:
    def __init__(self, invoices: Invoices) -> None:
        self._invoices = invoices

        self.create = to_streamed_response_wrapper(
            invoices.create,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.fetch = to_streamed_response_wrapper(
            invoices.fetch,
        )
        self.fetch_upcoming = to_streamed_response_wrapper(
            invoices.fetch_upcoming,
        )
        self.issue = to_streamed_response_wrapper(
            invoices.issue,
        )
        self.mark_paid = to_streamed_response_wrapper(
            invoices.mark_paid,
        )
        self.void = to_streamed_response_wrapper(
            invoices.void,
        )


class AsyncInvoicesWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoices) -> None:
        self._invoices = invoices

        self.create = async_to_streamed_response_wrapper(
            invoices.create,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            invoices.fetch,
        )
        self.fetch_upcoming = async_to_streamed_response_wrapper(
            invoices.fetch_upcoming,
        )
        self.issue = async_to_streamed_response_wrapper(
            invoices.issue,
        )
        self.mark_paid = async_to_streamed_response_wrapper(
            invoices.mark_paid,
        )
        self.void = async_to_streamed_response_wrapper(
            invoices.void,
        )
