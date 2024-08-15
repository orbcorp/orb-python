# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.types.customers import (
    CostListResponse,
    CostListByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        cost = client.customers.costs.list(
            customer_id="customer_id",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        cost = client.customers.costs.list(
            customer_id="customer_id",
            currency="currency",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.costs.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.costs.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = response.parse()
            assert_matches_type(CostListResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.costs.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    def test_method_list_by_external_id(self, client: Orb) -> None:
        cost = client.customers.costs.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    def test_method_list_by_external_id_with_all_params(self, client: Orb) -> None:
        cost = client.customers.costs.list_by_external_id(
            external_customer_id="external_customer_id",
            currency="currency",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    def test_raw_response_list_by_external_id(self, client: Orb) -> None:
        response = client.customers.costs.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    def test_streaming_response_list_by_external_id(self, client: Orb) -> None:
        with client.customers.costs.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = response.parse()
            assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            client.customers.costs.with_raw_response.list_by_external_id(
                external_customer_id="",
            )


class TestAsyncCosts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        cost = await async_client.customers.costs.list(
            customer_id="customer_id",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        cost = await async_client.customers.costs.list(
            customer_id="customer_id",
            currency="currency",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.costs.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListResponse, cost, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.costs.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = await response.parse()
            assert_matches_type(CostListResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.costs.with_raw_response.list(
                customer_id="",
            )

    @parametrize
    async def test_method_list_by_external_id(self, async_client: AsyncOrb) -> None:
        cost = await async_client.customers.costs.list_by_external_id(
            external_customer_id="external_customer_id",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    async def test_method_list_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        cost = await async_client.customers.costs.list_by_external_id(
            external_customer_id="external_customer_id",
            currency="currency",
            timeframe_end=parse_datetime("2022-03-01T05:00:00Z"),
            timeframe_start=parse_datetime("2022-02-01T05:00:00Z"),
            view_mode="periodic",
        )
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    async def test_raw_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.costs.with_raw_response.list_by_external_id(
            external_customer_id="external_customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cost = response.parse()
        assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

    @parametrize
    async def test_streaming_response_list_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.costs.with_streaming_response.list_by_external_id(
            external_customer_id="external_customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cost = await response.parse()
            assert_matches_type(CostListByExternalIDResponse, cost, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_customer_id` but received ''"):
            await async_client.customers.costs.with_raw_response.list_by_external_id(
                external_customer_id="",
            )
