# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Coupon
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoupons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        coupon = client.coupons.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        coupon = client.coupons.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
            duration_in_months=12,
            max_redemptions=1,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.coupons.with_raw_response.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.coupons.with_streaming_response.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        coupon = client.coupons.list()
        assert_matches_type(SyncPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        coupon = client.coupons.list(
            cursor="cursor",
            limit=1,
            redemption_code="redemption_code",
            show_archived=True,
        )
        assert_matches_type(SyncPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(SyncPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(SyncPage[Coupon], coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Orb) -> None:
        coupon = client.coupons.archive(
            "coupon_id",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Orb) -> None:
        response = client.coupons.with_raw_response.archive(
            "coupon_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Orb) -> None:
        with client.coupons.with_streaming_response.archive(
            "coupon_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.coupons.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        coupon = client.coupons.fetch(
            "coupon_id",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.coupons.with_raw_response.fetch(
            "coupon_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.coupons.with_streaming_response.fetch(
            "coupon_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            client.coupons.with_raw_response.fetch(
                "",
            )


class TestAsyncCoupons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        coupon = await async_client.coupons.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        coupon = await async_client.coupons.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
            duration_in_months=12,
            max_redemptions=1,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.coupons.with_raw_response.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.coupons.with_streaming_response.create(
            discount={
                "discount_type": "percentage",
                "percentage_discount": 0,
            },
            redemption_code="HALFOFF",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        coupon = await async_client.coupons.list()
        assert_matches_type(AsyncPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        coupon = await async_client.coupons.list(
            cursor="cursor",
            limit=1,
            redemption_code="redemption_code",
            show_archived=True,
        )
        assert_matches_type(AsyncPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(AsyncPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(AsyncPage[Coupon], coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncOrb) -> None:
        coupon = await async_client.coupons.archive(
            "coupon_id",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncOrb) -> None:
        response = await async_client.coupons.with_raw_response.archive(
            "coupon_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncOrb) -> None:
        async with async_client.coupons.with_streaming_response.archive(
            "coupon_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.coupons.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        coupon = await async_client.coupons.fetch(
            "coupon_id",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.coupons.with_raw_response.fetch(
            "coupon_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.coupons.with_streaming_response.fetch(
            "coupon_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await async_client.coupons.with_raw_response.fetch(
                "",
            )
