# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.pagination import SyncPage, AsyncPage
from orb.types.events import (
    BackfillListResponse,
    BackfillCloseResponse,
    BackfillFetchResponse,
    BackfillCreateResponse,
    BackfillRevertResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestBackfills:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Orb) -> None:
        backfill = client.events.backfills.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Orb) -> None:
        backfill = client.events.backfills.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            close_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="string",
            external_customer_id="string",
            replace_existing_events=True,
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        backfill = client.events.backfills.list()
        assert_matches_type(SyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        backfill = client.events.backfills.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(SyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    def test_method_close(self, client: Orb) -> None:
        backfill = client.events.backfills.close(
            "string",
        )
        assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        backfill = client.events.backfills.fetch(
            "string",
        )
        assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

    @parametrize
    def test_method_revert(self, client: Orb) -> None:
        backfill = client.events.backfills.revert(
            "string",
        )
        assert_matches_type(BackfillRevertResponse, backfill, path=["response"])


class TestAsyncBackfills:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            close_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="string",
            external_customer_id="string",
            replace_existing_events=True,
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.list()
        assert_matches_type(AsyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.list(
            cursor="string",
            limit=0,
        )
        assert_matches_type(AsyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    async def test_method_close(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.close(
            "string",
        )
        assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

    @parametrize
    async def test_method_fetch(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.fetch(
            "string",
        )
        assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

    @parametrize
    async def test_method_revert(self, client: AsyncOrb) -> None:
        backfill = await client.events.backfills.revert(
            "string",
        )
        assert_matches_type(BackfillRevertResponse, backfill, path=["response"])
