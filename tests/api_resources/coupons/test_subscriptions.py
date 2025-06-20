# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Subscription
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        subscription = client.coupons.subscriptions.list(
            coupon_id="coupon_id",
        )
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        subscription = client.coupons.subscriptions.list(
            coupon_id="coupon_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.coupons.subscriptions.with_raw_response.list(
            coupon_id="coupon_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.coupons.subscriptions.with_streaming_response.list(
            coupon_id="coupon_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.coupons.subscriptions.with_raw_response.list(
                coupon_id="",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.coupons.subscriptions.list(
            coupon_id="coupon_id",
        )
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        subscription = await async_client.coupons.subscriptions.list(
            coupon_id="coupon_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.coupons.subscriptions.with_raw_response.list(
            coupon_id="coupon_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.coupons.subscriptions.with_streaming_response.list(
            coupon_id="coupon_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.coupons.subscriptions.with_raw_response.list(
                coupon_id="",
            )
