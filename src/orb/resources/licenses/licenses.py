# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from .usage import (
    Usage,
    AsyncUsage,
    UsageWithRawResponse,
    AsyncUsageWithRawResponse,
    UsageWithStreamingResponse,
    AsyncUsageWithStreamingResponse,
)
from ...types import (
    license_list_params,
    license_create_params,
    license_deactivate_params,
    license_retrieve_by_external_id_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from .external_licenses import (
    ExternalLicenses,
    AsyncExternalLicenses,
    ExternalLicensesWithRawResponse,
    AsyncExternalLicensesWithRawResponse,
    ExternalLicensesWithStreamingResponse,
    AsyncExternalLicensesWithStreamingResponse,
)
from ...types.license_list_response import LicenseListResponse
from ...types.license_create_response import LicenseCreateResponse
from ...types.license_retrieve_response import LicenseRetrieveResponse
from ...types.license_deactivate_response import LicenseDeactivateResponse
from ...types.license_retrieve_by_external_id_response import LicenseRetrieveByExternalIDResponse

__all__ = ["Licenses", "AsyncLicenses"]


class Licenses(SyncAPIResource):
    @cached_property
    def external_licenses(self) -> ExternalLicenses:
        return ExternalLicenses(self._client)

    @cached_property
    def usage(self) -> Usage:
        return Usage(self._client)

    @cached_property
    def with_raw_response(self) -> LicensesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return LicensesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LicensesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return LicensesWithStreamingResponse(self)

    def create(
        self,
        *,
        external_license_id: str,
        license_type_id: str,
        subscription_id: str,
        end_date: Union[str, date, None] | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LicenseCreateResponse:
        """
        This endpoint is used to create a new license for a user.

        If a start date is provided, the license will be activated at the **start** of
        the specified date in the customer's timezone. Otherwise, the activation time
        will default to the **start** of the current day in the customer's timezone.

        Args:
          external_license_id: The external identifier for the license.

          end_date: The end date of the license. If not provided, the license will remain active
              until deactivated.

          start_date: The start date of the license. If not provided, defaults to start of day today
              in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/licenses",
            body=maybe_transform(
                {
                    "external_license_id": external_license_id,
                    "license_type_id": license_type_id,
                    "subscription_id": subscription_id,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                license_create_params.LicenseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LicenseCreateResponse,
        )

    def retrieve(
        self,
        license_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LicenseRetrieveResponse:
        """
        This endpoint is used to fetch a license given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license_id:
            raise ValueError(f"Expected a non-empty value for `license_id` but received {license_id!r}")
        return self._get(
            f"/licenses/{license_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseRetrieveResponse,
        )

    def list(
        self,
        *,
        subscription_id: str,
        cursor: Optional[str] | Omit = omit,
        external_license_id: Optional[str] | Omit = omit,
        license_type_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["active", "inactive"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[LicenseListResponse]:
        """
        This endpoint returns a list of all licenses for a subscription.

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
            "/licenses",
            page=SyncPage[LicenseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "subscription_id": subscription_id,
                        "cursor": cursor,
                        "external_license_id": external_license_id,
                        "license_type_id": license_type_id,
                        "limit": limit,
                        "status": status,
                    },
                    license_list_params.LicenseListParams,
                ),
            ),
            model=LicenseListResponse,
        )

    def deactivate(
        self,
        license_id: str,
        *,
        end_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LicenseDeactivateResponse:
        """
        This endpoint is used to deactivate an existing license.

        If an end date is provided, the license will be deactivated at the **start** of
        the specified date in the customer's timezone. Otherwise, the deactivation time
        will default to the **end** of the current day in the customer's timezone.

        Args:
          end_date: The date to deactivate the license. If not provided, defaults to end of day
              today in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not license_id:
            raise ValueError(f"Expected a non-empty value for `license_id` but received {license_id!r}")
        return self._post(
            f"/licenses/{license_id}/deactivate",
            body=maybe_transform({"end_date": end_date}, license_deactivate_params.LicenseDeactivateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LicenseDeactivateResponse,
        )

    def retrieve_by_external_id(
        self,
        external_license_id: str,
        *,
        license_type_id: str,
        subscription_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LicenseRetrieveByExternalIDResponse:
        """
        This endpoint is used to fetch a license given an external license identifier.

        Args:
          license_type_id: The ID of the license type to fetch the license for.

          subscription_id: The ID of the subscription to fetch the license for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_license_id:
            raise ValueError(
                f"Expected a non-empty value for `external_license_id` but received {external_license_id!r}"
            )
        return self._get(
            f"/licenses/external_license_id/{external_license_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "license_type_id": license_type_id,
                        "subscription_id": subscription_id,
                    },
                    license_retrieve_by_external_id_params.LicenseRetrieveByExternalIDParams,
                ),
            ),
            cast_to=LicenseRetrieveByExternalIDResponse,
        )


class AsyncLicenses(AsyncAPIResource):
    @cached_property
    def external_licenses(self) -> AsyncExternalLicenses:
        return AsyncExternalLicenses(self._client)

    @cached_property
    def usage(self) -> AsyncUsage:
        return AsyncUsage(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLicensesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLicensesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLicensesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncLicensesWithStreamingResponse(self)

    async def create(
        self,
        *,
        external_license_id: str,
        license_type_id: str,
        subscription_id: str,
        end_date: Union[str, date, None] | Omit = omit,
        start_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LicenseCreateResponse:
        """
        This endpoint is used to create a new license for a user.

        If a start date is provided, the license will be activated at the **start** of
        the specified date in the customer's timezone. Otherwise, the activation time
        will default to the **start** of the current day in the customer's timezone.

        Args:
          external_license_id: The external identifier for the license.

          end_date: The end date of the license. If not provided, the license will remain active
              until deactivated.

          start_date: The start date of the license. If not provided, defaults to start of day today
              in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/licenses",
            body=await async_maybe_transform(
                {
                    "external_license_id": external_license_id,
                    "license_type_id": license_type_id,
                    "subscription_id": subscription_id,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                license_create_params.LicenseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LicenseCreateResponse,
        )

    async def retrieve(
        self,
        license_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LicenseRetrieveResponse:
        """
        This endpoint is used to fetch a license given an identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license_id:
            raise ValueError(f"Expected a non-empty value for `license_id` but received {license_id!r}")
        return await self._get(
            f"/licenses/{license_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseRetrieveResponse,
        )

    def list(
        self,
        *,
        subscription_id: str,
        cursor: Optional[str] | Omit = omit,
        external_license_id: Optional[str] | Omit = omit,
        license_type_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        status: Optional[Literal["active", "inactive"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[LicenseListResponse, AsyncPage[LicenseListResponse]]:
        """
        This endpoint returns a list of all licenses for a subscription.

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
            "/licenses",
            page=AsyncPage[LicenseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "subscription_id": subscription_id,
                        "cursor": cursor,
                        "external_license_id": external_license_id,
                        "license_type_id": license_type_id,
                        "limit": limit,
                        "status": status,
                    },
                    license_list_params.LicenseListParams,
                ),
            ),
            model=LicenseListResponse,
        )

    async def deactivate(
        self,
        license_id: str,
        *,
        end_date: Union[str, date, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LicenseDeactivateResponse:
        """
        This endpoint is used to deactivate an existing license.

        If an end date is provided, the license will be deactivated at the **start** of
        the specified date in the customer's timezone. Otherwise, the deactivation time
        will default to the **end** of the current day in the customer's timezone.

        Args:
          end_date: The date to deactivate the license. If not provided, defaults to end of day
              today in the customer's timezone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not license_id:
            raise ValueError(f"Expected a non-empty value for `license_id` but received {license_id!r}")
        return await self._post(
            f"/licenses/{license_id}/deactivate",
            body=await async_maybe_transform({"end_date": end_date}, license_deactivate_params.LicenseDeactivateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LicenseDeactivateResponse,
        )

    async def retrieve_by_external_id(
        self,
        external_license_id: str,
        *,
        license_type_id: str,
        subscription_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LicenseRetrieveByExternalIDResponse:
        """
        This endpoint is used to fetch a license given an external license identifier.

        Args:
          license_type_id: The ID of the license type to fetch the license for.

          subscription_id: The ID of the subscription to fetch the license for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_license_id:
            raise ValueError(
                f"Expected a non-empty value for `external_license_id` but received {external_license_id!r}"
            )
        return await self._get(
            f"/licenses/external_license_id/{external_license_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "license_type_id": license_type_id,
                        "subscription_id": subscription_id,
                    },
                    license_retrieve_by_external_id_params.LicenseRetrieveByExternalIDParams,
                ),
            ),
            cast_to=LicenseRetrieveByExternalIDResponse,
        )


class LicensesWithRawResponse:
    def __init__(self, licenses: Licenses) -> None:
        self._licenses = licenses

        self.create = _legacy_response.to_raw_response_wrapper(
            licenses.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            licenses.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            licenses.list,
        )
        self.deactivate = _legacy_response.to_raw_response_wrapper(
            licenses.deactivate,
        )
        self.retrieve_by_external_id = _legacy_response.to_raw_response_wrapper(
            licenses.retrieve_by_external_id,
        )

    @cached_property
    def external_licenses(self) -> ExternalLicensesWithRawResponse:
        return ExternalLicensesWithRawResponse(self._licenses.external_licenses)

    @cached_property
    def usage(self) -> UsageWithRawResponse:
        return UsageWithRawResponse(self._licenses.usage)


class AsyncLicensesWithRawResponse:
    def __init__(self, licenses: AsyncLicenses) -> None:
        self._licenses = licenses

        self.create = _legacy_response.async_to_raw_response_wrapper(
            licenses.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            licenses.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            licenses.list,
        )
        self.deactivate = _legacy_response.async_to_raw_response_wrapper(
            licenses.deactivate,
        )
        self.retrieve_by_external_id = _legacy_response.async_to_raw_response_wrapper(
            licenses.retrieve_by_external_id,
        )

    @cached_property
    def external_licenses(self) -> AsyncExternalLicensesWithRawResponse:
        return AsyncExternalLicensesWithRawResponse(self._licenses.external_licenses)

    @cached_property
    def usage(self) -> AsyncUsageWithRawResponse:
        return AsyncUsageWithRawResponse(self._licenses.usage)


class LicensesWithStreamingResponse:
    def __init__(self, licenses: Licenses) -> None:
        self._licenses = licenses

        self.create = to_streamed_response_wrapper(
            licenses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            licenses.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            licenses.list,
        )
        self.deactivate = to_streamed_response_wrapper(
            licenses.deactivate,
        )
        self.retrieve_by_external_id = to_streamed_response_wrapper(
            licenses.retrieve_by_external_id,
        )

    @cached_property
    def external_licenses(self) -> ExternalLicensesWithStreamingResponse:
        return ExternalLicensesWithStreamingResponse(self._licenses.external_licenses)

    @cached_property
    def usage(self) -> UsageWithStreamingResponse:
        return UsageWithStreamingResponse(self._licenses.usage)


class AsyncLicensesWithStreamingResponse:
    def __init__(self, licenses: AsyncLicenses) -> None:
        self._licenses = licenses

        self.create = async_to_streamed_response_wrapper(
            licenses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            licenses.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            licenses.list,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            licenses.deactivate,
        )
        self.retrieve_by_external_id = async_to_streamed_response_wrapper(
            licenses.retrieve_by_external_id,
        )

    @cached_property
    def external_licenses(self) -> AsyncExternalLicensesWithStreamingResponse:
        return AsyncExternalLicensesWithStreamingResponse(self._licenses.external_licenses)

    @cached_property
    def usage(self) -> AsyncUsageWithStreamingResponse:
        return AsyncUsageWithStreamingResponse(self._licenses.usage)
