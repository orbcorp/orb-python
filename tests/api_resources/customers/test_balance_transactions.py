# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.customers import (
    BalanceTransactionListResponse,
    BalanceTransactionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalanceTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
            description="description",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.customers.balance_transactions.with_raw_response.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_transaction = response.parse()
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.customers.balance_transactions.with_streaming_response.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_transaction = response.parse()
            assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.balance_transactions.with_raw_response.create(
                customer_id="",
                amount="amount",
                type="increment",
            )

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.list(
            customer_id="customer_id",
        )
        assert_matches_type(SyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.list(
            customer_id="customer_id",
            cursor="cursor",
            limit=1,
            operation_time_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.customers.balance_transactions.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_transaction = response.parse()
        assert_matches_type(SyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.customers.balance_transactions.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_transaction = response.parse()
            assert_matches_type(SyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.balance_transactions.with_raw_response.list(
                customer_id="",
            )


class TestAsyncBalanceTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        balance_transaction = await async_client.customers.balance_transactions.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        balance_transaction = await async_client.customers.balance_transactions.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
            description="description",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.balance_transactions.with_raw_response.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_transaction = response.parse()
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.balance_transactions.with_streaming_response.create(
            customer_id="customer_id",
            amount="amount",
            type="increment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_transaction = await response.parse()
            assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.balance_transactions.with_raw_response.create(
                customer_id="",
                amount="amount",
                type="increment",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        balance_transaction = await async_client.customers.balance_transactions.list(
            customer_id="customer_id",
        )
        assert_matches_type(AsyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        balance_transaction = await async_client.customers.balance_transactions.list(
            customer_id="customer_id",
            cursor="cursor",
            limit=1,
            operation_time_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.balance_transactions.with_raw_response.list(
            customer_id="customer_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance_transaction = response.parse()
        assert_matches_type(AsyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.balance_transactions.with_streaming_response.list(
            customer_id="customer_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance_transaction = await response.parse()
            assert_matches_type(AsyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.balance_transactions.with_raw_response.list(
                customer_id="",
            )
