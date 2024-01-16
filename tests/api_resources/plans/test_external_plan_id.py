# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import Plan
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestExternalPlanID:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.update(
            "string",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.update(
            "string",
            external_plan_id="string",
            metadata={"foo": "string"},
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.plans.external_plan_id.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.plans.external_plan_id.with_streaming_response.update(
            "string",
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
                "",
                external_plan_id="",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.fetch(
            "string",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.plans.external_plan_id.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.plans.external_plan_id.with_streaming_response.fetch(
            "string",
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
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncOrb) -> None:
        external_plan_id = await client.plans.external_plan_id.update(
            "string",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncOrb) -> None:
        external_plan_id = await client.plans.external_plan_id.update(
            "string",
            external_plan_id="string",
            metadata={"foo": "string"},
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncOrb) -> None:
        response = await client.plans.external_plan_id.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncOrb) -> None:
        async with client.plans.external_plan_id.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_plan_id = await response.parse()
            assert_matches_type(Plan, external_plan_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, client: AsyncOrb) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `other_external_plan_id` but received ''"
        ):
            await client.plans.external_plan_id.with_raw_response.update(
                "",
                external_plan_id="",
            )

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        external_plan_id = await client.plans.external_plan_id.fetch(
            "string",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, client: AsyncOrb) -> None:
        response = await client.plans.external_plan_id.with_raw_response.fetch(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_plan_id = response.parse()
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, client: AsyncOrb) -> None:
        async with client.plans.external_plan_id.with_streaming_response.fetch(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_plan_id = await response.parse()
            assert_matches_type(Plan, external_plan_id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_plan_id` but received ''"):
            await client.plans.external_plan_id.with_raw_response.fetch(
                "",
            )
