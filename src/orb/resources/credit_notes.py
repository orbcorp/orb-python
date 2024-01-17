# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

import httpx

from .. import _legacy_response
from ..types import CreditNote, credit_note_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["CreditNotes", "AsyncCreditNotes"]


class CreditNotes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditNotesWithRawResponse:
        return CreditNotesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditNotesWithStreamingResponse:
        return CreditNotesWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditNote:
        """
        This endpoint is used to fetch a single
        [`Credit Note`](../guides/invoicing/credit-notes) given an identifier.

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
        return AsyncCreditNotesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditNotesWithStreamingResponse:
        return AsyncCreditNotesWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditNote:
        """
        This endpoint is used to fetch a single
        [`Credit Note`](../guides/invoicing/credit-notes) given an identifier.

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

        self.list = _legacy_response.to_raw_response_wrapper(
            credit_notes.list,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            credit_notes.fetch,
        )


class AsyncCreditNotesWithRawResponse:
    def __init__(self, credit_notes: AsyncCreditNotes) -> None:
        self._credit_notes = credit_notes

        self.list = _legacy_response.async_to_raw_response_wrapper(
            credit_notes.list,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            credit_notes.fetch,
        )


class CreditNotesWithStreamingResponse:
    def __init__(self, credit_notes: CreditNotes) -> None:
        self._credit_notes = credit_notes

        self.list = to_streamed_response_wrapper(
            credit_notes.list,
        )
        self.fetch = to_streamed_response_wrapper(
            credit_notes.fetch,
        )


class AsyncCreditNotesWithStreamingResponse:
    def __init__(self, credit_notes: AsyncCreditNotes) -> None:
        self._credit_notes = credit_notes

        self.list = async_to_streamed_response_wrapper(
            credit_notes.list,
        )
        self.fetch = async_to_streamed_response_wrapper(
            credit_notes.fetch,
        )
