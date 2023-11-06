# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import TopLevelPingResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Orb, AsyncOrb

__all__ = ["TopLevel", "AsyncTopLevel"]


class TopLevel(SyncAPIResource):
    with_raw_response: TopLevelWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.with_raw_response = TopLevelWithRawResponse(self)

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
    with_raw_response: AsyncTopLevelWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncTopLevelWithRawResponse(self)

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
        self.ping = to_raw_response_wrapper(
            top_level.ping,
        )


class AsyncTopLevelWithRawResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self.ping = async_to_raw_response_wrapper(
            top_level.ping,
        )
