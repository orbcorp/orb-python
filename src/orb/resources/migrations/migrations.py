# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import migration_list_params, migration_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
    SubscriptionsWithStreamingResponse,
    AsyncSubscriptionsWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.migration_list_response import MigrationListResponse
from ...types.migration_cancel_response import MigrationCancelResponse
from ...types.migration_create_response import MigrationCreateResponse
from ...types.migration_retrieve_response import MigrationRetrieveResponse

__all__ = ["Migrations", "AsyncMigrations"]


class Migrations(SyncAPIResource):
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    @cached_property
    def subscriptions(self) -> Subscriptions:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        return Subscriptions(self._client)

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

    def create(
        self,
        *,
        effective_time: Literal[
            "immediately", "requested_date", "start_of_term", "end_of_term", "start_of_invoice", "end_of_invoice"
        ],
        target_plan_version_number: int,
        allow_invoice_credit_or_void: bool | Omit = omit,
        can_defer_billing: bool | Omit = omit,
        effective_date: Union[str, date, None] | Omit = omit,
        excluded_subscription_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        in_trial: Optional[bool] | Omit = omit,
        included_subscription_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        plan_version_numbers: Optional[Iterable[int]] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        statuses: List[Literal["active", "upcoming"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MigrationCreateResponse:
        """
        This endpoint creates a migration of a plan's subscriptions to one of its
        versions. With `included_subscription_ids` it migrates exactly those
        subscriptions; otherwise it migrates the plan's subscriptions that match the
        filters. Each subscription is migrated asynchronously; fetch the migration to
        follow its status.

        Args:
          effective_time: When the migration takes effect: 'immediately', 'requested_date' on
              `effective_date`, 'start_of_term' or 'end_of_term' for the start or end of each
              subscription's current billing period, or 'start_of_invoice' or 'end_of_invoice'
              for the start of its current or next invoice.

          target_plan_version_number: The plan version to migrate subscriptions to. It can't be a draft version.

          allow_invoice_credit_or_void: When false, a subscription whose migration would void an issued invoice or
              create a credit note fails instead.

          can_defer_billing: When true, an in-arrears price the migration ends mid-cycle bills its final line
              item on the next scheduled invoice instead of on its end date.

          effective_date: The date the migration takes effect, at midnight in each customer's timezone.
              Required when `effective_time` is `requested_date`, and not allowed otherwise.

          excluded_subscription_ids: Leave these subscriptions out. Can't be combined with
              `included_subscription_ids`.

          external_plan_id: The external ID of the plan whose subscriptions to migrate.

          in_trial: `true` migrates only subscriptions in a trial, `false` only subscriptions not in
              a trial.

          included_subscription_ids: Migrate only these subscriptions. When set, the filters below are ignored.

          plan_id: The plan whose subscriptions to migrate. Exactly one of `plan_id` and
              `external_plan_id` is required.

          plan_version_numbers: Migrate only subscriptions currently on these plan versions.

          reason: Why the migration was created.

          statuses: Migrate subscriptions with these statuses. Defaults to active subscriptions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/migrations",
            body=maybe_transform(
                {
                    "effective_time": effective_time,
                    "target_plan_version_number": target_plan_version_number,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "can_defer_billing": can_defer_billing,
                    "effective_date": effective_date,
                    "excluded_subscription_ids": excluded_subscription_ids,
                    "external_plan_id": external_plan_id,
                    "in_trial": in_trial,
                    "included_subscription_ids": included_subscription_ids,
                    "plan_id": plan_id,
                    "plan_version_numbers": plan_version_numbers,
                    "reason": reason,
                    "statuses": statuses,
                },
                migration_create_params.MigrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MigrationCreateResponse,
        )

    def retrieve(
        self,
        migration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MigrationRetrieveResponse:
        """
        This endpoint returns a migration identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return self._get(
            path_template("/migrations/{migration_id}", migration_id=migration_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[MigrationListResponse]:
        """
        This endpoint returns a list of migrations across all plans in the account,
        optionally filtered by plan (`plan_id` or `external_plan_id`). The list of
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
        return self._get_api_list(
            "/migrations",
            page=SyncPage[MigrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "external_plan_id": external_plan_id,
                        "limit": limit,
                        "plan_id": plan_id,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MigrationCancelResponse:
        """
        This endpoint cancels a migration identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return self._post(
            path_template("/migrations/{migration_id}/cancel", migration_id=migration_id),
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
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        return AsyncSubscriptions(self._client)

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

    async def create(
        self,
        *,
        effective_time: Literal[
            "immediately", "requested_date", "start_of_term", "end_of_term", "start_of_invoice", "end_of_invoice"
        ],
        target_plan_version_number: int,
        allow_invoice_credit_or_void: bool | Omit = omit,
        can_defer_billing: bool | Omit = omit,
        effective_date: Union[str, date, None] | Omit = omit,
        excluded_subscription_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        in_trial: Optional[bool] | Omit = omit,
        included_subscription_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        plan_version_numbers: Optional[Iterable[int]] | Omit = omit,
        reason: Optional[str] | Omit = omit,
        statuses: List[Literal["active", "upcoming"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MigrationCreateResponse:
        """
        This endpoint creates a migration of a plan's subscriptions to one of its
        versions. With `included_subscription_ids` it migrates exactly those
        subscriptions; otherwise it migrates the plan's subscriptions that match the
        filters. Each subscription is migrated asynchronously; fetch the migration to
        follow its status.

        Args:
          effective_time: When the migration takes effect: 'immediately', 'requested_date' on
              `effective_date`, 'start_of_term' or 'end_of_term' for the start or end of each
              subscription's current billing period, or 'start_of_invoice' or 'end_of_invoice'
              for the start of its current or next invoice.

          target_plan_version_number: The plan version to migrate subscriptions to. It can't be a draft version.

          allow_invoice_credit_or_void: When false, a subscription whose migration would void an issued invoice or
              create a credit note fails instead.

          can_defer_billing: When true, an in-arrears price the migration ends mid-cycle bills its final line
              item on the next scheduled invoice instead of on its end date.

          effective_date: The date the migration takes effect, at midnight in each customer's timezone.
              Required when `effective_time` is `requested_date`, and not allowed otherwise.

          excluded_subscription_ids: Leave these subscriptions out. Can't be combined with
              `included_subscription_ids`.

          external_plan_id: The external ID of the plan whose subscriptions to migrate.

          in_trial: `true` migrates only subscriptions in a trial, `false` only subscriptions not in
              a trial.

          included_subscription_ids: Migrate only these subscriptions. When set, the filters below are ignored.

          plan_id: The plan whose subscriptions to migrate. Exactly one of `plan_id` and
              `external_plan_id` is required.

          plan_version_numbers: Migrate only subscriptions currently on these plan versions.

          reason: Why the migration was created.

          statuses: Migrate subscriptions with these statuses. Defaults to active subscriptions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/migrations",
            body=await async_maybe_transform(
                {
                    "effective_time": effective_time,
                    "target_plan_version_number": target_plan_version_number,
                    "allow_invoice_credit_or_void": allow_invoice_credit_or_void,
                    "can_defer_billing": can_defer_billing,
                    "effective_date": effective_date,
                    "excluded_subscription_ids": excluded_subscription_ids,
                    "external_plan_id": external_plan_id,
                    "in_trial": in_trial,
                    "included_subscription_ids": included_subscription_ids,
                    "plan_id": plan_id,
                    "plan_version_numbers": plan_version_numbers,
                    "reason": reason,
                    "statuses": statuses,
                },
                migration_create_params.MigrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=MigrationCreateResponse,
        )

    async def retrieve(
        self,
        migration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MigrationRetrieveResponse:
        """
        This endpoint returns a migration identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return await self._get(
            path_template("/migrations/{migration_id}", migration_id=migration_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MigrationRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        external_plan_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        plan_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MigrationListResponse, AsyncPage[MigrationListResponse]]:
        """
        This endpoint returns a list of migrations across all plans in the account,
        optionally filtered by plan (`plan_id` or `external_plan_id`). The list of
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
        return self._get_api_list(
            "/migrations",
            page=AsyncPage[MigrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "external_plan_id": external_plan_id,
                        "limit": limit,
                        "plan_id": plan_id,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> MigrationCancelResponse:
        """
        This endpoint cancels a migration identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not migration_id:
            raise ValueError(f"Expected a non-empty value for `migration_id` but received {migration_id!r}")
        return await self._post(
            path_template("/migrations/{migration_id}/cancel", migration_id=migration_id),
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

        self.create = _legacy_response.to_raw_response_wrapper(
            migrations.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            migrations.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            migrations.list,
        )
        self.cancel = _legacy_response.to_raw_response_wrapper(
            migrations.cancel,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsWithRawResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        return SubscriptionsWithRawResponse(self._migrations.subscriptions)


class AsyncMigrationsWithRawResponse:
    def __init__(self, migrations: AsyncMigrations) -> None:
        self._migrations = migrations

        self.create = _legacy_response.async_to_raw_response_wrapper(
            migrations.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            migrations.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            migrations.list,
        )
        self.cancel = _legacy_response.async_to_raw_response_wrapper(
            migrations.cancel,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithRawResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        return AsyncSubscriptionsWithRawResponse(self._migrations.subscriptions)


class MigrationsWithStreamingResponse:
    def __init__(self, migrations: Migrations) -> None:
        self._migrations = migrations

        self.create = to_streamed_response_wrapper(
            migrations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            migrations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            migrations.list,
        )
        self.cancel = to_streamed_response_wrapper(
            migrations.cancel,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsWithStreamingResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        return SubscriptionsWithStreamingResponse(self._migrations.subscriptions)


class AsyncMigrationsWithStreamingResponse:
    def __init__(self, migrations: AsyncMigrations) -> None:
        self._migrations = migrations

        self.create = async_to_streamed_response_wrapper(
            migrations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            migrations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            migrations.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            migrations.cancel,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithStreamingResponse:
        """
        The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
        customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
        in the [Price resource](/reference/price).
        """
        return AsyncSubscriptionsWithStreamingResponse(self._migrations.subscriptions)
