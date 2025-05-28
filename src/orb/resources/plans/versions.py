# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.plans import version_create_params
from ..._base_client import make_request_options
from ...types.plans.version_create_response import VersionCreateResponse
from ...types.plans.version_retrieve_response import VersionRetrieveResponse

__all__ = ["Versions", "AsyncVersions"]


class Versions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return VersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return VersionsWithStreamingResponse(self)

    def create(
        self,
        plan_id: str,
        *,
        version: int,
        add_adjustments: Optional[Iterable[version_create_params.AddAdjustment]] | NotGiven = NOT_GIVEN,
        add_prices: Optional[Iterable[version_create_params.AddPrice]] | NotGiven = NOT_GIVEN,
        remove_adjustments: Optional[Iterable[version_create_params.RemoveAdjustment]] | NotGiven = NOT_GIVEN,
        remove_prices: Optional[Iterable[version_create_params.RemovePrice]] | NotGiven = NOT_GIVEN,
        replace_adjustments: Optional[Iterable[version_create_params.ReplaceAdjustment]] | NotGiven = NOT_GIVEN,
        replace_prices: Optional[Iterable[version_create_params.ReplacePrice]] | NotGiven = NOT_GIVEN,
        set_as_default: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VersionCreateResponse:
        """This API endpoint is in beta and its interface may change.

        It is recommended for
        use only in test mode.

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
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._post(
            f"/plans/{plan_id}/versions",
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
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VersionCreateResponse,
        )

    def retrieve(
        self,
        version: str,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionRetrieveResponse:
        """This API endpoint is in beta and its interface may change.

        It is recommended for
        use only in test mode.

        This endpoint is used to fetch a plan version. It returns the phases, prices,
        and adjustments present on this version of the plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return self._get(
            f"/plans/{plan_id}/versions/{version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionRetrieveResponse,
        )


class AsyncVersions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncVersionsWithStreamingResponse(self)

    async def create(
        self,
        plan_id: str,
        *,
        version: int,
        add_adjustments: Optional[Iterable[version_create_params.AddAdjustment]] | NotGiven = NOT_GIVEN,
        add_prices: Optional[Iterable[version_create_params.AddPrice]] | NotGiven = NOT_GIVEN,
        remove_adjustments: Optional[Iterable[version_create_params.RemoveAdjustment]] | NotGiven = NOT_GIVEN,
        remove_prices: Optional[Iterable[version_create_params.RemovePrice]] | NotGiven = NOT_GIVEN,
        replace_adjustments: Optional[Iterable[version_create_params.ReplaceAdjustment]] | NotGiven = NOT_GIVEN,
        replace_prices: Optional[Iterable[version_create_params.ReplacePrice]] | NotGiven = NOT_GIVEN,
        set_as_default: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> VersionCreateResponse:
        """This API endpoint is in beta and its interface may change.

        It is recommended for
        use only in test mode.

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
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._post(
            f"/plans/{plan_id}/versions",
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
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VersionCreateResponse,
        )

    async def retrieve(
        self,
        version: str,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionRetrieveResponse:
        """This API endpoint is in beta and its interface may change.

        It is recommended for
        use only in test mode.

        This endpoint is used to fetch a plan version. It returns the phases, prices,
        and adjustments present on this version of the plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        if not version:
            raise ValueError(f"Expected a non-empty value for `version` but received {version!r}")
        return await self._get(
            f"/plans/{plan_id}/versions/{version}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionRetrieveResponse,
        )


class VersionsWithRawResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.create = _legacy_response.to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            versions.retrieve,
        )


class AsyncVersionsWithRawResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            versions.retrieve,
        )


class VersionsWithStreamingResponse:
    def __init__(self, versions: Versions) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )


class AsyncVersionsWithStreamingResponse:
    def __init__(self, versions: AsyncVersions) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
