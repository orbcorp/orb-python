# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Item
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        item = client.items.create(
            name="API requests",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        item = client.items.create(
            name="API requests",
            metadata={"foo": "string"},
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.items.with_raw_response.create(
            name="API requests",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.items.with_streaming_response.create(
            name="API requests",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        item = client.items.update(
            item_id="item_id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        item = client.items.update(
            item_id="item_id",
            external_connections=[
                {
                    "external_connection_name": "stripe",
                    "external_entity_id": "external_entity_id",
                }
            ],
            metadata={"foo": "string"},
            name="name",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.items.with_raw_response.update(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.items.with_streaming_response.update(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.items.with_raw_response.update(
                item_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        item = client.items.list()
        assert_matches_type(SyncPage[Item], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        item = client.items.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[Item], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncPage[Item], item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncPage[Item], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Orb) -> None:
        item = client.items.archive(
            "item_id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Orb) -> None:
        response = client.items.with_raw_response.archive(
            "item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Orb) -> None:
        with client.items.with_streaming_response.archive(
            "item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.items.with_raw_response.archive(
                "",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        item = client.items.fetch(
            "item_id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.items.with_raw_response.fetch(
            "item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.items.with_streaming_response.fetch(
            "item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.items.with_raw_response.fetch(
                "",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.create(
            name="API requests",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.create(
            name="API requests",
            metadata={"foo": "string"},
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.items.with_raw_response.create(
            name="API requests",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.items.with_streaming_response.create(
            name="API requests",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.update(
            item_id="item_id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.update(
            item_id="item_id",
            external_connections=[
                {
                    "external_connection_name": "stripe",
                    "external_entity_id": "external_entity_id",
                }
            ],
            metadata={"foo": "string"},
            name="name",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.items.with_raw_response.update(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.items.with_streaming_response.update(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.items.with_raw_response.update(
                item_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.list()
        assert_matches_type(AsyncPage[Item], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[Item], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.items.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(AsyncPage[Item], item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.items.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncPage[Item], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.archive(
            "item_id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncOrb) -> None:
        response = await async_client.items.with_raw_response.archive(
            "item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncOrb) -> None:
        async with async_client.items.with_streaming_response.archive(
            "item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.items.with_raw_response.archive(
                "",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        item = await async_client.items.fetch(
            "item_id",
        )
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.items.with_raw_response.fetch(
            "item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Item, item, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.items.with_streaming_response.fetch(
            "item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Item, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.items.with_raw_response.fetch(
                "",
            )
