# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.customers import (
    UsageUpdateResponse,
    UsageUpdateByExternalIDResponse,
    usage_update_params,
    usage_update_by_external_id_params,
)

__all__ = ["Usage", "AsyncUsage"]


class Usage(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageWithRawResponse:
        return UsageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageWithStreamingResponse:
        return UsageWithStreamingResponse(self)

    def update(
        self,
        id: Optional[str],
        *,
        events: Iterable[usage_update_params.Event],
        timeframe_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> UsageUpdateResponse:
        """
        This endpoint is used to amend usage within a timeframe for a customer that has
        an active subscription.

        This endpoint will mark _all_ existing events within
        `[timeframe_start, timeframe_end)` as _ignored_ for billing purposes, and Orb
        will only use the _new_ events passed in the body of this request as the source
        of truth for that timeframe moving forwards. Note that a given time period can
        be amended any number of times, so events can be overwritten in subsequent calls
        to th is endpoint.

        This is a powerful and audit-safe mechanism to retroactively change usage data
        in cases where you need to:

        - decrease historical usage consumption because of degraded service availability
          in your systems
        - account for gaps from your usage reporting mechanism
        - make point-in-time fixes for specific event records, while retaining the
          original time of usage and associated metadata. This amendment API is designed
          with two explicit goals:

        1. Amendments are **always audit-safe**. The amendment process will still retain
           original events in the timeframe, though they will be ignored for billing
           calculations. For auditing a nd data fidelity purposes, Orb never overwrites
           or permanently deletes ingested usage data.
        2. Amendments always preserve data **consistency**. In other words, either an
           amendment is fully processed by the system (and the new events for the
           timeframe are honored rather than the existing ones) or the amendment request
           fails. To maintain this important property, Orb prevents _partial event
           ingestion_ on this endpoint.

        ## Response semantics

        - Either all events are ingested successfully, or all fail to ingest (returning
          a `4xx` or `5xx` response code).
        - Any event that fails schema validation will lead to a `4xx` response. In this
          case, to maintain data consistency, Orb will not ingest any events and will
          also not deprecate existing events in the time period.
        - You can assume that the amendment is successful on receipt of a `2xx`
          response.While a successful response from this endpoint indicates that the new
          events have been ingested, updating usage totals happens asynchronously and
          may be delayed by a few minutes.

        As emphasized above, Orb will never show an inconsistent state (e.g. in invoice
        previews or dashboards); either it will show the existing state (before the
        amendment) or the new state (with new events in the requested timeframe).

        ## Sample request body

        ```json
        {
          "events": [
            {
              "event_name": "payment_processed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            },
            {
              "event_name": "payment_failed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            }
          ]
        }
        ```

        ## Request Validation

        - The `timestamp` of each event reported must fall within the bounds of
          `timeframe_start` and `timeframe_end`. As with ingestion, all timesta mps must
          be sent in ISO8601 format with UTC timezone offset.
        - Orb **does not accept an `idempotency_key`** with each event in this endpoint,
          since the entirety of the event list must be ingested to ensure consistency.
          On retryable errors , you should retry the request in its entirety, and assume
          that the amendment operation has not succeeded until receipt of a `2xx`.

        - Both `timeframe_start` and `timeframe_end` must be timestamps in the past.
          Furthermore, Orb will genera lly validate that the `timeframe_start` and
          `timeframe_end` fall within the customer's _current_ subscription billing pe
          riod. However, Orb does allow amendments while in the grace period of the
          previous billing period; in this instance, the timeframe can start before the
          current period.

        ## API Limits

        Note that Orb does not currently enforce a hard rate- limit for API usage or a
        maximum request payload size. Similar to the event ingestion API, this API is
        architected for h igh-throughput ingestion. It is also safe to
        _programmatically_ call this endpoint if your system can automatically dete ct a
        need for historical amendment.

        In order to overwrite timeframes with a very large number of events, we suggest
        using multiple calls with small adjacent (e.g. every hour) timeframes.

        Args:
          events: Events to update

          timeframe_end: This bound is exclusive (i.e. events before this timestamp will be updated)

          timeframe_start: This bound is inclusive (i.e. events with this timestamp onward, inclusive will
              be updated)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/customers/{id}/usage",
            body=maybe_transform({"events": events}, usage_update_params.UsageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                    },
                    usage_update_params.UsageUpdateParams,
                ),
            ),
            cast_to=UsageUpdateResponse,
        )

    def update_by_external_id(
        self,
        id: Optional[str],
        *,
        events: Iterable[usage_update_by_external_id_params.Event],
        timeframe_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> UsageUpdateByExternalIDResponse:
        """
        This endpoint is used to amend usage within a timeframe for a customer that has
        an active subscription.

        This endpoint will mark _all_ existing events within
        `[timeframe_start, timeframe_end)` as _ignored_ for billing purposes, and Orb
        will only use the _new_ events passed in the body of this request as the source
        of truth for that timeframe moving forwards. Note that a given time period can
        be amended any number of times, so events can be overwritten in subsequent calls
        to th is endpoint.

        This is a powerful and audit-safe mechanism to retroactively change usage data
        in cases where you need to:

        - decrease historical usage consumption because of degraded service availability
          in your systems
        - account for gaps from your usage reporting mechanism
        - make point-in-time fixes for specific event records, while retaining the
          original time of usage and associated metadata. This amendment API is designed
          with two explicit goals:

        1. Amendments are **always audit-safe**. The amendment process will still retain
           original events in the timeframe, though they will be ignored for billing
           calculations. For auditing a nd data fidelity purposes, Orb never overwrites
           or permanently deletes ingested usage data.
        2. Amendments always preserve data **consistency**. In other words, either an
           amendment is fully processed by the system (and the new events for the
           timeframe are honored rather than the existing ones) or the amendment request
           fails. To maintain this important property, Orb prevents _partial event
           ingestion_ on this endpoint.

        ## Response semantics

        - Either all events are ingested successfully, or all fail to ingest (returning
          a `4xx` or `5xx` response code).
        - Any event that fails schema validation will lead to a `4xx` response. In this
          case, to maintain data consistency, Orb will not ingest any events and will
          also not deprecate existing events in the time period.
        - You can assume that the amendment is successful on receipt of a `2xx`
          response.While a successful response from this endpoint indicates that the new
          events have been ingested, updating usage totals happens asynchronously and
          may be delayed by a few minutes.

        As emphasized above, Orb will never show an inconsistent state (e.g. in invoice
        previews or dashboards); either it will show the existing state (before the
        amendment) or the new state (with new events in the requested timeframe).

        ## Sample request body

        ```json
        {
          "events": [
            {
              "event_name": "payment_processed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            },
            {
              "event_name": "payment_failed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            }
          ]
        }
        ```

        ## Request Validation

        - The `timestamp` of each event reported must fall within the bounds of
          `timeframe_start` and `timeframe_end`. As with ingestion, all timesta mps must
          be sent in ISO8601 format with UTC timezone offset.
        - Orb **does not accept an `idempotency_key`** with each event in this endpoint,
          since the entirety of the event list must be ingested to ensure consistency.
          On retryable errors , you should retry the request in its entirety, and assume
          that the amendment operation has not succeeded until receipt of a `2xx`.

        - Both `timeframe_start` and `timeframe_end` must be timestamps in the past.
          Furthermore, Orb will genera lly validate that the `timeframe_start` and
          `timeframe_end` fall within the customer's _current_ subscription billing pe
          riod. However, Orb does allow amendments while in the grace period of the
          previous billing period; in this instance, the timeframe can start before the
          current period.

        ## API Limits

        Note that Orb does not currently enforce a hard rate- limit for API usage or a
        maximum request payload size. Similar to the event ingestion API, this API is
        architected for h igh-throughput ingestion. It is also safe to
        _programmatically_ call this endpoint if your system can automatically dete ct a
        need for historical amendment.

        In order to overwrite timeframes with a very large number of events, we suggest
        using multiple calls with small adjacent (e.g. every hour) timeframes.

        Args:
          events: Events to update

          timeframe_end: This bound is exclusive (i.e. events before this timestamp will be updated)

          timeframe_start: This bound is inclusive (i.e. events with this timestamp onward, inclusive will
              be updated)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/customers/external_customer_id/{id}/usage",
            body=maybe_transform({"events": events}, usage_update_by_external_id_params.UsageUpdateByExternalIDParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                    },
                    usage_update_by_external_id_params.UsageUpdateByExternalIDParams,
                ),
            ),
            cast_to=UsageUpdateByExternalIDResponse,
        )


class AsyncUsage(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageWithRawResponse:
        return AsyncUsageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageWithStreamingResponse:
        return AsyncUsageWithStreamingResponse(self)

    async def update(
        self,
        id: Optional[str],
        *,
        events: Iterable[usage_update_params.Event],
        timeframe_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> UsageUpdateResponse:
        """
        This endpoint is used to amend usage within a timeframe for a customer that has
        an active subscription.

        This endpoint will mark _all_ existing events within
        `[timeframe_start, timeframe_end)` as _ignored_ for billing purposes, and Orb
        will only use the _new_ events passed in the body of this request as the source
        of truth for that timeframe moving forwards. Note that a given time period can
        be amended any number of times, so events can be overwritten in subsequent calls
        to th is endpoint.

        This is a powerful and audit-safe mechanism to retroactively change usage data
        in cases where you need to:

        - decrease historical usage consumption because of degraded service availability
          in your systems
        - account for gaps from your usage reporting mechanism
        - make point-in-time fixes for specific event records, while retaining the
          original time of usage and associated metadata. This amendment API is designed
          with two explicit goals:

        1. Amendments are **always audit-safe**. The amendment process will still retain
           original events in the timeframe, though they will be ignored for billing
           calculations. For auditing a nd data fidelity purposes, Orb never overwrites
           or permanently deletes ingested usage data.
        2. Amendments always preserve data **consistency**. In other words, either an
           amendment is fully processed by the system (and the new events for the
           timeframe are honored rather than the existing ones) or the amendment request
           fails. To maintain this important property, Orb prevents _partial event
           ingestion_ on this endpoint.

        ## Response semantics

        - Either all events are ingested successfully, or all fail to ingest (returning
          a `4xx` or `5xx` response code).
        - Any event that fails schema validation will lead to a `4xx` response. In this
          case, to maintain data consistency, Orb will not ingest any events and will
          also not deprecate existing events in the time period.
        - You can assume that the amendment is successful on receipt of a `2xx`
          response.While a successful response from this endpoint indicates that the new
          events have been ingested, updating usage totals happens asynchronously and
          may be delayed by a few minutes.

        As emphasized above, Orb will never show an inconsistent state (e.g. in invoice
        previews or dashboards); either it will show the existing state (before the
        amendment) or the new state (with new events in the requested timeframe).

        ## Sample request body

        ```json
        {
          "events": [
            {
              "event_name": "payment_processed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            },
            {
              "event_name": "payment_failed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            }
          ]
        }
        ```

        ## Request Validation

        - The `timestamp` of each event reported must fall within the bounds of
          `timeframe_start` and `timeframe_end`. As with ingestion, all timesta mps must
          be sent in ISO8601 format with UTC timezone offset.
        - Orb **does not accept an `idempotency_key`** with each event in this endpoint,
          since the entirety of the event list must be ingested to ensure consistency.
          On retryable errors , you should retry the request in its entirety, and assume
          that the amendment operation has not succeeded until receipt of a `2xx`.

        - Both `timeframe_start` and `timeframe_end` must be timestamps in the past.
          Furthermore, Orb will genera lly validate that the `timeframe_start` and
          `timeframe_end` fall within the customer's _current_ subscription billing pe
          riod. However, Orb does allow amendments while in the grace period of the
          previous billing period; in this instance, the timeframe can start before the
          current period.

        ## API Limits

        Note that Orb does not currently enforce a hard rate- limit for API usage or a
        maximum request payload size. Similar to the event ingestion API, this API is
        architected for h igh-throughput ingestion. It is also safe to
        _programmatically_ call this endpoint if your system can automatically dete ct a
        need for historical amendment.

        In order to overwrite timeframes with a very large number of events, we suggest
        using multiple calls with small adjacent (e.g. every hour) timeframes.

        Args:
          events: Events to update

          timeframe_end: This bound is exclusive (i.e. events before this timestamp will be updated)

          timeframe_start: This bound is inclusive (i.e. events with this timestamp onward, inclusive will
              be updated)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/customers/{id}/usage",
            body=maybe_transform({"events": events}, usage_update_params.UsageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                    },
                    usage_update_params.UsageUpdateParams,
                ),
            ),
            cast_to=UsageUpdateResponse,
        )

    async def update_by_external_id(
        self,
        id: Optional[str],
        *,
        events: Iterable[usage_update_by_external_id_params.Event],
        timeframe_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        timeframe_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> UsageUpdateByExternalIDResponse:
        """
        This endpoint is used to amend usage within a timeframe for a customer that has
        an active subscription.

        This endpoint will mark _all_ existing events within
        `[timeframe_start, timeframe_end)` as _ignored_ for billing purposes, and Orb
        will only use the _new_ events passed in the body of this request as the source
        of truth for that timeframe moving forwards. Note that a given time period can
        be amended any number of times, so events can be overwritten in subsequent calls
        to th is endpoint.

        This is a powerful and audit-safe mechanism to retroactively change usage data
        in cases where you need to:

        - decrease historical usage consumption because of degraded service availability
          in your systems
        - account for gaps from your usage reporting mechanism
        - make point-in-time fixes for specific event records, while retaining the
          original time of usage and associated metadata. This amendment API is designed
          with two explicit goals:

        1. Amendments are **always audit-safe**. The amendment process will still retain
           original events in the timeframe, though they will be ignored for billing
           calculations. For auditing a nd data fidelity purposes, Orb never overwrites
           or permanently deletes ingested usage data.
        2. Amendments always preserve data **consistency**. In other words, either an
           amendment is fully processed by the system (and the new events for the
           timeframe are honored rather than the existing ones) or the amendment request
           fails. To maintain this important property, Orb prevents _partial event
           ingestion_ on this endpoint.

        ## Response semantics

        - Either all events are ingested successfully, or all fail to ingest (returning
          a `4xx` or `5xx` response code).
        - Any event that fails schema validation will lead to a `4xx` response. In this
          case, to maintain data consistency, Orb will not ingest any events and will
          also not deprecate existing events in the time period.
        - You can assume that the amendment is successful on receipt of a `2xx`
          response.While a successful response from this endpoint indicates that the new
          events have been ingested, updating usage totals happens asynchronously and
          may be delayed by a few minutes.

        As emphasized above, Orb will never show an inconsistent state (e.g. in invoice
        previews or dashboards); either it will show the existing state (before the
        amendment) or the new state (with new events in the requested timeframe).

        ## Sample request body

        ```json
        {
          "events": [
            {
              "event_name": "payment_processed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            },
            {
              "event_name": "payment_failed",
              "timestamp": "2022-03-24T07:15:00Z",
              "properties": {
                "amount": 100
              }
            }
          ]
        }
        ```

        ## Request Validation

        - The `timestamp` of each event reported must fall within the bounds of
          `timeframe_start` and `timeframe_end`. As with ingestion, all timesta mps must
          be sent in ISO8601 format with UTC timezone offset.
        - Orb **does not accept an `idempotency_key`** with each event in this endpoint,
          since the entirety of the event list must be ingested to ensure consistency.
          On retryable errors , you should retry the request in its entirety, and assume
          that the amendment operation has not succeeded until receipt of a `2xx`.

        - Both `timeframe_start` and `timeframe_end` must be timestamps in the past.
          Furthermore, Orb will genera lly validate that the `timeframe_start` and
          `timeframe_end` fall within the customer's _current_ subscription billing pe
          riod. However, Orb does allow amendments while in the grace period of the
          previous billing period; in this instance, the timeframe can start before the
          current period.

        ## API Limits

        Note that Orb does not currently enforce a hard rate- limit for API usage or a
        maximum request payload size. Similar to the event ingestion API, this API is
        architected for h igh-throughput ingestion. It is also safe to
        _programmatically_ call this endpoint if your system can automatically dete ct a
        need for historical amendment.

        In order to overwrite timeframes with a very large number of events, we suggest
        using multiple calls with small adjacent (e.g. every hour) timeframes.

        Args:
          events: Events to update

          timeframe_end: This bound is exclusive (i.e. events before this timestamp will be updated)

          timeframe_start: This bound is inclusive (i.e. events with this timestamp onward, inclusive will
              be updated)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/customers/external_customer_id/{id}/usage",
            body=maybe_transform({"events": events}, usage_update_by_external_id_params.UsageUpdateByExternalIDParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "timeframe_end": timeframe_end,
                        "timeframe_start": timeframe_start,
                    },
                    usage_update_by_external_id_params.UsageUpdateByExternalIDParams,
                ),
            ),
            cast_to=UsageUpdateByExternalIDResponse,
        )


class UsageWithRawResponse:
    def __init__(self, usage: Usage) -> None:
        self._usage = usage

        self.update = _legacy_response.to_raw_response_wrapper(
            usage.update,
        )
        self.update_by_external_id = _legacy_response.to_raw_response_wrapper(
            usage.update_by_external_id,
        )


class AsyncUsageWithRawResponse:
    def __init__(self, usage: AsyncUsage) -> None:
        self._usage = usage

        self.update = _legacy_response.async_to_raw_response_wrapper(
            usage.update,
        )
        self.update_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            usage.update_by_external_id,
        )


class UsageWithStreamingResponse:
    def __init__(self, usage: Usage) -> None:
        self._usage = usage

        self.update = to_streamed_response_wrapper(
            usage.update,
        )
        self.update_by_external_id = to_streamed_response_wrapper(
            usage.update_by_external_id,
        )


class AsyncUsageWithStreamingResponse:
    def __init__(self, usage: AsyncUsage) -> None:
        self._usage = usage

        self.update = async_to_streamed_response_wrapper(
            usage.update,
        )
        self.update_by_external_id = async_to_streamed_response_wrapper(
            usage.update_by_external_id,
        )
