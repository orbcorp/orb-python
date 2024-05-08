# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..types.alert import Alert
from .._base_client import (
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

        self.enable = _legacy_response.to_raw_response_wrapper(
            alerts.enable,
        )


class AsyncAlertsWithRawResponse:
    def __init__(self, alerts: AsyncAlerts) -> None:
        self._alerts = alerts

        self.enable = _legacy_response.async_to_raw_response_wrapper(
            alerts.enable,
        )


class AlertsWithStreamingResponse:
    def __init__(self, alerts: Alerts) -> None:
        self._alerts = alerts

        self.enable = to_streamed_response_wrapper(
            alerts.enable,
        )


class AsyncAlertsWithStreamingResponse:
    def __init__(self, alerts: AsyncAlerts) -> None:
        self._alerts = alerts

        self.enable = async_to_streamed_response_wrapper(
            alerts.enable,
        )
