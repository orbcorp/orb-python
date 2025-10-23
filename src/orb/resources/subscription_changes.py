# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from .. import _legacy_response
from ..types import subscription_change_apply_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.subscription_change_apply_response import SubscriptionChangeApplyResponse
from ..types.subscription_change_cancel_response import SubscriptionChangeCancelResponse
from ..types.subscription_change_retrieve_response import SubscriptionChangeRetrieveResponse

__all__ = ["SubscriptionChanges", "AsyncSubscriptionChanges"]


class SubscriptionChanges(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionChangesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionChangesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionChangesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return SubscriptionChangesWithStreamingResponse(self)

    def retrieve(
        self,
        subscription_change_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionChangeRetrieveResponse:
        """
        This endpoint returns a subscription change given an identifier.

        A subscription change is created by including
        `Create-Pending-Subscription-Change: True` in the header of a subscription
        mutation API call (e.g.
        [create subscription endpoint](/api-reference/subscription/create-subscription),
        [schedule plan change endpoint](/api-reference/subscription/schedule-plan-change),
        ...). The subscription change will be referenced by the
        `pending_subscription_change` field in the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_change_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_change_id` but received {subscription_change_id!r}"
            )
        return self._get(
            f"/subscription_changes/{subscription_change_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionChangeRetrieveResponse,
        )

    def apply(
        self,
        subscription_change_id: str,
        *,
        description: Optional[str] | Omit = omit,
        mark_as_paid: Optional[bool] | Omit = omit,
        payment_external_id: Optional[str] | Omit = omit,
        payment_notes: Optional[str] | Omit = omit,
        payment_received_date: Union[str, date, None] | Omit = omit,
        previously_collected_amount: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SubscriptionChangeApplyResponse:
        """Apply a subscription change to perform the intended action.

        If a positive amount
        is passed with a request to this endpoint, any eligible invoices that were
        created will be issued immediately if they only contain in-advance fees.

        Args:
          description: Description to apply to the balance transaction representing this credit.

          mark_as_paid: Mark all pending invoices that are payable as paid. If amount is also provided,
              mark as paid and credit the difference to the customer's balance.

          payment_external_id: An optional external ID to associate with the payment. Only applicable when
              mark_as_paid is true.

          payment_notes: Optional notes about the payment. Only applicable when mark_as_paid is true.

          payment_received_date: A date string to specify the date the payment was received. Only applicable when
              mark_as_paid is true. If not provided, defaults to the current date.

          previously_collected_amount: Amount already collected to apply to the customer's balance. If mark_as_paid is
              also provided, credit the difference to the customer's balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_change_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_change_id` but received {subscription_change_id!r}"
            )
        return self._post(
            f"/subscription_changes/{subscription_change_id}/apply",
            body=maybe_transform(
                {
                    "description": description,
                    "mark_as_paid": mark_as_paid,
                    "payment_external_id": payment_external_id,
                    "payment_notes": payment_notes,
                    "payment_received_date": payment_received_date,
                    "previously_collected_amount": previously_collected_amount,
                },
                subscription_change_apply_params.SubscriptionChangeApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SubscriptionChangeApplyResponse,
        )

    def cancel(
        self,
        subscription_change_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SubscriptionChangeCancelResponse:
        """Cancel a subscription change.

        The change can no longer be applied. A
        subscription can only have one "pending" change at a time - use this endpoint to
        cancel an existing change before creating a new one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_change_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_change_id` but received {subscription_change_id!r}"
            )
        return self._post(
            f"/subscription_changes/{subscription_change_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SubscriptionChangeCancelResponse,
        )


class AsyncSubscriptionChanges(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionChangesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionChangesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionChangesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncSubscriptionChangesWithStreamingResponse(self)

    async def retrieve(
        self,
        subscription_change_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionChangeRetrieveResponse:
        """
        This endpoint returns a subscription change given an identifier.

        A subscription change is created by including
        `Create-Pending-Subscription-Change: True` in the header of a subscription
        mutation API call (e.g.
        [create subscription endpoint](/api-reference/subscription/create-subscription),
        [schedule plan change endpoint](/api-reference/subscription/schedule-plan-change),
        ...). The subscription change will be referenced by the
        `pending_subscription_change` field in the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_change_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_change_id` but received {subscription_change_id!r}"
            )
        return await self._get(
            f"/subscription_changes/{subscription_change_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionChangeRetrieveResponse,
        )

    async def apply(
        self,
        subscription_change_id: str,
        *,
        description: Optional[str] | Omit = omit,
        mark_as_paid: Optional[bool] | Omit = omit,
        payment_external_id: Optional[str] | Omit = omit,
        payment_notes: Optional[str] | Omit = omit,
        payment_received_date: Union[str, date, None] | Omit = omit,
        previously_collected_amount: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SubscriptionChangeApplyResponse:
        """Apply a subscription change to perform the intended action.

        If a positive amount
        is passed with a request to this endpoint, any eligible invoices that were
        created will be issued immediately if they only contain in-advance fees.

        Args:
          description: Description to apply to the balance transaction representing this credit.

          mark_as_paid: Mark all pending invoices that are payable as paid. If amount is also provided,
              mark as paid and credit the difference to the customer's balance.

          payment_external_id: An optional external ID to associate with the payment. Only applicable when
              mark_as_paid is true.

          payment_notes: Optional notes about the payment. Only applicable when mark_as_paid is true.

          payment_received_date: A date string to specify the date the payment was received. Only applicable when
              mark_as_paid is true. If not provided, defaults to the current date.

          previously_collected_amount: Amount already collected to apply to the customer's balance. If mark_as_paid is
              also provided, credit the difference to the customer's balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_change_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_change_id` but received {subscription_change_id!r}"
            )
        return await self._post(
            f"/subscription_changes/{subscription_change_id}/apply",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "mark_as_paid": mark_as_paid,
                    "payment_external_id": payment_external_id,
                    "payment_notes": payment_notes,
                    "payment_received_date": payment_received_date,
                    "previously_collected_amount": previously_collected_amount,
                },
                subscription_change_apply_params.SubscriptionChangeApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SubscriptionChangeApplyResponse,
        )

    async def cancel(
        self,
        subscription_change_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SubscriptionChangeCancelResponse:
        """Cancel a subscription change.

        The change can no longer be applied. A
        subscription can only have one "pending" change at a time - use this endpoint to
        cancel an existing change before creating a new one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not subscription_change_id:
            raise ValueError(
                f"Expected a non-empty value for `subscription_change_id` but received {subscription_change_id!r}"
            )
        return await self._post(
            f"/subscription_changes/{subscription_change_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SubscriptionChangeCancelResponse,
        )


class SubscriptionChangesWithRawResponse:
    def __init__(self, subscription_changes: SubscriptionChanges) -> None:
        self._subscription_changes = subscription_changes

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            subscription_changes.retrieve,
        )
        self.apply = _legacy_response.to_raw_response_wrapper(
            subscription_changes.apply,
        )
        self.cancel = _legacy_response.to_raw_response_wrapper(
            subscription_changes.cancel,
        )


class AsyncSubscriptionChangesWithRawResponse:
    def __init__(self, subscription_changes: AsyncSubscriptionChanges) -> None:
        self._subscription_changes = subscription_changes

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            subscription_changes.retrieve,
        )
        self.apply = _legacy_response.async_to_raw_response_wrapper(
            subscription_changes.apply,
        )
        self.cancel = _legacy_response.async_to_raw_response_wrapper(
            subscription_changes.cancel,
        )


class SubscriptionChangesWithStreamingResponse:
    def __init__(self, subscription_changes: SubscriptionChanges) -> None:
        self._subscription_changes = subscription_changes

        self.retrieve = to_streamed_response_wrapper(
            subscription_changes.retrieve,
        )
        self.apply = to_streamed_response_wrapper(
            subscription_changes.apply,
        )
        self.cancel = to_streamed_response_wrapper(
            subscription_changes.cancel,
        )


class AsyncSubscriptionChangesWithStreamingResponse:
    def __init__(self, subscription_changes: AsyncSubscriptionChanges) -> None:
        self._subscription_changes = subscription_changes

        self.retrieve = async_to_streamed_response_wrapper(
            subscription_changes.retrieve,
        )
        self.apply = async_to_streamed_response_wrapper(
            subscription_changes.apply,
        )
        self.cancel = async_to_streamed_response_wrapper(
            subscription_changes.cancel,
        )
