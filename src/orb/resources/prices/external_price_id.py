# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Optional, cast

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.prices import external_price_id_update_params
from ...types.shared.price import Price

__all__ = ["ExternalPriceID", "AsyncExternalPriceID"]


class ExternalPriceID(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalPriceIDWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return ExternalPriceIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalPriceIDWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return ExternalPriceIDWithStreamingResponse(self)

    def update(
        self,
        external_price_id: str,
        *,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint allows you to update the `metadata` property on a price.

        If you
        pass null for the metadata value, it will clear any existing metadata for that
        price.

        Args:
          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_price_id:
            raise ValueError(f"Expected a non-empty value for `external_price_id` but received {external_price_id!r}")
        return cast(
            Price,
            self._put(
                f"/prices/external_price_id/{external_price_id}",
                body=maybe_transform(
                    {"metadata": metadata}, external_price_id_update_params.ExternalPriceIDUpdateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def fetch(
        self,
        external_price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Price:
        """This endpoint returns a price given an external price id.

        See the
        [price creation API](/api-reference/price/create-price) for more information
        about external price aliases.

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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalPriceIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalPriceIDWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncExternalPriceIDWithStreamingResponse(self)

    async def update(
        self,
        external_price_id: str,
        *,
        metadata: Optional[Dict[str, Optional[str]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Price:
        """This endpoint allows you to update the `metadata` property on a price.

        If you
        pass null for the metadata value, it will clear any existing metadata for that
        price.

        Args:
          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_price_id:
            raise ValueError(f"Expected a non-empty value for `external_price_id` but received {external_price_id!r}")
        return cast(
            Price,
            await self._put(
                f"/prices/external_price_id/{external_price_id}",
                body=await async_maybe_transform(
                    {"metadata": metadata}, external_price_id_update_params.ExternalPriceIDUpdateParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def fetch(
        self,
        external_price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Price:
        """This endpoint returns a price given an external price id.

        See the
        [price creation API](/api-reference/price/create-price) for more information
        about external price aliases.

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

        self.update = _legacy_response.to_raw_response_wrapper(
            external_price_id.update,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            external_price_id.fetch,
        )


class AsyncExternalPriceIDWithRawResponse:
    def __init__(self, external_price_id: AsyncExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.update = _legacy_response.async_to_raw_response_wrapper(
            external_price_id.update,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            external_price_id.fetch,
        )


class ExternalPriceIDWithStreamingResponse:
    def __init__(self, external_price_id: ExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.update = to_streamed_response_wrapper(
            external_price_id.update,
        )
        self.fetch = to_streamed_response_wrapper(
            external_price_id.fetch,
        )


class AsyncExternalPriceIDWithStreamingResponse:
    def __init__(self, external_price_id: AsyncExternalPriceID) -> None:
        self._external_price_id = external_price_id

        self.update = async_to_streamed_response_wrapper(
            external_price_id.update,
        )
        self.fetch = async_to_streamed_response_wrapper(
            external_price_id.fetch,
        )
