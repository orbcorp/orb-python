# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb.types import TopLevelPingResponse
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestTopLevel:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_ping(self, client: Orb) -> None:
        top_level = client.top_level.ping()
        assert_matches_type(TopLevelPingResponse, top_level, path=["response"])

    @parametrize
    def test_raw_response_ping(self, client: Orb) -> None:
        response = client.top_level.with_raw_response.ping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(TopLevelPingResponse, top_level, path=["response"])

    @parametrize
    def test_streaming_response_ping(self, client: Orb) -> None:
        with client.top_level.with_streaming_response.ping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = response.parse()
            assert_matches_type(TopLevelPingResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTopLevel:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_ping(self, client: AsyncOrb) -> None:
        top_level = await client.top_level.ping()
        assert_matches_type(TopLevelPingResponse, top_level, path=["response"])

    @parametrize
    async def test_raw_response_ping(self, client: AsyncOrb) -> None:
        response = await client.top_level.with_raw_response.ping()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top_level = response.parse()
        assert_matches_type(TopLevelPingResponse, top_level, path=["response"])

    @parametrize
    async def test_streaming_response_ping(self, client: AsyncOrb) -> None:
        async with client.top_level.with_streaming_response.ping() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top_level = await response.parse()
            assert_matches_type(TopLevelPingResponse, top_level, path=["response"])

        assert cast(Any, response.is_closed) is True
