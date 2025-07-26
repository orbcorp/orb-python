# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import (
    DimensionalPriceGroup,
)
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDimensionalPriceGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
            external_dimensional_price_group_id="external_dimensional_price_group_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.dimensional_price_groups.with_raw_response.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.dimensional_price_groups.with_streaming_response.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = response.parse()
            assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.retrieve(
            "dimensional_price_group_id",
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.dimensional_price_groups.with_raw_response.retrieve(
            "dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.dimensional_price_groups.with_streaming_response.retrieve(
            "dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = response.parse()
            assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            client.dimensional_price_groups.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.update(
            dimensional_price_group_id="dimensional_price_group_id",
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.update(
            dimensional_price_group_id="dimensional_price_group_id",
            external_dimensional_price_group_id="external_dimensional_price_group_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.dimensional_price_groups.with_raw_response.update(
            dimensional_price_group_id="dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.dimensional_price_groups.with_streaming_response.update(
            dimensional_price_group_id="dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = response.parse()
            assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            client.dimensional_price_groups.with_raw_response.update(
                dimensional_price_group_id="",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.list()
        assert_matches_type(SyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        dimensional_price_group = client.dimensional_price_groups.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.dimensional_price_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(SyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.dimensional_price_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = response.parse()
            assert_matches_type(SyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDimensionalPriceGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
            external_dimensional_price_group_id="external_dimensional_price_group_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.dimensional_price_groups.with_raw_response.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.dimensional_price_groups.with_streaming_response.create(
            billable_metric_id="billable_metric_id",
            dimensions=["region", "instance_type"],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = await response.parse()
            assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.retrieve(
            "dimensional_price_group_id",
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = await async_client.dimensional_price_groups.with_raw_response.retrieve(
            "dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with async_client.dimensional_price_groups.with_streaming_response.retrieve(
            "dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = await response.parse()
            assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            await async_client.dimensional_price_groups.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.update(
            dimensional_price_group_id="dimensional_price_group_id",
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.update(
            dimensional_price_group_id="dimensional_price_group_id",
            external_dimensional_price_group_id="external_dimensional_price_group_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.dimensional_price_groups.with_raw_response.update(
            dimensional_price_group_id="dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.dimensional_price_groups.with_streaming_response.update(
            dimensional_price_group_id="dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = await response.parse()
            assert_matches_type(DimensionalPriceGroup, dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            await async_client.dimensional_price_groups.with_raw_response.update(
                dimensional_price_group_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.list()
        assert_matches_type(AsyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        dimensional_price_group = await async_client.dimensional_price_groups.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.dimensional_price_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dimensional_price_group = response.parse()
        assert_matches_type(AsyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.dimensional_price_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dimensional_price_group = await response.parse()
            assert_matches_type(AsyncPage[DimensionalPriceGroup], dimensional_price_group, path=["response"])

        assert cast(Any, response.is_closed) is True
