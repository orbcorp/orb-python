# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .price import Price, AsyncPrice, PriceWithRawResponse, AsyncPriceWithRawResponse
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


class AsyncBeta(AsyncAPIResource):
    @cached_property
    def price(self) -> AsyncPrice:
        return AsyncPrice(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaWithRawResponse:
        return AsyncBetaWithRawResponse(self)


class BetaWithRawResponse:
    def __init__(self, beta: Beta) -> None:
        self.price = PriceWithRawResponse(beta.price)


class AsyncBetaWithRawResponse:
    def __init__(self, beta: AsyncBeta) -> None:
        self.price = AsyncPriceWithRawResponse(beta.price)
