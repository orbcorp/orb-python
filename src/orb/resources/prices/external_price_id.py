# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.price import Price
from ..._base_client import (
    make_request_options,
)

__all__ = ["ExternalPriceID", "AsyncExternalPriceID"]


class ExternalPriceID(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalPriceIDWithRawResponse:
        return ExternalPriceIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalPriceIDWithStreamingResponse:
        return ExternalPriceIDWithStreamingResponse(self)

    def fetch(
        self,
        external_price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Price:
        """This endpoint returns a price given an external price id.

        See the
        [price creation API](../reference/create-price) for more information about
        external price aliases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_price_id:
            raise ValueError(f"Expected a non-empty value for `external_price_id` but received {external_price_id!r}")
        return cast(
            Price,
            self._get(
                f"/prices/external_price_id/{external_price_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncExternalPriceID(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalPriceIDWithRawResponse:
        return AsyncExternalPriceIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalPriceIDWithStreamingResponse:
        return AsyncExternalPriceIDWithStreamingResponse(self)

    async def fetch(
        self,
        external_price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Price:
        """This endpoint returns a price given an external price id.

        See the
        [price creation API](../reference/create-price) for more information about
        external price aliases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_price_id:
            raise ValueError(f"Expected a non-empty value for `external_price_id` but received {external_price_id!r}")
        return cast(
            Price,
            await self._get(
                f"/prices/external_price_id/{external_price_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ExternalPriceIDWithRawResponse:
    def __init__(self, external_price_id: ExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.fetch = _legacy_response.to_raw_response_wrapper(
            external_price_id.fetch,
        )


class AsyncExternalPriceIDWithRawResponse:
    def __init__(self, external_price_id: AsyncExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            external_price_id.fetch,
        )


class ExternalPriceIDWithStreamingResponse:
    def __init__(self, external_price_id: ExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.fetch = to_streamed_response_wrapper(
            external_price_id.fetch,
        )


class AsyncExternalPriceIDWithStreamingResponse:
    def __init__(self, external_price_id: AsyncExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.fetch = async_to_streamed_response_wrapper(
            external_price_id.fetch,
        )
