# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import httpx

from ...types import Coupon, coupon_list_params, coupon_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncPage, AsyncPage
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
)
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Orb, AsyncOrb

__all__ = ["Coupons", "AsyncCoupons"]


class Coupons(SyncAPIResource):
    subscriptions: Subscriptions
    with_raw_response: CouponsWithRawResponse

    def __init__(self, client: Orb) -> None:
        super().__init__(client)
        self.subscriptions = Subscriptions(client)
        self.with_raw_response = CouponsWithRawResponse(self)

    def create(
        self,
        *,
        discount: coupon_create_params.Discount,
        redemption_code: str,
        duration_in_months: Optional[int] | NotGiven = NOT_GIVEN,
        max_redemptions: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Coupon:
        """
        This endpoint allows the creation of coupons, which can then be redeemed at
        subscription creation or plan change.

        Args:
          redemption_code: This string can be used to redeem this coupon for a given subscription.

          duration_in_months: This allows for a coupon's discount to apply for a limited time (determined in
              months); a `null` value here means "unlimited time".

          max_redemptions: The maximum number of redemptions allowed for this coupon before it is
              exhausted;`null` here means "unlimited".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/coupons",
            body=maybe_transform(
                {
                    "discount": discount,
                    "redemption_code": redemption_code,
                    "duration_in_months": duration_in_months,
                    "max_redemptions": max_redemptions,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Coupon,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        redemption_code: Optional[str] | NotGiven = NOT_GIVEN,
        show_archived: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Coupon]:
        """
        This endpoint returns a list of all coupons for an account in a list format.

        The list of coupons is ordered starting from the most recently created coupon.
        The response also includes `pagination_metadata`, which lets the caller retrieve
        the next page of results if they exist. More information about pagination can be
        found in the Pagination-metadata schema.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          redemption_code: Filter to coupons matching this redemption code.

          show_archived: Show archived coupons as well (by default, this endpoint only returns active
              coupons).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/coupons",
            page=SyncPage[Coupon],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "redemption_code": redemption_code,
                        "show_archived": show_archived,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            model=Coupon,
        )

    def archive(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Coupon:
        """This endpoint allows a coupon to be archived.

        Archived coupons can no longer be
        redeemed, and will be hidden from lists of active coupons. Additionally, once a
        coupon is archived, its redemption code can be reused for a different coupon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/coupons/{coupon_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Coupon,
        )

    def fetch(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Coupon:
        """This endpoint retrieves a coupon by its ID.

        To fetch coupons by their redemption
        code, use the [List coupons](list-coupons) endpoint with the redemption_code
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/coupons/{coupon_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )


class AsyncCoupons(AsyncAPIResource):
    subscriptions: AsyncSubscriptions
    with_raw_response: AsyncCouponsWithRawResponse

    def __init__(self, client: AsyncOrb) -> None:
        super().__init__(client)
        self.subscriptions = AsyncSubscriptions(client)
        self.with_raw_response = AsyncCouponsWithRawResponse(self)

    async def create(
        self,
        *,
        discount: coupon_create_params.Discount,
        redemption_code: str,
        duration_in_months: Optional[int] | NotGiven = NOT_GIVEN,
        max_redemptions: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Coupon:
        """
        This endpoint allows the creation of coupons, which can then be redeemed at
        subscription creation or plan change.

        Args:
          redemption_code: This string can be used to redeem this coupon for a given subscription.

          duration_in_months: This allows for a coupon's discount to apply for a limited time (determined in
              months); a `null` value here means "unlimited time".

          max_redemptions: The maximum number of redemptions allowed for this coupon before it is
              exhausted;`null` here means "unlimited".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/coupons",
            body=maybe_transform(
                {
                    "discount": discount,
                    "redemption_code": redemption_code,
                    "duration_in_months": duration_in_months,
                    "max_redemptions": max_redemptions,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Coupon,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        redemption_code: Optional[str] | NotGiven = NOT_GIVEN,
        show_archived: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Coupon, AsyncPage[Coupon]]:
        """
        This endpoint returns a list of all coupons for an account in a list format.

        The list of coupons is ordered starting from the most recently created coupon.
        The response also includes `pagination_metadata`, which lets the caller retrieve
        the next page of results if they exist. More information about pagination can be
        found in the Pagination-metadata schema.

        Args:
          cursor: Cursor for pagination. This can be populated by the `next_cursor` value returned
              from the initial request.

          limit: The number of items to fetch. Defaults to 20.

          redemption_code: Filter to coupons matching this redemption code.

          show_archived: Show archived coupons as well (by default, this endpoint only returns active
              coupons).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/coupons",
            page=AsyncPage[Coupon],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "redemption_code": redemption_code,
                        "show_archived": show_archived,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            model=Coupon,
        )

    async def archive(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Coupon:
        """This endpoint allows a coupon to be archived.

        Archived coupons can no longer be
        redeemed, and will be hidden from lists of active coupons. Additionally, once a
        coupon is archived, its redemption code can be reused for a different coupon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/coupons/{coupon_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Coupon,
        )

    async def fetch(
        self,
        coupon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Coupon:
        """This endpoint retrieves a coupon by its ID.

        To fetch coupons by their redemption
        code, use the [List coupons](list-coupons) endpoint with the redemption_code
        parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/coupons/{coupon_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )


class CouponsWithRawResponse:
    def __init__(self, coupons: Coupons) -> None:
        self.subscriptions = SubscriptionsWithRawResponse(coupons.subscriptions)

        self.create = to_raw_response_wrapper(
            coupons.create,
        )
        self.list = to_raw_response_wrapper(
            coupons.list,
        )
        self.archive = to_raw_response_wrapper(
            coupons.archive,
        )
        self.fetch = to_raw_response_wrapper(
            coupons.fetch,
        )


class AsyncCouponsWithRawResponse:
    def __init__(self, coupons: AsyncCoupons) -> None:
        self.subscriptions = AsyncSubscriptionsWithRawResponse(coupons.subscriptions)

        self.create = async_to_raw_response_wrapper(
            coupons.create,
        )
        self.list = async_to_raw_response_wrapper(
            coupons.list,
        )
        self.archive = async_to_raw_response_wrapper(
            coupons.archive,
        )
        self.fetch = async_to_raw_response_wrapper(
            coupons.fetch,
        )
