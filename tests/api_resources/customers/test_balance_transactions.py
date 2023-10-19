# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

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
api_key = "My API Key"


class TestBalanceTransactions:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.create(
            "string",
            amount="string",
            type="increment",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.create(
            "string",
            amount="string",
            type="increment",
            description="string",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.list(
            "string",
        )
        assert_matches_type(SyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        balance_transaction = client.customers.balance_transactions.list(
            "string",
            cursor="string",
            limit=0,
            operation_time_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])


class TestAsyncBalanceTransactions:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        balance_transaction = await client.customers.balance_transactions.create(
            "string",
            amount="string",
            type="increment",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncOrb) -> None:
        balance_transaction = await client.customers.balance_transactions.create(
            "string",
            amount="string",
            type="increment",
            description="string",
        )
        assert_matches_type(BalanceTransactionCreateResponse, balance_transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        balance_transaction = await client.customers.balance_transactions.list(
            "string",
        )
        assert_matches_type(AsyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        balance_transaction = await client.customers.balance_transactions.list(
            "string",
            cursor="string",
            limit=0,
            operation_time_gt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lt=parse_datetime("2019-12-27T18:11:19.117Z"),
            operation_time_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(AsyncPage[BalanceTransactionListResponse], balance_transaction, path=["response"])
