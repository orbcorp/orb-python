# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import Item
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestItems:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        item = client.items.create(
            name="API requests",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.items.with_raw_response.create(
            name="API requests",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        item = client.items.list()
        assert_matches_type(SyncPage[Item], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        item = client.items.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[Item], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.items.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncPage[Item], item, path=["response"])

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        item = client.items.fetch(
            "string",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.items.with_raw_response.fetch(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])


class TestAsyncItems:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        item = await client.items.create(
            name="API requests",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncOrb) -> None:
        response = await client.items.with_raw_response.create(
            name="API requests",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        item = await client.items.list()
        assert_matches_type(AsyncPage[Item], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        item = await client.items.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[Item], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOrb) -> None:
        response = await client.items.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(AsyncPage[Item], item, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        item = await client.items.fetch(
            "string",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, client: AsyncOrb) -> None:
        response = await client.items.with_raw_response.fetch(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])
