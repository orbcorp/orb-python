# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Subscription
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestSubscriptions:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        subscription = client.coupons.subscriptions.list(
            "string",
        )
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        subscription = client.coupons.subscriptions.list(
            "string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.coupons.subscriptions.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncPage[Subscription], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.coupons.subscriptions.with_streaming_response.list(
            "string",
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
                "",
            )


class TestAsyncSubscriptions:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        subscription = await client.coupons.subscriptions.list(
            "string",
        )
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        subscription = await client.coupons.subscriptions.list(
            "string",
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOrb) -> None:
        response = await client.coupons.subscriptions.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncOrb) -> None:
        async with client.coupons.subscriptions.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncPage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `coupon_id` but received ''"):
            await client.coupons.subscriptions.with_raw_response.list(
                "",
            )
