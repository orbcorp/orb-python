# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from tests.utils import assert_matches_type
from orb.types.customers import (
    UsageUpdateResponse,
    UsageUpdateByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        usage = client.customers.usage.update(
            id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        usage = client.customers.usage.update(
            id="customer_id",
            events=[
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Orb) -> None:
        response = client.customers.usage.with_raw_response.update(
            id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Orb) -> None:
        with client.customers.usage.with_streaming_response.update(
            id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageUpdateResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.usage.with_raw_response.update(
                id="",
                events=[
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                ],
            )

    @parametrize
    def test_method_update_by_external_id(self, client: Orb) -> None:
        usage = client.customers.usage.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    def test_method_update_by_external_id_with_all_params(self, client: Orb) -> None:
        usage = client.customers.usage.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    def test_raw_response_update_by_external_id(self, client: Orb) -> None:
        response = client.customers.usage.with_raw_response.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    def test_streaming_response_update_by_external_id(self, client: Orb) -> None:
        with client.customers.usage.with_streaming_response.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_by_external_id(self, client: Orb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.usage.with_raw_response.update_by_external_id(
                id="",
                events=[
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                ],
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncOrb) -> None:
        usage = await async_client.customers.usage.update(
            id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOrb) -> None:
        usage = await async_client.customers.usage.update(
            id="customer_id",
            events=[
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.usage.with_raw_response.update(
            id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.usage.with_streaming_response.update(
            id="customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageUpdateResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.usage.with_raw_response.update(
                id="",
                events=[
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                ],
            )

    @parametrize
    async def test_method_update_by_external_id(self, async_client: AsyncOrb) -> None:
        usage = await async_client.customers.usage.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, async_client: AsyncOrb) -> None:
        usage = await async_client.customers.usage.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "customer_id",
                    "external_customer_id": "external_customer_id",
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        response = await async_client.customers.usage.with_raw_response.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    async def test_streaming_response_update_by_external_id(self, async_client: AsyncOrb) -> None:
        async with async_client.customers.usage.with_streaming_response.update_by_external_id(
            id="external_customer_id",
            events=[
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "event_name",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_by_external_id(self, async_client: AsyncOrb) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.usage.with_raw_response.update_by_external_id(
                id="",
                events=[
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                    {
                        "event_name": "event_name",
                        "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                        "properties": {},
                    },
                ],
            )
