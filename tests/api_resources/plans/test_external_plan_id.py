# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Plan
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalPlanID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.update(
            other_external_plan_id="external_plan_id",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.update(
            other_external_plan_id="external_plan_id",
            external_plan_id="external_plan_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.plans.external_plan_id.with_raw_response.update(
            other_external_plan_id="external_plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.plans.external_plan_id.with_streaming_response.update(
            other_external_plan_id="external_plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_plan_id = response.parse()
            assert_matches_type(Plan, external_plan_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `other_external_plan_id` but received ''"
        ):
            client.plans.external_plan_id.with_raw_response.update(
                other_external_plan_id="",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.fetch(
            "external_plan_id",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.plans.external_plan_id.with_raw_response.fetch(
            "external_plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.plans.external_plan_id.with_streaming_response.fetch(
            "external_plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_plan_id = response.parse()
            assert_matches_type(Plan, external_plan_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            client.plans.external_plan_id.with_raw_response.fetch(
                "",
            )


class TestAsyncExternalPlanID:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        external_plan_id = await async_client.plans.external_plan_id.update(
            other_external_plan_id="external_plan_id",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        external_plan_id = await async_client.plans.external_plan_id.update(
            other_external_plan_id="external_plan_id",
            external_plan_id="external_plan_id",
            metadata={"foo": "string"},
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.external_plan_id.with_raw_response.update(
            other_external_plan_id="external_plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.external_plan_id.with_streaming_response.update(
            other_external_plan_id="external_plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_plan_id = await response.parse()
            assert_matches_type(Plan, external_plan_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `other_external_plan_id` but received ''"
        ):
            await async_client.plans.external_plan_id.with_raw_response.update(
                other_external_plan_id="",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        external_plan_id = await async_client.plans.external_plan_id.fetch(
            "external_plan_id",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.plans.external_plan_id.with_raw_response.fetch(
            "external_plan_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.plans.external_plan_id.with_streaming_response.fetch(
            "external_plan_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_plan_id = await response.parse()
            assert_matches_type(Plan, external_plan_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            await async_client.plans.external_plan_id.with_raw_response.fetch(
                "",
            )
