# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from orb import Orb, AsyncOrb
from orb._utils import parse_datetime
from orb._client import Orb, AsyncOrb
from tests.utils import assert_matches_type
from orb.types.customers import (
    UsageUpdateResponse,
    UsageUpdateByExternalIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My API Key"


class TestUsage:
    strict_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Orb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_update(self, client: Orb) -> None:
        usage = client.customers.usage.update(
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Orb) -> None:
        usage = client.customers.usage.update(
            "string",
            events=[
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
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
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    def test_method_update_by_external_id(self, client: Orb) -> None:
        usage = client.customers.usage.update_by_external_id(
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    def test_method_update_by_external_id_with_all_params(self, client: Orb) -> None:
        usage = client.customers.usage.update_by_external_id(
            "string",
            events=[
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
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
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])


class TestAsyncUsage:
    strict_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncOrb(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_update(self, client: AsyncOrb) -> None:
        usage = await client.customers.usage.update(
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncOrb) -> None:
        usage = await client.customers.usage.update(
            "string",
            events=[
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncOrb) -> None:
        response = await client.customers.usage.with_raw_response.update(
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateResponse, usage, path=["response"])

    @parametrize
    async def test_method_update_by_external_id(self, client: AsyncOrb) -> None:
        usage = await client.customers.usage.update_by_external_id(
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    async def test_method_update_by_external_id_with_all_params(self, client: AsyncOrb) -> None:
        usage = await client.customers.usage.update_by_external_id(
            "string",
            events=[
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "customer_id": "string",
                    "external_customer_id": "string",
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
            timeframe_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            timeframe_start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])

    @parametrize
    async def test_raw_response_update_by_external_id(self, client: AsyncOrb) -> None:
        response = await client.customers.usage.with_raw_response.update_by_external_id(
            "string",
            events=[
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
                {
                    "event_name": "string",
                    "timestamp": parse_datetime("2020-12-09T16:09:53Z"),
                    "properties": {},
                },
            ],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageUpdateByExternalIDResponse, usage, path=["response"])
