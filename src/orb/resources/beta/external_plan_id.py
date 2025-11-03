# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.beta import external_plan_id_create_plan_version_params, external_plan_id_set_default_plan_version_params
from ...types.plan import Plan
from ..._base_client import make_request_options
from ...types.plan_version import PlanVersion

__all__ = ["ExternalPlanID", "AsyncExternalPlanID"]


class ExternalPlanID(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalPlanIDWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return ExternalPlanIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalPlanIDWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return ExternalPlanIDWithStreamingResponse(self)

    def create_plan_version(
        self,
        external_plan_id: str,
        *,
        version: int,
        add_adjustments: Optional[Iterable[external_plan_id_create_plan_version_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[external_plan_id_create_plan_version_params.AddPrice]] | Omit = omit,
        remove_adjustments: Optional[Iterable[external_plan_id_create_plan_version_params.RemoveAdjustment]]
        | Omit = omit,
        remove_prices: Optional[Iterable[external_plan_id_create_plan_version_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[external_plan_id_create_plan_version_params.ReplaceAdjustment]]
        | Omit = omit,
        replace_prices: Optional[Iterable[external_plan_id_create_plan_version_params.ReplacePrice]] | Omit = omit,
        set_as_default: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PlanVersion:
        """
        This endpoint allows the creation of a new plan version for an existing plan.

        Args:
          version: New version number.

          add_adjustments: Additional adjustments to be added to the plan.

          add_prices: Additional prices to be added to the plan.

          remove_adjustments: Adjustments to be removed from the plan.

          remove_prices: Prices to be removed from the plan.

          replace_adjustments: Adjustments to be replaced with additional adjustments on the plan.

          replace_prices: Prices to be replaced with additional prices on the plan.

          set_as_default: Set this new plan version as the default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_plan_id:
            raise ValueError(f"Expected a non-empty value for `external_plan_id` but received {external_plan_id!r}")
        return self._post(
            f"/plans/external_plan_id/{external_plan_id}/versions",
            body=maybe_transform(
                {
                    "version": version,
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                    "set_as_default": set_as_default,
                },
                external_plan_id_create_plan_version_params.ExternalPlanIDCreatePlanVersionParams,
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

    def fetch_plan_version(
        self,
        version: str,
        *,
        external_plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanVersion:
        """This endpoint is used to fetch a plan version.

        It returns the phases, prices,
        and adjustments present on this version of the plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_plan_id:
            raise ValueError(f"Expected a non-empty value for `external_plan_id` but received {external_plan_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get(
            f"/plans/external_plan_id/{external_plan_id}/versions/{version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanVersion,
        )

    def set_default_plan_version(
        self,
        external_plan_id: str,
        *,
        version: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint allows setting the default version of a plan.

        Args:
          version: Plan version to set as the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_plan_id:
            raise ValueError(f"Expected a non-empty value for `external_plan_id` but received {external_plan_id!r}")
        return self._post(
            f"/plans/external_plan_id/{external_plan_id}/set_default_version",
            body=maybe_transform(
                {"version": version},
                external_plan_id_set_default_plan_version_params.ExternalPlanIDSetDefaultPlanVersionParams,
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


class AsyncExternalPlanID(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalPlanIDWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalPlanIDWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalPlanIDWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncExternalPlanIDWithStreamingResponse(self)

    async def create_plan_version(
        self,
        external_plan_id: str,
        *,
        version: int,
        add_adjustments: Optional[Iterable[external_plan_id_create_plan_version_params.AddAdjustment]] | Omit = omit,
        add_prices: Optional[Iterable[external_plan_id_create_plan_version_params.AddPrice]] | Omit = omit,
        remove_adjustments: Optional[Iterable[external_plan_id_create_plan_version_params.RemoveAdjustment]]
        | Omit = omit,
        remove_prices: Optional[Iterable[external_plan_id_create_plan_version_params.RemovePrice]] | Omit = omit,
        replace_adjustments: Optional[Iterable[external_plan_id_create_plan_version_params.ReplaceAdjustment]]
        | Omit = omit,
        replace_prices: Optional[Iterable[external_plan_id_create_plan_version_params.ReplacePrice]] | Omit = omit,
        set_as_default: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PlanVersion:
        """
        This endpoint allows the creation of a new plan version for an existing plan.

        Args:
          version: New version number.

          add_adjustments: Additional adjustments to be added to the plan.

          add_prices: Additional prices to be added to the plan.

          remove_adjustments: Adjustments to be removed from the plan.

          remove_prices: Prices to be removed from the plan.

          replace_adjustments: Adjustments to be replaced with additional adjustments on the plan.

          replace_prices: Prices to be replaced with additional prices on the plan.

          set_as_default: Set this new plan version as the default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_plan_id:
            raise ValueError(f"Expected a non-empty value for `external_plan_id` but received {external_plan_id!r}")
        return await self._post(
            f"/plans/external_plan_id/{external_plan_id}/versions",
            body=await async_maybe_transform(
                {
                    "version": version,
                    "add_adjustments": add_adjustments,
                    "add_prices": add_prices,
                    "remove_adjustments": remove_adjustments,
                    "remove_prices": remove_prices,
                    "replace_adjustments": replace_adjustments,
                    "replace_prices": replace_prices,
                    "set_as_default": set_as_default,
                },
                external_plan_id_create_plan_version_params.ExternalPlanIDCreatePlanVersionParams,
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

    async def fetch_plan_version(
        self,
        version: str,
        *,
        external_plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanVersion:
        """This endpoint is used to fetch a plan version.

        It returns the phases, prices,
        and adjustments present on this version of the plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_plan_id:
            raise ValueError(f"Expected a non-empty value for `external_plan_id` but received {external_plan_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._get(
            f"/plans/external_plan_id/{external_plan_id}/versions/{version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanVersion,
        )

    async def set_default_plan_version(
        self,
        external_plan_id: str,
        *,
        version: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Plan:
        """
        This endpoint allows setting the default version of a plan.

        Args:
          version: Plan version to set as the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not external_plan_id:
            raise ValueError(f"Expected a non-empty value for `external_plan_id` but received {external_plan_id!r}")
        return await self._post(
            f"/plans/external_plan_id/{external_plan_id}/set_default_version",
            body=await async_maybe_transform(
                {"version": version},
                external_plan_id_set_default_plan_version_params.ExternalPlanIDSetDefaultPlanVersionParams,
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


class ExternalPlanIDWithRawResponse:
    def __init__(self, external_plan_id: ExternalPlanID) -> None:
        self._external_plan_id = external_plan_id

        self.create_plan_version = _legacy_response.to_raw_response_wrapper(
            external_plan_id.create_plan_version,
        )
        self.fetch_plan_version = _legacy_response.to_raw_response_wrapper(
            external_plan_id.fetch_plan_version,
        )
        self.set_default_plan_version = _legacy_response.to_raw_response_wrapper(
            external_plan_id.set_default_plan_version,
        )


class AsyncExternalPlanIDWithRawResponse:
    def __init__(self, external_plan_id: AsyncExternalPlanID) -> None:
        self._external_plan_id = external_plan_id

        self.create_plan_version = _legacy_response.async_to_raw_response_wrapper(
            external_plan_id.create_plan_version,
        )
        self.fetch_plan_version = _legacy_response.async_to_raw_response_wrapper(
            external_plan_id.fetch_plan_version,
        )
        self.set_default_plan_version = _legacy_response.async_to_raw_response_wrapper(
            external_plan_id.set_default_plan_version,
        )


class ExternalPlanIDWithStreamingResponse:
    def __init__(self, external_plan_id: ExternalPlanID) -> None:
        self._external_plan_id = external_plan_id

        self.create_plan_version = to_streamed_response_wrapper(
            external_plan_id.create_plan_version,
        )
        self.fetch_plan_version = to_streamed_response_wrapper(
            external_plan_id.fetch_plan_version,
        )
        self.set_default_plan_version = to_streamed_response_wrapper(
            external_plan_id.set_default_plan_version,
        )


class AsyncExternalPlanIDWithStreamingResponse:
    def __init__(self, external_plan_id: AsyncExternalPlanID) -> None:
        self._external_plan_id = external_plan_id

        self.create_plan_version = async_to_streamed_response_wrapper(
            external_plan_id.create_plan_version,
        )
        self.fetch_plan_version = async_to_streamed_response_wrapper(
            external_plan_id.fetch_plan_version,
        )
        self.set_default_plan_version = async_to_streamed_response_wrapper(
            external_plan_id.set_default_plan_version,
        )
