# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

import httpx

from .... import _legacy_response
from .ledger import (
    Ledger,
    AsyncLedger,
    LedgerWithRawResponse,
    AsyncLedgerWithRawResponse,
    LedgerWithStreamingResponse,
    AsyncLedgerWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncPage, AsyncPage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.customers import (
    CreditListResponse,
    CreditListByExternalIDResponse,
    credit_list_params,
    credit_list_by_external_id_params,
)

__all__ = ["Credits", "AsyncCredits"]


class Credits(SyncAPIResource):
    @cached_property
    def ledger(self) -> Ledger:
        return Ledger(self._client)

    @cached_property
    def with_raw_response(self) -> CreditsWithRawResponse:
        return CreditsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsWithStreamingResponse:
        return CreditsWithStreamingResponse(self)

    def list(
        self,
        customer_id: Optional[str],
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CreditListResponse]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
        return self._get_api_list(
            f"/customers/{customer_id}/credits",
            page=SyncPage[CreditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    credit_list_params.CreditListParams,
                ),
            ),
            model=CreditListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: Optional[str],
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CreditListByExternalIDResponse]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
        return self._get_api_list(
            f"/customers/external_customer_id/{external_customer_id}/credits",
            page=SyncPage[CreditListByExternalIDResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    credit_list_by_external_id_params.CreditListByExternalIDParams,
                ),
            ),
            model=CreditListByExternalIDResponse,
        )


class AsyncCredits(AsyncAPIResource):
    @cached_property
    def ledger(self) -> AsyncLedger:
        return AsyncLedger(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCreditsWithRawResponse:
        return AsyncCreditsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsWithStreamingResponse:
        return AsyncCreditsWithStreamingResponse(self)

    def list(
        self,
        customer_id: Optional[str],
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CreditListResponse, AsyncPage[CreditListResponse]]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
        return self._get_api_list(
            f"/customers/{customer_id}/credits",
            page=AsyncPage[CreditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    credit_list_params.CreditListParams,
                ),
            ),
            model=CreditListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: Optional[str],
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CreditListByExternalIDResponse, AsyncPage[CreditListByExternalIDResponse]]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
        return self._get_api_list(
            f"/customers/external_customer_id/{external_customer_id}/credits",
            page=AsyncPage[CreditListByExternalIDResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency": currency,
                        "cursor": cursor,
                        "limit": limit,
                    },
                    credit_list_by_external_id_params.CreditListByExternalIDParams,
                ),
            ),
            model=CreditListByExternalIDResponse,
        )


class CreditsWithRawResponse:
    def __init__(self, credits: Credits) -> None:
        self.ledger = LedgerWithRawResponse(credits.ledger)

        self.list = _legacy_response.to_raw_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = _legacy_response.to_raw_response_wrapper(
            credits.list_by_external_id,
        )


class AsyncCreditsWithRawResponse:
    def __init__(self, credits: AsyncCredits) -> None:
        self.ledger = AsyncLedgerWithRawResponse(credits.ledger)

        self.list = _legacy_response.async_to_raw_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            credits.list_by_external_id,
        )


class CreditsWithStreamingResponse:
    def __init__(self, credits: Credits) -> None:
        self.ledger = LedgerWithStreamingResponse(credits.ledger)

        self.list = to_streamed_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = to_streamed_response_wrapper(
            credits.list_by_external_id,
        )


class AsyncCreditsWithStreamingResponse:
    def __init__(self, credits: AsyncCredits) -> None:
        self.ledger = AsyncLedgerWithStreamingResponse(credits.ledger)

        self.list = async_to_streamed_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = async_to_streamed_response_wrapper(
            credits.list_by_external_id,
        )
