# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

import httpx

from ...types import Price
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["ExternalPriceID", "AsyncExternalPriceID"]


class ExternalPriceID(SyncAPIResource):
    with_raw_response: ExternalPriceIDWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = ExternalPriceIDWithRawResponse(self)

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
    with_raw_response: AsyncExternalPriceIDWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncExternalPriceIDWithRawResponse(self)

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
        self.fetch = to_raw_response_wrapper(
            external_price_id.fetch,
        )


class AsyncExternalPriceIDWithRawResponse:
    def __init__(self, external_price_id: AsyncExternalPriceID) -> None:
        self.fetch = async_to_raw_response_wrapper(
            external_price_id.fetch,
        )
