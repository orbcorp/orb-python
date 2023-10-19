# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import TopLevelPingResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["TopLevel", "AsyncTopLevel"]


class TopLevel(SyncAPIResource):
    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
