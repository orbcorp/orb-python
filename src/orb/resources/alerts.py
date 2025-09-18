# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    alert_list_params,
    alert_enable_params,
    alert_update_params,
    alert_disable_params,
    alert_create_for_customer_params,
    alert_create_for_subscription_params,
    alert_create_for_external_customer_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from ..types.alert import Alert
from .._base_client import AsyncPaginator, make_request_options
from ..types.threshold_param import ThresholdParam

__all__ = ["Alerts", "AsyncAlerts"]


class Alerts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlertsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AlertsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        thresholds: Iterable[ThresholdParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[Alert]:
        """
        This endpoint returns a list of alerts within Orb.

        The request must specify one of `customer_id`, `external_customer_id`, or
        `subscription_id`.

        If querying by subscription_id, the endpoint will return the subscription level
        alerts as well as the plan level alerts associated with the subscription.

        The list of alerts is ordered starting from the most recently created alert.
        This endpoint follows Orb's
        [standardized pagination format](/api-reference/pagination).

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
        type: Literal["credit_balance_depleted", "credit_balance_dropped", "credit_balance_recovered"],
        thresholds: Optional[Iterable[ThresholdParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per [credit balance currency](/product-catalog/prepurchase).
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
        type: Literal["credit_balance_depleted", "credit_balance_dropped", "credit_balance_recovered"],
        thresholds: Optional[Iterable[ThresholdParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per [credit balance currency](/product-catalog/prepurchase).
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
        thresholds: Iterable[ThresholdParam],
        type: Literal["usage_exceeded", "cost_exceeded"],
        metric_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint allows you to disable an alert.

        To disable a plan-level alert for
        a specific subscription, you must include the `subscription_id`. The
        `subscription_id` is not required for customer or subscription level alerts.

        Args:
          subscription_id: Used to update the status of a plan alert scoped to this subscription_id

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
                query=maybe_transform({"subscription_id": subscription_id}, alert_disable_params.AlertDisableParams),
            ),
            cast_to=Alert,
        )

    def enable(
        self,
        alert_configuration_id: str,
        *,
        subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint allows you to enable an alert.

        To enable a plan-level alert for a
        specific subscription, you must include the `subscription_id`. The
        `subscription_id` is not required for customer or subscription level alerts.

        Args:
          subscription_id: Used to update the status of a plan alert scoped to this subscription_id

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
                query=maybe_transform({"subscription_id": subscription_id}, alert_enable_params.AlertEnableParams),
            ),
            cast_to=Alert,
        )


class AsyncAlerts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlertsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        thresholds: Iterable[ThresholdParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        created_at_gt: Union[str, datetime, None] | Omit = omit,
        created_at_gte: Union[str, datetime, None] | Omit = omit,
        created_at_lt: Union[str, datetime, None] | Omit = omit,
        created_at_lte: Union[str, datetime, None] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        customer_id: Optional[str] | Omit = omit,
        external_customer_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Alert, AsyncPage[Alert]]:
        """
        This endpoint returns a list of alerts within Orb.

        The request must specify one of `customer_id`, `external_customer_id`, or
        `subscription_id`.

        If querying by subscription_id, the endpoint will return the subscription level
        alerts as well as the plan level alerts associated with the subscription.

        The list of alerts is ordered starting from the most recently created alert.
        This endpoint follows Orb's
        [standardized pagination format](/api-reference/pagination).

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
        type: Literal["credit_balance_depleted", "credit_balance_dropped", "credit_balance_recovered"],
        thresholds: Optional[Iterable[ThresholdParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per [credit balance currency](/product-catalog/prepurchase).
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
        type: Literal["credit_balance_depleted", "credit_balance_dropped", "credit_balance_recovered"],
        thresholds: Optional[Iterable[ThresholdParam]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint creates a new alert to monitor a customer's credit balance.

        There
        are three types of alerts that can be scoped to customers:
        `credit_balance_depleted`, `credit_balance_dropped`, and
        `credit_balance_recovered`. Customers can have a maximum of one of each type of
        alert per [credit balance currency](/product-catalog/prepurchase).
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
        thresholds: Iterable[ThresholdParam],
        type: Literal["usage_exceeded", "cost_exceeded"],
        metric_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint allows you to disable an alert.

        To disable a plan-level alert for
        a specific subscription, you must include the `subscription_id`. The
        `subscription_id` is not required for customer or subscription level alerts.

        Args:
          subscription_id: Used to update the status of a plan alert scoped to this subscription_id

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
                query=await async_maybe_transform(
                    {"subscription_id": subscription_id}, alert_disable_params.AlertDisableParams
                ),
            ),
            cast_to=Alert,
        )

    async def enable(
        self,
        alert_configuration_id: str,
        *,
        subscription_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint allows you to enable an alert.

        To enable a plan-level alert for a
        specific subscription, you must include the `subscription_id`. The
        `subscription_id` is not required for customer or subscription level alerts.

        Args:
          subscription_id: Used to update the status of a plan alert scoped to this subscription_id

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
                query=await async_maybe_transform(
                    {"subscription_id": subscription_id}, alert_enable_params.AlertEnableParams
                ),
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
