# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_date
from tests.utils import assert_matches_type
from orb.types.licenses import (
    UsageGetUsageResponse,
    UsageGetAllUsageResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_all_usage(self, client: Orb) -> None:
        usage = client.licenses.usage.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

    @parametrize
    def test_method_get_all_usage_with_all_params(self, client: Orb) -> None:
        usage = client.licenses.usage.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
            cursor="cursor",
            end_date=parse_date("2019-12-27"),
            group_by=["string"],
            limit=1,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_get_all_usage(self, client: Orb) -> None:
        response = client.licenses.usage.with_raw_response.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_get_all_usage(self, client: Orb) -> None:
        with client.licenses.usage.with_streaming_response.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_usage(self, client: Orb) -> None:
        usage = client.licenses.usage.get_usage(
            license_id="license_id",
        )
        assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

    @parametrize
    def test_method_get_usage_with_all_params(self, client: Orb) -> None:
        usage = client.licenses.usage.get_usage(
            license_id="license_id",
            cursor="cursor",
            end_date=parse_date("2019-12-27"),
            group_by=["string"],
            limit=1,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_get_usage(self, client: Orb) -> None:
        response = client.licenses.usage.with_raw_response.get_usage(
            license_id="license_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_get_usage(self, client: Orb) -> None:
        with client.licenses.usage.with_streaming_response.get_usage(
            license_id="license_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_usage(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `license_id` but received ''"):
            client.licenses.usage.with_raw_response.get_usage(
                license_id="",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_all_usage(self, async_client: AsyncOrb) -> None:
        usage = await async_client.licenses.usage.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )
        assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

    @parametrize
    async def test_method_get_all_usage_with_all_params(self, async_client: AsyncOrb) -> None:
        usage = await async_client.licenses.usage.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
            cursor="cursor",
            end_date=parse_date("2019-12-27"),
            group_by=["string"],
            limit=1,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_get_all_usage(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.usage.with_raw_response.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_all_usage(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.usage.with_streaming_response.get_all_usage(
            license_type_id="license_type_id",
            subscription_id="subscription_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetAllUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_usage(self, async_client: AsyncOrb) -> None:
        usage = await async_client.licenses.usage.get_usage(
            license_id="license_id",
        )
        assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

    @parametrize
    async def test_method_get_usage_with_all_params(self, async_client: AsyncOrb) -> None:
        usage = await async_client.licenses.usage.get_usage(
            license_id="license_id",
            cursor="cursor",
            end_date=parse_date("2019-12-27"),
            group_by=["string"],
            limit=1,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncOrb) -> None:
        response = await async_client.licenses.usage.with_raw_response.get_usage(
            license_id="license_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncOrb) -> None:
        async with async_client.licenses.usage.with_streaming_response.get_usage(
            license_id="license_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetUsageResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_usage(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `license_id` but received ''"):
            await async_client.licenses.usage.with_raw_response.get_usage(
                license_id="",
            )
