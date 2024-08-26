# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ledger import Ledger, AsyncLedger

from ...._compat import cached_property

from .top_ups import TopUps, AsyncTopUps

from ....types.customers.credit_list_response import CreditListResponse

from ....pagination import SyncPage, AsyncPage

from ...._utils import maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing import Optional

from ....types.customers.credit_list_by_external_id_response import CreditListByExternalIDResponse

from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper

from .... import _legacy_response

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.customers import credit_list_params
from ....types.customers import credit_list_by_external_id_params
from .ledger import (
    Ledger,
    AsyncLedger,
    LedgerWithRawResponse,
    AsyncLedgerWithRawResponse,
    LedgerWithStreamingResponse,
    AsyncLedgerWithStreamingResponse,
)
from .top_ups import (
    TopUps,
    AsyncTopUps,
    TopUpsWithRawResponse,
    AsyncTopUpsWithRawResponse,
    TopUpsWithStreamingResponse,
    AsyncTopUpsWithStreamingResponse,
)

__all__ = ["Credits", "AsyncCredits"]


class Credits(SyncAPIResource):
    @cached_property
    def ledger(self) -> Ledger:
        return Ledger(self._client)

    @cached_property
    def top_ups(self) -> TopUps:
        return TopUps(self._client)

    @cached_property
    def with_raw_response(self) -> CreditsWithRawResponse:
        return CreditsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsWithStreamingResponse:
        return CreditsWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        include_all_blocks: bool | NotGiven = NOT_GIVEN,
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

        Note that `currency` defaults to credits if not specified. To use a real world
        currency, set `currency` to an ISO 4217 string.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          include_all_blocks: Include all blocks, not just active ones.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
                        "include_all_blocks": include_all_blocks,
                        "limit": limit,
                    },
                    credit_list_params.CreditListParams,
                ),
            ),
            model=CreditListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        include_all_blocks: bool | NotGiven = NOT_GIVEN,
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

        Note that `currency` defaults to credits if not specified. To use a real world
        currency, set `currency` to an ISO 4217 string.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          include_all_blocks: Include all blocks, not just active ones.

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
                        "include_all_blocks": include_all_blocks,
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
    def top_ups(self) -> AsyncTopUps:
        return AsyncTopUps(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCreditsWithRawResponse:
        return AsyncCreditsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsWithStreamingResponse:
        return AsyncCreditsWithStreamingResponse(self)

    def list(
        self,
        customer_id: str,
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        include_all_blocks: bool | NotGiven = NOT_GIVEN,
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

        Note that `currency` defaults to credits if not specified. To use a real world
        currency, set `currency` to an ISO 4217 string.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          include_all_blocks: Include all blocks, not just active ones.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
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
                        "include_all_blocks": include_all_blocks,
                        "limit": limit,
                    },
                    credit_list_params.CreditListParams,
                ),
            ),
            model=CreditListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        currency: Optional[str] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        include_all_blocks: bool | NotGiven = NOT_GIVEN,
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

        Note that `currency` defaults to credits if not specified. To use a real world
        currency, set `currency` to an ISO 4217 string.

        Args:
          currency: The ledger currency or custom pricing unit to use.

          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          include_all_blocks: Include all blocks, not just active ones.

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
                        "include_all_blocks": include_all_blocks,
                        "limit": limit,
                    },
                    credit_list_by_external_id_params.CreditListByExternalIDParams,
                ),
            ),
            model=CreditListByExternalIDResponse,
        )


class CreditsWithRawResponse:
    def __init__(self, credits: Credits) -> None:
        self._credits = credits

        self.list = _legacy_response.to_raw_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = _legacy_response.to_raw_response_wrapper(
            credits.list_by_external_id,
        )

    @cached_property
    def ledger(self) -> LedgerWithRawResponse:
        return LedgerWithRawResponse(self._credits.ledger)

    @cached_property
    def top_ups(self) -> TopUpsWithRawResponse:
        return TopUpsWithRawResponse(self._credits.top_ups)


class AsyncCreditsWithRawResponse:
    def __init__(self, credits: AsyncCredits) -> None:
        self._credits = credits

        self.list = _legacy_response.async_to_raw_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            credits.list_by_external_id,
        )

    @cached_property
    def ledger(self) -> AsyncLedgerWithRawResponse:
        return AsyncLedgerWithRawResponse(self._credits.ledger)

    @cached_property
    def top_ups(self) -> AsyncTopUpsWithRawResponse:
        return AsyncTopUpsWithRawResponse(self._credits.top_ups)


class CreditsWithStreamingResponse:
    def __init__(self, credits: Credits) -> None:
        self._credits = credits

        self.list = to_streamed_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = to_streamed_response_wrapper(
            credits.list_by_external_id,
        )

    @cached_property
    def ledger(self) -> LedgerWithStreamingResponse:
        return LedgerWithStreamingResponse(self._credits.ledger)

    @cached_property
    def top_ups(self) -> TopUpsWithStreamingResponse:
        return TopUpsWithStreamingResponse(self._credits.top_ups)


class AsyncCreditsWithStreamingResponse:
    def __init__(self, credits: AsyncCredits) -> None:
        self._credits = credits

        self.list = async_to_streamed_response_wrapper(
            credits.list,
        )
        self.list_by_external_id = async_to_streamed_response_wrapper(
            credits.list_by_external_id,
        )

    @cached_property
    def ledger(self) -> AsyncLedgerWithStreamingResponse:
        return AsyncLedgerWithStreamingResponse(self._credits.ledger)

    @cached_property
    def top_ups(self) -> AsyncTopUpsWithStreamingResponse:
        return AsyncTopUpsWithStreamingResponse(self._credits.top_ups)
