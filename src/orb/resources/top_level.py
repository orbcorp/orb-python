# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import TopLevelPingResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["TopLevel", "AsyncTopLevel"]


class TopLevel(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopLevelWithRawResponse:
        return TopLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopLevelWithStreamingResponse:
        return TopLevelWithStreamingResponse(self)

    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopLevelPingResponse:
        """
        This endpoint allows you to test your connection to the Orb API and check the
        validity of your API key, passed in the Authorization header. This is
        particularly useful for checking that your environment is set up properly, and
        is a great choice for connectors and integrations.

        This API does not have any side-effects or return any Orb resources.
        """
        return self._get(
            "/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TopLevelPingResponse,
        )


class AsyncTopLevel(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopLevelWithRawResponse:
        return AsyncTopLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopLevelWithStreamingResponse:
        return AsyncTopLevelWithStreamingResponse(self)

    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TopLevelPingResponse:
        """
        This endpoint allows you to test your connection to the Orb API and check the
        validity of your API key, passed in the Authorization header. This is
        particularly useful for checking that your environment is set up properly, and
        is a great choice for connectors and integrations.

        This API does not have any side-effects or return any Orb resources.
        """
        return await self._get(
            "/ping",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TopLevelPingResponse,
        )


class TopLevelWithRawResponse:
    def __init__(self, top_level: TopLevel) -> None:
        self.ping = _legacy_response.to_raw_response_wrapper(
            top_level.ping,
        )


class AsyncTopLevelWithRawResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self.ping = _legacy_response.async_to_raw_response_wrapper(
            top_level.ping,
        )


class TopLevelWithStreamingResponse:
    def __init__(self, top_level: TopLevel) -> None:
        self.ping = to_streamed_response_wrapper(
            top_level.ping,
        )


class AsyncTopLevelWithStreamingResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self.ping = async_to_streamed_response_wrapper(
            top_level.ping,
        )
