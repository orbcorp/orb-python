# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types.shared import Price

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalPriceID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        external_price_id = client.prices.external_price_id.update(
            external_price_id="external_price_id",
        )
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        external_price_id = client.prices.external_price_id.update(
            external_price_id="external_price_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.prices.external_price_id.with_raw_response.update(
            external_price_id="external_price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_price_id = response.parse()
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.prices.external_price_id.with_streaming_response.update(
            external_price_id="external_price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_price_id = response.parse()
            assert_matches_type(Price, external_price_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_price_id` but received ''"):
            client.prices.external_price_id.with_raw_response.update(
                external_price_id="",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        external_price_id = client.prices.external_price_id.fetch(
            "external_price_id",
        )
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.prices.external_price_id.with_raw_response.fetch(
            "external_price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_price_id = response.parse()
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.prices.external_price_id.with_streaming_response.fetch(
            "external_price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_price_id = response.parse()
            assert_matches_type(Price, external_price_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_price_id` but received ''"):
            client.prices.external_price_id.with_raw_response.fetch(
                "",
            )


class TestAsyncExternalPriceID:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        external_price_id = await async_client.prices.external_price_id.update(
            external_price_id="external_price_id",
        )
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        external_price_id = await async_client.prices.external_price_id.update(
            external_price_id="external_price_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.external_price_id.with_raw_response.update(
            external_price_id="external_price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_price_id = response.parse()
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.external_price_id.with_streaming_response.update(
            external_price_id="external_price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_price_id = await response.parse()
            assert_matches_type(Price, external_price_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_price_id` but received ''"):
            await async_client.prices.external_price_id.with_raw_response.update(
                external_price_id="",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        external_price_id = await async_client.prices.external_price_id.fetch(
            "external_price_id",
        )
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.prices.external_price_id.with_raw_response.fetch(
            "external_price_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_price_id = response.parse()
        assert_matches_type(Price, external_price_id, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.prices.external_price_id.with_streaming_response.fetch(
            "external_price_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_price_id = await response.parse()
            assert_matches_type(Price, external_price_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_price_id` but received ''"):
            await async_client.prices.external_price_id.with_raw_response.fetch(
                "",
            )
