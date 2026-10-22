# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import webhook_endpoint_list_params, webhook_endpoint_create_params, webhook_endpoint_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.webhook_endpoint import WebhookEndpoint
from ..types.webhook_endpoint_with_secret import WebhookEndpointWithSecret

__all__ = ["WebhookEndpoints", "AsyncWebhookEndpoints"]


class WebhookEndpoints(SyncAPIResource):
    """
    A webhook endpoint is an HTTPS URL that Orb sends [webhook events](/integrations-and-exports/webhooks) to.
    """

    @cached_property
    def with_raw_response(self) -> WebhookEndpointsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return WebhookEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookEndpointsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return WebhookEndpointsWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        enabled_event_types: Optional[SequenceNotStr[str]] | Omit = omit,
        payload_style: Optional[Literal["expanded", "standard"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpointWithSecret:
        """
        This endpoint creates a webhook endpoint and returns the secret used to sign its
        webhook events. The secret isn't returned by any other endpoint. An account can
        have at most 20 webhook endpoints by default.

        Args:
          url: The HTTPS URL that Orb sends webhook events to.

          enabled_event_types: The webhook event types to send to this endpoint. If omitted or null, all event
              types are sent.

          payload_style: The payload style of the webhook events sent to this endpoint. If omitted or
              null, the account's default style is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/webhook_endpoints",
            body=maybe_transform(
                {
                    "url": url,
                    "enabled_event_types": enabled_event_types,
                    "payload_style": payload_style,
                },
                webhook_endpoint_create_params.WebhookEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpointWithSecret,
        )

    def retrieve(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEndpoint:
        """
        This endpoint returns a webhook endpoint identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return self._get(
            path_template("/webhook_endpoints/{webhook_endpoint_id}", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpoint,
        )

    def update(
        self,
        webhook_endpoint_id: str,
        *,
        enabled_event_types: Optional[SequenceNotStr[str]] | Omit = omit,
        payload_style: Optional[Literal["expanded", "standard"]] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpoint:
        """
        This endpoint updates a webhook endpoint's URL or the event types sent to it.

        Args:
          enabled_event_types: The webhook event types to send to this endpoint. Null sends all event types;
              omit to leave them unchanged.

          payload_style: The payload style of the webhook events sent to this endpoint. Applies to events
              created after the change; omit to leave it unchanged.

          url: The HTTPS URL that Orb sends webhook events to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return self._put(
            path_template("/webhook_endpoints/{webhook_endpoint_id}", webhook_endpoint_id=webhook_endpoint_id),
            body=maybe_transform(
                {
                    "enabled_event_types": enabled_event_types,
                    "payload_style": payload_style,
                    "url": url,
                },
                webhook_endpoint_update_params.WebhookEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpoint,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[WebhookEndpoint]:
        """
        This endpoint returns the account's webhook endpoints, ordered starting from the
        most recently created.

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
            "/webhook_endpoints",
            page=SyncPage[WebhookEndpoint],
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
                    webhook_endpoint_list_params.WebhookEndpointListParams,
                ),
            ),
            model=WebhookEndpoint,
        )

    def delete(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """This endpoint deletes a webhook endpoint.

        Orb stops sending webhook events to it
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/webhook_endpoints/{webhook_endpoint_id}", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def disable(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpoint:
        """
        This endpoint disables a webhook endpoint, so Orb stops sending webhook events
        to it until it is enabled again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return self._post(
            path_template("/webhook_endpoints/{webhook_endpoint_id}/disable", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpoint,
        )

    def enable(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpoint:
        """
        This endpoint enables a webhook endpoint, so Orb resumes sending webhook events
        to it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return self._post(
            path_template("/webhook_endpoints/{webhook_endpoint_id}/enable", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpoint,
        )


class AsyncWebhookEndpoints(AsyncAPIResource):
    """
    A webhook endpoint is an HTTPS URL that Orb sends [webhook events](/integrations-and-exports/webhooks) to.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWebhookEndpointsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookEndpointsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncWebhookEndpointsWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        enabled_event_types: Optional[SequenceNotStr[str]] | Omit = omit,
        payload_style: Optional[Literal["expanded", "standard"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpointWithSecret:
        """
        This endpoint creates a webhook endpoint and returns the secret used to sign its
        webhook events. The secret isn't returned by any other endpoint. An account can
        have at most 20 webhook endpoints by default.

        Args:
          url: The HTTPS URL that Orb sends webhook events to.

          enabled_event_types: The webhook event types to send to this endpoint. If omitted or null, all event
              types are sent.

          payload_style: The payload style of the webhook events sent to this endpoint. If omitted or
              null, the account's default style is used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/webhook_endpoints",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "enabled_event_types": enabled_event_types,
                    "payload_style": payload_style,
                },
                webhook_endpoint_create_params.WebhookEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpointWithSecret,
        )

    async def retrieve(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookEndpoint:
        """
        This endpoint returns a webhook endpoint identified by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return await self._get(
            path_template("/webhook_endpoints/{webhook_endpoint_id}", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookEndpoint,
        )

    async def update(
        self,
        webhook_endpoint_id: str,
        *,
        enabled_event_types: Optional[SequenceNotStr[str]] | Omit = omit,
        payload_style: Optional[Literal["expanded", "standard"]] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpoint:
        """
        This endpoint updates a webhook endpoint's URL or the event types sent to it.

        Args:
          enabled_event_types: The webhook event types to send to this endpoint. Null sends all event types;
              omit to leave them unchanged.

          payload_style: The payload style of the webhook events sent to this endpoint. Applies to events
              created after the change; omit to leave it unchanged.

          url: The HTTPS URL that Orb sends webhook events to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return await self._put(
            path_template("/webhook_endpoints/{webhook_endpoint_id}", webhook_endpoint_id=webhook_endpoint_id),
            body=await async_maybe_transform(
                {
                    "enabled_event_types": enabled_event_types,
                    "payload_style": payload_style,
                    "url": url,
                },
                webhook_endpoint_update_params.WebhookEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpoint,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WebhookEndpoint, AsyncPage[WebhookEndpoint]]:
        """
        This endpoint returns the account's webhook endpoints, ordered starting from the
        most recently created.

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
            "/webhook_endpoints",
            page=AsyncPage[WebhookEndpoint],
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
                    webhook_endpoint_list_params.WebhookEndpointListParams,
                ),
            ),
            model=WebhookEndpoint,
        )

    async def delete(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """This endpoint deletes a webhook endpoint.

        Orb stops sending webhook events to it
        immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/webhook_endpoints/{webhook_endpoint_id}", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def disable(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpoint:
        """
        This endpoint disables a webhook endpoint, so Orb stops sending webhook events
        to it until it is enabled again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return await self._post(
            path_template("/webhook_endpoints/{webhook_endpoint_id}/disable", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpoint,
        )

    async def enable(
        self,
        webhook_endpoint_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> WebhookEndpoint:
        """
        This endpoint enables a webhook endpoint, so Orb resumes sending webhook events
        to it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not webhook_endpoint_id:
            raise ValueError(
                f"Expected a non-empty value for `webhook_endpoint_id` but received {webhook_endpoint_id!r}"
            )
        return await self._post(
            path_template("/webhook_endpoints/{webhook_endpoint_id}/enable", webhook_endpoint_id=webhook_endpoint_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=WebhookEndpoint,
        )


class WebhookEndpointsWithRawResponse:
    def __init__(self, webhook_endpoints: WebhookEndpoints) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.delete,
        )
        self.disable = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.disable,
        )
        self.enable = _legacy_response.to_raw_response_wrapper(
            webhook_endpoints.enable,
        )


class AsyncWebhookEndpointsWithRawResponse:
    def __init__(self, webhook_endpoints: AsyncWebhookEndpoints) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.delete,
        )
        self.disable = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.disable,
        )
        self.enable = _legacy_response.async_to_raw_response_wrapper(
            webhook_endpoints.enable,
        )


class WebhookEndpointsWithStreamingResponse:
    def __init__(self, webhook_endpoints: WebhookEndpoints) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = to_streamed_response_wrapper(
            webhook_endpoints.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhook_endpoints.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhook_endpoints.update,
        )
        self.list = to_streamed_response_wrapper(
            webhook_endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhook_endpoints.delete,
        )
        self.disable = to_streamed_response_wrapper(
            webhook_endpoints.disable,
        )
        self.enable = to_streamed_response_wrapper(
            webhook_endpoints.enable,
        )


class AsyncWebhookEndpointsWithStreamingResponse:
    def __init__(self, webhook_endpoints: AsyncWebhookEndpoints) -> None:
        self._webhook_endpoints = webhook_endpoints

        self.create = async_to_streamed_response_wrapper(
            webhook_endpoints.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhook_endpoints.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhook_endpoints.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhook_endpoints.delete,
        )
        self.disable = async_to_streamed_response_wrapper(
            webhook_endpoints.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            webhook_endpoints.enable,
        )
