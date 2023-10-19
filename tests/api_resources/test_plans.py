# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb.types import Plan
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestPlans:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        plan = client.plans.create(
            currency="string",
            name="string",
            prices=[{}],
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        plan = client.plans.create(
            currency="string",
            name="string",
            prices=[{}],
            default_invoice_memo="string",
            external_plan_id="string",
            metadata={},
            net_terms=0,
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        plan = client.plans.update(
            "string",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        plan = client.plans.update(
            "string",
            external_plan_id="string",
            metadata={},
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        plan = client.plans.list()
        assert_matches_type(SyncPage[Plan], plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        plan = client.plans.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            limit=0,
            status="active",
        )
        assert_matches_type(SyncPage[Plan], plan, path=["response"])

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        plan = client.plans.fetch(
            "string",
        )
        assert_matches_type(Plan, plan, path=["response"])


class TestAsyncPlans:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        plan = await client.plans.create(
            currency="string",
            name="string",
            prices=[{}],
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncOrb) -> None:
        plan = await client.plans.create(
            currency="string",
            name="string",
            prices=[{}],
            default_invoice_memo="string",
            external_plan_id="string",
            metadata={},
            net_terms=0,
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncOrb) -> None:
        plan = await client.plans.update(
            "string",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncOrb) -> None:
        plan = await client.plans.update(
            "string",
            external_plan_id="string",
            metadata={},
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        plan = await client.plans.list()
        assert_matches_type(AsyncPage[Plan], plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        plan = await client.plans.list(
            created_at_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            limit=0,
            status="active",
        )
        assert_matches_type(AsyncPage[Plan], plan, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        plan = await client.plans.fetch(
            "string",
        )
        assert_matches_type(Plan, plan, path=["response"])
