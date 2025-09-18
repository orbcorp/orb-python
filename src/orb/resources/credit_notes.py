# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import credit_note_list_params, credit_note_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.credit_note import CreditNote

__all__ = ["CreditNotes", "AsyncCreditNotes"]


class CreditNotes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditNotesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return CreditNotesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditNotesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return CreditNotesWithStreamingResponse(self)

    def create(
        self,
        *,
        line_items: Iterable[credit_note_create_params.LineItem],
        reason: Literal["duplicate", "fraudulent", "order_change", "product_unsatisfactory"],
        end_date: Union[str, date, None] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CreditNote:
        """
        This endpoint is used to create a single
        [`Credit Note`](/invoicing/credit-notes).

        The credit note service period configuration supports two explicit modes:

        1. Global service periods: Specify start_date and end_date at the credit note
           level. These dates will be applied to all line items uniformly.

        2. Individual service periods: Specify start_date and end_date for each line
           item. When using this mode, ALL line items must have individual periods
           specified.

        3. Default behavior: If no service periods are specified (neither global nor
           individual), the original invoice line item service periods will be used.

        Note: Mixing global and individual service periods in the same request is not
        allowed to prevent confusion.

        Service period dates are normalized to the start of the day in the customer's
        timezone to ensure consistent handling across different timezones.

        Date Format: Use start_date and end_date with format "YYYY-MM-DD" (e.g.,
        "2023-09-22") to match other Orb APIs like /v1/invoice_line_items.

        Note: Both start_date and end_date are inclusive - the service period will cover
        both the start date and end date completely (from start of start_date to end of
        end_date).

        Args:
          reason: An optional reason for the credit note.

          end_date: A date string to specify the global credit note service period end date in the
              customer's timezone. This will be applied to all line items that don't have
              their own individual service periods specified. If not provided, line items will
              use their original invoice line item service periods. This date is inclusive.

          memo: An optional memo to attach to the credit note.

          start_date: A date string to specify the global credit note service period start date in the
              customer's timezone. This will be applied to all line items that don't have
              their own individual service periods specified. If not provided, line items will
              use their original invoice line item service periods. This date is inclusive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/credit_notes",
            body=maybe_transform(
                {
                    "line_items": line_items,
                    "reason": reason,
                    "end_date": end_date,
                    "memo": memo,
                    "start_date": start_date,
                },
                credit_note_create_params.CreditNoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CreditNote,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[CreditNote]:
        """Get a paginated list of CreditNotes.

        Users can also filter by customer_id,
        subscription_id, or external_customer_id. The credit notes will be returned in
        reverse chronological order by `creation_time`.

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
            "/credit_notes",
            page=SyncPage[CreditNote],
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
                        "cursor": cursor,
                        "limit": limit,
                    },
                    credit_note_list_params.CreditNoteListParams,
                ),
            ),
            model=CreditNote,
        )

    def fetch(
        self,
        credit_note_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditNote:
        """
        This endpoint is used to fetch a single [`Credit Note`](/invoicing/credit-notes)
        given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_note_id:
            raise ValueError(f"Expected a non-empty value for `credit_note_id` but received {credit_note_id!r}")
        return self._get(
            f"/credit_notes/{credit_note_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditNote,
        )


class AsyncCreditNotes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditNotesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditNotesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditNotesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncCreditNotesWithStreamingResponse(self)

    async def create(
        self,
        *,
        line_items: Iterable[credit_note_create_params.LineItem],
        reason: Literal["duplicate", "fraudulent", "order_change", "product_unsatisfactory"],
        end_date: Union[str, date, None] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CreditNote:
        """
        This endpoint is used to create a single
        [`Credit Note`](/invoicing/credit-notes).

        The credit note service period configuration supports two explicit modes:

        1. Global service periods: Specify start_date and end_date at the credit note
           level. These dates will be applied to all line items uniformly.

        2. Individual service periods: Specify start_date and end_date for each line
           item. When using this mode, ALL line items must have individual periods
           specified.

        3. Default behavior: If no service periods are specified (neither global nor
           individual), the original invoice line item service periods will be used.

        Note: Mixing global and individual service periods in the same request is not
        allowed to prevent confusion.

        Service period dates are normalized to the start of the day in the customer's
        timezone to ensure consistent handling across different timezones.

        Date Format: Use start_date and end_date with format "YYYY-MM-DD" (e.g.,
        "2023-09-22") to match other Orb APIs like /v1/invoice_line_items.

        Note: Both start_date and end_date are inclusive - the service period will cover
        both the start date and end date completely (from start of start_date to end of
        end_date).

        Args:
          reason: An optional reason for the credit note.

          end_date: A date string to specify the global credit note service period end date in the
              customer's timezone. This will be applied to all line items that don't have
              their own individual service periods specified. If not provided, line items will
              use their original invoice line item service periods. This date is inclusive.

          memo: An optional memo to attach to the credit note.

          start_date: A date string to specify the global credit note service period start date in the
              customer's timezone. This will be applied to all line items that don't have
              their own individual service periods specified. If not provided, line items will
              use their original invoice line item service periods. This date is inclusive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/credit_notes",
            body=await async_maybe_transform(
                {
                    "line_items": line_items,
                    "reason": reason,
                    "end_date": end_date,
                    "memo": memo,
                    "start_date": start_date,
                },
                credit_note_create_params.CreditNoteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CreditNote,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CreditNote, AsyncPage[CreditNote]]:
        """Get a paginated list of CreditNotes.

        Users can also filter by customer_id,
        subscription_id, or external_customer_id. The credit notes will be returned in
        reverse chronological order by `creation_time`.

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
            "/credit_notes",
            page=AsyncPage[CreditNote],
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
                        "cursor": cursor,
                        "limit": limit,
                    },
                    credit_note_list_params.CreditNoteListParams,
                ),
            ),
            model=CreditNote,
        )

    async def fetch(
        self,
        credit_note_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditNote:
        """
        This endpoint is used to fetch a single [`Credit Note`](/invoicing/credit-notes)
        given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_note_id:
            raise ValueError(f"Expected a non-empty value for `credit_note_id` but received {credit_note_id!r}")
        return await self._get(
            f"/credit_notes/{credit_note_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditNote,
        )


class CreditNotesWithRawResponse:
    def __init__(self, credit_notes: CreditNotes) -> None:
        self._credit_notes = credit_notes

        self.create = _legacy_response.to_raw_response_wrapper(
            credit_notes.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            credit_notes.list,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            credit_notes.fetch,
        )


class AsyncCreditNotesWithRawResponse:
    def __init__(self, credit_notes: AsyncCreditNotes) -> None:
        self._credit_notes = credit_notes

        self.create = _legacy_response.async_to_raw_response_wrapper(
            credit_notes.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            credit_notes.list,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            credit_notes.fetch,
        )


class CreditNotesWithStreamingResponse:
    def __init__(self, credit_notes: CreditNotes) -> None:
        self._credit_notes = credit_notes

        self.create = to_streamed_response_wrapper(
            credit_notes.create,
        )
        self.list = to_streamed_response_wrapper(
            credit_notes.list,
        )
        self.fetch = to_streamed_response_wrapper(
            credit_notes.fetch,
        )


class AsyncCreditNotesWithStreamingResponse:
    def __init__(self, credit_notes: AsyncCreditNotes) -> None:
        self._credit_notes = credit_notes

        self.create = async_to_streamed_response_wrapper(
            credit_notes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_notes.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            credit_notes.fetch,
        )
