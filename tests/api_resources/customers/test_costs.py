# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types.customers import CostListResponse, CostListByExternalIDResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestCosts:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        cost = client.customers.costs.list(
            "string",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        cost = client.customers.costs.list(
            "string",
            group_by="string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.costs.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        cost = client.customers.costs.list_by_external_id(
            "string",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        cost = client.customers.costs.list_by_external_id(
            "string",
            group_by="string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.costs.with_raw_response.list_by_external_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])


class TestAsyncCosts:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        cost = await client.customers.costs.list(
            "string",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        cost = await client.customers.costs.list(
            "string",
            group_by="string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncOrb) -> None:
        response = await client.customers.costs.with_raw_response.list(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    async def test_method_list_by_external_id(self, client: AsyncOrb) -> None:
        cost = await client.customers.costs.list_by_external_id(
            "string",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, client: AsyncOrb) -> None:
        cost = await client.customers.costs.list_by_external_id(
            "string",
            group_by="string",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    async def test_raw_response_list_by_external_id(self, client: AsyncOrb) -> None:
        response = await client.customers.costs.with_raw_response.list_by_external_id(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])
