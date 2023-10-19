# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

from ...types import Price
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["ExternalPriceID", "AsyncExternalPriceID"]


class ExternalPriceID(SyncAPIResource):
    def fetch(
        self,
        external_price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def fetch(
        self,
        external_price_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
