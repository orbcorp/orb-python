# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.credit_block_retrieve_response import CreditBlockRetrieveResponse

__all__ = ["CreditBlocks", "AsyncCreditBlocks"]


class CreditBlocks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditBlocksWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return CreditBlocksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditBlocksWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return CreditBlocksWithStreamingResponse(self)

    def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditBlockRetrieveResponse:
        """
        This endpoint returns a credit block identified by its block_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._get(
            f"/credit_blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditBlockRetrieveResponse,
        )

    def delete(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        This endpoint deletes a credit block by its ID.

        When a credit block is deleted:

        - The block is removed from the customer's credit ledger.
        - Any usage of the credit block is reversed, and the ledger is replayed as if
          the block never existed.
        - If invoices were generated from the purchase of the credit block, they will be
          deleted if in draft status, voided if issued, or a credit note will be issued
          if the invoice is paid.

        <Note>
        Issued invoices that had credits applied from this block will not be regenerated, but the ledger will
        reflect the state as if credits from the deleted block were never applied.
        </Note>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/credit_blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncCreditBlocks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditBlocksWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditBlocksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditBlocksWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncCreditBlocksWithStreamingResponse(self)

    async def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditBlockRetrieveResponse:
        """
        This endpoint returns a credit block identified by its block_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._get(
            f"/credit_blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditBlockRetrieveResponse,
        )

    async def delete(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """
        This endpoint deletes a credit block by its ID.

        When a credit block is deleted:

        - The block is removed from the customer's credit ledger.
        - Any usage of the credit block is reversed, and the ledger is replayed as if
          the block never existed.
        - If invoices were generated from the purchase of the credit block, they will be
          deleted if in draft status, voided if issued, or a credit note will be issued
          if the invoice is paid.

        <Note>
        Issued invoices that had credits applied from this block will not be regenerated, but the ledger will
        reflect the state as if credits from the deleted block were never applied.
        </Note>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/credit_blocks/{block_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class CreditBlocksWithRawResponse:
    def __init__(self, credit_blocks: CreditBlocks) -> None:
        self._credit_blocks = credit_blocks

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            credit_blocks.retrieve,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            credit_blocks.delete,
        )


class AsyncCreditBlocksWithRawResponse:
    def __init__(self, credit_blocks: AsyncCreditBlocks) -> None:
        self._credit_blocks = credit_blocks

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            credit_blocks.retrieve,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            credit_blocks.delete,
        )


class CreditBlocksWithStreamingResponse:
    def __init__(self, credit_blocks: CreditBlocks) -> None:
        self._credit_blocks = credit_blocks

        self.retrieve = to_streamed_response_wrapper(
            credit_blocks.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            credit_blocks.delete,
        )


class AsyncCreditBlocksWithStreamingResponse:
    def __init__(self, credit_blocks: AsyncCreditBlocks) -> None:
        self._credit_blocks = credit_blocks

        self.retrieve = async_to_streamed_response_wrapper(
            credit_blocks.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            credit_blocks.delete,
        )
