# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import (
    alert_list_params,
    alert_enable_params,
    alert_disable_params,
    alert_create_for_plan_params,
    alert_create_for_customer_params,
    alert_create_for_subscription_params,
    alert_create_for_external_customer_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from ..types.alert import Alert
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

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
        plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        plan_version: Optional[int] | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Alert]:
        """
        This endpoint returns a list of all
        [`alerts`](https://docs.withorb.com/guides/product-catalog/configuring-alerts).

        The list of alerts is ordered starting from the most recently created alert.
        This endpoint follows Orb's
        [standardized pagination format](../reference/pagination).

        The request must specify one of customer_id, external_customer_id,
        subscription_id, or plan_id

        If querying by subscripion_id, the endpoint will return the subscription level
        alerts as well as the plan level alerts associated with the subscription.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          customer_id: Fetch alerts scoped to this customer_id

          external_customer_id: Fetch alerts scoped to this external_customer_id

          limit: The number of items to fetch. Defaults to 20.

          plan_id: Fetch alerts scoped to this plan_id

          plan_version: If provided alongside plan_id, only the alerts that are scoped to the specified plan_version will be returned.

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
                        "plan_id": plan_id,
                        "plan_version": plan_version,
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
        type: str,
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

          type: The thresholds that define the values at which the alert will be triggered.

          thresholds: The thresholds for the alert.

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
        type: str,
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

          type: The thresholds that define the values at which the alert will be triggered.

          thresholds: The thresholds for the alert.

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

    def create_for_plan(
        self,
        plan_id: str,
        *,
        thresholds: Iterable[alert_create_for_plan_params.Threshold],
        type: str,
        metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        plan_version: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint is used to create alerts at the plan level.

        Plan level alerts are
        automatically propagated to all subscriptions associated with the plan. These
        alerts are scoped to a specific plan version; if no version is specified, the
        active plan version is used.

        Plan level alerts can be of two types: `usage_exceeded` or `cost_exceeded`. A
        `usage_exceeded` alert is scoped to a particular metric and is triggered when
        the usage of that metric exceeds a predefined thresholds during the current
        invoice cycle. A `cost_exceeded` alert is triggered when the total cost of the
        subscription on the plan surpasses predefined thresholds in the current invoice
        cycle.Each plan can have one `cost_exceeded` alert and one `usage_exceeded`
        alert per metric that is apart of the plan.

        Args:
          thresholds: The thresholds for the alert.

          type: The thresholds that define the values at which the alert will be triggered.

          metric_id: The metric to track usage for.

          plan_version: The plan version to create alerts for. If not specified, the default will be the plan's active plan version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._post(
            f"/alerts/plan_id/{plan_id}",
            body=maybe_transform(
                {
                    "thresholds": thresholds,
                    "type": type,
                    "metric_id": metric_id,
                    "plan_version": plan_version,
                },
                alert_create_for_plan_params.AlertCreateForPlanParams,
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
        type: str,
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
        is triggered when the usage of that metric exceeds a predefined thresholds
        during the current invoice cycle. A `cost_exceeded` alert is triggered when the
        total cost of the subscription surpasses predefined thresholds in the current
        invoice cycle. Each subscription can have one `cost_exceeded` alert and one
        `usage_exceeded` alert per metric that is apart of the subscription. Alerts are
        triggered based on usage or cost conditions met during the current invoice
        cycle.

        Args:
          thresholds: The thresholds for the alert.

          type: The thresholds that define the values at which the alert will be triggered.

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
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
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

        By default, disabling a plan level alert will apply to all subscriptions on that
        plan. In order to toggle a plan level alert for a specific subscription, the
        client must provide the plan level alert id as well as the subscription_id
        parameter.

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
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
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

        By default, enabling a plan level alert will apply to all subscriptions on that
        plan. In order to toggle a plan level alert for a specific subscription, the
        client must provide the plan level alert id as well as the subscription_id
        parameter.

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
        plan_id: Optional[str] | NotGiven = NOT_GIVEN,
        plan_version: Optional[int] | NotGiven = NOT_GIVEN,
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Alert, AsyncPage[Alert]]:
        """
        This endpoint returns a list of all
        [`alerts`](https://docs.withorb.com/guides/product-catalog/configuring-alerts).

        The list of alerts is ordered starting from the most recently created alert.
        This endpoint follows Orb's
        [standardized pagination format](../reference/pagination).

        The request must specify one of customer_id, external_customer_id,
        subscription_id, or plan_id

        If querying by subscripion_id, the endpoint will return the subscription level
        alerts as well as the plan level alerts associated with the subscription.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          customer_id: Fetch alerts scoped to this customer_id

          external_customer_id: Fetch alerts scoped to this external_customer_id

          limit: The number of items to fetch. Defaults to 20.

          plan_id: Fetch alerts scoped to this plan_id

          plan_version: If provided alongside plan_id, only the alerts that are scoped to the specified plan_version will be returned.

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
                        "plan_id": plan_id,
                        "plan_version": plan_version,
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
        type: str,
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

          type: The thresholds that define the values at which the alert will be triggered.

          thresholds: The thresholds for the alert.

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
        type: str,
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

          type: The thresholds that define the values at which the alert will be triggered.

          thresholds: The thresholds for the alert.

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

    async def create_for_plan(
        self,
        plan_id: str,
        *,
        thresholds: Iterable[alert_create_for_plan_params.Threshold],
        type: str,
        metric_id: Optional[str] | NotGiven = NOT_GIVEN,
        plan_version: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Alert:
        """This endpoint is used to create alerts at the plan level.

        Plan level alerts are
        automatically propagated to all subscriptions associated with the plan. These
        alerts are scoped to a specific plan version; if no version is specified, the
        active plan version is used.

        Plan level alerts can be of two types: `usage_exceeded` or `cost_exceeded`. A
        `usage_exceeded` alert is scoped to a particular metric and is triggered when
        the usage of that metric exceeds a predefined thresholds during the current
        invoice cycle. A `cost_exceeded` alert is triggered when the total cost of the
        subscription on the plan surpasses predefined thresholds in the current invoice
        cycle.Each plan can have one `cost_exceeded` alert and one `usage_exceeded`
        alert per metric that is apart of the plan.

        Args:
          thresholds: The thresholds for the alert.

          type: The thresholds that define the values at which the alert will be triggered.

          metric_id: The metric to track usage for.

          plan_version: The plan version to create alerts for. If not specified, the default will be the plan's active plan version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._post(
            f"/alerts/plan_id/{plan_id}",
            body=await async_maybe_transform(
                {
                    "thresholds": thresholds,
                    "type": type,
                    "metric_id": metric_id,
                    "plan_version": plan_version,
                },
                alert_create_for_plan_params.AlertCreateForPlanParams,
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
        type: str,
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
        is triggered when the usage of that metric exceeds a predefined thresholds
        during the current invoice cycle. A `cost_exceeded` alert is triggered when the
        total cost of the subscription surpasses predefined thresholds in the current
        invoice cycle. Each subscription can have one `cost_exceeded` alert and one
        `usage_exceeded` alert per metric that is apart of the subscription. Alerts are
        triggered based on usage or cost conditions met during the current invoice
        cycle.

        Args:
          thresholds: The thresholds for the alert.

          type: The thresholds that define the values at which the alert will be triggered.

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
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
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

        By default, disabling a plan level alert will apply to all subscriptions on that
        plan. In order to toggle a plan level alert for a specific subscription, the
        client must provide the plan level alert id as well as the subscription_id
        parameter.

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
        subscription_id: Optional[str] | NotGiven = NOT_GIVEN,
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

        By default, enabling a plan level alert will apply to all subscriptions on that
        plan. In order to toggle a plan level alert for a specific subscription, the
        client must provide the plan level alert id as well as the subscription_id
        parameter.

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
        self.list = _legacy_response.to_raw_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = _legacy_response.to_raw_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = _legacy_response.to_raw_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_plan = _legacy_response.to_raw_response_wrapper(
            alerts.create_for_plan,
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
        self.list = _legacy_response.async_to_raw_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = _legacy_response.async_to_raw_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = _legacy_response.async_to_raw_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_plan = _legacy_response.async_to_raw_response_wrapper(
            alerts.create_for_plan,
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
        self.list = to_streamed_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = to_streamed_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = to_streamed_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_plan = to_streamed_response_wrapper(
            alerts.create_for_plan,
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
        self.list = async_to_streamed_response_wrapper(
            alerts.list,
        )
        self.create_for_customer = async_to_streamed_response_wrapper(
            alerts.create_for_customer,
        )
        self.create_for_external_customer = async_to_streamed_response_wrapper(
            alerts.create_for_external_customer,
        )
        self.create_for_plan = async_to_streamed_response_wrapper(
            alerts.create_for_plan,
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
