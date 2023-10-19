# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import Plan
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
            metadata={},
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        external_plan_id = client.plans.external_plan_id.fetch(
            "string",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])


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
            metadata={},
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        external_plan_id = await client.plans.external_plan_id.fetch(
            "string",
        )
        assert_matches_type(Plan, external_plan_id, path=["response"])
