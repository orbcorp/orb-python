# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .ledger import Ledger, AsyncLedger
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.customers import (
    CreditListResponse,
    CreditListByExternalIDResponse,
    credit_list_params,
    credit_list_by_external_id_params,
)

if TYPE_CHECKING:
    from ...._client import Orb, AsyncOrb

__all__ = ["Credits", "AsyncCredits"]


class Credits(SyncAPIResource):
    ledger: Ledger

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.ledger = Ledger(client)

    def list(
        self,
        customer_id: Optional[str],
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CreditListResponse]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
            f"/customers/{customer_id}/credits",
            page=SyncPage[CreditListResponse],
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
                    credit_list_params.CreditListParams,
                ),
            ),
            model=CreditListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: Optional[str],
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CreditListByExternalIDResponse]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
            f"/customers/external_customer_id/{external_customer_id}/credits",
            page=SyncPage[CreditListByExternalIDResponse],
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
                    credit_list_by_external_id_params.CreditListByExternalIDParams,
                ),
            ),
            model=CreditListByExternalIDResponse,
        )


class AsyncCredits(AsyncAPIResource):
    ledger: AsyncLedger

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.ledger = AsyncLedger(client)

    def list(
        self,
        customer_id: Optional[str],
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CreditListResponse, AsyncPage[CreditListResponse]]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
            f"/customers/{customer_id}/credits",
            page=AsyncPage[CreditListResponse],
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
                    credit_list_params.CreditListParams,
                ),
            ),
            model=CreditListResponse,
        )

    def list_by_external_id(
        self,
        external_customer_id: Optional[str],
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CreditListByExternalIDResponse, AsyncPage[CreditListByExternalIDResponse]]:
        """
        Returns a paginated list of unexpired, non-zero credit blocks for a customer.

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
            f"/customers/external_customer_id/{external_customer_id}/credits",
            page=AsyncPage[CreditListByExternalIDResponse],
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
                    credit_list_by_external_id_params.CreditListByExternalIDParams,
                ),
            ),
            model=CreditListByExternalIDResponse,
        )
