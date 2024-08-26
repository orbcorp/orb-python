# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.alert import Alert

from .._base_client import make_request_options, AsyncPaginator

from .._utils import maybe_transform, async_maybe_transform

from typing import Iterable, Union, Optional

from ..pagination import SyncPage, AsyncPage

from datetime import datetime

from typing_extensions import Literal

from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ..types import (
    alert_update_params,
    alert_create_for_customer_params,
    alert_create_for_external_customer_params,
    alert_create_for_subscription_params,
)

from .. import _legacy_response

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from ..types import shared_params
from ..types import alert_update_params
from ..types import alert_list_params
from ..types import alert_create_for_customer_params
from ..types import alert_create_for_external_customer_params
from ..types import alert_create_for_subscription_params

__all__ = ["Alerts", "AsyncAlerts"]


class Alerts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlertsWithRawResponse:
        return AlertsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertsWithStreamingResponse:
        return AlertsWithStreamingResponse(self)

    def retrieve(
        self,
        alert_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Alert:
        """
        This endpoint retrieves an alert by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        return self._get(
            f"/alerts/{alert_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Alert,
        )

    def update(
        self,
        alert_configuration_id: str,
        *,
        thresholds: Iterable[alert_update_params.Threshold],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint updates the thresholds of an alert.

        Args:
          thresholds: The thresholds that define the values at which the alert will be triggered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not alert_configuration_id:
            raise ValueError(
                f"Expected a non-empty value for `alert_configuration_id` but received {alert_configuration_id!r}"
            )
        return self._put(
            f"/alerts/{alert_configuration_id}",
            body=maybe_transform({"thresholds": thresholds}, alert_update_params.AlertUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Alert]:
        """
        This endpoint returns a list of alerts within Orb.

        The request must specify one of `customer_id`, `external_customer_id`, or
        `subscription_id`.

        If querying by subscripion_id, the endpoint will return the subscription level
        alerts as well as the plan level alerts associated with the subscription.

        The list of alerts is ordered starting from the most recently created alert.
        This endpoint follows Orb's
        [standardized pagination format](../reference/pagination).

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          customer_id: Fetch alerts scoped to this customer_id

          external_customer_id: Fetch alerts scoped to this external_customer_id

          limit: The number of items to fetch. Defaults to 20.

          subscription_id: Fetch alerts scoped to this subscription_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/alerts",
            page=SyncPage[Alert],
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
                        "customer_id": customer_id,
                        "external_customer_id": external_customer_id,
                        "limit": limit,
                        "subscription_id": subscription_id,
                    },
                    alert_list_params.AlertListParams,
                ),
            ),
            model=Alert,
        )

    def create_for_customer(
        self,
        customer_id: str,
        *,
        currency: str,
        type: Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ],
        thresholds: Optional[Iterable[alert_create_for_customer_params.Threshold]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per
        [credit balance currency](https://docs.withorb.com/guides/product-catalog/prepurchase).
        `credit_balance_dropped` alerts require a list of thresholds to be provided
        while `credit_balance_depleted` and `credit_balance_recovered` alerts do not
        require thresholds.

        Args:
          currency: The case sensitive currency or custom pricing unit to use for this alert.

          type: The type of alert to create. This must be a valid alert type.

          thresholds: The thresholds that define the values at which the alert will be triggered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/alerts/customer_id/{customer_id}",
            body=maybe_transform(
                {
                    "currency": currency,
                    "type": type,
                    "thresholds": thresholds,
                },
                alert_create_for_customer_params.AlertCreateForCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    def create_for_external_customer(
        self,
        external_customer_id: str,
        *,
        currency: str,
        type: Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ],
        thresholds: Optional[Iterable[alert_create_for_external_customer_params.Threshold]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per
        [credit balance currency](https://docs.withorb.com/guides/product-catalog/prepurchase).
        `credit_balance_dropped` alerts require a list of thresholds to be provided
        while `credit_balance_depleted` and `credit_balance_recovered` alerts do not
        require thresholds.

        Args:
          currency: The case sensitive currency or custom pricing unit to use for this alert.

          type: The type of alert to create. This must be a valid alert type.

          thresholds: The thresholds that define the values at which the alert will be triggered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._post(
            f"/alerts/external_customer_id/{external_customer_id}",
            body=maybe_transform(
                {
                    "currency": currency,
                    "type": type,
                    "thresholds": thresholds,
                },
                alert_create_for_external_customer_params.AlertCreateForExternalCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    def create_for_subscription(
        self,
        subscription_id: str,
        *,
        thresholds: Iterable[alert_create_for_subscription_params.Threshold],
        type: Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ],
        metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint is used to create alerts at the subscription level.

        Subscription level alerts can be one of two types: `usage_exceeded` or
        `cost_exceeded`. A `usage_exceeded` alert is scoped to a particular metric and
        is triggered when the usage of that metric exceeds predefined thresholds during
        the current billing cycle. A `cost_exceeded` alert is triggered when the total
        amount due during the current billing cycle surpasses predefined thresholds.
        `cost_exceeded` alerts do not include burndown of pre-purchase credits. Each
        subscription can have one `cost_exceeded` alert and one `usage_exceeded` alert
        per metric that is a part of the subscription. Alerts are triggered based on
        usage or cost conditions met during the current billing cycle.

        Args:
          thresholds: The thresholds that define the values at which the alert will be triggered.

          type: The type of alert to create. This must be a valid alert type.

          metric_id: The metric to track usage for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._post(
            f"/alerts/subscription_id/{subscription_id}",
            body=maybe_transform(
                {
                    "thresholds": thresholds,
                    "type": type,
                    "metric_id": metric_id,
                },
                alert_create_for_subscription_params.AlertCreateForSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    def disable(
        self,
        alert_configuration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint can be used to disable an alert.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not alert_configuration_id:
            raise ValueError(
                f"Expected a non-empty value for `alert_configuration_id` but received {alert_configuration_id!r}"
            )
        return self._post(
            f"/alerts/{alert_configuration_id}/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    def enable(
        self,
        alert_configuration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint can be used to enable an alert.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not alert_configuration_id:
            raise ValueError(
                f"Expected a non-empty value for `alert_configuration_id` but received {alert_configuration_id!r}"
            )
        return self._post(
            f"/alerts/{alert_configuration_id}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )


class AsyncAlerts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlertsWithRawResponse:
        return AsyncAlertsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertsWithStreamingResponse:
        return AsyncAlertsWithStreamingResponse(self)

    async def retrieve(
        self,
        alert_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Alert:
        """
        This endpoint retrieves an alert by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alert_id:
            raise ValueError(f"Expected a non-empty value for `alert_id` but received {alert_id!r}")
        return await self._get(
            f"/alerts/{alert_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Alert,
        )

    async def update(
        self,
        alert_configuration_id: str,
        *,
        thresholds: Iterable[alert_update_params.Threshold],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint updates the thresholds of an alert.

        Args:
          thresholds: The thresholds that define the values at which the alert will be triggered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not alert_configuration_id:
            raise ValueError(
                f"Expected a non-empty value for `alert_configuration_id` but received {alert_configuration_id!r}"
            )
        return await self._put(
            f"/alerts/{alert_configuration_id}",
            body=await async_maybe_transform({"thresholds": thresholds}, alert_update_params.AlertUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    def list(
        self,
        *,
        created_at_gt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_gte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lt: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        created_at_lte: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        external_customer_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Alert, AsyncPage[Alert]]:
        """
        This endpoint returns a list of alerts within Orb.

        The request must specify one of `customer_id`, `external_customer_id`, or
        `subscription_id`.

        If querying by subscripion_id, the endpoint will return the subscription level
        alerts as well as the plan level alerts associated with the subscription.

        The list of alerts is ordered starting from the most recently created alert.
        This endpoint follows Orb's
        [standardized pagination format](../reference/pagination).

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          customer_id: Fetch alerts scoped to this customer_id

          external_customer_id: Fetch alerts scoped to this external_customer_id

          limit: The number of items to fetch. Defaults to 20.

          subscription_id: Fetch alerts scoped to this subscription_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/alerts",
            page=AsyncPage[Alert],
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
                        "customer_id": customer_id,
                        "external_customer_id": external_customer_id,
                        "limit": limit,
                        "subscription_id": subscription_id,
                    },
                    alert_list_params.AlertListParams,
                ),
            ),
            model=Alert,
        )

    async def create_for_customer(
        self,
        customer_id: str,
        *,
        currency: str,
        type: Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ],
        thresholds: Optional[Iterable[alert_create_for_customer_params.Threshold]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per
        [credit balance currency](https://docs.withorb.com/guides/product-catalog/prepurchase).
        `credit_balance_dropped` alerts require a list of thresholds to be provided
        while `credit_balance_depleted` and `credit_balance_recovered` alerts do not
        require thresholds.

        Args:
          currency: The case sensitive currency or custom pricing unit to use for this alert.

          type: The type of alert to create. This must be a valid alert type.

          thresholds: The thresholds that define the values at which the alert will be triggered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/alerts/customer_id/{customer_id}",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "type": type,
                    "thresholds": thresholds,
                },
                alert_create_for_customer_params.AlertCreateForCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    async def create_for_external_customer(
        self,
        external_customer_id: str,
        *,
        currency: str,
        type: Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ],
        thresholds: Optional[Iterable[alert_create_for_external_customer_params.Threshold]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per
        [credit balance currency](https://docs.withorb.com/guides/product-catalog/prepurchase).
        `credit_balance_dropped` alerts require a list of thresholds to be provided
        while `credit_balance_depleted` and `credit_balance_recovered` alerts do not
        require thresholds.

        Args:
          currency: The case sensitive currency or custom pricing unit to use for this alert.

          type: The type of alert to create. This must be a valid alert type.

          thresholds: The thresholds that define the values at which the alert will be triggered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return await self._post(
            f"/alerts/external_customer_id/{external_customer_id}",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "type": type,
                    "thresholds": thresholds,
                },
                alert_create_for_external_customer_params.AlertCreateForExternalCustomerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    async def create_for_subscription(
        self,
        subscription_id: str,
        *,
        thresholds: Iterable[alert_create_for_subscription_params.Threshold],
        type: Literal[
            "usage_exceeded",
            "cost_exceeded",
            "credit_balance_depleted",
            "credit_balance_dropped",
            "credit_balance_recovered",
        ],
        metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint is used to create alerts at the subscription level.

        Subscription level alerts can be one of two types: `usage_exceeded` or
        `cost_exceeded`. A `usage_exceeded` alert is scoped to a particular metric and
        is triggered when the usage of that metric exceeds predefined thresholds during
        the current billing cycle. A `cost_exceeded` alert is triggered when the total
        amount due during the current billing cycle surpasses predefined thresholds.
        `cost_exceeded` alerts do not include burndown of pre-purchase credits. Each
        subscription can have one `cost_exceeded` alert and one `usage_exceeded` alert
        per metric that is a part of the subscription. Alerts are triggered based on
        usage or cost conditions met during the current billing cycle.

        Args:
          thresholds: The thresholds that define the values at which the alert will be triggered.

          type: The type of alert to create. This must be a valid alert type.

          metric_id: The metric to track usage for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._post(
            f"/alerts/subscription_id/{subscription_id}",
            body=await async_maybe_transform(
                {
                    "thresholds": thresholds,
                    "type": type,
                    "metric_id": metric_id,
                },
                alert_create_for_subscription_params.AlertCreateForSubscriptionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    async def disable(
        self,
        alert_configuration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint can be used to disable an alert.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not alert_configuration_id:
            raise ValueError(
                f"Expected a non-empty value for `alert_configuration_id` but received {alert_configuration_id!r}"
            )
        return await self._post(
            f"/alerts/{alert_configuration_id}/disable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )

    async def enable(
        self,
        alert_configuration_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """
        This endpoint can be used to enable an alert.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not alert_configuration_id:
            raise ValueError(
                f"Expected a non-empty value for `alert_configuration_id` but received {alert_configuration_id!r}"
            )
        return await self._post(
            f"/alerts/{alert_configuration_id}/enable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Alert,
        )


class AlertsWithRawResponse:
    def __init__(self, alerts: Alerts) -> None:
        self._alerts = alerts

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            alerts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = _legacy_response.to_raw_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = _legacy_response.to_raw_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_subscription = _legacy_response.to_raw_response_wrapper(
            alerts.create_for_subscription,
        )
        self.disable = _legacy_response.to_raw_response_wrapper(
            alerts.disable,
        )
        self.enable = _legacy_response.to_raw_response_wrapper(
            alerts.enable,
        )


class AsyncAlertsWithRawResponse:
    def __init__(self, alerts: AsyncAlerts) -> None:
        self._alerts = alerts

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            alerts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = _legacy_response.async_to_raw_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = _legacy_response.async_to_raw_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_subscription = _legacy_response.async_to_raw_response_wrapper(
            alerts.create_for_subscription,
        )
        self.disable = _legacy_response.async_to_raw_response_wrapper(
            alerts.disable,
        )
        self.enable = _legacy_response.async_to_raw_response_wrapper(
            alerts.enable,
        )


class AlertsWithStreamingResponse:
    def __init__(self, alerts: Alerts) -> None:
        self._alerts = alerts

        self.retrieve = to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            alerts.update,
        )
        self.list = to_streamed_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = to_streamed_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = to_streamed_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_subscription = to_streamed_response_wrapper(
            alerts.create_for_subscription,
        )
        self.disable = to_streamed_response_wrapper(
            alerts.disable,
        )
        self.enable = to_streamed_response_wrapper(
            alerts.enable,
        )


class AsyncAlertsWithStreamingResponse:
    def __init__(self, alerts: AsyncAlerts) -> None:
        self._alerts = alerts

        self.retrieve = async_to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            alerts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = async_to_streamed_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = async_to_streamed_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_subscription = async_to_streamed_response_wrapper(
            alerts.create_for_subscription,
        )
        self.disable = async_to_streamed_response_wrapper(
            alerts.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            alerts.enable,
        )
