# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import date

import httpx

from ..types import InvoiceLineItemCreateResponse, invoice_line_item_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Orb, AsyncOrb

__all__ = ["InvoiceLineItems", "AsyncInvoiceLineItems"]


class InvoiceLineItems(SyncAPIResource):
    with_raw_response: InvoiceLineItemsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = InvoiceLineItemsWithRawResponse(self)

    def create(
        self,
        *,
        amount: str,
        end_date: Union[str, date],
        invoice_id: str,
        name: str,
        quantity: float,
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItemCreateResponse:
        """This creates a one-off fixed fee invoice line item on an Invoice.

        This can only
        be done for invoices that are in a `draft` status.

        Args:
          amount: The total amount in the invoice's currency to add to the line item.

          end_date: A date string to specify the line item's end date in the customer's timezone.

          invoice_id: The id of the Invoice to add this line item.

          name: The item name associated with this line item. If an item with the same name
              exists in Orb, that item will be associated with the line item.

          quantity: The number of units on the line item

          start_date: A date string to specify the line item's start date in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/invoice_line_items",
            body=maybe_transform(
                {
                    "amount": amount,
                    "end_date": end_date,
                    "invoice_id": invoice_id,
                    "name": name,
                    "quantity": quantity,
                    "start_date": start_date,
                },
                invoice_line_item_create_params.InvoiceLineItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InvoiceLineItemCreateResponse,
        )


class AsyncInvoiceLineItems(AsyncAPIResource):
    with_raw_response: AsyncInvoiceLineItemsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncInvoiceLineItemsWithRawResponse(self)

    async def create(
        self,
        *,
        amount: str,
        end_date: Union[str, date],
        invoice_id: str,
        name: str,
        quantity: float,
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItemCreateResponse:
        """This creates a one-off fixed fee invoice line item on an Invoice.

        This can only
        be done for invoices that are in a `draft` status.

        Args:
          amount: The total amount in the invoice's currency to add to the line item.

          end_date: A date string to specify the line item's end date in the customer's timezone.

          invoice_id: The id of the Invoice to add this line item.

          name: The item name associated with this line item. If an item with the same name
              exists in Orb, that item will be associated with the line item.

          quantity: The number of units on the line item

          start_date: A date string to specify the line item's start date in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/invoice_line_items",
            body=maybe_transform(
                {
                    "amount": amount,
                    "end_date": end_date,
                    "invoice_id": invoice_id,
                    "name": name,
                    "quantity": quantity,
                    "start_date": start_date,
                },
                invoice_line_item_create_params.InvoiceLineItemCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=InvoiceLineItemCreateResponse,
        )


class InvoiceLineItemsWithRawResponse:
    def __init__(self, invoice_line_items: InvoiceLineItems) -> None:
        self.create = to_raw_response_wrapper(
            invoice_line_items.create,
        )


class AsyncInvoiceLineItemsWithRawResponse:
    def __init__(self, invoice_line_items: AsyncInvoiceLineItems) -> None:
        self.create = async_to_raw_response_wrapper(
            invoice_line_items.create,
        )
