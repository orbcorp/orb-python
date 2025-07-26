# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import DimensionalPriceGroup
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalDimensionalPriceGroupID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Orb) -> None:
        external_dimensional_price_group_id = (
            client.dimensional_price_groups.external_dimensional_price_group_id.retrieve(
                "external_dimensional_price_group_id",
            )
        )
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Orb) -> None:
        response = client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.retrieve(
            "external_dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_dimensional_price_group_id = response.parse()
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Orb) -> None:
        with client.dimensional_price_groups.external_dimensional_price_group_id.with_streaming_response.retrieve(
            "external_dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_dimensional_price_group_id = response.parse()
            assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_dimensional_price_group_id` but received ''"
        ):
            client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        external_dimensional_price_group_id = (
            client.dimensional_price_groups.external_dimensional_price_group_id.update(
                path_external_dimensional_price_group_id="external_dimensional_price_group_id",
            )
        )
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        external_dimensional_price_group_id = (
            client.dimensional_price_groups.external_dimensional_price_group_id.update(
                path_external_dimensional_price_group_id="external_dimensional_price_group_id",
                body_external_dimensional_price_group_id="external_dimensional_price_group_id",
                metadata={"foo": "string"},
            )
        )
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.update(
            path_external_dimensional_price_group_id="external_dimensional_price_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_dimensional_price_group_id = response.parse()
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.dimensional_price_groups.external_dimensional_price_group_id.with_streaming_response.update(
            path_external_dimensional_price_group_id="external_dimensional_price_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_dimensional_price_group_id = response.parse()
            assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `path_external_dimensional_price_group_id` but received ''",
        ):
            client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.update(
                path_external_dimensional_price_group_id="",
            )


class TestAsyncExternalDimensionalPriceGroupID:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOrb) -> None:
        external_dimensional_price_group_id = (
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.retrieve(
                "external_dimensional_price_group_id",
            )
        )
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOrb) -> None:
        response = (
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.retrieve(
                "external_dimensional_price_group_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_dimensional_price_group_id = response.parse()
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOrb) -> None:
        async with (
            async_client.dimensional_price_groups.external_dimensional_price_group_id.with_streaming_response.retrieve(
                "external_dimensional_price_group_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_dimensional_price_group_id = await response.parse()
            assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_dimensional_price_group_id` but received ''"
        ):
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        external_dimensional_price_group_id = (
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.update(
                path_external_dimensional_price_group_id="external_dimensional_price_group_id",
            )
        )
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        external_dimensional_price_group_id = (
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.update(
                path_external_dimensional_price_group_id="external_dimensional_price_group_id",
                body_external_dimensional_price_group_id="external_dimensional_price_group_id",
                metadata={"foo": "string"},
            )
        )
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = (
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.update(
                path_external_dimensional_price_group_id="external_dimensional_price_group_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_dimensional_price_group_id = response.parse()
        assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with (
            async_client.dimensional_price_groups.external_dimensional_price_group_id.with_streaming_response.update(
                path_external_dimensional_price_group_id="external_dimensional_price_group_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_dimensional_price_group_id = await response.parse()
            assert_matches_type(DimensionalPriceGroup, external_dimensional_price_group_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError,
            match=r"Expected a non-empty value for `path_external_dimensional_price_group_id` but received ''",
        ):
            await async_client.dimensional_price_groups.external_dimensional_price_group_id.with_raw_response.update(
                path_external_dimensional_price_group_id="",
            )
