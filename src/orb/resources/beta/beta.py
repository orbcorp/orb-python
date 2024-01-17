# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .price import (
    Price,
    AsyncPrice,
    PriceWithRawResponse,
    AsyncPriceWithRawResponse,
    PriceWithStreamingResponse,
    AsyncPriceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Beta", "AsyncBeta"]


class Beta(SyncAPIResource):
    @cached_property
    def price(self) -> Price:
        return Price(self._client)

    @cached_property
    def with_raw_response(self) -> BetaWithRawResponse:
        return BetaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaWithStreamingResponse:
        return BetaWithStreamingResponse(self)


class AsyncBeta(AsyncAPIResource):
    @cached_property
    def price(self) -> AsyncPrice:
        return AsyncPrice(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaWithRawResponse:
        return AsyncBetaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaWithStreamingResponse:
        return AsyncBetaWithStreamingResponse(self)


class BetaWithRawResponse:
    def __init__(self, beta: Beta) -> None:
        self._beta = beta

    @cached_property
    def price(self) -> PriceWithRawResponse:
        return PriceWithRawResponse(self._beta.price)


class AsyncBetaWithRawResponse:
    def __init__(self, beta: AsyncBeta) -> None:
        self._beta = beta

    @cached_property
    def price(self) -> AsyncPriceWithRawResponse:
        return AsyncPriceWithRawResponse(self._beta.price)


class BetaWithStreamingResponse:
    def __init__(self, beta: Beta) -> None:
        self._beta = beta

    @cached_property
    def price(self) -> PriceWithStreamingResponse:
        return PriceWithStreamingResponse(self._beta.price)


class AsyncBetaWithStreamingResponse:
    def __init__(self, beta: AsyncBeta) -> None:
        self._beta = beta

    @cached_property
    def price(self) -> AsyncPriceWithStreamingResponse:
        return AsyncPriceWithStreamingResponse(self._beta.price)
