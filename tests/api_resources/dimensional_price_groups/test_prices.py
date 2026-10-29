# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.shared import Price
from orb.types.dimensional_price_groups import PriceCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        price = client.dimensional_price_groups.prices.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                }
            ],
        )
        assert_matches_type(PriceCreateResponse, price, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        price = client.dimensional_price_groups.prices.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                    "name": "name",
                }
            ],
            tiers=[
                {
                    "first_unit": 0,
                    "last_unit": 0,
                }
            ],
        )
        assert_matches_type(PriceCreateResponse, price, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.dimensional_price_groups.prices.with_raw_response.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceCreateResponse, price, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.dimensional_price_groups.prices.with_streaming_response.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(PriceCreateResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            client.dimensional_price_groups.prices.with_raw_response.create(
                dimensional_price_group_id="",
                cadence="one_time",
                currency="USD",
                item_id="item_id",
                model_type="unit",
                prices=[
                    {
                        "amounts": [0],
                        "dimension_values": ["x"],
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        price = client.dimensional_price_groups.prices.list(
            dimensional_price_group_id="dimensional_price_group_id",
        )
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        price = client.dimensional_price_groups.prices.list(
            dimensional_price_group_id="dimensional_price_group_id",
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.dimensional_price_groups.prices.with_raw_response.list(
            dimensional_price_group_id="dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(SyncPage[Price], price, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.dimensional_price_groups.prices.with_streaming_response.list(
            dimensional_price_group_id="dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = response.parse()
            assert_matches_type(SyncPage[Price], price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            client.dimensional_price_groups.prices.with_raw_response.list(
                dimensional_price_group_id="",
            )


class TestAsyncPrices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        price = await async_client.dimensional_price_groups.prices.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                }
            ],
        )
        assert_matches_type(PriceCreateResponse, price, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.dimensional_price_groups.prices.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                    "name": "name",
                }
            ],
            tiers=[
                {
                    "first_unit": 0,
                    "last_unit": 0,
                }
            ],
        )
        assert_matches_type(PriceCreateResponse, price, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.dimensional_price_groups.prices.with_raw_response.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(PriceCreateResponse, price, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.dimensional_price_groups.prices.with_streaming_response.create(
            dimensional_price_group_id="dimensional_price_group_id",
            cadence="one_time",
            currency="USD",
            item_id="item_id",
            model_type="unit",
            prices=[
                {
                    "amounts": [0],
                    "dimension_values": ["x"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(PriceCreateResponse, price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            await async_client.dimensional_price_groups.prices.with_raw_response.create(
                dimensional_price_group_id="",
                cadence="one_time",
                currency="USD",
                item_id="item_id",
                model_type="unit",
                prices=[
                    {
                        "amounts": [0],
                        "dimension_values": ["x"],
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        price = await async_client.dimensional_price_groups.prices.list(
            dimensional_price_group_id="dimensional_price_group_id",
        )
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        price = await async_client.dimensional_price_groups.prices.list(
            dimensional_price_group_id="dimensional_price_group_id",
            cursor="cursor",
            limit=1,
            status="active",
        )
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.dimensional_price_groups.prices.with_raw_response.list(
            dimensional_price_group_id="dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        price = response.parse()
        assert_matches_type(AsyncPage[Price], price, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.dimensional_price_groups.prices.with_streaming_response.list(
            dimensional_price_group_id="dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            price = await response.parse()
            assert_matches_type(AsyncPage[Price], price, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `dimensional_price_group_id` but received ''"
        ):
            await async_client.dimensional_price_groups.prices.with_raw_response.list(
                dimensional_price_group_id="",
            )
