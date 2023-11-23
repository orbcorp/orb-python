# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import Plan, plan_list_params, plan_create_params, plan_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .external_plan_id import (
    ExternalPlanID,
    AsyncExternalPlanID,
    ExternalPlanIDWithRawResponse,
    AsyncExternalPlanIDWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["Plans", "AsyncPlans"]


class Plans(SyncAPIResource):
    external_plan_id: ExternalPlanID
    with_raw_response: PlansWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.external_plan_id = ExternalPlanID(client)
        self.with_raw_response = PlansWithRawResponse(self)

    def create(
        self,
        *,
        currency: str,
        name: str,
        prices: List[plan_create_params.Price],
        default_invoice_memo: Optional[str] | NotGiven = NOT_GIVEN,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        net_terms: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint allows creation of plans including their prices.

        Args:
          currency: An ISO 4217 currency string or custom pricing unit (`credits`) for this plan's
              prices.

          prices: Prices for this plan. If the plan has phases, this includes prices across all
              phases of the plan.

          default_invoice_memo: Free-form text which is available on the invoice PDF and the Orb invoice portal.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          net_terms: The net terms determines the difference between the invoice date and the issue
              date for the invoice. If you intend the invoice to be due on issue, set this
              to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/plans",
            body=maybe_transform(
                {
                    "currency": currency,
                    "name": name,
                    "prices": prices,
                    "default_invoice_memo": default_invoice_memo,
                    "external_plan_id": external_plan_id,
                    "metadata": metadata,
                    "net_terms": net_terms,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Plan,
        )

    def update(
        self,
        plan_id: str,
        *,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint can be used to update the `external_plan_id`, and `metadata` of an
        existing plan.

        Other fields on a customer are currently immutable.

        Args:
          external_plan_id: An optional user-defined ID for this plan resource, used throughout the system
              as an alias for this Plan. Use this field to identify a plan by an existing
              identifier in your system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._put(
            f"/plans/{plan_id}",
            body=maybe_transform(
                {
                    "external_plan_id": external_plan_id,
                    "metadata": metadata,
                },
                plan_update_params.PlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Plan,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived", "draft"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Plan]:
        """
        This endpoint returns a list of all [plans](../guides/concepts##plan-and-price)
        for an account in a list format. The list of plans is ordered starting from the
        most recently created plan. The response also includes
        [`pagination_metadata`](../reference/pagination), which lets the caller retrieve
        the next page of results if they exist.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: The plan status to filter to ('active', 'archived', or 'draft').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/plans",
            page=SyncPage[Plan],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    plan_list_params.PlanListParams,
                ),
            ),
            model=Plan,
        )

    def fetch(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Plan:
        """
        This endpoint is used to fetch [plan](../guides/concepts##plan-and-price)
        details given a plan identifier. It returns information about the prices
        included in the plan and their configuration, as well as the product that the
        plan is attached to.

        ## Serialized prices

        Orb supports a few different pricing models out of the box. Each of these models
        is serialized differently in a given [Price](../guides/concepts#plan-and-price)
        object. The `model_type` field determines the key for the configuration object
        that is present. A detailed explanation of price types can be found in the
        [Price schema](../guides/concepts#plan-and-price).

        ## Phases

        Orb supports plan phases, also known as contract ramps. For plans with phases,
        the serialized prices refer to all prices across all phases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/plans/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )


class AsyncPlans(AsyncAPIResource):
    external_plan_id: AsyncExternalPlanID
    with_raw_response: AsyncPlansWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.external_plan_id = AsyncExternalPlanID(client)
        self.with_raw_response = AsyncPlansWithRawResponse(self)

    async def create(
        self,
        *,
        currency: str,
        name: str,
        prices: List[plan_create_params.Price],
        default_invoice_memo: Optional[str] | NotGiven = NOT_GIVEN,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        net_terms: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint allows creation of plans including their prices.

        Args:
          currency: An ISO 4217 currency string or custom pricing unit (`credits`) for this plan's
              prices.

          prices: Prices for this plan. If the plan has phases, this includes prices across all
              phases of the plan.

          default_invoice_memo: Free-form text which is available on the invoice PDF and the Orb invoice portal.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          net_terms: The net terms determines the difference between the invoice date and the issue
              date for the invoice. If you intend the invoice to be due on issue, set this
              to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/plans",
            body=maybe_transform(
                {
                    "currency": currency,
                    "name": name,
                    "prices": prices,
                    "default_invoice_memo": default_invoice_memo,
                    "external_plan_id": external_plan_id,
                    "metadata": metadata,
                    "net_terms": net_terms,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Plan,
        )

    async def update(
        self,
        plan_id: str,
        *,
        external_plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Optional[Dict[str, Optional[str]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint can be used to update the `external_plan_id`, and `metadata` of an
        existing plan.

        Other fields on a customer are currently immutable.

        Args:
          external_plan_id: An optional user-defined ID for this plan resource, used throughout the system
              as an alias for this Plan. Use this field to identify a plan by an existing
              identifier in your system.

          metadata: User-specified key/value pairs for the resource. Individual keys can be removed
              by setting the value to `null`, and the entire metadata mapping can be cleared
              by setting `metadata` to `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._put(
            f"/plans/{plan_id}",
            body=maybe_transform(
                {
                    "external_plan_id": external_plan_id,
                    "metadata": metadata,
                },
                plan_update_params.PlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Plan,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        status: Literal["active", "archived", "draft"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Plan, AsyncPage[Plan]]:
        """
        This endpoint returns a list of all [plans](../guides/concepts##plan-and-price)
        for an account in a list format. The list of plans is ordered starting from the
        most recently created plan. The response also includes
        [`pagination_metadata`](../reference/pagination), which lets the caller retrieve
        the next page of results if they exist.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          status: The plan status to filter to ('active', 'archived', or 'draft').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/plans",
            page=AsyncPage[Plan],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_gt": created_at_gt,
                        "created_at_gte": created_at_gte,
                        "created_at_lt": created_at_lt,
                        "created_at_lte": created_at_lte,
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                    },
                    plan_list_params.PlanListParams,
                ),
            ),
            model=Plan,
        )

    async def fetch(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Plan:
        """
        This endpoint is used to fetch [plan](../guides/concepts##plan-and-price)
        details given a plan identifier. It returns information about the prices
        included in the plan and their configuration, as well as the product that the
        plan is attached to.

        ## Serialized prices

        Orb supports a few different pricing models out of the box. Each of these models
        is serialized differently in a given [Price](../guides/concepts#plan-and-price)
        object. The `model_type` field determines the key for the configuration object
        that is present. A detailed explanation of price types can be found in the
        [Price schema](../guides/concepts#plan-and-price).

        ## Phases

        Orb supports plan phases, also known as contract ramps. For plans with phases,
        the serialized prices refer to all prices across all phases.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/plans/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )


class PlansWithRawResponse:
    def __init__(self, plans: Plans) -> None:
        self.external_plan_id = ExternalPlanIDWithRawResponse(plans.external_plan_id)

        self.create = to_raw_response_wrapper(
            plans.create,
        )
        self.update = to_raw_response_wrapper(
            plans.update,
        )
        self.list = to_raw_response_wrapper(
            plans.list,
        )
        self.fetch = to_raw_response_wrapper(
            plans.fetch,
        )


class AsyncPlansWithRawResponse:
    def __init__(self, plans: AsyncPlans) -> None:
        self.external_plan_id = AsyncExternalPlanIDWithRawResponse(plans.external_plan_id)

        self.create = async_to_raw_response_wrapper(
            plans.create,
        )
        self.update = async_to_raw_response_wrapper(
            plans.update,
        )
        self.list = async_to_raw_response_wrapper(
            plans.list,
        )
        self.fetch = async_to_raw_response_wrapper(
            plans.fetch,
        )
