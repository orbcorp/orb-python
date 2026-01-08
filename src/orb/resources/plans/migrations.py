# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ...types.plans import migration_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.plans.migration_list_response import MigrationListResponse
from ...types.plans.migration_cancel_response import MigrationCancelResponse
from ...types.plans.migration_retrieve_response import MigrationRetrieveResponse

__all__ = ["Migrations", "AsyncMigrations"]


class Migrations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MigrationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return MigrationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MigrationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return MigrationsWithStreamingResponse(self)

    def retrieve(
        self,
        migration_id: str,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MigrationRetrieveResponse:
        """
        Fetch migration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return self._get(
            f"/plans/{plan_id}/migrations/{migration_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationRetrieveResponse,
        )

    def list(
        self,
        plan_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[MigrationListResponse]:
        """This endpoint returns a list of all migrations for a plan.

        The list of
        migrations is ordered starting from the most recently created migration. The
        response also includes pagination_metadata, which lets the caller retrieve the
        next page of results if they exist.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get_api_list(
            f"/plans/{plan_id}/migrations",
            page=SyncPage[MigrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    migration_list_params.MigrationListParams,
                ),
            ),
            model=MigrationListResponse,
        )

    def cancel(
        self,
        migration_id: str,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MigrationCancelResponse:
        """
        This endpoint cancels a migration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return self._post(
            f"/plans/{plan_id}/migrations/{migration_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MigrationCancelResponse,
        )


class AsyncMigrations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMigrationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMigrationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMigrationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncMigrationsWithStreamingResponse(self)

    async def retrieve(
        self,
        migration_id: str,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MigrationRetrieveResponse:
        """
        Fetch migration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return await self._get(
            f"/plans/{plan_id}/migrations/{migration_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationRetrieveResponse,
        )

    def list(
        self,
        plan_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MigrationListResponse, AsyncPage[MigrationListResponse]]:
        """This endpoint returns a list of all migrations for a plan.

        The list of
        migrations is ordered starting from the most recently created migration. The
        response also includes pagination_metadata, which lets the caller retrieve the
        next page of results if they exist.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get_api_list(
            f"/plans/{plan_id}/migrations",
            page=AsyncPage[MigrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    migration_list_params.MigrationListParams,
                ),
            ),
            model=MigrationListResponse,
        )

    async def cancel(
        self,
        migration_id: str,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MigrationCancelResponse:
        """
        This endpoint cancels a migration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return await self._post(
            f"/plans/{plan_id}/migrations/{migration_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MigrationCancelResponse,
        )


class MigrationsWithRawResponse:
    def __init__(self, migrations: Migrations) -> None:
        self._migrations = migrations

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            migrations.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            migrations.list,
        )
        self.cancel = _legacy_response.to_raw_response_wrapper(
            migrations.cancel,
        )


class AsyncMigrationsWithRawResponse:
    def __init__(self, migrations: AsyncMigrations) -> None:
        self._migrations = migrations

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            migrations.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            migrations.list,
        )
        self.cancel = _legacy_response.async_to_raw_response_wrapper(
            migrations.cancel,
        )


class MigrationsWithStreamingResponse:
    def __init__(self, migrations: Migrations) -> None:
        self._migrations = migrations

        self.retrieve = to_streamed_response_wrapper(
            migrations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            migrations.list,
        )
        self.cancel = to_streamed_response_wrapper(
            migrations.cancel,
        )


class AsyncMigrationsWithStreamingResponse:
    def __init__(self, migrations: AsyncMigrations) -> None:
        self._migrations = migrations

        self.retrieve = async_to_streamed_response_wrapper(
            migrations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            migrations.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            migrations.cancel,
        )
