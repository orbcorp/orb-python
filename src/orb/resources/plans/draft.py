# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.plans import draft_save_params, draft_publish_params
from ..._base_client import make_request_options
from ...types.plan_version import PlanVersion
from ...types.plans.plan_version_draft import PlanVersionDraft

__all__ = ["Draft", "AsyncDraft"]


class Draft(SyncAPIResource):
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    @cached_property
    def with_raw_response(self) -> DraftWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return DraftWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return DraftWithStreamingResponse(self)

    def discard(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """This endpoint discards the plan's draft version.

        Prices and adjustments the
        draft created stay in the Pricebook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/plans/{plan_id}/draft", plan_id=plan_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanVersionDraft:
        """
        This endpoint returns the plan's unpublished draft version, with its changes
        applied on top of the latest published version. It returns a 404 if the plan has
        no draft.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get(
            path_template("/plans/{plan_id}/draft", plan_id=plan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanVersionDraft,
        )

    def publish(
        self,
        plan_id: str,
        *,
        set_as_default: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PlanVersion:
        """This endpoint publishes the plan's draft as the next numbered version.

        A draft
        that fails plan version validation is a 400 and is left as it was.

        Args:
          set_as_default: Also make the new version the plan's default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._post(
            path_template("/plans/{plan_id}/draft/publish", plan_id=plan_id),
            body=maybe_transform({"set_as_default": set_as_default}, draft_publish_params.DraftPublishParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PlanVersion,
        )

    def save(
        self,
        plan_id: str,
        *,
        add_adjustments: Optional[Iterable[draft_save_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[draft_save_params.AddPrice]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        remove_adjustments: Optional[Iterable[draft_save_params.RemoveAdjustment]] | Omit = omit,
        remove_prices: Optional[Iterable[draft_save_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[draft_save_params.ReplaceAdjustment]] | Omit = omit,
        replace_prices: Optional[Iterable[draft_save_params.ReplacePrice]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PlanVersionDraft:
        """
        This endpoint creates the plan's draft version or fully replaces its changes.
        The changes are always relative to the latest published version. A save replaces
        the draft; last write wins.

        Args:
          add_adjustments: Additional adjustments to be added to the plan.

          add_prices: Additional prices to be added to the plan.

          description: Optional description of what changes in this draft

          remove_adjustments: Adjustments to be removed from the plan.

          remove_prices: Prices to be removed from the plan.

          replace_adjustments: Adjustments to be replaced with additional adjustments on the plan.

          replace_prices: Prices to be replaced with additional prices on the plan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._put(
            path_template("/plans/{plan_id}/draft", plan_id=plan_id),
            body=maybe_transform(
                {
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "description": description,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                },
                draft_save_params.DraftSaveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PlanVersionDraft,
        )


class AsyncDraft(AsyncAPIResource):
    """
    The [Plan](/core-concepts#plan-and-price) resource represents a plan that can be subscribed to by a
    customer. Plans define the billing behavior of the subscription. You can see more about how to configure prices
    in the [Price resource](/reference/price).
    """

    @cached_property
    def with_raw_response(self) -> AsyncDraftWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncDraftWithStreamingResponse(self)

    async def discard(
        self,
        plan_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """This endpoint discards the plan's draft version.

        Prices and adjustments the
        draft created stay in the Pricebook.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/plans/{plan_id}/draft", plan_id=plan_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanVersionDraft:
        """
        This endpoint returns the plan's unpublished draft version, with its changes
        applied on top of the latest published version. It returns a 404 if the plan has
        no draft.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._get(
            path_template("/plans/{plan_id}/draft", plan_id=plan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanVersionDraft,
        )

    async def publish(
        self,
        plan_id: str,
        *,
        set_as_default: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PlanVersion:
        """This endpoint publishes the plan's draft as the next numbered version.

        A draft
        that fails plan version validation is a 400 and is left as it was.

        Args:
          set_as_default: Also make the new version the plan's default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._post(
            path_template("/plans/{plan_id}/draft/publish", plan_id=plan_id),
            body=await async_maybe_transform(
                {"set_as_default": set_as_default}, draft_publish_params.DraftPublishParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PlanVersion,
        )

    async def save(
        self,
        plan_id: str,
        *,
        add_adjustments: Optional[Iterable[draft_save_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[draft_save_params.AddPrice]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        remove_adjustments: Optional[Iterable[draft_save_params.RemoveAdjustment]] | Omit = omit,
        remove_prices: Optional[Iterable[draft_save_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[draft_save_params.ReplaceAdjustment]] | Omit = omit,
        replace_prices: Optional[Iterable[draft_save_params.ReplacePrice]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PlanVersionDraft:
        """
        This endpoint creates the plan's draft version or fully replaces its changes.
        The changes are always relative to the latest published version. A save replaces
        the draft; last write wins.

        Args:
          add_adjustments: Additional adjustments to be added to the plan.

          add_prices: Additional prices to be added to the plan.

          description: Optional description of what changes in this draft

          remove_adjustments: Adjustments to be removed from the plan.

          remove_prices: Prices to be removed from the plan.

          replace_adjustments: Adjustments to be replaced with additional adjustments on the plan.

          replace_prices: Prices to be replaced with additional prices on the plan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._put(
            path_template("/plans/{plan_id}/draft", plan_id=plan_id),
            body=await async_maybe_transform(
                {
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "description": description,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                },
                draft_save_params.DraftSaveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PlanVersionDraft,
        )


class DraftWithRawResponse:
    def __init__(self, draft: Draft) -> None:
        self._draft = draft

        self.discard = _legacy_response.to_raw_response_wrapper(
            draft.discard,
        )
        self.fetch = _legacy_response.to_raw_response_wrapper(
            draft.fetch,
        )
        self.publish = _legacy_response.to_raw_response_wrapper(
            draft.publish,
        )
        self.save = _legacy_response.to_raw_response_wrapper(
            draft.save,
        )


class AsyncDraftWithRawResponse:
    def __init__(self, draft: AsyncDraft) -> None:
        self._draft = draft

        self.discard = _legacy_response.async_to_raw_response_wrapper(
            draft.discard,
        )
        self.fetch = _legacy_response.async_to_raw_response_wrapper(
            draft.fetch,
        )
        self.publish = _legacy_response.async_to_raw_response_wrapper(
            draft.publish,
        )
        self.save = _legacy_response.async_to_raw_response_wrapper(
            draft.save,
        )


class DraftWithStreamingResponse:
    def __init__(self, draft: Draft) -> None:
        self._draft = draft

        self.discard = to_streamed_response_wrapper(
            draft.discard,
        )
        self.fetch = to_streamed_response_wrapper(
            draft.fetch,
        )
        self.publish = to_streamed_response_wrapper(
            draft.publish,
        )
        self.save = to_streamed_response_wrapper(
            draft.save,
        )


class AsyncDraftWithStreamingResponse:
    def __init__(self, draft: AsyncDraft) -> None:
        self._draft = draft

        self.discard = async_to_streamed_response_wrapper(
            draft.discard,
        )
        self.fetch = async_to_streamed_response_wrapper(
            draft.fetch,
        )
        self.publish = async_to_streamed_response_wrapper(
            draft.publish,
        )
        self.save = async_to_streamed_response_wrapper(
            draft.save,
        )
