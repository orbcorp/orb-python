# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.types.events import EventVolumes

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVolume:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Orb) -> None:
        volume = client.events.volume.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventVolumes, volume, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Orb) -> None:
        volume = client.events.volume.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
            timeframe_end=parse_datetime("2024-10-11T06:00:00Z"),
        )
        assert_matches_type(EventVolumes, volume, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Orb) -> None:
        response = client.events.volume.with_raw_response.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(EventVolumes, volume, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Orb) -> None:
        with client.events.volume.with_streaming_response.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = response.parse()
            assert_matches_type(EventVolumes, volume, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVolume:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOrb) -> None:
        volume = await async_client.events.volume.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(EventVolumes, volume, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOrb) -> None:
        volume = await async_client.events.volume.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="cursor",
            limit=1,
            timeframe_end=parse_datetime("2024-10-11T06:00:00Z"),
        )
        assert_matches_type(EventVolumes, volume, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOrb) -> None:
        response = await async_client.events.volume.with_raw_response.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        volume = response.parse()
        assert_matches_type(EventVolumes, volume, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOrb) -> None:
        async with async_client.events.volume.with_streaming_response.list(
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            volume = await response.parse()
            assert_matches_type(EventVolumes, volume, path=["response"])

        assert cast(Any, response.is_closed) is True
