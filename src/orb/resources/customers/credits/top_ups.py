# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.customers.credits import (
    top_up_list_params,
    top_up_create_params,
    top_up_list_by_external_id_params,
    top_up_create_by_external_id_params,
)
from ....types.customers.credits.top_up_list_response import TopUpListResponse
from ....types.customers.credits.top_up_create_response import TopUpCreateResponse
from ....types.customers.credits.top_up_list_by_external_id_response import TopUpListByExternalIDResponse
from ....types.customers.credits.top_up_create_by_external_id_response import TopUpCreateByExternalIDResponse

__all__ = ["TopUps", "AsyncTopUps"]


class TopUps(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopUpsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return TopUpsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopUpsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return TopUpsWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        amount: str,
        currency: str,
        invoice_settings: top_up_create_params.InvoiceSettings,
        per_unit_cost_basis: str,
        threshold: str,
        active_from: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        expires_after: Optional[int] | NotGiven = NOT_GIVEN,
        expires_after_unit: Optional[Literal["day", "month"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TopUpCreateResponse:
        """
        This endpoint allows you to create a new top-up for a specified customer's
        balance. While this top-up is active, the customer's balance will added in
        increments of the specified amount whenever the balance reaches the specified
        threshold.

        If a top-up already exists for this customer in the same currency, the existing
        top-up will be replaced.

        Args:
          amount: The amount to increment when the threshold is reached.

          currency: The currency or custom pricing unit to use for this top-up. If this is a
              real-world currency, it must match the customer's invoicing currency.

          invoice_settings: Settings for invoices generated by triggered top-ups.

          per_unit_cost_basis: How much, in the customer's currency, to charge for each unit.

          threshold: The threshold at which to trigger the top-up. If the balance is at or below this
              threshold, the top-up will be triggered.

          active_from: The date from which the top-up is active. If unspecified, the top-up is active
              immediately.

          expires_after: The number of days or months after which the top-up expires. If unspecified, it
              does not expire.

          expires_after_unit: The unit of expires_after.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/customers/{customer_id}/credits/top_ups",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "invoice_settings": invoice_settings,
                    "per_unit_cost_basis": per_unit_cost_basis,
                    "threshold": threshold,
                    "active_from": active_from,
                    "expires_after": expires_after,
                    "expires_after_unit": expires_after_unit,
                },
                top_up_create_params.TopUpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TopUpCreateResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TopUpListResponse]:
        """List top-ups

        Args:
          cursor: Cursor for pagination.

        This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/credits/top_ups",
            page=SyncPage[TopUpListResponse],
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
                    top_up_list_params.TopUpListParams,
                ),
            ),
            model=TopUpListResponse,
        )

    def delete(
        self,
        top_up_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete top-up

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not top_up_id:
            raise ValueError(f"Expected a non-empty value for `top_up_id` but received {top_up_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/customers/{customer_id}/credits/top_ups/{top_up_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def create_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: str,
        currency: str,
        invoice_settings: top_up_create_by_external_id_params.InvoiceSettings,
        per_unit_cost_basis: str,
        threshold: str,
        active_from: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        expires_after: Optional[int] | NotGiven = NOT_GIVEN,
        expires_after_unit: Optional[Literal["day", "month"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TopUpCreateByExternalIDResponse:
        """
        This endpoint allows you to create a new top-up for a specified customer's
        balance. While this top-up is active, the customer's balance will added in
        increments of the specified amount whenever the balance reaches the specified
        threshold.

        If a top-up already exists for this customer in the same currency, the existing
        top-up will be replaced.

        Args:
          amount: The amount to increment when the threshold is reached.

          currency: The currency or custom pricing unit to use for this top-up. If this is a
              real-world currency, it must match the customer's invoicing currency.

          invoice_settings: Settings for invoices generated by triggered top-ups.

          per_unit_cost_basis: How much, in the customer's currency, to charge for each unit.

          threshold: The threshold at which to trigger the top-up. If the balance is at or below this
              threshold, the top-up will be triggered.

          active_from: The date from which the top-up is active. If unspecified, the top-up is active
              immediately.

          expires_after: The number of days or months after which the top-up expires. If unspecified, it
              does not expire.

          expires_after_unit: The unit of expires_after.

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
            f"/customers/external_customer_id/{external_customer_id}/credits/top_ups",
            body=maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "invoice_settings": invoice_settings,
                    "per_unit_cost_basis": per_unit_cost_basis,
                    "threshold": threshold,
                    "active_from": active_from,
                    "expires_after": expires_after,
                    "expires_after_unit": expires_after_unit,
                },
                top_up_create_by_external_id_params.TopUpCreateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TopUpCreateByExternalIDResponse,
        )

    def delete_by_external_id(
        self,
        top_up_id: str,
        *,
        external_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete top-up by external ID

        Args:
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
        if not top_up_id:
            raise ValueError(f"Expected a non-empty value for `top_up_id` but received {top_up_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/customers/external_customer_id/{external_customer_id}/credits/top_ups/{top_up_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TopUpListByExternalIDResponse]:
        """List top-ups by external ID

        Args:
          cursor: Cursor for pagination.

        This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._get_api_list(
            f"/customers/external_customer_id/{external_customer_id}/credits/top_ups",
            page=SyncPage[TopUpListByExternalIDResponse],
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
                    top_up_list_by_external_id_params.TopUpListByExternalIDParams,
                ),
            ),
            model=TopUpListByExternalIDResponse,
        )


class AsyncTopUps(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopUpsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopUpsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopUpsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncTopUpsWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        amount: str,
        currency: str,
        invoice_settings: top_up_create_params.InvoiceSettings,
        per_unit_cost_basis: str,
        threshold: str,
        active_from: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        expires_after: Optional[int] | NotGiven = NOT_GIVEN,
        expires_after_unit: Optional[Literal["day", "month"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TopUpCreateResponse:
        """
        This endpoint allows you to create a new top-up for a specified customer's
        balance. While this top-up is active, the customer's balance will added in
        increments of the specified amount whenever the balance reaches the specified
        threshold.

        If a top-up already exists for this customer in the same currency, the existing
        top-up will be replaced.

        Args:
          amount: The amount to increment when the threshold is reached.

          currency: The currency or custom pricing unit to use for this top-up. If this is a
              real-world currency, it must match the customer's invoicing currency.

          invoice_settings: Settings for invoices generated by triggered top-ups.

          per_unit_cost_basis: How much, in the customer's currency, to charge for each unit.

          threshold: The threshold at which to trigger the top-up. If the balance is at or below this
              threshold, the top-up will be triggered.

          active_from: The date from which the top-up is active. If unspecified, the top-up is active
              immediately.

          expires_after: The number of days or months after which the top-up expires. If unspecified, it
              does not expire.

          expires_after_unit: The unit of expires_after.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/customers/{customer_id}/credits/top_ups",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "invoice_settings": invoice_settings,
                    "per_unit_cost_basis": per_unit_cost_basis,
                    "threshold": threshold,
                    "active_from": active_from,
                    "expires_after": expires_after,
                    "expires_after_unit": expires_after_unit,
                },
                top_up_create_params.TopUpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TopUpCreateResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TopUpListResponse, AsyncPage[TopUpListResponse]]:
        """List top-ups

        Args:
          cursor: Cursor for pagination.

        This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/credits/top_ups",
            page=AsyncPage[TopUpListResponse],
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
                    top_up_list_params.TopUpListParams,
                ),
            ),
            model=TopUpListResponse,
        )

    async def delete(
        self,
        top_up_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete top-up

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not top_up_id:
            raise ValueError(f"Expected a non-empty value for `top_up_id` but received {top_up_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/customers/{customer_id}/credits/top_ups/{top_up_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def create_by_external_id(
        self,
        external_customer_id: str,
        *,
        amount: str,
        currency: str,
        invoice_settings: top_up_create_by_external_id_params.InvoiceSettings,
        per_unit_cost_basis: str,
        threshold: str,
        active_from: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        expires_after: Optional[int] | NotGiven = NOT_GIVEN,
        expires_after_unit: Optional[Literal["day", "month"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> TopUpCreateByExternalIDResponse:
        """
        This endpoint allows you to create a new top-up for a specified customer's
        balance. While this top-up is active, the customer's balance will added in
        increments of the specified amount whenever the balance reaches the specified
        threshold.

        If a top-up already exists for this customer in the same currency, the existing
        top-up will be replaced.

        Args:
          amount: The amount to increment when the threshold is reached.

          currency: The currency or custom pricing unit to use for this top-up. If this is a
              real-world currency, it must match the customer's invoicing currency.

          invoice_settings: Settings for invoices generated by triggered top-ups.

          per_unit_cost_basis: How much, in the customer's currency, to charge for each unit.

          threshold: The threshold at which to trigger the top-up. If the balance is at or below this
              threshold, the top-up will be triggered.

          active_from: The date from which the top-up is active. If unspecified, the top-up is active
              immediately.

          expires_after: The number of days or months after which the top-up expires. If unspecified, it
              does not expire.

          expires_after_unit: The unit of expires_after.

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
            f"/customers/external_customer_id/{external_customer_id}/credits/top_ups",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "currency": currency,
                    "invoice_settings": invoice_settings,
                    "per_unit_cost_basis": per_unit_cost_basis,
                    "threshold": threshold,
                    "active_from": active_from,
                    "expires_after": expires_after,
                    "expires_after_unit": expires_after_unit,
                },
                top_up_create_by_external_id_params.TopUpCreateByExternalIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TopUpCreateByExternalIDResponse,
        )

    async def delete_by_external_id(
        self,
        top_up_id: str,
        *,
        external_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete top-up by external ID

        Args:
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
        if not top_up_id:
            raise ValueError(f"Expected a non-empty value for `top_up_id` but received {top_up_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/customers/external_customer_id/{external_customer_id}/credits/top_ups/{top_up_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def list_by_external_id(
        self,
        external_customer_id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TopUpListByExternalIDResponse, AsyncPage[TopUpListByExternalIDResponse]]:
        """List top-ups by external ID

        Args:
          cursor: Cursor for pagination.

        This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_customer_id:
            raise ValueError(
                f"Expected a non-empty value for `external_customer_id` but received {external_customer_id!r}"
            )
        return self._get_api_list(
            f"/customers/external_customer_id/{external_customer_id}/credits/top_ups",
            page=AsyncPage[TopUpListByExternalIDResponse],
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
                    top_up_list_by_external_id_params.TopUpListByExternalIDParams,
                ),
            ),
            model=TopUpListByExternalIDResponse,
        )


class TopUpsWithRawResponse:
    def __init__(self, top_ups: TopUps) -> None:
        self._top_ups = top_ups

        self.create = _legacy_response.to_raw_response_wrapper(
            top_ups.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            top_ups.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            top_ups.delete,
        )
        self.create_by_external_id = _legacy_response.to_raw_response_wrapper(
            top_ups.create_by_external_id,
        )
        self.delete_by_external_id = _legacy_response.to_raw_response_wrapper(
            top_ups.delete_by_external_id,
        )
        self.list_by_external_id = _legacy_response.to_raw_response_wrapper(
            top_ups.list_by_external_id,
        )


class AsyncTopUpsWithRawResponse:
    def __init__(self, top_ups: AsyncTopUps) -> None:
        self._top_ups = top_ups

        self.create = _legacy_response.async_to_raw_response_wrapper(
            top_ups.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            top_ups.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            top_ups.delete,
        )
        self.create_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            top_ups.create_by_external_id,
        )
        self.delete_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            top_ups.delete_by_external_id,
        )
        self.list_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            top_ups.list_by_external_id,
        )


class TopUpsWithStreamingResponse:
    def __init__(self, top_ups: TopUps) -> None:
        self._top_ups = top_ups

        self.create = to_streamed_response_wrapper(
            top_ups.create,
        )
        self.list = to_streamed_response_wrapper(
            top_ups.list,
        )
        self.delete = to_streamed_response_wrapper(
            top_ups.delete,
        )
        self.create_by_external_id = to_streamed_response_wrapper(
            top_ups.create_by_external_id,
        )
        self.delete_by_external_id = to_streamed_response_wrapper(
            top_ups.delete_by_external_id,
        )
        self.list_by_external_id = to_streamed_response_wrapper(
            top_ups.list_by_external_id,
        )


class AsyncTopUpsWithStreamingResponse:
    def __init__(self, top_ups: AsyncTopUps) -> None:
        self._top_ups = top_ups

        self.create = async_to_streamed_response_wrapper(
            top_ups.create,
        )
        self.list = async_to_streamed_response_wrapper(
            top_ups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            top_ups.delete,
        )
        self.create_by_external_id = async_to_streamed_response_wrapper(
            top_ups.create_by_external_id,
        )
        self.delete_by_external_id = async_to_streamed_response_wrapper(
            top_ups.delete_by_external_id,
        )
        self.list_by_external_id = async_to_streamed_response_wrapper(
            top_ups.list_by_external_id,
        )
