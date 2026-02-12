# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .. import _legacy_response
from ..types import license_type_list_params, license_type_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.license_type_list_response import LicenseTypeListResponse
from ..types.license_type_create_response import LicenseTypeCreateResponse
from ..types.license_type_retrieve_response import LicenseTypeRetrieveResponse

__all__ = ["LicenseTypes", "AsyncLicenseTypes"]


class LicenseTypes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LicenseTypesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return LicenseTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LicenseTypesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return LicenseTypesWithStreamingResponse(self)

    def create(
        self,
        *,
        grouping_key: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LicenseTypeCreateResponse:
        """
        This endpoint is used to create a new license type.

        License types are used to group licenses and define billing behavior. Each
        license type has a name and a grouping key that determines how metrics are
        aggregated for billing purposes.

        Args:
          grouping_key: The key used for grouping licenses of this type. This is typically a user
              identifier field.

          name: The name of the license type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/license_types",
            body=maybe_transform(
                {
                    "grouping_key": grouping_key,
                    "name": name,
                },
                license_type_create_params.LicenseTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LicenseTypeCreateResponse,
        )

    def retrieve(
        self,
        license_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LicenseTypeRetrieveResponse:
        """
        This endpoint returns a license type identified by its license_type_id.

        Use this endpoint to retrieve details about a specific license type, including
        its name and grouping key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license_type_id:
            raise ValueError(f"Expected a non-empty value for `license_type_id` but received {license_type_id!r}")
        return self._get(
            f"/license_types/{license_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseTypeRetrieveResponse,
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
    ) -> SyncPage[LicenseTypeListResponse]:
        """
        This endpoint returns a list of all license types configured for the account,
        ordered in ascending order by creation time.

        License types are used to group licenses and define billing behavior. Each
        license type has a name and a grouping key that determines how metrics are
        aggregated for billing purposes.

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
            "/license_types",
            page=SyncPage[LicenseTypeListResponse],
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
                    license_type_list_params.LicenseTypeListParams,
                ),
            ),
            model=LicenseTypeListResponse,
        )


class AsyncLicenseTypes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLicenseTypesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/orbcorp/orb-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLicenseTypesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLicenseTypesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/orbcorp/orb-python#with_streaming_response
        """
        return AsyncLicenseTypesWithStreamingResponse(self)

    async def create(
        self,
        *,
        grouping_key: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> LicenseTypeCreateResponse:
        """
        This endpoint is used to create a new license type.

        License types are used to group licenses and define billing behavior. Each
        license type has a name and a grouping key that determines how metrics are
        aggregated for billing purposes.

        Args:
          grouping_key: The key used for grouping licenses of this type. This is typically a user
              identifier field.

          name: The name of the license type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/license_types",
            body=await async_maybe_transform(
                {
                    "grouping_key": grouping_key,
                    "name": name,
                },
                license_type_create_params.LicenseTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LicenseTypeCreateResponse,
        )

    async def retrieve(
        self,
        license_type_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LicenseTypeRetrieveResponse:
        """
        This endpoint returns a license type identified by its license_type_id.

        Use this endpoint to retrieve details about a specific license type, including
        its name and grouping key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not license_type_id:
            raise ValueError(f"Expected a non-empty value for `license_type_id` but received {license_type_id!r}")
        return await self._get(
            f"/license_types/{license_type_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LicenseTypeRetrieveResponse,
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
    ) -> AsyncPaginator[LicenseTypeListResponse, AsyncPage[LicenseTypeListResponse]]:
        """
        This endpoint returns a list of all license types configured for the account,
        ordered in ascending order by creation time.

        License types are used to group licenses and define billing behavior. Each
        license type has a name and a grouping key that determines how metrics are
        aggregated for billing purposes.

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
            "/license_types",
            page=AsyncPage[LicenseTypeListResponse],
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
                    license_type_list_params.LicenseTypeListParams,
                ),
            ),
            model=LicenseTypeListResponse,
        )


class LicenseTypesWithRawResponse:
    def __init__(self, license_types: LicenseTypes) -> None:
        self._license_types = license_types

        self.create = _legacy_response.to_raw_response_wrapper(
            license_types.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            license_types.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            license_types.list,
        )


class AsyncLicenseTypesWithRawResponse:
    def __init__(self, license_types: AsyncLicenseTypes) -> None:
        self._license_types = license_types

        self.create = _legacy_response.async_to_raw_response_wrapper(
            license_types.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            license_types.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            license_types.list,
        )


class LicenseTypesWithStreamingResponse:
    def __init__(self, license_types: LicenseTypes) -> None:
        self._license_types = license_types

        self.create = to_streamed_response_wrapper(
            license_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            license_types.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            license_types.list,
        )


class AsyncLicenseTypesWithStreamingResponse:
    def __init__(self, license_types: AsyncLicenseTypes) -> None:
        self._license_types = license_types

        self.create = async_to_streamed_response_wrapper(
            license_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            license_types.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            license_types.list,
        )
