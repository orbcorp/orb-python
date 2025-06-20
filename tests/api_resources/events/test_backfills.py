# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

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


class TestBackfills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            customer_id="customer_id",
            deprecation_filter="my_numeric_property > 100 AND my_other_property = 'bar'",
            external_customer_id="external_customer_id",
            replace_existing_events=True,
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Orb) -> None:
        response = client.events.backfills.with_raw_response.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Orb) -> None:
        with client.events.backfills.with_streaming_response.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = response.parse()
            assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        backfill = client.events.backfills.list()
        assert_matches_type(SyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        backfill = client.events.backfills.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(SyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.events.backfills.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(SyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.events.backfills.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = response.parse()
            assert_matches_type(SyncPage[BackfillListResponse], backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_close(self, client: Orb) -> None:
        backfill = client.events.backfills.close(
            "backfill_id",
        )
        assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

    @parametrize
    def test_raw_response_close(self, client: Orb) -> None:
        response = client.events.backfills.with_raw_response.close(
            "backfill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

    @parametrize
    def test_streaming_response_close(self, client: Orb) -> None:
        with client.events.backfills.with_streaming_response.close(
            "backfill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = response.parse()
            assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            client.events.backfills.with_raw_response.close(
                "",
            )

    @parametrize
    def test_method_fetch(self, client: Orb) -> None:
        backfill = client.events.backfills.fetch(
            "backfill_id",
        )
        assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

    @parametrize
    def test_raw_response_fetch(self, client: Orb) -> None:
        response = client.events.backfills.with_raw_response.fetch(
            "backfill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

    @parametrize
    def test_streaming_response_fetch(self, client: Orb) -> None:
        with client.events.backfills.with_streaming_response.fetch(
            "backfill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = response.parse()
            assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_fetch(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            client.events.backfills.with_raw_response.fetch(
                "",
            )

    @parametrize
    def test_method_revert(self, client: Orb) -> None:
        backfill = client.events.backfills.revert(
            "backfill_id",
        )
        assert_matches_type(BackfillRevertResponse, backfill, path=["response"])

    @parametrize
    def test_raw_response_revert(self, client: Orb) -> None:
        response = client.events.backfills.with_raw_response.revert(
            "backfill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillRevertResponse, backfill, path=["response"])

    @parametrize
    def test_streaming_response_revert(self, client: Orb) -> None:
        with client.events.backfills.with_streaming_response.revert(
            "backfill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = response.parse()
            assert_matches_type(BackfillRevertResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_revert(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            client.events.backfills.with_raw_response.revert(
                "",
            )


class TestAsyncBackfills:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            close_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_id="customer_id",
            deprecation_filter="my_numeric_property > 100 AND my_other_property = 'bar'",
            external_customer_id="external_customer_id",
            replace_existing_events=True,
        )
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOrb) -> None:
        response = await async_client.events.backfills.with_raw_response.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOrb) -> None:
        async with async_client.events.backfills.with_streaming_response.create(
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = await response.parse()
            assert_matches_type(BackfillCreateResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.list()
        assert_matches_type(AsyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AsyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.events.backfills.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(AsyncPage[BackfillListResponse], backfill, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.events.backfills.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = await response.parse()
            assert_matches_type(AsyncPage[BackfillListResponse], backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_close(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.close(
            "backfill_id",
        )
        assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncOrb) -> None:
        response = await async_client.events.backfills.with_raw_response.close(
            "backfill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncOrb) -> None:
        async with async_client.events.backfills.with_streaming_response.close(
            "backfill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = await response.parse()
            assert_matches_type(BackfillCloseResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            await async_client.events.backfills.with_raw_response.close(
                "",
            )

    @parametrize
    async def test_method_fetch(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.fetch(
            "backfill_id",
        )
        assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

    @parametrize
    async def test_raw_response_fetch(self, async_client: AsyncOrb) -> None:
        response = await async_client.events.backfills.with_raw_response.fetch(
            "backfill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

    @parametrize
    async def test_streaming_response_fetch(self, async_client: AsyncOrb) -> None:
        async with async_client.events.backfills.with_streaming_response.fetch(
            "backfill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = await response.parse()
            assert_matches_type(BackfillFetchResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_fetch(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            await async_client.events.backfills.with_raw_response.fetch(
                "",
            )

    @parametrize
    async def test_method_revert(self, async_client: AsyncOrb) -> None:
        backfill = await async_client.events.backfills.revert(
            "backfill_id",
        )
        assert_matches_type(BackfillRevertResponse, backfill, path=["response"])

    @parametrize
    async def test_raw_response_revert(self, async_client: AsyncOrb) -> None:
        response = await async_client.events.backfills.with_raw_response.revert(
            "backfill_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backfill = response.parse()
        assert_matches_type(BackfillRevertResponse, backfill, path=["response"])

    @parametrize
    async def test_streaming_response_revert(self, async_client: AsyncOrb) -> None:
        async with async_client.events.backfills.with_streaming_response.revert(
            "backfill_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backfill = await response.parse()
            assert_matches_type(BackfillRevertResponse, backfill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_revert(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `backfill_id` but received ''"):
            await async_client.events.backfills.with_raw_response.revert(
                "",
            )
