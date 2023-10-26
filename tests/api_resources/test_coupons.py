# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import Coupon
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCoupons:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        coupon = client.coupons.create(
            discount={
                "discount_type": "percentage",
                "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                "percentage_discount": 0.15,
            },
            redemption_code="HALFOFF",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        coupon = client.coupons.create(
            discount={
                "discount_type": "percentage",
                "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                "reason": "string",
                "percentage_discount": 0.15,
            },
            redemption_code="HALFOFF",
            duration_in_months=12,
            max_redemptions=0,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        coupon = client.coupons.list()
        assert_matches_type(SyncPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        coupon = client.coupons.list(
            cursor="string",
            limit=0,
            redemption_code="string",
            show_archived=True,
        )
        assert_matches_type(SyncPage[Coupon], coupon, path=["response"])

    @parametrize
    def test_method_archive(self, client: Orb) -> None:
        coupon = client.coupons.archive(
            "string",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        coupon = client.coupons.fetch(
            "string",
        )
        assert_matches_type(Coupon, coupon, path=["response"])


class TestAsyncCoupons:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        coupon = await client.coupons.create(
            discount={
                "discount_type": "percentage",
                "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                "percentage_discount": 0.15,
            },
            redemption_code="HALFOFF",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncOrb) -> None:
        coupon = await client.coupons.create(
            discount={
                "discount_type": "percentage",
                "applies_to_price_ids": ["h74gfhdjvn7ujokd", "7hfgtgjnbvc3ujkl"],
                "reason": "string",
                "percentage_discount": 0.15,
            },
            redemption_code="HALFOFF",
            duration_in_months=12,
            max_redemptions=0,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        coupon = await client.coupons.list()
        assert_matches_type(AsyncPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        coupon = await client.coupons.list(
            cursor="string",
            limit=0,
            redemption_code="string",
            show_archived=True,
        )
        assert_matches_type(AsyncPage[Coupon], coupon, path=["response"])

    @parametrize
    async def test_method_archive(self, client: AsyncOrb) -> None:
        coupon = await client.coupons.archive(
            "string",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        coupon = await client.coupons.fetch(
            "string",
        )
        assert_matches_type(Coupon, coupon, path=["response"])
