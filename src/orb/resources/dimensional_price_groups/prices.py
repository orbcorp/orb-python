# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared.price import Price
from ...types.dimensional_price_groups import price_list_params, price_create_params
from ...types.dimensional_price_groups.price_create_response import PriceCreateResponse

__all__ = ["Prices", "AsyncPrices"]


class Prices(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PricesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return PricesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return PricesWithStreamingResponse(self)

    def create(
        self,
        dimensional_price_group_id: str,
        *,
        cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual"],
        currency: str,
        item_id: str,
        model_type: Literal["unit", "tiered"],
        prices: Iterable[price_create_params.Price],
        tiers: Optional[Iterable[price_create_params.Tier]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PriceCreateResponse:
        """Create prices in a dimensional price group.

        Every price shares `item_id`,
        `cadence`, `currency`, and `model_type`. Tiered prices also share tier
        boundaries; each row supplies its own amounts. The request is one transaction.

        Args:
          cadence: Billing cadence for every price

          currency: An ISO 4217 currency string for every price.

          item_id: The item for every price. Must be the group's billable metric item.

          tiers: Shared tier boundaries. Required for tiered prices and omitted for unit prices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return self._post(
            path_template(
                "/dimensional_price_groups/{dimensional_price_group_id}/prices",
                dimensional_price_group_id=dimensional_price_group_id,
            ),
            body=maybe_transform(
                {
                    "cadence": cadence,
                    "currency": currency,
                    "item_id": item_id,
                    "model_type": model_type,
                    "prices": prices,
                    "tiers": tiers,
                },
                price_create_params.PriceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceCreateResponse,
        )

    def list(
        self,
        dimensional_price_group_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "archived", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Price]:
        """This endpoint returns the prices in a dimensional price group.

        Subscription
        overrides are omitted. Archived prices are omitted unless `status` is `archived`
        or `all`.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: active omits archived prices. archived returns only archived prices. all returns
              both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/dimensional_price_groups/{dimensional_price_group_id}/prices",
                dimensional_price_group_id=dimensional_price_group_id,
            ),
            page=SyncPage[Price],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    price_list_params.PriceListParams,
                ),
            ),
            model=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncPrices(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPricesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncPricesWithStreamingResponse(self)

    async def create(
        self,
        dimensional_price_group_id: str,
        *,
        cadence: Literal["one_time", "monthly", "quarterly", "semi_annual", "annual"],
        currency: str,
        item_id: str,
        model_type: Literal["unit", "tiered"],
        prices: Iterable[price_create_params.Price],
        tiers: Optional[Iterable[price_create_params.Tier]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PriceCreateResponse:
        """Create prices in a dimensional price group.

        Every price shares `item_id`,
        `cadence`, `currency`, and `model_type`. Tiered prices also share tier
        boundaries; each row supplies its own amounts. The request is one transaction.

        Args:
          cadence: Billing cadence for every price

          currency: An ISO 4217 currency string for every price.

          item_id: The item for every price. Must be the group's billable metric item.

          tiers: Shared tier boundaries. Required for tiered prices and omitted for unit prices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return await self._post(
            path_template(
                "/dimensional_price_groups/{dimensional_price_group_id}/prices",
                dimensional_price_group_id=dimensional_price_group_id,
            ),
            body=await async_maybe_transform(
                {
                    "cadence": cadence,
                    "currency": currency,
                    "item_id": item_id,
                    "model_type": model_type,
                    "prices": prices,
                    "tiers": tiers,
                },
                price_create_params.PriceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PriceCreateResponse,
        )

    def list(
        self,
        dimensional_price_group_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["active", "archived", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Price, AsyncPage[Price]]:
        """This endpoint returns the prices in a dimensional price group.

        Subscription
        overrides are omitted. Archived prices are omitted unless `status` is `archived`
        or `all`.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: active omits archived prices. archived returns only archived prices. all returns
              both.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dimensional_price_group_id:
            raise ValueError(
                f"Expected a non-empty value for `dimensional_price_group_id` but received {dimensional_price_group_id!r}"
            )
        return self._get_api_list(
            path_template(
                "/dimensional_price_groups/{dimensional_price_group_id}/prices",
                dimensional_price_group_id=dimensional_price_group_id,
            ),
            page=AsyncPage[Price],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    price_list_params.PriceListParams,
                ),
            ),
            model=cast(Any, Price),  # Union types cannot be passed in as arguments in the type system
        )


class PricesWithRawResponse:
    def __init__(self, prices: Prices) -> None:
        self._prices = prices

        self.create = _legacy_response.to_raw_response_wrapper(
            prices.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            prices.list,
        )


class AsyncPricesWithRawResponse:
    def __init__(self, prices: AsyncPrices) -> None:
        self._prices = prices

        self.create = _legacy_response.async_to_raw_response_wrapper(
            prices.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            prices.list,
        )


class PricesWithStreamingResponse:
    def __init__(self, prices: Prices) -> None:
        self._prices = prices

        self.create = to_streamed_response_wrapper(
            prices.create,
        )
        self.list = to_streamed_response_wrapper(
            prices.list,
        )


class AsyncPricesWithStreamingResponse:
    def __init__(self, prices: AsyncPrices) -> None:
        self._prices = prices

        self.create = async_to_streamed_response_wrapper(
            prices.create,
        )
        self.list = async_to_streamed_response_wrapper(
            prices.list,
        )
