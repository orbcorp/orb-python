# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from .. import _legacy_response
from ..types import invoice_line_item_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.invoice_line_item_create_response import InvoiceLineItemCreateResponse

__all__ = ["InvoiceLineItems", "AsyncInvoiceLineItems"]


class InvoiceLineItems(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoiceLineItemsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return InvoiceLineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoiceLineItemsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return InvoiceLineItemsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: str,
        end_date: Union[str, date],
        invoice_id: str,
        quantity: float,
        start_date: Union[str, date],
        item_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItemCreateResponse:
        """This creates a one-off fixed fee invoice line item on an Invoice.

        This can only
        be done for invoices that are in a `draft` status.

        The behavior depends on which parameters are provided:

        - If `item_id` is provided without `name`: The item is looked up by ID, and the
          item's name is used for the line item.
        - If `name` is provided without `item_id`: An item with the given name is
          searched for in the account. If found, that item is used. If not found, a new
          item is created with that name. The new item's name is used for the line item.
        - If both `item_id` and `name` are provided: The item is looked up by ID for
          association, but the provided `name` is used for the line item (not the item's
          name).

        Args:
          amount: The total amount in the invoice's currency to add to the line item.

          end_date: A date string to specify the line item's end date in the customer's timezone.

          invoice_id: The id of the Invoice to add this line item.

          quantity: The number of units on the line item

          start_date: A date string to specify the line item's start date in the customer's timezone.

          item_id: The id of the item to associate with this line item. If provided without `name`,
              the item's name will be used for the price/line item. If provided with `name`,
              the item will be associated but `name` will be used for the line item. At least
              one of `name` or `item_id` must be provided.

          name: The name to use for the line item. If `item_id` is not provided, Orb will search
              for an item with this name. If found, that item will be associated with the line
              item. If not found, a new item will be created with this name. If `item_id` is
              provided, this name will be used for the line item, but the item association
              will be based on `item_id`. At least one of `name` or `item_id` must be
              provided.

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
                    "quantity": quantity,
                    "start_date": start_date,
                    "item_id": item_id,
                    "name": name,
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
    @cached_property
    def with_raw_response(self) -> AsyncInvoiceLineItemsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoiceLineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoiceLineItemsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncInvoiceLineItemsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: str,
        end_date: Union[str, date],
        invoice_id: str,
        quantity: float,
        start_date: Union[str, date],
        item_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> InvoiceLineItemCreateResponse:
        """This creates a one-off fixed fee invoice line item on an Invoice.

        This can only
        be done for invoices that are in a `draft` status.

        The behavior depends on which parameters are provided:

        - If `item_id` is provided without `name`: The item is looked up by ID, and the
          item's name is used for the line item.
        - If `name` is provided without `item_id`: An item with the given name is
          searched for in the account. If found, that item is used. If not found, a new
          item is created with that name. The new item's name is used for the line item.
        - If both `item_id` and `name` are provided: The item is looked up by ID for
          association, but the provided `name` is used for the line item (not the item's
          name).

        Args:
          amount: The total amount in the invoice's currency to add to the line item.

          end_date: A date string to specify the line item's end date in the customer's timezone.

          invoice_id: The id of the Invoice to add this line item.

          quantity: The number of units on the line item

          start_date: A date string to specify the line item's start date in the customer's timezone.

          item_id: The id of the item to associate with this line item. If provided without `name`,
              the item's name will be used for the price/line item. If provided with `name`,
              the item will be associated but `name` will be used for the line item. At least
              one of `name` or `item_id` must be provided.

          name: The name to use for the line item. If `item_id` is not provided, Orb will search
              for an item with this name. If found, that item will be associated with the line
              item. If not found, a new item will be created with this name. If `item_id` is
              provided, this name will be used for the line item, but the item association
              will be based on `item_id`. At least one of `name` or `item_id` must be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/invoice_line_items",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "end_date": end_date,
                    "invoice_id": invoice_id,
                    "quantity": quantity,
                    "start_date": start_date,
                    "item_id": item_id,
                    "name": name,
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
        self._invoice_line_items = invoice_line_items

        self.create = _legacy_response.to_raw_response_wrapper(
            invoice_line_items.create,
        )


class AsyncInvoiceLineItemsWithRawResponse:
    def __init__(self, invoice_line_items: AsyncInvoiceLineItems) -> None:
        self._invoice_line_items = invoice_line_items

        self.create = _legacy_response.async_to_raw_response_wrapper(
            invoice_line_items.create,
        )


class InvoiceLineItemsWithStreamingResponse:
    def __init__(self, invoice_line_items: InvoiceLineItems) -> None:
        self._invoice_line_items = invoice_line_items

        self.create = to_streamed_response_wrapper(
            invoice_line_items.create,
        )


class AsyncInvoiceLineItemsWithStreamingResponse:
    def __init__(self, invoice_line_items: AsyncInvoiceLineItems) -> None:
        self._invoice_line_items = invoice_line_items

        self.create = async_to_streamed_response_wrapper(
            invoice_line_items.create,
        )
